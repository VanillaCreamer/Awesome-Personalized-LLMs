#!/usr/bin/env python3
import json
import os
import re
import textwrap
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Dict, List, Tuple

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / 'README.md'
OUT = ROOT / 'output'
OUT.mkdir(parents=True, exist_ok=True)

KEYWORDS = [
    'personalized llm', 'personalization', 'persona', 'personality',
    'preference alignment', 'pluralistic alignment', 'user modeling',
    'personalized generation', 'personalized retrieval',
    'personalized agent', 'memory personalization',
    'decoding-time personalization', 'steering'
]
ATOM_NS = {'a': 'http://www.w3.org/2005/Atom'}
SECTION_MAP = {
    '2.1 Survey/Tutorial/Framework': '### 2.1 Survey/Tutorial/Framework',
    '2.2 Benchmark/Dataset': '### 2.2 Benchmark/Dataset',
    '2.3 Memory / Retrieval-based Methods': '### 2.3 Memory / Retrieval-based Methods',
    '2.4 Prompt/Vector-based Methods': '### 2.4 Prompt/Vector-based Methods',
    '2.5 SFT/RL Methods': '### 2.5 Supervised Fine-Tuning-based (SFT) / Reinforcement Learning (RL) Methods',
}
HARD_EXCLUDE_PATTERNS = [
    r'federated learning', r'fitness', r'workout', r'emotion recognition',
    r'facial expression', r'gpu kernel', r'diabetes', r'darts training',
    r'wearable human activity', r'earthquake', r'kubernetes', r'genome',
    r'protein', r'super-resolution', r'temporal action detection',
    r'programming courses', r'retail stores', r'marketing', r'negotiation',
    r'game development', r'avatar', r'diffusion model', r'text-to-image'
]
TITLE_STRONG_TERMS = [
    'personalized', 'personalization', 'persona', 'personality',
    'preference', 'pluralistic', 'alignment', 'user', 'memory', 'agent'
]
LLM_TERMS = ['large language model', 'large language models', 'llm', 'llms', 'language model']
METHOD_TERMS = [
    'framework', 'method', 'prompt', 'vector', 'decoding', 'test-time',
    'inference-time', 'adapter', 'lora', 'fine-tuning', 'sft',
    'reinforcement learning', 'reward', 'optimization', 'preference modeling'
]
BENCHMARK_TERMS = ['benchmark', 'dataset', 'evaluation framework', 'bench']
SURVEY_TERMS = ['survey', 'tutorial', 'overview', 'review']


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def today_iso() -> str:
    return utc_now().date().isoformat()


def env_int(name: str, default: int) -> int:
    try:
        return int(os.getenv(name, str(default)))
    except ValueError:
        return default


def normalize(text: str) -> str:
    return re.sub(r'\s+', ' ', text.strip()).lower()


def existing_readme_signatures() -> Tuple[set, set]:
    text = README.read_text(encoding='utf-8') if README.exists() else ''
    titles = set()
    ids = set(re.findall(r'arxiv\.org/(?:abs|pdf)/(\d{4}\.\d{4,5})(?:v\d+)?', text, flags=re.I))
    for line in text.splitlines():
        m = re.search(r'\*\*.*?\*\*\s*(.+?)\.\s*\(\[Paper\]', line)
        if m:
            titles.add(normalize(m.group(1)))
    return titles, ids


def has_any(text: str, terms: List[str]) -> bool:
    return any(term in text for term in terms)


def strong_relevance(title: str, summary: str) -> bool:
    hay = normalize(f'{title} {summary}')
    title_n = normalize(title)

    if any(re.search(pat, hay) for pat in HARD_EXCLUDE_PATTERNS):
        return False

    has_llm = has_any(hay, LLM_TERMS)
    has_personal = has_any(hay, ['personalized', 'personalization', 'persona', 'personality', 'user-specific', 'pluralistic'])
    has_pref_align = has_any(hay, ['preference', 'alignment', 'reward factorization', 'preference modeling'])
    has_agent_memory = has_any(hay, ['memory', 'retrieval', 'agent', 'profile'])

    # require explicit LLM/personalization signal, not just generic "personalized"
    if not has_llm and not ('gui agent' in hay and has_personal):
        return False

    # require a meaningful personalization/alignment hook
    if not (has_personal or has_pref_align or (has_agent_memory and has_personal)):
        return False

    # title should carry strong signal unless benchmark/method summary is very explicit
    if not has_any(title_n, TITLE_STRONG_TERMS):
        if not (has_any(hay, BENCHMARK_TERMS) and has_personal and has_llm):
            if not (has_any(hay, METHOD_TERMS) and has_personal and has_llm):
                return False

    return True


