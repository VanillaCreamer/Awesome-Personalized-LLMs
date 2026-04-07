# Local Maintenance Rules

This file is private/local context for maintaining this paper repository. It should stay out of the public repo.

## Current live policy

### Schedule
- Weekly maintenance runs every **Monday 09:00 Asia/Shanghai**.
- The task is **weekly paper updating**, not generic daily repo inspection.

### Scope
- Require strong thematic fit with the repository topic.
- Accept papers only when they are clearly about **personalization** and also belong to a relevant model family.
- The currently accepted model families are:
  - LLMs / language models
  - VLMs
  - VLAs
  - agents
  - multimodal model settings
- Do not accept papers based on keyword overlap alone.
- Practical rule: a paper should show clear signals such as personalization / preference / persona / personality / memory / profile / retrieval / user modeling, and also clearly sit in one of the model families above.

### Query / retrieval seed terms
Use these query themes for weekly search:
- personalized llm
- personalization
- persona
- personality
- preference alignment
- pluralistic alignment
- user modeling
- personalized generation
- personalized retrieval
- personalized agent
- memory personalization
- decoding-time personalization
- steering

### Time window and search size
- Default time window: **last 7 days**.
- Default search size: **MAX_RESULTS=100**.

### Deduplication
Always skip:
- papers whose arXiv id is already present in README
- papers whose title is already present in README
- duplicates inside the current weekly batch
- obvious version-bump near-duplicates when they do not add new value

### Volume
- Do **not** impose a fixed weekly cap such as 10 papers.
- If a paper is strong and in-scope, it can be added.

### Hard excludes
Keep hard excludes for recurring noisy adjacent areas that are clearly off-scope.
Current explicit exclude set includes:
- federated learning
- fitness / workout
- emotion recognition / facial expression
- gpu kernel
- diabetes
- darts training
- wearable human activity
- earthquake
- kubernetes
- genome / protein
- super-resolution
- temporal action detection
- programming courses
- retail stores / marketing
- negotiation
- game development
- avatar
- diffusion model
- text-to-image

Review the hard-exclude list occasionally so it does not become stale.

### Classification
- Keep the current section structure unless there is a strong reason to change it:
  - 2.1 Survey/Tutorial/Framework
  - 2.2 Benchmark/Dataset
  - 2.3 Memory / Retrieval-based Methods
  - 2.4 Prompt/Vector-based Methods
  - 2.5 SFT/RL Methods
- Classify by main contribution rather than secondary framing.
- Prefer method-based placement over application framing.
- If a paper fits multiple sections, choose one primary home.
- Only propose category restructuring when it improves retrieval or reduces repeated misclassification.

### Public repo boundary
Only public reader-facing files should be committed:
- README.md
- MAINTENANCE.md
- .gitignore (when needed)

Keep local/private:
- scripts/
- docs/
- config/
- output/
- logs/
- config.weekly_maintenance.env.example

### Weekly workflow
1. Pull latest default branch.
2. Run paper selection using the current weekly rules.
3. Generate the digest.
4. Send weekly digest email.
5. Commit only public reader-facing files.
6. **Open or update the weekly PR**.

### Reminder
- The user explicitly wants weekly email digests to continue.
- The user also explicitly expects the weekly maintenance flow to include **PR creation/update**; this is a required step, not an optional follow-up.
- Public repo policy should stay reader-facing even if local maintenance assets become more detailed.
