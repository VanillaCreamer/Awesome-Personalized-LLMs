# MAINTENANCE.md

This repository is intentionally reader-facing. The public surface should stay lightweight, with the README as the main artifact.

## What contributors should optimize for

Contributions should improve the quality of the curated paper list rather than expand scope aggressively.

### Include papers when they are clearly about personalized LLMs

Strong fits include papers centered on:
- user preference modeling
- persona / personality control
- profile- or memory-based personalization
- personalized retrieval or generation
- personalized alignment
- benchmarks / datasets / evaluation where personalization is a central task

### Be conservative with borderline papers

Papers should usually **not** be added when personalization is only incidental or mentioned as a side setting.

Examples of weak fits:
- generic alignment papers without a personalization focus
- generic safety / jailbreak / trustworthiness papers
- generic multimodal perception papers
- generic recommendation or agent papers with only loose personalization language
- papers whose main contribution is unrelated infrastructure, systems, compression, or deployment

## Classification rules

Use the existing README section structure and place papers by their **main technical contribution**, not by a secondary application framing.

Current preference order:
- **Benchmark / Dataset**: only if personalization is the core evaluation target
- **Memory / Retrieval-based Methods**: memory construction, profile building, retrieval, graph memory, preference memory
- **Prompt / Vector-based Methods**: prompting, steering, decoding-time control, activation / persona vectors
- **SFT / RL Methods**: fine-tuning, reward modeling, preference optimization, adapters, RLHF-style methods

If a paper could fit multiple sections, choose the section that best reflects the main method or contribution.

## Quality bar for changes

Contributors are encouraged to:
- remove duplicates
- reclassify misfiled papers
- remove obviously off-scope papers
- preserve a clean and readable README

Please avoid:
- bulk-adding many loosely related papers
- introducing new sections unless they materially improve clarity
- expanding the repository into a general alignment / agents / recommendation list

## Formatting

Follow the README contribution format:

`+ **[Year Venue]** Title. ([Paper](link), [Code](link))`

Include code links only when they are real and accessible.

## Philosophy

This repository prefers **precision over coverage**.
A smaller, cleaner, better-classified list is more useful than a large noisy one.