def score_paper(title: str, summary: str) -> int:
    hay = normalize(f'{title} {summary}')
    score = 0
    for term in TITLE_STRONG_TERMS:
        if term in hay:
            score += 3
    for term in LLM_TERMS:
        if term in hay:
            score += 2
    for term in ['memory', 'retrieval', 'agent', 'benchmark', 'dataset', 'steering', 'prompt', 'reward', 'alignment']:
        if term in hay:
            score += 1
    return score


def classify(title: str, summary: str) -> str:
    hay = normalize(f'{title} {summary}')
    if has_any(hay, SURVEY_TERMS):
        return '2.1 Survey/Tutorial/Framework'
    if has_any(hay, BENCHMARK_TERMS):
        return '2.2 Benchmark/Dataset'
    if has_any(hay, ['prompt', 'vector', 'steering', 'decoding', 'test-time', 'inference-time', 'activation', 'persona projection']):
        return '2.4 Prompt/Vector-based Methods'
    if has_any(hay, ['memory', 'retrieval', 'profile', 'graph', 'rerank']):
        return '2.3 Memory / Retrieval-based Methods'
    if has_any(hay, ['fine-tuning', 'sft', 'reinforcement learning', 'reward', 'optimization', 'lora', 'adapter', 'dpo', 'factorization']):
        return '2.5 SFT/RL Methods'
    if has_any(hay, ['agent', 'persona', 'personality']):
        return '2.4 Prompt/Vector-based Methods'
    return '2.5 SFT/RL Methods'


def build_query() -> str:
    parts = [f'all:"{kw}"' for kw in KEYWORDS]
    return ' OR '.join(parts)


def fetch_arxiv() -> List[Dict[str, str]]:
    max_results = env_int('MAX_RESULTS', 100)
    query = build_query()
    params = {
        'search_query': query,
        'start': '0',
        'max_results': str(max_results),
        'sortBy': 'submittedDate',
        'sortOrder': 'descending'
    }
    url = 'http://export.arxiv.org/api/query?' + urllib.parse.urlencode(params)
    with urllib.request.urlopen(url, timeout=60) as resp:
        xml_text = resp.read()
    root = ET.fromstring(xml_text)
    papers = []
    for entry in root.findall('a:entry', ATOM_NS):
        title = ' '.join((entry.findtext('a:title', default='', namespaces=ATOM_NS) or '').split())
        summary = ' '.join((entry.findtext('a:summary', default='', namespaces=ATOM_NS) or '').split())
        entry_id = entry.findtext('a:id', default='', namespaces=ATOM_NS)
        published = entry.findtext('a:published', default='', namespaces=ATOM_NS)
        updated = entry.findtext('a:updated', default='', namespaces=ATOM_NS)
        authors = [a.findtext('a:name', default='', namespaces=ATOM_NS) for a in entry.findall('a:author', ATOM_NS)]
        arxiv_id_match = re.search(r'(\d{4}\.\d{4,5})(v\d+)?$', entry_id)
        if not arxiv_id_match:
            continue
        arxiv_id = arxiv_id_match.group(1)
        papers.append({
            'id': arxiv_id,
            'title': title,
            'summary': summary,
            'published': published,
            'updated': updated,
            'authors': authors,
            'abs_url': f'https://arxiv.org/abs/{arxiv_id}',
            'pdf_url': f'https://arxiv.org/pdf/{arxiv_id}.pdf'
        })
    return papers


def within_window(ts: str, days: int) -> bool:
    try:
        dt = datetime.fromisoformat(ts.replace('Z', '+00:00'))
    except ValueError:
        return False
    return dt >= utc_now() - timedelta(days=days)


