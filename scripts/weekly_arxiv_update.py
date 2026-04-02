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
POSITIVE_TERMS = {
    'personalized': 4, 'personalization': 4, 'persona': 4, 'personality': 3,
    'preference': 3, 'pluralistic': 3, 'user': 2, 'profile': 2, 'memory': 2,
    'retrieval': 2, 'steering': 2, 'alignment': 2, 'agent': 2, 'style': 2,
    'multimodal': 1, 'dialogue': 2, 'generation': 1, 'custom': 1
}
NEGATIVE_PATTERNS = [
    r'protein', r'genome', r'medical imaging', r'earthquake', r'kubernetes',
    r'ancient egyptian', r'super-resolution', r'temporal action detection'
]
START_MARKER = '<!-- WEEKLY-UPDATES:START -->'
END_MARKER = '<!-- WEEKLY-UPDATES:END -->'
ATOM_NS = {'a': 'http://www.w3.org/2005/Atom'}


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


def score_paper(title: str, summary: str) -> int:
    hay = normalize(f'{title} {summary}')
    score = 0
    for term, weight in POSITIVE_TERMS.items():
        if term in hay:
            score += weight
    if 'large language model' in hay or 'llm' in hay:
        score += 3
    if any(re.search(pat, hay) for pat in NEGATIVE_PATTERNS):
        score -= 6
    return score


def classify(title: str, summary: str) -> str:
    hay = normalize(f'{title} {summary}')
    if 'survey' in hay or 'tutorial' in hay or 'benchmark' in hay or 'dataset' in hay:
        return 'Survey / Benchmark'
    if 'persona' in hay or 'personality' in hay or 'style' in hay:
        return 'Persona / Personality'
    if 'steering' in hay or 'decoding' in hay or 'test-time' in hay or 'inference' in hay:
        return 'Test-time / Steering'
    if 'memory' in hay or 'retrieval' in hay or 'user modeling' in hay or 'profile' in hay:
        return 'Memory / Retrieval / User Modeling'
    if 'agent' in hay or 'multimodal' in hay or 'vision-language' in hay:
        return 'Agents / Multimodal'
    if 'preference' in hay or 'alignment' in hay or 'pluralistic' in hay:
        return 'Preference / Alignment'
    return 'Other Personalized LLMs'


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
        score = score_paper(paper['title'], paper['summary'])
        if score < 7:
            continue
        paper['score'] = score
        paper['category'] = classify(paper['title'], paper['summary'])
        accepted.append(paper)
        seen_ids.add(paper['id'])
    accepted.sort(key=lambda x: (-x['score'], x['id']))
    return accepted[:20], skipped_duplicates


def weekly_section(items: List[Dict[str, str]], today: str) -> str:
    lines = [START_MARKER, '## Weekly Updates (Automated)', f'### {today}']
    if not items:
        lines.append('- No qualified new arXiv papers this week.')
    else:
        for item in items:
            ym = item['id'].replace('.', '')[:6]
            lines.append(f"+ **\\[{today[:4]} Arxiv-{ym}\\]** {item['title']}. ([Paper]({item['pdf_url']}))")
    lines.append(END_MARKER)
    return '\n'.join(lines)


def update_readme(items: List[Dict[str, str]], today: str) -> bool:
    text = README.read_text(encoding='utf-8')
    section = weekly_section(items, today)
    pattern = re.compile(re.escape(START_MARKER) + r'.*?' + re.escape(END_MARKER), re.S)
    if START_MARKER in text and END_MARKER in text:
        new_text = pattern.sub(section, text)
    else:
        insert_at = text.find('## 1. Human Value Alignment')
        if insert_at == -1:
            new_text = text.rstrip() + '\n\n' + section + '\n'
        else:
            new_text = text[:insert_at].rstrip() + '\n\n' + section + '\n\n' + text[insert_at:]
    if new_text != text:
        README.write_text(new_text, encoding='utf-8')
        return True
    return False


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
    readme_changed = update_readme(items, today)
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
        'sections_updated': ['Weekly Updates (Automated)'] if readme_changed else [],
        'duplicates_removed': duplicates,
        'status': 'ok'
    }
    (OUT / 'candidates.json').write_text(json.dumps(candidates, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    (OUT / 'email_digest.json').write_text(json.dumps(digest, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    (OUT / 'pr_summary.json').write_text(json.dumps(pr_summary, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(f"Accepted {len(items)} papers; README changed={readme_changed}; duplicates skipped={duplicates}")
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
