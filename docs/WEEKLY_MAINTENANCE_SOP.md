# Weekly Maintenance SOP for Awesome-Personalized-LLMs

## Scope
This repository is maintained weekly to track newly posted **arXiv** papers that are highly relevant to personalized large language models.

Accepted scope:
- Personalized LLMs / persona / personality / style control
- Preference alignment / pluralistic alignment / multi-objective alignment
- Test-time personalization / decoding-time personalization / steering
- Memory personalization / retrieval personalization / user modeling
- Personalized agents / personalized multimodal LLMs
- Surveys, benchmarks, datasets, and application papers in the above scope

Excluded by default:
- Generic alignment papers without a meaningful personalization component
- Generic recommendation or multimodal papers that only mention preference superficially
- Non-arXiv-only additions during weekly updates

## Weekly cadence
- **Schedule:** Every Monday, 09:00 Asia/Shanghai
- **Output:** One summary PR per week
- **Extra output:** A separate email digest containing the paper titles plus abstracts/brief descriptions
- **PR content:** Title + links only; no abstracts in the PR

## Weekly workflow
1. Query arXiv for papers posted in the last 7 days.
2. Score/filter candidates by repository scope.
3. Deduplicate against:
   - existing README entries
   - duplicate arXiv IDs within the weekly candidate set
   - obvious near-duplicates caused by version bumps
4. Assign each accepted paper to one primary category.
5. Update README with normalized formatting.
6. Create a single weekly PR.
7. Send an email digest with titles + abstracts/brief descriptions.

## Working rules
- Prefer precision over recall. Skip weakly related papers.
- Keep one paper in one primary category to reduce clutter.
- Normalize links to arXiv abs pages when possible in machine-readable data; README can keep pdf links if desired.
- Preserve repository style unless performing a deliberate cleanup.
- Remove exact duplicates when discovered.

## Initial keyword set
Positive query terms:
- "personalized llm"
- personalization
- persona
- personality
- "preference alignment"
- "pluralistic alignment"
- "user modeling"
- "personalized generation"
- "personalized retrieval"
- "personalized agent"
- "memory personalization"
- "decoding-time personalization"
- steering

Soft reject signals:
- alignment without user/personal/persona/preference-specific context
- generic VLM / recommender / agent papers with no clear personalization contribution

## Category map
Use the closest existing README section when possible. Preferred mapping:
- Human Value Alignment
  - Survey/Tutorial/Framework
  - Benchmark/Dataset
  - Training-based Methods
  - Training-free Methods
- Preference Alignment
  - Survey/Tutorial/Framework
  - Benchmark/Dataset
  - Prompt/Vector-based Methods
  - SFT / RL Methods

If a paper fits multiple places, choose the most specific one.

## PR convention
- **Branch:** `weekly/arxiv-YYYY-MM-DD`
- **PR title:** `weekly: arXiv update for YYYY-MM-DD`
- **Commit title:** same as PR title

PR body template:
- date window covered
- number of accepted papers
- sections updated
- duplicates removed/fixed
- note that abstracts were sent by email separately

## Email digest convention
Subject:
- `Weekly Personalized-LLMs arXiv Digest - YYYY-MM-DD`

Body for each paper:
- Title
- arXiv link
- Primary category
- 3-8 sentence abstract/brief intro

## Required configuration
The weekly workflow needs:
- GitHub write access (already available)
- A mail delivery method
- A recipient email address

Recommended GitHub repository variables/secrets:
- `DIGEST_EMAIL_TO` (repository variable or secret)
- `SMTP_HOST`
- `SMTP_PORT`
- `SMTP_USER`
- `SMTP_PASS`
- `SMTP_FROM`

## Notes
This scaffold intentionally separates:
- repository update logic
- candidate storage
- email digest generation

That keeps future migration to a stronger retrieval/ranking pipeline simple.
