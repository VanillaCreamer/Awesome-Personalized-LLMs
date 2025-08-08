# Awesome Personalized Large Language Models
This repository collects the latest research progress on personalized large language models (LLMs), including preference alignment and user-customized generation. Comments and contributions are welcome.

> The contributions are expected to be submitted as follows:
> 
> `+ **\[Year Conference/Jounal\]** Title. ([Paper](link), [Code](link))`  (if accessible).

+ **\[2025 Arxiv-2503\]** Personalized Generation In Large Model Era: A Survey. ([Paper](https://arxiv.org/pdf/2503.02614))

+ **\[2024 Arxiv-2411\]** Personalization of Large Language Models: A Survey. ([Paper](https://arxiv.org/pdf/2411.00027))

## 1. Human Value Alignment

### 1.1 Survey/Tutorial/Framework

+ **\[2024 GitHub\]** Personalized LMs: Aligning Language Models with Diverse Human Preference. ([Link](https://github.com/allenai/compred))


### 1.2 Benchmark/Dataset

+ **\[2025 ICLR\]** DreamBench++: A Human-Aligned Benchmark for Personalized Image Generation. ([Paper](https://openreview.net/forum?id=4GSOESJrk6))

+ **\[2025 ICLR\]** DailyDilemmas: Revealing Value Preferences of LLMs with Quandaries of Daily Life. ([Paper](https://openreview.net/forum?id=PGhiPGBf47))

+ **\[2024 NeurIPS\]** The PRISM Alignment Project: What Participatory, Representative and Individualised Human Feedback Reveals About the Subjective and Multicultural Alignment of Large Language Models. ([Paper](https://arxiv.org/pdf/2404.16019), [Code](https://hannahkirk.github.io/prism-alignment/))

+ **\[2024 NeurIPS\]** Aligning to Thousands of Preferences via System Message Generalization. ([Paper](https://arxiv.org/pdf/2405.17977), [website](https://arxiv.org/pdf/2405.17977))

+ **\[2024 NeurIPS\]** Improving Context-Aware Preference Modeling for Language Models. ([Paper](https://arxiv.org/pdf/2407.14916))

+ **\[2023 Arxiv-2310\]** Personalized Soups: Personalized Large Language Model Alignment via Post-hoc Parameter Merging. ([Paper](https://arxiv.org/pdf/2310.11564), [Code](https://github.com/joeljang/RLPHF))

### 1.3 Fine-tuning-based Methods

+ **\[2025 ICLR\]** PAL: Sample-Efficient Personalized Reward Modeling for Pluralistic Alignment. ([Paper](https://openreview.net/forum?id=1kFDrYCuSu))


+ **\[2025 ICLR\]** MAP: Multi-Human-Value Alignment Palette. ([Paper](https://openreview.net/forum?id=NN6QHwgRrQ))

+ **\[2025 Arxiv-2504\]** Persona-judge: Personalized Alignment of Large Language Models via Token-level Self-judgment

+ **\[2025 Arxiv-2503\]** Language Model Personalization via Reward Factorization. ([Paper](https://arxiv.org/pdf/2503.06358), [Code](https://idanshen.github.io/PReF/))

+ **\[2024 Arxiv-2410\]** COMPO: Community Preferences for Language Model Personalization. ([Paper](https://arxiv.org/pdf/2410.16027))

+ **\[2024 Arxiv-2408\]** Personality Alignment of Large Language Models. ([Paper](https://arxiv.org/pdf/2408.11779), [Code](https://github.com/zhu-minjun/PAlign))

+ **\[2024 Arxiv-2407\]** Orchestrating LLMs with Different Personalizations. ([Paper](https://arxiv.org/pdf/2407.04181))

+ **\[2024 Arxiv-2405\]** Multi-Reference Preference Optimization for Large Language Models. ([Paper](https://arxiv.org/pdf/2405.16388))

+ **\[2024 Arxiv-2402\]** Personalized Language Modeling from Personalized Human Feedback. ([Paper](https://openreview.net/pdf?id=bqUsdBeRjQ))

+ **\[2024 ACL\]** Arithmetic Control of LLMs for Diverse User Preferences: Directional Preference Alignment with Multi-Objective Rewards. ([Paper](https://aclanthology.org/2024.acl-long.468.pdf), [Code](https://github.com/RLHFlow/Directional-Preference-Alignment))

+ **\[2024 EMNLP\]** On Diversified Preferences of Large Language Model Alignment. ([Paper](https://arxiv.org/pdf/2312.07401), [Code](https://github.com/dunzeng/MORE))

+ **\[2024 EMNLP\]** Learning Personalized Alignment for Evaluating Open-ended Text Generation. ([Paper](https://aclanthology.org/2024.emnlp-main.737.pdf))

+ **\[2024 EMNLP\]** BAPO: Base-Anchored Preference Optimization for Personalized Alignment in Large Language Models. ([Paper](https://aclanthology.org/2024.findings-emnlp.398.pdf))

+ **\[2024 EMNLP\]** Dynamic Multi-Reward Weighting for Multi-Style Controllable Generation. ([Paper](https://aclanthology.org/2024.emnlp-main.386.pdf), [Code](https://aclanthology.org/2024.emnlp-main.386.pdf))

+ **\[2024 ICML\]** MaxMin-RLHF: Alignment with Diverse Human Preferences. ([Paper](https://openreview.net/forum?id=8tzjEMF0Vq))

+ **\[2024 NeurIPS\]** Panacea: Pareto Alignment via Preference Adaptation for LLMs. ([Paper](https://arxiv.org/pdf/2402.02030))

+ **\[2024 NeurIPS\]** Personalized Steering of Large Language Models: Versatile Steering Vectors Through Bi-directional Preference Optimization. ([Paper](https://openreview.net/pdf?id=7qJFkuZdYo), [Code](https://github.com/CaoYuanpu/BiPO))

+ **\[2024 NeurIPS Workshop\]** Personalizing Reinforcement Learning from Human Feedback with Variational Preference Learning. ([Paper](https://openreview.net/pdf?id=zsXKtupv2I), [Code](https://github.com/WEIRDLabUW/vpl_llm), [website](https://weirdlabuw.github.io/vpl/))

+ **\[2024 PMLR\]** Rewards-in-Context: Multi-objective Alignment of Foundation Models with Dynamic Preference Adjustment. ([Paper](https://openreview.net/pdf?id=QLcBzRI3V3))

+ **\[2023 NeurIPS\]** Rewarded soups: towards Pareto-optimal alignment by interpolating weights fine-tuned on diverse rewards. ([Paper](https://proceedings.neurips.cc/Paper_files/Paper/2023/file/e12a3b98b67e8395f639fde4c2b03168-Paper-Conference.pdf), [Code](https://github.com/alexrame/rewardedsoups))




### 1.4 Training-free Methods

+ **\[2025 ICLR\]** On-the-fly Preference Alignment via Principle-Guided Decoding. ([Paper](https://openreview.net/forum?id=cfn2O1qvxp))

+ **\[2025 ICLR\]** PAD: Personalized Alignment of LLMs at Decoding-Time. ([Paper](https://arxiv.org/pdf/2410.04070))

+ **\[2025 Arxiv-2502\]** Drift: Decoding-time Personalized Alignments with Implicit User Preferences. ([paper](https://arxiv.org/pdf/2502.14289))

+ **\[2024 Arxiv-2410\]** Neuron-based Personality Trait Induction in Large Language Models. ([Paper](https://arxiv.org/pdf/2410.12327), [Code](https://github.com/RUCAIBox/NPTI))

+ **\[2024 Arxiv-2408\]** Unlocking Decoding-time Controllability: Gradient-Free Multi-Objective Alignment with Contrastive Prompts. ([Paper](https://arxiv.org/pdf/2408.05094))

+ **\[2024 ACL\]** Conditioned Language Policy: A General Framework for Steerable Multi-Objective Finetuning. ([Paper](https://aclanthology.org/2024.findings-emnlp.118.pdf))

+ **\[2024 EMNLP\]** Modular Pluralism: Pluralistic Alignment via Multi-LLM Collaboration. ([Paper](https://aclanthology.org/2024.emnlp-main.240.pdf), [Code](https://github.com/BunsenFeng/modular_pluralism/tree/main))

+ **\[2024 EMNLP\]** Controllable Preference Optimization: Toward Controllable Multi-Objective Alignment. ([Paper](https://aclanthology.org/2024.emnlp-main.85.pdf))

+ **\[2024 ICLR Workshop\]** Prompt Optimization with Logged Bandit Data. ([Paper](https://openreview.net/pdf?id=Byj8MMJmoL))

+ **\[2024 NeurIPS\]** Decoding-Time Language Model Alignment with Multiple Objectives. ([Paper](https://openreview.net/pdf?id=RmGvEmttB7))



## 2 Preference Alignment

### 2.1 Survey/Tutorial/Framework

+ **\[2025 Arxiv-2504\]** A Survey on Personalized and Pluralistic Preference Alignment in Large Language Models. ([Paper](https://arxiv.org/pdf/2504.07070))

+ **\[2024 EMNLP\]** Two Tales of Persona in LLMs: A Survey of Role-Playing and Personalization. ([Paper](https://arxiv.org/pdf/2406.01171), [Code](https://github.com/MiuLab/PersonaLLM-Survey))

+ **\[2024 Arxiv-2412\]** Personalized Multimodal Large Language Models: A Survey. ([Paper](https://arxiv.org/pdf/2412.02142))

+ **\[2024 Arxiv-2502\]** A Survey of Personalized Large Language Models: Progress and Future Directions. ([paper](https://arxiv.org/pdf/2502.11528))

+ **\[2024 Arxiv-2503\]** A Survey on Personalized Alignment -- The Missing Piece for Large Language Models in Real-World Applications. ([paper](https://arxiv.org/pdf/2503.17003))



### 2.2 Benchmark/Dataset

+ **\[2025 ICLR\]** Neuron-based Personality Trait Induction in Large Language Models. ([Paper](https://openreview.net/forum?id=LYHEY783Np))

+ **\[2025 ICLR\]** Personality Alignment of Large Language Models. ([Paper](https://openreview.net/forum?id=0DZEs8NpUH))

+ **\[2025 ICLR\]** PersonalLLM: Tailoring LLMs to Individual Preferences. ([Paper](https://openreview.net/forum?id=2R7498e2Tx))

+ **\[2025 ICLR\]** Do LLMs Recognize Your Preferences? Evaluating Personalized Preference Following in LLMs. ([Paper](https://openreview.net/forum?id=QWunLKbBGF))

+ **\[2025 Arxiv-2505\]** LaMP-QA: A Benchmark for Personalized Long-form Question Answering. ([Paper](https://arxiv.org/pdf/2506.00137), [Code](https://github.com/LaMP-Benchmark/LaMP-QA))

+ **\[2025 Arxiv-2501\]** Personalized Graph-Based Retrieval for Large Language Models. ([Paper](https://arxiv.org/pdf/2501.02157), [Code](https://github.com/PGraphRAG-benchmark/PGraphRAG))

+ **\[2025 WWW\]** Large Language Models Empowered Personalized Web Agents. ([Paper](https://arxiv.org/pdf/2410.17236), [Code](https://github.com/HongruCai/PersonalWAB))

+ **\[2025 AAAI\]** CharacterBench: Benchmarking Character Customization of Large Language Models. ([Paper](https://arxiv.org/pdf/2412.11912), [Code](https://github.com/thu-coai/CharacterBench))

+ **\[2024 Arxiv-2412\]** Can Large Language Models Understand You Better? An MBTI Personality Detection Dataset Aligned with Population Traits. ([Paper](https://arxiv.org/pdf/2412.12510), [Code](https://github.com/Personality-NLP/MbtiBench))

+ **\[2024 Arxiv-2410\]** Large Language Models Empowered Personalized Web Agents. ([Paper](https://arxiv.org/pdf/2410.17236), [Code](https://hongrucai.github.io/PersonalWAB/))

+ **\[2024 Arxiv-2407\]** PEFT-U: Parameter-Efficient Fine-Tuning for User Personalization. ([Paper](https://arxiv.org/pdf/2407.18078), [Code](https://github.com/ChrisIsKing/Parameter-Efficient-Personalization))

+ **\[2024 Arxiv-2407\]** LongLaMP: A Benchmark for Personalized Long-form Text Generation. ([Paper](https://arxiv.org/pdf/2407.11016), [Code](https://longlamp-benchmark.github.io/Papers))

+ **\[2024 Arxiv-2406\]** STEP-BACK PROFILING: Distilling User History for Personalized Scientific Writing. ([Paper](https://arxiv.org/pdf/2406.14275), [Code](https://github.com/gersteinlab/step-back-profiling))

+ **\[2024 ACL\]** LaMP: When Large Language Models Meet Personalization. ([Paper](https://aclanthology.org/2024.acl-long.399.pdf), [Code](https://lamp-benchmark.github.io/))

+ **\[2024 NeurIPS\]** PersonalSum: A User-Subjective Guided Personalized Summarization Dataset for Large Language Models. ([Paper](https://arxiv.org/pdf/2410.03905), [Code](https://github.com/SmartmediaAI/PersonalSum))

+ **\[2024 PERSONALIZE\]** Personalized Text Generation with Fine-Grained Linguistic Control. ([Paper](https://aclanthology.org/2024.personalize-1.8.pdf), [Code](https://github.com/balhafni/personalized-gen))

+ **\[2024 WI-IAT\]** Synthetic Data Generation with Large Language Models for Personalized Community Question Answering. ([Paper](https://arxiv.org/pdf/2410.22182))



### 2.3 Retrieval-Augmented Generation / Profile-Augmented Generation (RAG/PAG)-based Methods

+ **\[2025 Arxiv-2506\]** PersonaAgent: When Large Language Model Agents Meet Personalization at Test Time. ([Paper](https://arxiv.org/pdf/2506.06254))

+ **\[2025 ICLR\]** SeCom: On Memory Construction and Retrieval for Personalized Conversational Agents. ([Paper](https://openreview.net/forum?id=xKDZAW0He3))

+ **\[2025 ICLR\]** Amulet: ReAlignment During Test Time for Personalized Preference Adaptation of LLMs. ([Paper](https://openreview.net/forum?id=f9w89OY2cp))

+ **\[2025 ICLR\]** Context Steering: Controllable Personalization at Inference Time. ([Paper](https://openreview.net/forum?id=xQCXInDq0m))

+ **\[2025 Arxiv-2503\]** Personalized Language Models via Privacy-Preserving Evolutionary Model Merging. ([Paper](https://arxiv.org/pdf/2503.18008))

+ **\[2025 Arxiv-2503\]** Personalized Text Generation with Contrastive Activation Steering. ([Paper](https://arxiv.org/pdf/2503.05213))

+ **\[2025 Arxiv-2501\]** Investigating Large Language Models in Inferring Personality Traits from User Conversations. ([Paper](https://arxiv.org/pdf/2501.07532))

+ **\[2024 Arxiv-2411\]** Unims-rag A unified multi-source retrieval-augmented generation for personalized dialogue systems. ([Paper](https://arxiv.org/pdf/2401.13256))

+ **\[2024 Arxiv-2411\]** PIORS: Personalized Intelligent Outpatient Reception based on Large Language Model with Multi-Agents Medical Scenario Simulation. ([Paper](https://arxiv.org/pdf/2411.13902))

+ **\[2024 Arxiv-2411\]** Orca: Enhancing Role-Playing Abilities of Large Language Models by Integrating Personality Traits. ([Paper](https://arxiv.org/pdf/2411.10006)) 

+ **\[2024 Arxiv-2411\]** The Dark Patterns of Personalized Persuasion in Large Language Models: Exposing Persuasive Linguistic Features for Big Five Personality Traits in LLMs Responses. ([Paper](https://arxiv.org/pdf/2411.06008))

+ **\[2024 Arxiv-2410\]** Using Prompts to Guide Large Language Models in Imitating a Real Person's Language Style. ([Paper](https://arxiv.org/pdf/2410.03848))

+ **\[2024 Arxiv-2404\]** Dynamic Generation of Personalities with Large Language Models. ([Paper](https://arxiv.org/pdf/2404.07084v1), )

+ **\[2024 WWW\]** Learning to Rewrite Prompts for Personalized Text Generation. ([Paper](https://arxiv.org/pdf/2310.00152))

+ **\[2023 CIKM\]** Integrating Summarization and Retrieval for Enhanced Personalization via Large Language Models. ([Paper](https://arxiv.org/pdf/2310.20081))

+ **\[2024 EMNLP\]** Guided Profile Generation Improves Personalization with LLMs. ([Paper](https://arxiv.org/pdf/2409.13093))

+ **\[2024 SIGIR\]** Optimization Methods for Personalizing Large Language Models through Retrieval Augmentation. ([Paper](https://dlnext.acm.org/doi/pdf/10.1145/3626772.3657783), [Code](https://dlnext.acm.org/doi/pdf/10.1145/3626772.3657783))


### 2.4 Parameter-Efficient-Fine-Tuning (PEFT)-based Methods

+ **\[2025 Arxiv-2508\]** CAP-LLM: Context-Augmented Personalized Large Language Models for News Headline Generation. ([Paper](https://arxiv.org/pdf/2508.03935))

+ **\[2025 Arxiv-2507\]** Persona Vectors: Monitoring and Controlling Character Traits in Language Models. ([Paper](https://arxiv.org/pdf/2507.21509))

+ **\[2025 Arxiv-2506\]** Personalized LLM Decoding via Contrasting Personal Preference. ([Paper](https://arxiv.org/pdf/2506.12109v1))

+ **\[2025 ICLR\]** Generative Adapter: Contextualizing Language Models in Parameters with A Single Forward Pass. ([Paper](https://openreview.net/forum?id=bc3sUsS6ck))

+ **\[2025 Arxiv-2504\]** Energy-Based Reward Models for Robust Language Model Alignment.

+ **\[2025 Arxiv-2503\]** DiffPO: Diffusion-styled Preference Optimization for Efficient Inference-Time Alignment of Large Language Models. ([Paper](https://arxiv.org/pdf/2503.04240), [Code](https://github.com/arctanxarc/MC-LLaVA))

+ **\[2025 Arxiv-2503\]** MC-LLaVA: Multi-Concept Personalized Vision-Language Model. ([Paper](https://arxiv.org/pdf/2503.18854), [Code](https://github.com/arctanxarc/MC-LLaVA))

+ **\[2025 Arxiv-2501\]** Personalized Language Model Learning on Text Data Without User Identifiers. ([Paper](https://arxiv.org/pdf/2501.06062), [Code](https://github.com/sjtu-yc/IDfree-Personalized-Learning))

+ **\[2024 Arxiv-2412\]** Personalizing Multimodal Large Language Models for Image Captioning: An Experimental Analysis. ([Paper](https://arxiv.org/pdf/2412.03665))

+ **\[2024 Arxiv-2411\]** When Large Vision-Language Models Meet Person Re-Identification. ([Paper](https://arxiv.org/pdf/2411.18111))

+ **\[2024 Arxiv-2411\]** On the Way to LLM Personalization: Learning to Remember User Conversations. ([Paper](https://arxiv.org/pdf/2411.13405))

+ **\[2024 Arxiv-2411\]** MC-LLaVA: Multi-Concept Personalized Vision-Language Model. ([Paper](https://arxiv.org/pdf/2411.11706), [Code](https://github.com/arctanxarc/MC-LLaVA))

+ **\[2024 Arxiv-2410\]** LMLPA: Language Model Linguistic Personality Assessment. ([Paper](https://arxiv.org/pdf/2410.17632))

+ **\[2024 Arxiv-2409\]** LLMs + Persona-Plug = Personalized LLMs. ([Paper](https://arxiv.org/pdf/2409.11901))

+ **\[2024 Arxiv-2408\]** StyleRemix: Interpretable Authorship Obfuscation via Distillation and Perturbation of Style Elements. ([Paper](https://arxiv.org/pdf/2408.15666), [Code](https://github.com/jfisher52/StyleRemix))

+ **\[2024 Arxiv-2406\]** P-Tailor: Customizing Personality Traits for Language Models via Mixture of Specialized LoRA Experts. ([Paper](https://arxiv.org/pdf/2406.12548v1))

+ **\[2024 Arxiv-2404\]** Online Personalizing White-box LLMs Generation with Neural Bandits. ([Paper](https://arxiv.org/pdf/2404.16115))

+ **\[2024 EMNLP\]** Can LLM be a Personalized Judge? ([Paper]([link](https://arxiv.org/pdf/2406.11657)), [Code]([link](https://github.com/dong-river/Personalized-Judge)))

+ **\[2024 EMNLP\]** Democratizing Large Language Models via Personalized Parameter-Efficient Fine-tuning. ([Paper](https://arxiv.org/pdf/2402.04401), [Code](https://github.com/TamSiuhin/OPPU))
 
+ **\[2024 EMNLP\]** Guided Profile Generation Improves Personalization with LLMs. ([Paper](https://arxiv.org/pdf/2409.13093))

+ **\[2024 EMNLP\]** HEART-felt Narratives: Tracing Empathy and Narrative Style in Personal Stories with LLMs. ([Paper](https://arxiv.org/pdf/2405.17633), [Code](https://github.com/mitmedialab/heartfelt-narratives-emnlp))

+ **\[2024 EMNLP\]** Personalized Pieces: Efficient Personalized Large Language Models through Collaborative Efforts. ([Paper](https://arxiv.org/pdf/2406.10471), [Code](https://github.com/TamSiuhin/Per-Pcs))

+ **\[2024 EMNLP\]** PersonalizedVideoCommentGeneration. ([Paper](https://aclanthology.org/2024.findings-emnlp.979.pdf))

+ **\[2024 NeurIPS\]** HYDRA: Model Factorization Framework for Black-Box LLM Personalization. ([Paper](https://arxiv.org/pdf/2406.02888v1), [Code](https://arxiv.org/pdf/2406.02888v1))