def format_entry(item: Dict[str, str]) -> str:
    ym = item['id'].replace('.', '')[:6]
    year = item['published'][:4] if item.get('published') else today_iso()[:4]
    return f"+ **\\[{year} Arxiv-{ym}\\]** {item['title']}. ([Paper]({item['pdf_url']}))"


def pick_papers() -> Tuple[List[Dict[str, str]], int]:
    window_days = env_int('WINDOW_DAYS', 7)
    existing_titles, existing_ids = existing_readme_signatures()
    raw = fetch_arxiv()
    accepted = []
    seen_ids = set()
    skipped_duplicates = 0
    for paper in raw:
        if not within_window(paper['published'] or paper['updated'], window_days):
            continue
        if paper['id'] in seen_ids or paper['id'] in existing_ids or normalize(paper['title']) in existing_titles:
            skipped_duplicates += 1
            continue
        if not strong_relevance(paper['title'], paper['summary']):
            continue
        paper['score'] = score_paper(paper['title'], paper['summary'])
        paper['category'] = classify(paper['title'], paper['summary'])
        accepted.append(paper)
        seen_ids.add(paper['id'])
    accepted.sort(key=lambda x: (-x['score'], x['id']))
    return accepted[:10], skipped_duplicates


def remove_weekly_updates_block(text: str) -> str:
    return re.sub(r'<!-- WEEKLY-UPDATES:START -->.*?<!-- WEEKLY-UPDATES:END -->\n*', '', text, flags=re.S)


def insert_into_section(text: str, heading: str, entries: List[str]) -> str:
    if not entries:
        return text
    idx = text.find(heading)
    if idx == -1:
        return text
    after_heading = text.find('\n', idx)
    if after_heading == -1:
        return text
    insert_pos = after_heading + 1
    block = '\n'.join(entries) + '\n\n'
    return text[:insert_pos] + block + text[insert_pos:]


def update_readme(items: List[Dict[str, str]]) -> Tuple[bool, List[str]]:
    text = README.read_text(encoding='utf-8')
    text = remove_weekly_updates_block(text)
    by_section: Dict[str, List[str]] = {key: [] for key in SECTION_MAP}
    for item in items:
        by_section[item['category']].append(format_entry(item))
    touched = []
    new_text = text
    for section_key, heading in SECTION_MAP.items():
        entries = by_section.get(section_key, [])
        if entries:
            new_text = insert_into_section(new_text, heading, entries)
            touched.append(section_key)
    if new_text != text:
        README.write_text(new_text, encoding='utf-8')
        return True, touched
    return False, touched


def build_digest(items: List[Dict[str, str]], today: str) -> Dict:
    digest_items = []
    for item in items:
        digest_items.append({
            'title': item['title'],
            'category': item['category'],
            'link': item['abs_url'],
            'summary': textwrap.shorten(item['summary'], width=1400, placeholder='...')
        })
    return {
        'date': today,
        'subject': f'Weekly Personalized-LLMs arXiv Digest - {today}',
        'to': os.getenv('DIGEST_EMAIL_TO', ''),
        'items': digest_items,
        'status': 'ok'
    }


def main() -> int:
    today = today_iso()
    items, duplicates = pick_papers()
    readme_changed, touched = update_readme(items)
    candidates = {
        'generated_at': utc_now().isoformat(),
        'source': 'arXiv',
        'window_days': env_int('WINDOW_DAYS', 7),
        'keywords': KEYWORDS,
        'accepted_papers': items,
        'status': 'ok'
    }
    digest = build_digest(items, today)
    pr_summary = {
        'date': today,
        'branch': f'weekly/arxiv-{today}',
        'title': f'weekly: arXiv update for {today}',
        'accepted_count': len(items),
        'sections_updated': touched,
        'duplicates_removed': duplicates,
        'status': 'ok'
    }
    (OUT / 'candidates.json').write_text(json.dumps(candidates, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    (OUT / 'email_digest.json').write_text(json.dumps(digest, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    (OUT / 'pr_summary.json').write_text(json.dumps(pr_summary, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(f"Accepted {len(items)} papers; README changed={readme_changed}; duplicates skipped={duplicates}; sections={touched}")
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
