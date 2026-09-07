# Awesome Personalized Large Language Models

<!-- weekly-trend:start -->
> [!IMPORTANT]
> **📌 本周趋势 · 2026-09-07**
>
> 本周趋势仅反映当前 weekly screening corpus，不代表全局引用、下载或社区热度。本轮共审阅 25 篇，其中收录 14 篇、候选 4 篇、剔除 7 篇；趋势判断基于 18 篇相关论文。
>
> 1. 记忆与检索仍是最密集主题：18 篇相关论文中有 6 篇属于 Memory / Retrieval-based Methods。代表方向包括个人聊天历史检索（LINE Conversation History Retrieval）、隐藏用户模型隐私攻击（Inferring Hidden User Models）、以及带动态偏好记忆的群组推荐代理（Enhancing Group Recommendation with Memory-Augmented Reasoning）。这说明“如何存、取、更新、保护用户记忆”仍是个性化 LLM 的核心工程与评测问题。
>
> 2. 评测从“是否更个性化”转向“个性化是否正确、稳健、不过度”：Benchmark / Dataset / Evaluation 有 5 篇。PersonaMem-v3 把跨平台用户理解、推荐、主动任务和个性化边界合并评测；VIBE-Bench 专门测试画像与偏好概念错位；PRISK 则评估无关个性化、偏好收窄和迎合偏差。值得注意的是，评测对象正在覆盖 failure regime 和 hidden cost，而不只是个性化准确率。
>
> 3. 参数高效个性化集中在共享结构 + 每用户轻量调制：SFT / RL / Preference Optimization Methods 有 5 篇，其中 Aplaud 与 PLUME 都采用共享低秩/共享子空间，再叠加用户特定小参数的思路；Behaviorally Grounded User Profiles 则强调真实行为画像可同时支持训练时对齐和测试时推理。这个方向的共同目标是降低 per-user storage，同时保留个体差异。
>
> 4. 下周值得关注：提示空间和纯测试时个性化需要更严格的诊断。Prompt-Space Meta-Learning Does Not Transfer Across Users 给出的负结果提示，跨用户适配实验应加入 wrong-support、seed prompt、结构破坏等控制项。后续可以重点观察新论文是否能证明模型真正利用用户对应关系，而不是只获得更好的通用指令格式。
<!-- weekly-trend:end -->

This repository collects the latest research progress on personalized large language models (LLMs), including preference alignment and user-customized generation. Comments and contributions are welcome.

🆕 GPT-5.4 is being used to maintain this repository, and weekly updates can be viewed through different branches.

For contribution and scope rules, please see [MAINTENANCE.md](./MAINTENANCE.md).

> Inclusion criteria:
> - keep papers whose main task or technical method is personalized LLMs, e.g., user preference modeling, persona/personality control, profile or user-memory personalization, personalized retrieval/generation, or evaluation of personalized capabilities;
> - keep benchmark/dataset papers only when personalization is a central task rather than a side setting;
> - keep agent papers only when the agent is personalized through user preferences, profiles, personal memory, user-adaptive planning/tool use, or personalized web/GUI/mobile interaction;
> - deprioritize generic alignment, safety, multimodal perception, recommendation, memory, or agent papers when personalization is only a loose keyword, demographic/persona audit variable, or downstream application context.

> The contributions are expected to be submitted as follows:
>
> `+ **\[Year Conference/Journal\]** Title. ([Paper](link), [Code](link))` (if accessible).



### 1. Survey / Tutorial / Framework

+ **\[2025 Arxiv-2510\]** From Adaptation to Intelligence: A Systematic Review of Data, Strategies, and Impact in Personalized VR. ([Paper](http://arxiv.org/pdf/2510.13123))

+ **\[2026 Arxiv-2608\]** ComBodied Agents: a New Paradigm of Human-Centric Agentic AI. ([Paper](http://arxiv.org/pdf/2608.10915))

+ **\[2026 Arxiv-2605\]** Toward User Preference Alignment in LLM Recommendation via Explicit Context Feedback. ([Paper](http://arxiv.org/pdf/2605.29141v1))

+ Awesome Personalization in MLLMs. ([Website](https://clare-nie.github.io/Awesome-Personalization-in-MLLMs/))

+ **\[2026 Arxiv-2602\]** Toward Personalized LLM-Powered Agents: Foundations, Evaluation, and Future Directions. ([Paper](https://arxiv.org/pdf/2602.22680v1))

+ **\[2025 Arxiv-2503\]** Personalized Generation In Large Model Era: A Survey. ([Paper](https://arxiv.org/pdf/2503.02614))

+ **\[2024 Arxiv-2411\]** Personalization of Large Language Models: A Survey. ([Paper](https://arxiv.org/pdf/2411.00027))

+ **\[2024 Arxiv-2409\]** PersonalLLM: Tailoring Large Language Models to Individual Preferences. ([Paper](https://arxiv.org/pdf/2409.15746))

+ **\[2024 Arxiv-2402\]** Amulet: Personalized Large Language Model Fine-tuning for User-centric Text Generation. ([Paper](https://arxiv.org/pdf/2402.11115))

+ **\[2024 Arxiv-2407\]** Large Language Models Empowered Personalized Web Agents. ([Paper](https://arxiv.org/pdf/2407.20509))

+ **\[2025 Arxiv-2504\]** A Survey on Personalized and Pluralistic Preference Alignment in Large Language Models. ([Paper](https://arxiv.org/pdf/2504.07070))

+ **\[2024 EMNLP\]** Two Tales of Persona in LLMs: A Survey of Role-Playing and Personalization. ([Paper](https://arxiv.org/pdf/2406.01171), [Code](https://github.com/MiuLab/PersonaLLM-Survey))

+ **\[2024 Arxiv-2412\]** Personalized Multimodal Large Language Models: A Survey. ([Paper](https://arxiv.org/pdf/2412.02142))

+ **\[2024 Arxiv-2502\]** A Survey of Personalized Large Language Models: Progress and Future Directions. ([Paper](https://arxiv.org/pdf/2502.11528))

+ **\[2024 Arxiv-2503\]** A Survey on Personalized Alignment -- The Missing Piece for Large Language Models in Real-World Applications. ([Paper](https://arxiv.org/pdf/2503.17003))

### 2. Benchmark / Dataset / Evaluation

+ **\[2026 Arxiv-2609\]** VIBE-Bench: Evaluating Personalized Large Language Models When Profiles Don't Mean Preferences. ([Paper](http://arxiv.org/pdf/2609.00921v1))
+ **\[2026 Arxiv-2608\]** Evaluating the Hidden Costs of Personalization in Large Language Models. ([Paper](http://arxiv.org/pdf/2608.28833v1))
+ **\[2026 Arxiv-2608\]** PersonaMem-v3: Toward Omni-Platform Personal Intelligence for Holistic User Understanding, Recommendation, and Agentic Tasks. ([Paper](http://arxiv.org/pdf/2608.21381v1))

+ **\[2026 Arxiv-2608\]** Beyond Task-Only Matching: Personalized Skill Routing with Counterfactual Evaluation. ([Paper](http://arxiv.org/pdf/2608.28241))
+ **\[2026 Arxiv-2608\]** Behavior2Trip: Towards Personalized Travel Planning via User Behavior Trajectory. ([Paper](http://arxiv.org/pdf/2608.26807))

+ **\[2026 Arxiv-2608\]** PersonalBench: Measuring the Authorship Gap in LLM Personalization. ([Paper](http://arxiv.org/pdf/2608.19746v1))
+ **\[2026 Arxiv-2608\]** Act2Intention: A Benchmark For Developing Active Mobile Agents Through Inferring User Intention from GUI Actions. ([Paper](http://arxiv.org/pdf/2608.14132))

+ **\[2026 Arxiv-2608\]** When Personal Memory Has No Single Answer: Evaluating LLM Agents under Irreducible Conflict. ([Paper](http://arxiv.org/pdf/2608.13921v1))
+ **\[2026 Arxiv-2608\]** WebRider: Persona-Conditioned Intent Controllers for Live-Web Assistance. ([Paper](http://arxiv.org/pdf/2608.06704))

+ **\[2026 Arxiv-2608\]** Do AI Personas Grow? Analyzing and Benchmarking Personality Evolution in LLM Agents After Life Events. ([Paper](http://arxiv.org/pdf/2608.06485v1))
+ **\[2026 Arxiv-2608\]** Evaluating Investment Logic in Large Language Models: A Real-World Benchmark Towards Personalzied Financial Agents. ([Paper](http://arxiv.org/pdf/2608.06108))
+ **\[2026 Arxiv-2608\]** LUNAR: Benchmarking Personalized Large Language Models on UNiversal User BehAvioR Logs. ([Paper](http://arxiv.org/pdf/2608.05246v1))
+ **\[2026 Arxiv-2608\]** The Personalization Mirage: How LLMs Fabricate User Profiles, and Why Self-Monitoring Misleads. ([Paper](http://arxiv.org/pdf/2608.04570v1))
+ **\[2026 Arxiv-2608\]** FinPerMA: A Theory-Informed, Event-Grounded Personalized-Memory Benchmark for LLM Agents. ([Paper](http://arxiv.org/pdf/2608.04095v1))
+ **\[2026 Arxiv-2608\]** PAST-Bench: Benchmarking the Foundations of Recursive Self-Improvement in Personal Agents. ([Paper](http://arxiv.org/pdf/2608.04003))

+ **\[2026 Arxiv-2608\]** From Profiling to Synthesis: Benchmarking Implicit Behavioral Alignment in Personalized LLM Agents. ([Paper](http://arxiv.org/pdf/2608.02171v1))
+ **\[2026 Arxiv-2607\]** Beyond Borrowed Histories: Person-Aligned User Simulation for Interactive Role-Playing Evaluation. ([Paper](http://arxiv.org/pdf/2607.27816v2))
+ **\[2026 Arxiv-2607\]** Setoka: A Benchmark for Hierarchical User Understanding in Personalized Agents over Heterogeneous Data. ([Paper](http://arxiv.org/pdf/2607.27056))
+ **\[2026 Arxiv-2607\]** Fewer Clarifications, Better Code: Benchmarking Cross-Session Personalized Ambiguity Adaptation in Coding Assistants. ([Paper](http://arxiv.org/pdf/2607.26611))
+ **\[2026 Arxiv-2607\]** ClawRec: A Claw-Native Recommender System. ([Paper](http://arxiv.org/pdf/2607.23779))
+ **\[2026 Arxiv-2607\]** APeB: Benchmarking Personalization Ability of Large Language Model Agents. ([Paper](http://arxiv.org/pdf/2607.03162v1))
+ **\[2026 Arxiv-2607\]** Benchmarking the Personalization Capabilities of Large Language Models. ([Paper](http://arxiv.org/pdf/2607.20471v1))
+ **\[2026 Arxiv-2606\]** DynamicMem: A Long-Horizon Memory Benchmark in Real-World Settings. ([Paper](http://arxiv.org/pdf/2606.22877v1))
+ **\[2026 Arxiv-2605\]** DirectorBench: Diagnosing Long-Form Video Generation with Personalized Multi-Agent Evaluation. ([Paper](http://arxiv.org/pdf/2605.30090))
+ **\[2026 Arxiv-2605\]** GroupTravelBench: Benchmarking LLM Agents on Multi-Person Travel Planning. ([Paper](http://arxiv.org/pdf/2605.25200v2))
+ **\[2026 Arxiv-2605\]** MemConflict: Evaluating Long-Term Memory Systems Under Memory Conflicts. ([Paper](http://arxiv.org/pdf/2605.20926v1))
+ **\[2026 Arxiv-2605\]** $π$-Bench: Evaluating Proactive Personal Assistant Agents in Long-Horizon Workflows. ([Paper](http://arxiv.org/pdf/2605.14678v3))
+ **\[2026 Arxiv-2605\]** GroupMemBench: Benchmarking LLM Agent Memory in Multi-Party Conversations. ([Paper](http://arxiv.org/pdf/2605.14498v2))

+ **\[2026 Arxiv-2607\]** Toward User-Conditioned Evaluation of Personal LLM Agents under Temporal Interventions. ([Paper](http://arxiv.org/pdf/2607.21635v1))
+ **\[2026 Arxiv-2607\]** PersonaTrail: Benchmarking Personalized Web Agents through Browsing Trails. ([Paper](http://arxiv.org/pdf/2607.20482v1))
+ **\[2026 Arxiv-2607\]** SenWorld: A Digital-Twin Simulation for Generating Context-Rich Evaluation Data. ([Paper](http://arxiv.org/pdf/2607.19949v2))
+ **\[2026 Arxiv-2607\]** DRIFTLENS: Measuring Memory-Induced Reasoning Drift in Personalized Language Models. ([Paper](http://arxiv.org/pdf/2607.02374v1))

+ **\[2026 Arxiv-2606\]** SocialPersona: Benchmarking Personalized Profiling and Response with Multimodal Social-Media Context. ([Paper](http://arxiv.org/pdf/2606.26654v1))

+ **\[2026 Arxiv-2606\]** PEC-Home: Interpretation of Progressively Elliptical Commands in Smart Homes. ([Paper](http://arxiv.org/pdf/2606.18636v1))
+ **\[2026 Arxiv-2606\]** Evaluating LLM Personalization via Semantic Constraint Verification. ([Paper](http://arxiv.org/pdf/2606.16368v1))

+ **\[2026 Arxiv-2606\]** Whose Norms? Disentangling Cultural and Personal Alignment in Large Language Models. ([Paper](http://arxiv.org/pdf/2606.07877v1))
  
+ **\[2026 Arxiv-2606\]** Re-Centering Humans in LLM Personalization. ([Paper](http://arxiv.org/pdf/2606.06614v1))

+ **\[2026 Arxiv-2606\]** SenseJudge: Human-Centric Preference-Driven Judgment Framework. ([Paper](http://arxiv.org/pdf/2606.03189v2))
+ **\[2026 Arxiv-2606\]** $Ψ$-Bench: Evaluating Persona-Sensitive Influencing in Persuasive Dialogues. ([Paper](http://arxiv.org/pdf/2606.02754v1))

+ **\[2026 CVPR\]** PersonaVLM — Long-Term Personalized Multimodal LLMs. ([Paper](https://arxiv.org/pdf/2604.13074), [Data](https://huggingface.co/datasets/ClareNie/Persona-MME))

+ **\[2026 Arxiv-2605\]** Preference-Aware Rubric Learning for Personalized Evaluation. ([Paper](http://arxiv.org/pdf/2605.31545v1))
+ **\[2026 Arxiv-2605\]** Beyond Static Dialogues: Benchmarking Realistic, Heterogeneous, and Evolving Long-Term Memory. ([Paper](http://arxiv.org/pdf/2605.31086v2))
+ **\[2026 Arxiv-2605\]** Ask Now, Use Later: Benchmarking the Proactivity Gap in Long-Lived LLM Agents. ([Paper](http://arxiv.org/pdf/2605.28108v2))

+ **\[2026 Arxiv-2605\]** ChildEval: When large language models meet children's personalities. ([Paper](http://arxiv.org/pdf/2605.27805))

+ **\[2026 Arxiv-2605\]** VitaBench 2.0: Evaluating Personalized and Proactive Agents in Long-Term User Interactions. ([Paper](http://arxiv.org/pdf/2605.27141v1))
+ **\[2026 Arxiv-2605\]** Claw-Anything: Benchmarking Always-On Personal Assistants with Broader Access to User's Digital World. ([Paper](http://arxiv.org/pdf/2605.26086v1))
+ **\[2026 Arxiv-2605\]** StreamProfileBench: A Benchmark for Fine-Grained User Profile Inference in Real-World Streaming Scenarios. ([Paper](http://arxiv.org/pdf/2605.25758v3))
+ **\[2026 Arxiv-2605\]** Personalize-then-Store: Benchmarking and Learning Personalized Memory for Long-horizon Agents. ([Paper](http://arxiv.org/pdf/2605.25535v1))

+ **\[2026 Arxiv-2605\]** Think Thrice Before You Speak: Dual knowledge-enhanced Theory-of-Mind Reasoning for Persuasive Agents. ([Paper](http://arxiv.org/pdf/2605.22602))
  
+ **\[2026 Arxiv-2605\]** Psy-Chronicle:A Structured Pipeline for Synthesizing Long-Horizon Campus Psychological Counseling Dialogues. ([Paper](http://arxiv.org/pdf/2605.22140))
  
+ **\[2026 Arxiv-2605\]** APM: Evaluating Style Personalization in LLMs with Arbitrary Preference Mappings. ([Paper](http://arxiv.org/pdf/2605.21063))

+ **\[2026 Arxiv-2605\]** Personalized Deep Research: A User-Centric Framework, Dataset, and Hybrid Evaluation for Knowledge Discovery. ([Paper](http://arxiv.org/pdf/2605.10530v1))

+ **\[2026 Arxiv-2605\]** STALE: Can LLM Agents Know When Their Memories Are No Longer Valid?. ([Paper](http://arxiv.org/pdf/2605.06527v1))

+ **\[2026 Arxiv-2604\]** Personalized Benchmarking: Evaluating LLMs by Individual Preferences. ([Paper](http://arxiv.org/pdf/2604.18943v1))

+ **\[2026 Arxiv-2604\]** KnowU-Bench: A Benchmark for Personalized Agents with User Profiles in E-Commerce. ([Paper](https://arxiv.org/pdf/2604.08455), [Code](https://github.com/ZJU-REAL/KnowU-Bench))


+ **\[2026 Arxiv-2604\]** Beyond Static Personas: Situational Personality Steering for Large Language Models. ([Paper](http://arxiv.org/pdf/2604.13846v3))


+ **\[2026 Arxiv-2604\]** TSUBASA: Improving Long-Horizon Personalization via Evolving Memory and Self-Learning with Context Distillation. ([Paper](http://arxiv.org/pdf/2604.07894v1))


+ **\[2026 Arxiv-2604\]** Personalized RewardBench: Evaluating Reward Models with Human Aligned Personalization. ([Paper](https://arxiv.org/pdf/2604.07343))

+ **\[2026 Arxiv-2604\]** Stories of Your Life as Others: A Round-Trip Evaluation of LLM-Generated Life Stories Conditioned on Rich Psychometric Profiles. ([Paper](https://arxiv.org/pdf/2604.06071))

+ **\[2026 Arxiv-2604\]** Ego-Grounding for Personalized Question-Answering in Egocentric Videos. ([Paper](https://arxiv.org/pdf/2604.01966), [Code](https://github.com/Ryougetsu3606/MyEgo))

+ **\[2026 Arxiv-2603\]** AlpsBench: An LLM Personalization Benchmark for Real-Dialogue Memorization and Preference Alignment. ([Paper](https://arxiv.org/pdf/2603.26680v2))

+ **\[2026 Arxiv-2603\]** PSPA-Bench: A Personalized Benchmark for Smartphone GUI Agent. ([Paper](https://arxiv.org/pdf/2603.29318))

+ **\[2026 Arxiv-2603\]** Mimetic Alignment with ASPECT: Evaluation of AI-inferred Personal Profiles. ([Paper](https://arxiv.org/pdf/2603.26922))

+ **\[2026 Arxiv-2603\]** MemoryCD: Benchmarking Long-Context User Memory of LLM Agents for Lifelong Cross-Domain Personalization. ([Paper](https://arxiv.org/pdf/2603.25973))

+ **\[2026 Arxiv-2603\]** PICon: A Multi-Turn Interrogation Framework for Evaluating Persona Agent Consistency. ([Paper](https://arxiv.org/pdf/2603.25620))

+ **\[2026 Arxiv-2603\]** PERMA: Benchmarking Personalized Memory Agents via Event-Driven Preference and Realistic Task Environments. ([Paper](https://arxiv.org/pdf/2603.23231))

+ **\[2026 Arxiv-2602\]** AgenticShop: Benchmarking Agentic Product Curation for Personalized Web Shopping. ([Paper](https://arxiv.org/pdf/2602.12315))

+ **\[2026 Arxiv-2602\]** Persona2Web: Learning Personalized Agents from User Preferences and Habits for Personalized Web Service. ([Paper](https://arxiv.org/pdf/2602.17003))

+ **\[2026 Arxiv-2601\]** EmoHarbor: Evaluating Personalized Emotional Support by Simulating the User's Internal World. ([Paper](https://arxiv.org/pdf/2601.01530))

+ **\[2025 Arxiv-2512\]** The Mental World of Large Language Models in Recommendation: A Benchmark on Association, Personalization, and Knowledgeability. ([Paper](https://arxiv.org/pdf/2512.17389))

+ **\[2025 Arxiv-2509\]** BESPOKE: Benchmark for Search-Augmented Large Language Model Personalization via Diagnostic Feedback. ([Paper](https://arxiv.org/pdf/2509.21106), [Code](https://augustinlib.github.io/BESPOKE/))

+ **\[2025 Arxiv-2508\]** CAPE: Context-Aware Personality Evaluation Framework for Large Language Models. ([Paper](https://arxiv.org/pdf/2508.20385))

+ **\[2025 Arxiv-2509\]** PerFairX: Is There a Balance Between Fairness and Personality in Large Language Model Recommendations? ([Paper](https://arxiv.org/pdf/2509.08829))

+ **\[2025 ICLR\]** Neuron-based Personality Trait Induction in Large Language Models. ([Paper](https://openreview.net/forum?id=LYHEY783Np))

+ **\[2025 ICLR\]** Personality Alignment of Large Language Models. ([Paper](https://openreview.net/forum?id=0DZEs8NpUH))

+ **\[2025 ICLR\]** Do LLMs Recognize Your Preferences? Evaluating Personalized Preference Following in LLMs. ([Paper](https://openreview.net/forum?id=QWunLKbBGF))

+ **\[2025 Arxiv-2505\]** LaMP-QA: A Benchmark for Personalized Long-form Question Answering. ([Paper](https://arxiv.org/pdf/2506.00137), [Code](https://github.com/LaMP-Benchmark/LaMP-QA))

+ **\[2025 AAAI\]** CharacterBench: Benchmarking Character Customization of Large Language Models. ([Paper](https://arxiv.org/pdf/2412.11912), [Code](https://github.com/thu-coai/CharacterBench))

+ **\[2024 Arxiv-2412\]** Can Large Language Models Understand You Better? An MBTI Personality Detection Dataset Aligned with Population Traits. ([Paper](https://arxiv.org/pdf/2412.12510), [Code](https://github.com/Personality-NLP/MbtiBench))

+ **\[2024 Arxiv-2407\]** LongLaMP: A Benchmark for Personalized Long-form Text Generation. ([Paper](https://arxiv.org/pdf/2407.11016), [Code](https://longlamp-benchmark.github.io/Papers))

+ **\[2024 ACL\]** LaMP: When Large Language Models Meet Personalization. ([Paper](https://aclanthology.org/2024.acl-long.399.pdf), [Code](https://lamp-benchmark.github.io/))

+ **\[2024 NeurIPS\]** PersonalSum: A User-Subjective Guided Personalized Summarization Dataset for Large Language Models. ([Paper](https://arxiv.org/pdf/2410.03905), [Code](https://github.com/SmartmediaAI/PersonalSum))

+ **\[2024 EMNLP\]** Can LLM be a Personalized Judge? ([Paper](https://arxiv.org/pdf/2406.11657), [Code](https://github.com/dong-river/Personalized-Judge))

### 3. Memory / Retrieval-based Methods

+ **\[2026 Arxiv-2609\]** Inferring Hidden User Models from the Behavior of Personalized LLM Agents. ([Paper](http://arxiv.org/pdf/2609.03815v1))
+ **\[2026 Arxiv-2608\]** LINE Conversation History Retrieval for Personal Memory RAG: Evaluating Search Representations and Hybrid Retrieval. ([Paper](http://arxiv.org/pdf/2608.27809v1))
+ **\[2026 Arxiv-2608\]** Enhancing Group Recommendation with Memory-Augmented Reasoning in LLM Agent. ([Paper](http://arxiv.org/pdf/2608.21939v1))

+ **\[2026 Arxiv-2609\]** CAPTURE: Disentangling Preference Drift from Memory Poisoning in Personalized LLM Agents. ([Paper](http://arxiv.org/pdf/2609.02265))
+ **\[2026 Arxiv-2608\]** hoBIT: A Profile-Aware Retrieval-Augmented Chatbot for University Academic Advising. ([Paper](http://arxiv.org/pdf/2608.26604))
+ **\[2026 Arxiv-2608\]** Learning What to Share and What to Personalize: Hierarchical Strategy Co-Evolution for Agent Memory. ([Paper](http://arxiv.org/pdf/2608.25329))

+ **\[2026 Arxiv-2608\]** rEDMRec: Distilling Large Language Model Reasoning into an Editable Experience Memory for Recommendation. ([Paper](http://arxiv.org/pdf/2608.18952v1))
+ **\[2026 Arxiv-2608\]** QUMem: Personalized Memory for Query-Conditioned User-State Inference in LLM Agents. ([Paper](http://arxiv.org/pdf/2608.16168v1))
+ **\[2026 Arxiv-2608\]** CogChat: Knowledge Graph-Augmented Conversational AI with Heterogeneous Graph Transformer for Cognitive Grounding in Design Generation. ([Paper](http://arxiv.org/pdf/2608.13216))
+ **\[2026 Arxiv-2608\]** MindMemOS: A Portable and Self-Evolving Memory Operating Layer for AI Agents. ([Paper](http://arxiv.org/pdf/2608.12428))
+ **\[2026 Arxiv-2608\]** Sci-Surf: Navigating Scientific Literature Discovery through Human Feedback and Intelligent Summarization. ([Paper](http://arxiv.org/pdf/2608.11973))

+ **\[2026 Arxiv-2608\]** Hierarchical Compositionality for An Assistive AI Agent. ([Paper](http://arxiv.org/pdf/2608.10330v1))
+ **\[2026 Arxiv-2608\]** Learning Preference Adaptation for Large Language Model Personalization via Verbal Reinforcement Learning. ([Paper](http://arxiv.org/pdf/2608.09507v2))
+ **\[2026 Arxiv-2608\]** Muscle Memory for Agents: Compile not Merely Retrieve. ([Paper](http://arxiv.org/pdf/2608.08995))

+ **\[2026 Arxiv-2608\]** Embedding Large Language Models into Flow Controls: An Agentic Framework for Adaptive and Trustworthy Automated Cooking. ([Paper](http://arxiv.org/pdf/2608.04768v1))
+ **\[2026 Arxiv-2608\]** DP-MemView: A Memory Interface for Attribute-Level Transcript Privacy in Long-Term LLM Agents. ([Paper](http://arxiv.org/pdf/2608.03130))
+ **\[2026 Arxiv-2608\]** PGMem: Tightly Coupled Persona-Memory Graph for Lifelong Personalized Agents. ([Paper](http://arxiv.org/pdf/2608.01708))

+ **\[2026 Arxiv-2607\]** Know It, Act on It: Investigating Memory Utilization in LLM Personalization. ([Paper](http://arxiv.org/pdf/2607.29433v1))
+ **\[2026 Arxiv-2607\]** LoopMemGR: From Behavior Logs to Evolving Memory for Generative Recommendation. ([Paper](http://arxiv.org/pdf/2607.27647))
+ **\[2026 Arxiv-2607\]** InferScale: GPU-Native KV Injection for Personalized LLM Serving. ([Paper](http://arxiv.org/pdf/2607.27090v1))
+ **\[2026 Arxiv-2607\]** Learning Dynamic User Personas from Implicit Interaction Streams via Iterative Refinement. ([Paper](http://arxiv.org/pdf/2607.26473v1))
+ **\[2026 Arxiv-2606\]** Latent Personal Memory: Represent personal memory as dynamic soft prompts. ([Paper](http://arxiv.org/pdf/2606.20911v1))
+ **\[2026 Arxiv-2606\]** MemToolAgent: Leveraging Memory for Tool Using Agents Based on Environment and User Feedback. ([Paper](http://arxiv.org/pdf/2606.07909v2))
+ **\[2026 Arxiv-2605\]** Know You Before You Speak: User-State Modeling for LLM Personalization in Multi-Turn Conversation. ([Paper](http://arxiv.org/pdf/2605.24647v1))
+ **\[2026 Arxiv-2605\]** From Volume to Value: Preference-Aligned Memory Construction for On-Device RAG. ([Paper](http://arxiv.org/pdf/2605.18271v2))
+ **\[2026 Arxiv-2605\]** Agentic Recommender System with Hierarchical Belief-State Memory. ([Paper](http://arxiv.org/pdf/2605.14401v2))
+ **\[2026 Arxiv-2605\]** AwareLLM: A Proactive Multimodal Ecosystem for Personalized Human-AI Collaboration to Enhance Productivity. ([Paper](http://arxiv.org/pdf/2605.09625v2))

+ **\[2026 Arxiv-2607\]** Personalized Recommendation Tool Learning via Autonomous Language Agents. ([Paper](http://arxiv.org/pdf/2607.19739v1))

+ **\[2026 Arxiv-2607\]** Seeing and Reflecting: Multimodal Memory-Enhanced Agent Collaboration for Recommendation. ([Paper](http://arxiv.org/pdf/2607.07108v1))
+ **\[2026 Arxiv-2607\]** When Agents Remember Too Much: Memory Poisoning Attacks on Large Language Model Agents. ([Paper](http://arxiv.org/pdf/2607.06595v1))

+ **\[2026 Arxiv-2607\]** CoPersona: Collaborative Persona Graphs for Robust LLM Personalization. ([Paper](http://arxiv.org/pdf/2607.01485v1))

+ **\[2026 Arxiv-2607\]** Learning User-Aware Recall: Personalized Retrieval in Long-Term Conversational Memory. ([Paper](http://arxiv.org/pdf/2607.00017v2))

+ **\[2026 Arxiv-2606\]** TRUSTMEM: Learning Trustworthy Memory Consolidation for LLM Agents with Long-Term Memory. ([Paper](http://arxiv.org/pdf/2606.25161v1))
+ **\[2026 Arxiv-2606\]** Towards Root Memories: Benchmarking and Enhancing Implicit Logical Memory Retrieval for Personalized LLMs. ([Paper](http://arxiv.org/pdf/2606.23283v1))
+ **\[2026 Arxiv-2606\]** Wireless Personal Agent: Extending Wireless Intelligence from Networks to Terminals. ([Paper](http://arxiv.org/pdf/2606.23255v1))

+ **\[2026 Arxiv-2606\]** AtomMem: Building Simple and Effective Memory System for LLM Agents via Atomic Facts. ([Paper](http://arxiv.org/pdf/2606.19847v1))

+ **\[2026 Arxiv-2606\]** Statistical Priors for Implicit Preferences: Decoupling Skill Selection as a Local Harness in Personal Agents. ([Paper](http://arxiv.org/pdf/2606.05828v1))

+ **\[2026 Arxiv-2606\]** Beyond Isolated Behaviors: Hierarchical User Modeling for LLM Personalization. ([Paper](http://arxiv.org/pdf/2606.02300v1))

+ **\[2026 CVPR\]** PersonaVLM — Long-Term Personalized Multimodal LLMs. ([Paper](https://arxiv.org/pdf/2604.13074), [Code](https://github.com/MiG-NJU/PersonaVLM))

+ **\[2026 Arxiv-2605\]** MemGuard: Preventing Memory Contamination in Long-Term Memory-Augmented Large Language Models. ([Paper](http://arxiv.org/pdf/2605.28009))

+ **\[2026 Arxiv-2605\]** Personalizing Embodied Multimodal Large Language Model Agents over Long-term User Interactions. ([Paper](http://arxiv.org/pdf/2605.26256v1))

+ **\[2026 Arxiv-2605\]** DeferMem: Query-Time Evidence Distillation via Reinforcement Learning for Long-Term Memory QA. ([Paper](http://arxiv.org/pdf/2605.22411))
  
+ **\[2026 Arxiv-2605\]** EmoTrack: Robust Depression Tracking from Counseling Transcripts across Session Regimes. ([Paper](http://arxiv.org/pdf/2605.22286))
  
+ **\[2026 Arxiv-2605\]** CALMem : Application-Layer Dual Memory for Conversational AI. ([Paper](http://arxiv.org/pdf/2605.20724))
  
+ **\[2026 Arxiv-2605\]** Rethinking How to Remember: Beyond Atomic Facts in Lifelong LLM Agent Memory. ([Paper](http://arxiv.org/pdf/2605.19952))

+ **\[2026 Arxiv-2604\]** Response-Aware User Memory Selection for LLM Personalization. ([Paper](http://arxiv.org/pdf/2604.14473v1))


+ **\[2026 Arxiv-2604\]** HingeMem: Boundary Guided Long-Term Memory with Query Adaptive Retrieval for Scalable Dialogues. ([Paper](https://arxiv.org/pdf/2604.06845))

+ **\[2026 Arxiv-2604\]** SensorPersona: An LLM-Empowered System for Continual Persona Extraction from Longitudinal Mobile Sensor Streams. ([Paper](https://arxiv.org/pdf/2604.06204))

+ **\[2026 Arxiv-2604\]** FileGram: Grounding Agent Personalization in File-System Behavioral Traces. ([Paper](https://arxiv.org/pdf/2604.04901))

+ **\[2026 Arxiv-2604\]** MemMachine: A Ground-Truth-Preserving Memory System for Personalized AI Agents. ([Paper](https://arxiv.org/pdf/2604.04853))

+ **\[2026 AAAI\]** Orion: A Personalized Web Agent with Global-Micro Profiling and Adaptive Intent Tracking. ([Paper](https://ojs.aaai.org/index.php/AAAI/article/view/40188))

+ **\[2026 Arxiv-2603\]** MemRerank: Preference Memory for Personalized Product Reranking. ([Paper](https://arxiv.org/pdf/2603.29247))

+ **\[2026 Arxiv-2602\]** Learning to Reason for Multi-Step Retrieval of Personal Context in Personalized Question Answering. ([Paper](https://arxiv.org/pdf/2602.19317))

+ **\[2026 Arxiv-2601\]** Improving User Privacy in Personalized Generation: Client-Side Retrieval-Augmented Modification of Server-Side Generated Speculations. ([Paper](https://arxiv.org/pdf/2601.17569))

+ **\[2026 Arxiv-2601\]** Optimizing User Profiles via Contextual Bandits for Retrieval-Augmented LLM Personalization. ([Paper](https://arxiv.org/pdf/2601.12078))

+ **\[2026 Arxiv-2601\]** Bi-Mem: Bidirectional Construction of Hierarchical Memory for Personalized LLMs via Inductive-Reflective Agents. ([Paper](https://arxiv.org/pdf/2601.06490))

+ **\[2026 Arxiv-2601\]** Me-Agent: A Personalized Mobile Agent with Two-Level User Habit Learning. ([Paper](https://arxiv.org/pdf/2601.20162))

+ **\[2026 Arxiv-2601\]** Inside Out: Evolving User-Centric Core Memory Trees for Long-Term Personalized Dialogue Systems. ([Paper](https://arxiv.org/pdf/2601.05171))

+ **\[2025 Arxiv-2501\]** Personalized Graph-Based Retrieval for Large Language Models. ([Paper](https://arxiv.org/pdf/2501.02157), [Code](https://github.com/PGraphRAG-benchmark/PGraphRAG))

+ **\[2025 ICLR\]** SeCom: On Memory Construction and Retrieval for Personalized Conversational Agents. ([Paper](https://openreview.net/forum?id=xKDZAW0He3))

+ **\[2024 Arxiv-2406\]** STEP-BACK PROFILING: Distilling User History for Personalized Scientific Writing. ([Paper](https://arxiv.org/pdf/2406.14275), [Code](https://github.com/gersteinlab/step-back-profiling))

+ **\[2023 CIKM\]** Integrating Summarization and Retrieval for Enhanced Personalization via Large Language Models. ([Paper](https://arxiv.org/pdf/2310.20081))

+ **\[2024 Arxiv-2411\]** On the Way to LLM Personalization: Learning to Remember User Conversations. ([Paper](https://arxiv.org/pdf/2411.13405))

+ **\[2024 SIGIR\]** Optimization Methods for Personalizing Large Language Models through Retrieval Augmentation. ([Paper](https://dl.acm.org/doi/pdf/10.1145/3626772.3657783))

### 4. Prompt / Vector / Decoding-time Methods

+ **\[2026 Arxiv-2609\]** Prompt-Space Meta-Learning Does Not Transfer Across Users: A Frozen-LLM Negative Result. ([Paper](http://arxiv.org/pdf/2609.01615v1))

+ **\[2026 Arxiv-2608\]** Locating and Controlling Implicit Personalization in Large Language Models. ([Paper](http://arxiv.org/pdf/2608.11735))
+ **\[2026 Arxiv-2608\]** Role of Personality in Conversational Information Seeking. ([Paper](http://arxiv.org/pdf/2608.11164v1))
+ **\[2026 Arxiv-2608\]** Inverse Theory of Mind Modeling for Content Recommendation: From Web Browsing to Dynamic Intelligent Interfaces. ([Paper](http://arxiv.org/pdf/2608.11354))

+ **\[2026 Arxiv-2606\]** Beyond Retrieval: Learning Compact User Representations for Scalable LLM Personalization. ([Paper](http://arxiv.org/pdf/2606.04547v2))

+ **\[2026 Arxiv-2607\]** PrefReward: Learning User Preference Matrix for Personalized Text Generation. ([Paper](http://arxiv.org/pdf/2607.21067v1))

+ **\[2026 Arxiv-2606\]** A Large-Language-Model Supported Personalized Driving Framework for Lane Change in Highway Scenarios. ([Paper](http://arxiv.org/pdf/2606.31483v2))

+ **\[2026 Arxiv-2606\]** Continuous Behavioral Synthesis for Adaptive Health Dashboards: An LLM-Mediated Architecture Integrating Explicit Preference, Spatial Reorganization, and Attention Allocation Signals. ([Paper](http://arxiv.org/pdf/2606.26937v1))

+ **\[2026 Arxiv-2606\]** Self-supervised User Profile Generation for Personalization. ([Paper](http://arxiv.org/pdf/2606.05336v1))

+ **\[2026 Arxiv-2605\]** LATTE: Forecasting Peer Anchored Preference Trajectories for Personalized LLM Generation. ([Paper](http://arxiv.org/pdf/2605.26612v1))
+ **\[2026 Arxiv-2605\]** MATO: Multi-objective Personalized Alignment with Test-time Optimization for Large Language Models. ([Paper](http://arxiv.org/pdf/2605.25342v1))

+ **\[2026 Arxiv-2605\]** Playing Devil's Advocate: Off-the-Shelf Persona Vectors Rival Targeted Steering for Sycophancy. ([Paper](http://arxiv.org/pdf/2605.21006))

+ **\[2026 Arxiv-2605\]** Capability Conditioned Scaffolding for Professional Human LLM Collaboration. ([Paper](http://arxiv.org/pdf/2605.15404v1))
  
+ **\[2026 Arxiv-2605\]** Tracing Persona Vectors Through LLM Pretraining. ([Paper](http://arxiv.org/pdf/2605.13329v1))
  
+ **\[2026 Arxiv-2605\]** Learning Transferable Latent User Preferences for Human-Aligned Decision Making. ([Paper](http://arxiv.org/pdf/2605.12682v1))

+ **\[2026 Arxiv-2605\]** CLIPer: Tailoring Diverse User Preference via Classifier-Guided Inference-Time Personalization. ([Paper](http://arxiv.org/pdf/2605.07162v1))

+ **\[2026 Arxiv-2604\]** MAESTRO: Adapting GUIs and Guiding Navigation with User Preferences in Conversational Agents with GUIs. ([Paper](https://arxiv.org/pdf/2604.06134))

+ **\[2026 Arxiv-2604\]** AdaptFuse: Training-Free Sequential Preference Learning via Externalized Bayesian Inference. ([Paper](https://arxiv.org/pdf/2604.03925))

+ **\[2026 Arxiv-2603\]** Persona Vectors in Games: Measuring and Steering Strategies via Activation Vectors. ([Paper](https://arxiv.org/pdf/2603.21398))

+ **\[2026 Arxiv-2602\]** Attn-GS: Attention-Guided Context Compression for Efficient Personalized LLMs. ([Paper](https://arxiv.org/pdf/2602.07778))

+ **\[2024 Arxiv-2408\]** Personalized Text Generation with Fine-Grained Linguistic Control. ([Paper](https://arxiv.org/pdf/2408.08103))

+ **\[2025 Arxiv-2512\]** Bring My Cup! Personalizing Vision-Language-Action Models with Visual Attentive Prompting. ([Paper](https://arxiv.org/pdf/2512.20014))

+ **\[2025 Arxiv-2512\]** The Geometry of Persona: Disentangling Personality from Reasoning in Large Language Models. ([Paper](https://arxiv.org/pdf/2512.07092))

+ **\[2025 Arxiv-2511\]** Moral Susceptibility and Robustness under Persona Role-Play in Large Language Models. ([Paper](https://arxiv.org/pdf/2511.08565))

+ **\[2025 Arxiv-2509\]** Harnessing Multimodal Large Language Models for Personalized Product Search with Query-aware Refinement. ([Paper](https://arxiv.org/pdf/2509.18682))

+ **\[2025 Arxiv-2509\]** Reasoning with Preference Constraints: A Benchmark for Language Models in Many-to-One Matching Markets. ([Paper](https://arxiv.org/pdf/2509.13131))

+ **\[2025 Arxiv-2506\]** PersonaAgent: When Large Language Model Agents Meet Personalization at Test Time. ([Paper](https://arxiv.org/pdf/2506.06254))

+ **\[2025 ICLR\]** Context Steering: Controllable Personalization at Inference Time. ([Paper](https://openreview.net/forum?id=xQCXInDq0m))

+ **\[2025 Arxiv-2503\]** Personalized Language Models via Privacy-Preserving Evolutionary Model Merging. ([Paper](https://arxiv.org/pdf/2503.18008))

+ **\[2025 Arxiv-2503\]** Personalized Text Generation with Contrastive Activation Steering. ([Paper](https://arxiv.org/pdf/2503.05213))

+ **\[2025 Arxiv-2501\]** Investigating Large Language Models in Inferring Personality Traits from User Conversations. ([Paper](https://arxiv.org/pdf/2501.07532))

+ **\[2024 Arxiv-2411\]** Unims-rag: A Unified Multi-source Retrieval-Augmented Generation for Personalized Dialogue Systems. ([Paper](https://arxiv.org/pdf/2401.13256))

+ **\[2024 Arxiv-2411\]** Orca: Enhancing Role-Playing Abilities of Large Language Models by Integrating Personality Traits. ([Paper](https://arxiv.org/pdf/2411.10006))

+ **\[2024 Arxiv-2410\]** Using Prompts to Guide Large Language Models in Imitating a Real Person's Language Style. ([Paper](https://arxiv.org/pdf/2410.03848))

+ **\[2024 Arxiv-2404\]** Dynamic Generation of Personalities with Large Language Models. ([Paper](https://arxiv.org/pdf/2404.07084v1))

+ **\[2024 WWW\]** Learning to Rewrite Prompts for Personalized Text Generation. ([Paper](https://arxiv.org/pdf/2310.00152))

+ **\[2024 EMNLP\]** Guided Profile Generation Improves Personalization with LLMs. ([Paper](https://arxiv.org/pdf/2409.13093))

### 5. SFT / RL / Preference Optimization Methods

+ **\[2026 Arxiv-2609\]** Aplaud: Adaptive Personalized Low-Rank Decomposition for User-Specific LLM. ([Paper](http://arxiv.org/pdf/2609.04738v1))
+ **\[2026 Arxiv-2609\]** PLUME: Parameter-Efficient Personalization of Large Language Models via Low-Rank User Modulation in Shared Subspaces. ([Paper](http://arxiv.org/pdf/2609.04715v1))
+ **\[2026 Arxiv-2609\]** Behaviorally Grounded User Profiles from the Wild for Personalized Alignment and Multi-Perspective Reasoning. ([Paper](http://arxiv.org/pdf/2609.00014v1))

+ **\[2026 Arxiv-2608\]** PersonaEdit: Representative Sample Selection for Personalized Model Editing. ([Paper](http://arxiv.org/pdf/2608.27816))

+ **\[2026 Arxiv-2608\]** Think-to-Personalize: Unifying Reasoning and Retrieval for User-Centric Personalized Dense Retrieval. ([Paper](http://arxiv.org/pdf/2608.18855v1))
+ **\[2026 Arxiv-2608\]** Ask to Be Sure: Informative Interactions for Confident Multi-Turn LLM Recommendation. ([Paper](http://arxiv.org/pdf/2608.15949v2))

+ **\[2026 Arxiv-2608\]** Learning from Online User Feedback for Shopping Agents. ([Paper](http://arxiv.org/pdf/2608.11604))
+ **\[2026 Arxiv-2608\]** From Prompting to Behavioral Alignment: Personalized LLM Judges for Recommendation Evaluation. ([Paper](http://arxiv.org/pdf/2608.11493v1))
+ **\[2026 Arxiv-2608\]** Weightless Fine-Tuning: Personalizing LLMs via Logit-Space Transport. ([Paper](http://arxiv.org/pdf/2608.11342v1))
+ **\[2026 Arxiv-2608\]** Learning to Adapt Cross-Domain Preferences via Meta-LoRA for LLM Personalization. ([Paper](http://arxiv.org/pdf/2608.12389v1))

+ **\[2026 Arxiv-2608\]** Cautious Context Steering for Language Model Personalization. ([Paper](http://arxiv.org/pdf/2608.05813v1))
+ **\[2026 Arxiv-2608\]** PALMs: Using Multi Construct-Grounded Rationales for Modeling Population Preferences in LLMs. ([Paper](http://arxiv.org/pdf/2608.01458))

+ **\[2026 Arxiv-2608\]** Rethinking Personalized Reward Modeling for LLMs under Preference Heterogeneity via Group-Debiased Federated Learning. ([Paper](http://arxiv.org/pdf/2608.01556v1))
+ **\[2026 Arxiv-2608\]** Personalizing Large Language Model Agents with Small Policy Models. ([Paper](http://arxiv.org/pdf/2608.00215v1))
+ **\[2026 Arxiv-2607\]** ODYSSE: Episode-wise Policy Optimization for Personalized Agentic Reasoning. ([Paper](http://arxiv.org/pdf/2607.25369))
+ **\[2026 Arxiv-2607\]** Group Preference Collapse in Personalized Multimodal Large Language Models. ([Paper](http://arxiv.org/pdf/2607.22603v1))
+ **\[2026 Arxiv-2606\]** Personalizing MLLMs via Reinforced Multimodal Reference Game. ([Paper](http://arxiv.org/pdf/2606.28845v1))
+ **\[2026 Arxiv-2606\]** PEBS: Per-rater Empirical-Bayes Shrinkage for RLHF Reward-Model Calibration. ([Paper](http://arxiv.org/pdf/2606.27578))
+ **\[2026 Arxiv-2606\]** ChatPlanner: A Large Language Model Framework for Personalized Public Transit Routing. ([Paper](http://arxiv.org/pdf/2606.15315v1))
+ **\[2026 Arxiv-2605\]** Spectral Souping: A Unified Framework for Online Preference Alignment. ([Paper](http://arxiv.org/pdf/2605.20408v1))
+ **\[2026 Arxiv-2605\]** Personalizing LLMs with Binary Feedback: A Preference-Corrected Optimization Framework. ([Paper](http://arxiv.org/pdf/2605.10043v1))
+ **\[2026 Arxiv-2605\]** Personalized Alignment Revisited: The Necessity and Sufficiency of User Diversity. ([Paper](http://arxiv.org/pdf/2605.09119v1))
+ **\[2026 Arxiv-2605\]** Test-Time Personalization: A Diagnostic Framework and Probabilistic Fix for Scaling Failures. ([Paper](http://arxiv.org/pdf/2605.10991v1))
+ **\[2026 Arxiv-2605\]** UserGPT Technical Report. ([Paper](http://arxiv.org/pdf/2605.08766v1))

+ **\[2026 Arxiv-2607\]** Personalized Image Aesthetic Assessment via Preference-rich Sample Mining and Cohort Merging. ([Paper](http://arxiv.org/pdf/2607.15752v1))
+ **\[2026 Arxiv-2607\]** Supervised Fine-Tuning vs. In-Context Learning: An Equilibrium Analysis of LLM Personalization under Congestion. ([Paper](http://arxiv.org/pdf/2607.14371v1))

+ **\[2026 Arxiv-2607\]** Persona Cartography: Charting Language Model Personality Traits in Weight Space. ([Paper](http://arxiv.org/pdf/2607.07916v1))

+ **\[2026 Arxiv-2606\]** REAR: Test-time Preference Realignment through Reward Decomposition. ([Paper](http://arxiv.org/pdf/2606.30339v1))

+ **\[2026 Arxiv-2606\]** ProfiLLM: Utility-Aligned Agentic User Profiling for Industrial Ride-Hailing Dispatch. ([Paper](http://arxiv.org/pdf/2606.18803v1))

+ **\[2026 Arxiv-2606\]** CFALR: Collaborative Filtering-Augmented Large Language Model for Personalized Fashion Outfit Recommendation. ([Paper](http://arxiv.org/pdf/2606.13001v1))
+ **\[2026 Arxiv-2606\]** Mult-DPO: Multinomial Direct Preference Optimization for Recommender Systems. ([Paper](http://arxiv.org/pdf/2606.10078v1))

+ **\[2026 Arxiv-2606\]** PAFO: Pareto Fairness Optimization for Personalized Reward Modeling. ([Paper](http://arxiv.org/pdf/2606.07988v1))
+ **\[2026 Arxiv-2606\]** Learning to Route LLMs from Implicit Cost-Performance Preferences via Meta-Learning. ([Paper](http://arxiv.org/pdf/2606.06178v1))

+ **\[2026 Arxiv-2606\]** TriAlign: Towards Universal Truth Consistency in Personalized LLM Alignment. ([Paper](http://arxiv.org/pdf/2606.01755v1))

+ **\[2026 Arxiv-2605\]** Federated Variational Preference Alignment with Gumbel-Softmax Prior for Personalized User Preferences. ([Paper](http://arxiv.org/pdf/2605.30873v1))

+ **\[2026 Arxiv-2605\]** Human Label Variation as Stable Signal: Learning Annotator-Specific Explanation Behavior via Cross-Annotator Preference Optimization. ([Paper](http://arxiv.org/pdf/2605.28802))
+ **\[2026 Arxiv-2605\]** Semantic Flow Regularization: Teaching LLMs to Generate Diverse Yet Coherent Responses. ([Paper](http://arxiv.org/pdf/2605.27971))

+ **\[2026 Arxiv-2605\]** L2Rec: Towards Dual-View Understanding of LLMs for Personalized Recommendation. ([Paper](http://arxiv.org/pdf/2605.26717v1))

+ **\[2026 Arxiv-2605\]** Unlocking Proactivity in Task-Oriented Dialogue. ([Paper](http://arxiv.org/pdf/2605.22240))

+ **\[2026 Arxiv-2604\]** One Model for All: Multi-Objective Controllable Language Models. ([Paper](http://arxiv.org/pdf/2604.04497v1))


+ **\[2026 Arxiv-2604\]** Many Preferences, Few Policies: Towards Scalable Language Model Personalization. ([Paper](https://arxiv.org/pdf/2604.04144))

+ **\[2026 Arxiv-2604\]** Uncertainty-Aware Variational Reward Factorization via Probabilistic Preference Bases for LLM Personalization. ([Paper](https://arxiv.org/pdf/2604.00997))

+ **\[2026 Arxiv-2603\]** EpiPersona: Persona Projection and Episode Coupling for Pluralistic Preference Modeling. ([Paper](https://arxiv.org/pdf/2603.28197))

+ **\[2026 Arxiv-2602\]** Learning Personalized Agents from Human Feedback. ([Paper](https://arxiv.org/pdf/2602.16173))

+ **\[2026 Arxiv-2602\]** Synthetic Interaction Data for Scalable Personalization in Large Language Models. ([Paper](https://arxiv.org/pdf/2602.12394))

+ **\[2026 Arxiv-2601\]** UserLM-R1: Modeling Human Reasoning in User Language Models with Multi-Reward Reinforcement Learning. ([Paper](https://arxiv.org/pdf/2601.09215))

+ **\[2025 Arxiv-2511\]** MTA: A Merge-then-Adapt Framework for Personalized Large Language Model. ([Paper](https://arxiv.org/pdf/2511.20072))

+ **\[2025 Arxiv-2511\]** Multimodal Large Language Models with Adaptive Preference Optimization for Sequential Recommendation. ([Paper](https://arxiv.org/pdf/2511.18740))

+ **\[2025 Arxiv-2511\]** Reflective Personalization Optimization: A Post-hoc Rewriting Framework for Black-Box Large Language Models. ([Paper](https://arxiv.org/pdf/2511.05286))

+ **\[2025 Arxiv-2510\]** Instant Personalized Large Language Model Adaptation via Hypernetwork. ([Paper](https://arxiv.org/pdf/2510.16282))

+ **\[2025 Arxiv-2510\]** POPI: Personalizing LLMs via Optimized Natural Language Preference Inference. ([Paper](https://arxiv.org/pdf/2510.17881))

+ **\[2025 Arxiv-2510\]** Asking Clarifying Questions for Preference Elicitation With Large Language Models. ([Paper](https://arxiv.org/pdf/2510.12015))

+ **\[2025 Arxiv-2509\]** Personas within Parameters: Fine-Tuning Small Language Models with Low-Rank Adapters to Mimic User Behaviors. ([Paper](https://arxiv.org/pdf/2509.09689))

+ **\[2025 Arxiv-2509\]** CBP-Tuning: Efficient Local Customization for Black-box Large Language Models. ([Paper](https://arxiv.org/pdf/2509.12112))

+ **\[2025 Arxiv-2508\]** Towards On-Device Personalization: Cloud-device Collaborative Data Augmentation for Efficient On-device Language Model. ([Paper](https://arxiv.org/pdf/2508.21313))

+ **\[2025 Arxiv-2508\]** Learning from Natural Language Feedback for Personalized Question Answering. ([Paper](https://arxiv.org/pdf/2508.10695))

+ **\[2025 Arxiv-2508\]** MM-R1: Unleashing the Power of Unified Multimodal Large Language Models for Personalized Image Generation. ([Paper](https://arxiv.org/pdf/2508.11433))

+ **\[2025 Arxiv-2508\]** End-to-End Personalization: Unifying Recommender Systems with Large Language Models. ([Paper](https://arxiv.org/pdf/2508.01514))

+ **\[2025 Arxiv-2508\]** CAP-LLM: Context-Augmented Personalized Large Language Models for News Headline Generation. ([Paper](https://arxiv.org/pdf/2508.03935))

+ **\[2025 Arxiv-2507\]** Persona Vectors: Monitoring and Controlling Character Traits in Language Models. ([Paper](https://arxiv.org/pdf/2507.21509))

+ **\[2025 Arxiv-2506\]** Personalized LLM Decoding via Contrasting Personal Preference. ([Paper](https://arxiv.org/pdf/2506.12109v1))

+ **\[2025 ICLR\]** Generative Adapter: Contextualizing Language Models in Parameters with A Single Forward Pass. ([Paper](https://openreview.net/forum?id=bc3sUsS6ck))

+ **\[2025 Arxiv-2503\]** DiffPO: Diffusion-styled Preference Optimization for Efficient Inference-Time Alignment of Large Language Models. ([Paper](https://arxiv.org/pdf/2503.04240), [Code](https://github.com/arctanxarc/MC-LLaVA))

+ **\[2025 Arxiv-2503\]** MC-LLaVA: Multi-Concept Personalized Vision-Language Model. ([Paper](https://arxiv.org/pdf/2503.18854), [Code](https://github.com/arctanxarc/MC-LLaVA))

+ **\[2025 Arxiv-2501\]** Personalized Language Model Learning on Text Data Without User Identifiers. ([Paper](https://arxiv.org/pdf/2501.06062), [Code](https://github.com/sjtu-yc/IDfree-Personalized-Learning))

+ **\[2024 Arxiv-2412\]** Personalizing Multimodal Large Language Models for Image Captioning: An Experimental Analysis. ([Paper](https://arxiv.org/pdf/2412.03665))

+ **\[2024 Arxiv-2410\]** LMLPA: Language Model Linguistic Personality Assessment. ([Paper](https://arxiv.org/pdf/2410.17632))

+ **\[2024 Arxiv-2409\]** LLMs + Persona-Plug = Personalized LLMs. ([Paper](https://arxiv.org/pdf/2409.11901))

+ **\[2024 Arxiv-2407\]** PEFT-U: Parameter-Efficient Fine-Tuning for User Personalization. ([Paper](https://arxiv.org/pdf/2407.18078), [Code](https://github.com/ChrisIsKing/Parameter-Efficient-Personalization))

+ **\[2024 Arxiv-2406\]** P-Tailor: Customizing Personality Traits for Language Models via Mixture of Specialized LoRA Experts. ([Paper](https://arxiv.org/pdf/2406.12548v1))

+ **\[2024 Arxiv-2404\]** Online Personalizing White-box LLMs Generation with Neural Bandits. ([Paper](https://arxiv.org/pdf/2404.16115))

+ **\[2024 EMNLP\]** Democratizing Large Language Models via Personalized Parameter-Efficient Fine-tuning. ([Paper](https://arxiv.org/pdf/2402.04401), [Code](https://github.com/TamSiuhin/OPPU))

+ **\[2024 EMNLP\]** Personalized Pieces: Efficient Personalized Large Language Models through Collaborative Efforts. ([Paper](https://arxiv.org/pdf/2406.10471), [Code](https://github.com/TamSiuhin/Per-Pcs))

+ **\[2024 NeurIPS\]** HYDRA: Model Factorization Framework for Black-Box LLM Personalization. ([Paper](https://arxiv.org/pdf/2406.02888v1))
