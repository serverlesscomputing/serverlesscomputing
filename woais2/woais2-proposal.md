# Workshop Proposal

## Title

Second International Workshop on AI and Serverless (WoAIS) part of ACM/IFIP Middleware 2026 in Universitat Rovira i Virgili, Tarragona, Spain (December 14-18)

## The names, affiliations and e-mail addresses of the organizing committee

### Paul Castro, IBM Research

Paul Castro, Ph.D., is a Senior Research Manager at the IBM Watson Research Center, where he focuses on hybrid cloud platforms for AI. His work explores serverless computing for model serving, agentic programming models and runtimes, cloud platforms, and developer tooling for cloud-native development. Over his career, he has conducted extensive research across mobile and pervasive computing, cloud infrastructure, wireless location systems, location databases, stream processing, and enterprise web applications, earning multiple patents in these areas. He has contributed to cloud services supporting mobile applications across smartphone platforms, received several IBM Research Accomplishment Awards in mobile computing and cloud-native systems, played a key role in enterprise solutions for the Apple–IBM partnership, and was an early contributor to the Apache OpenWhisk project.

### Pedro García López, University Rovira i Virgili

Pedro Garcia Lopez is full professor in Computer Science and Artificial Intelligence at Universitat Rovira i Virgili (URV).  He leads CLOUDLAB: Cloud and Distributed Systems  research group and he currently coordinates three large European research projects related to Serverless technologies (cloudstars.eu, neardata.eu, cloudskin.eu). His research topics are Serverless Computing, Big Data analytics, Cloud Computing, distributed systems, Cloud Storage, software architectures and middleware.

### Vatche Isahagian, IBM Research

Vatche Ishakian is a Research Staff Member in the AI Engineering group at the IBM Thomas J. Watson Research Center. He earned his PhD in Computer Science from Boston University under the supervision of Professor Azer Bestavros. His research interests include developing platforms and tools in support of AI cloud applications.

### Vinod Muthusamy, IBM Research

Vinod Muthusamy is a Research Staff Member in the Agentic AI Middleware group at the IBM Thomas J. Watson Research Center. His current research interests include LLM-based agents, AI middleware, agent orchestration, and all elements of the application lifecycle to build, monitor, and maintain robust AI applications.

### Aleksander Slominski, IBM Research

Aleksander Slominski is Research Staff Member in the Serverless Group at the IBM T.J. Watson Research Center. He is interested in development of applications for next generation Internet, Web Services, Orchestration, Components, AI, Workflows, and Clouds.

## Brief Technical Description

The rise of new AI agents—which involve multiple LLM calls, dynamic plans, and a mix of deterministic code and AI models—is creating uniquely complex workloads for serverless platforms. These agentic applications may be triggered by events, run quickly for a few seconds or autonomously for days, and communicate with other agents. This new reality has already resurfaced classic serverless challenges, such as cold starts, state management, and resource allocation, but within the demanding context of modern AI applications. Furthermore, new complications are emerging, including mixed GPU/CPU needs, unpredictable (stochastic) execution plans, long-running yet highly bursty processes, the critical need for robust agent-to-agent communication, and integrations with agentic programming models and frameworks such as [LangGraph](https://langchain-ai.github.io/langgraph/), [CrewAI](https://www.crewai.com/), [AutoGen/AG2](https://github.com/microsoft/autogen), [Google ADK](https://adk.dev/), and IBM's open-source [BeeAI](https://www.ibm.com/think/topics/beeai).

Looking beyond the cloud, the scope of serverless is expanding. The workshop looks ahead at future architectures involving AI, hybrid clouds, and especially edge/IoT devices, which current serverless platforms are not well-equipped to support. These next-gen computing architectures are becoming more common but bring new challenges to old concerns such as resource optimization, scaling, cost, monitoring, and ease of use. The serverless experience becomes essential to emerging trends such as DevOps and [Platform Engineering](https://platformengineering.org/) in industry and will be critical to the success of next-gen computing.

This naturally leads to a discussion of the role of LLMs and Foundation Models (FMs) in serverless, where the workshop will explore how hybrid serverless platforms can be leveraged for the entire lifecycle of LLMs and FMs—from fine-tuning and customization to inference serving and ongoing management—with a focus on use cases, resource allocations, optimizations, and using AI to improve the serverless experience itself.

The workshop also plans to explore broader system-level perspectives such as AI Operating Systems and infrastructure for scaling AI (distributed training and evaluation systems, compilers, and data engines that support continual updates), as well as operating AI at scale with heterogeneous data streams and real-time costs. Memory layers for LLM-based agents (episodic vs. semantic memory, retrieval mechanisms, consolidation of interaction-driven experiences), orchestration of multiple agents running as serverless functions, autonomous lifecycle management, and emerging interfaces such as the Model Context Protocol (MCP) are all in scope.

A rapidly emerging part of this landscape is the agent platform layer: open-source, Kubernetes-native runtimes that support CRD-based agent lifecycle, are framework-agnostic, with native MCP/A2A/OpenTelemetry integrations, with SPIFFE workload identity and Istio Ambient mesh for zero-trust mTLS between agents as well as enterprise control planes such as [IBM watsonx Orchestrate](https://www.ibm.com/products/watsonx-orchestrate) and [Amazon Bedrock Agents](https://aws.amazon.com/bedrock/agents/) that unify agents built on different frameworks under a single governance and observability surface. Closely tied to these platforms is the rise of standardized inter-agent protocols. The [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) addresses agent-to-tool interaction, while the [Agent2Agent (A2A) protocol](https://a2a-protocol.org/latest/), originally from Google and donated to the Linux Foundation, addresses agent-to-agent discovery, delegation, and coordination. The workshop welcomes work on the systems implications of these platforms and protocols on serverless: zero-trust identity for ephemeral agents, autoscaling for A2A/MCP traffic, cold-start and connection-pooling for protocol endpoints, sandboxed tool execution, and multi-tenant isolation of agents that may originate from many vendors.

A closely related emerging area is the rise of agentic coding harnesses such as [Claude Code](https://github.com/anthropics/claude-code) and [OpenClaw](https://openclaw.ai/), which wrap LLMs with tool use, memory, sandboxed execution, and multi-step planning. These harnesses are simultaneously a representative workload for serverless platforms (bursty multi-LLM sessions, tool calls that fan out to deterministic code and external services, long-lived agent state) and a new programming model that shapes how serverless platforms should expose execution, isolation, and inter-agent communication primitives (see protocols discussed above, such as MCP, A2A, and ACP). The workshop welcomes work on running, scaling, securing, and observing such harnesses on serverless infrastructure, including harness-to-harness (multi-agent) orchestration.

The workshop is also interested in AI-Driven Research for Systems (ADRS) the emerging paradigm, articulated in recent work such as [Barbarians at the Gate](https://arxiv.org/abs/2510.06189) and [Let the Barbarians In](https://arxiv.org/abs/2512.14806), in which LLM-based agents iteratively generate, evaluate, and refine systems-level solutions and have already matched or outperformed human state-of-the-art in domains such as scheduling, load balancing, and query optimization. ADRS is doubly relevant to WoAIS: its evaluation loops are themselves elastic, embarrassingly bursty workloads naturally suited to serverless execution, and serverless systems are a promising target for ADRS-driven design and autotuning. Submissions on using ADRS-style methodologies to advance serverless and AI systems research, as well as on the infrastructure needed to operate ADRS at scale, are encouraged.

ADRS belongs to a broader, rapidly growing family of AI-agent-driven research loops that share an iterative generate–evaluate–refine pattern. Closely related are evolutionary code-search agents such as DeepMind's [FunSearch](https://deepmind.google/blog/funsearch-making-new-discoveries-in-mathematical-sciences-using-large-language-models/) and [AlphaEvolve](https://deepmind.google/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/) (which has produced concrete systems wins such as a 32.5% FlashAttention kernel speedup and the first improvement in 56 years to Strassen-style 4×4 matrix multiplication), the open-source [CodeEvolve](https://arxiv.org/abs/2510.14150), and tree-search ML-engineering agents such as Weco AI's [AIDE](https://github.com/WecoAI/aideml). At a higher level of autonomy, end-to-end "AI scientist" systems—Sakana's [AI Scientist](https://sakana.ai/ai-scientist-nature/) (whose v2 uses agentic tree search and produced a manuscript that passed peer review at an ICLR 2025 workshop) and Google's multi-agent [AI co-scientist](https://research.google/blog/accelerating-scientific-breakthroughs-with-an-ai-co-scientist/) (with specialized Generation, Reflection, Ranking, Evolution, Proximity, and Meta-review agents)—automate larger fractions of the research lifecycle, as do frameworks such as [AI-Researcher](https://arxiv.org/abs/2505.18705) and Microsoft Research's [R\&D-Agent](https://arxiv.org/abs/2505.14738). A complementary line of work focuses on evaluation infrastructure for such agents, including OpenAI's [MLE-Bench](https://github.com/openai/mle-bench), the open-ended [MLR-Bench](https://github.com/chchenhui/mlrbench), Google's [MLE-STAR](https://research.google/blog/mle-star-a-state-of-the-art-machine-learning-engineering-agents/), and the [OpenHands](https://www.openhands.dev/blog/openhands-index) software-engineering agent stack and leaderboard. From a systems perspective, all of these are structurally serverless-shaped workloads: each iteration spawns many parallel, independently evaluable trials, often inside sandboxed containers, with sharply variable resource needs and mixed CPU/GPU usage. They surface a coherent set of questions for WoAIS—evaluation-as-a-service at FaaS granularity, secure sandboxed trial execution, cost-aware search heuristics, reproducibility when candidate designs are AI-generated, and multi-agent orchestration of specialized research roles—and submissions on any of these directions are welcome.

A complementary thread is the emerging idea of [AI-Native Systems](https://ai-native-systems-research.github.io/ai-native-systems-research/) — running software systems that continuously observe their own behavior, hypothesize improvements, implement and experiment with changes, and deploy validated updates without human mediation, with humans only in a governance role. The recent vision article [Autonomous Evolution at Machine Speed](https://ai-native-systems-research.github.io/ai-native-systems-research/blog/2026/04/21/ai-native-systems-autonomous-evolution-at-machine-speed/) (Eilam, Oliveira, Factor, 2026\) frames this as a Controlling System (Reasoner \+ Changer) wrapped around a System Under Control via a continuous meta-loop. Concrete instances already exist for serverless-adjacent stacks, including the Kubernetes-native distributed LLM inference platform [llm-d](https://llm-d.ai/) (admission control, routing, autoscaling, KV-cache management, prefill-decode disaggregation), the open-source [llm-d inference simulator](https://github.com/llm-d/llm-d-inference-sim) that serves as a cheap GPU-free evaluator in the loop, and autonomous kernel-optimization efforts in the spirit of [OpenEvolve](https://github.com/algorithmicsuperintelligence/openevolve), Stanford's [KernelBench](https://github.com/ScalingIntelligence/KernelBench), and AlphaEvolve. AI-Native Systems extend ADRS-style research loops into production and raise distinct serverless questions: governed autonomy with full provenance for AI-driven changes, cheap simulator-based evaluation, multi-timescale control loops (seconds to months), and the boundary between runtime adaptation and design-time evolution.

This workshop brings together researchers and practitioners to discuss their experiences and ideas for future directions in AI and serverless research.

### Interest to the Research Community

Serverless architectures offer different tradeoffs in terms of control, cost, and flexibility compared to distributed applications built on an Infrastructure as a Service (IaaS) substrate, and the addition of AI workloads sharpens those tradeoffs in new ways. Developers must reason about GPU and accelerator usage alongside CPU time and memory, about elastic pay-as-you-go pricing for accelerators with very different cost metrics, and about the cost-per-token and energy footprint of operating AI agents and models. Classic concerns around latency, scalability, and elasticity remain, but are now joined by economics and pricing models specific to AI and serverless.

Tooling and developer experience are also open research areas. The transition from “traditional” serverless and FaaS toward AI agentic programming raises new questions about debugging AI serverless applications, observability and maintenance from local source to production, low-code and no-code abstractions, and the use of generative LLMs such as ChatGPT to assist in building, running, and maintaining serverless-like applications. Serverless data management for AI—including Retrieval-Augmented Generation (RAGs), vector and graph databases applied to the serverless experience—presents further challenges for composition and performance.

Beyond the cloud, an intriguing area of research lies in the emergence of innovative FaaS runtimes tailored to specific application domains. Serverless is being explored in multi-cloud and hybrid-cloud settings spanning edge, fog, and IoT, including support for customization and for running user-provided AI models in any of these environments. Cloud AI security—AI-driven cybersecurity risk analysis and secure machine learning for vulnerability assessment of AI and related technologies using serverless and other scalable techniques—is becoming an essential research direction. Adjacent topics such as confidential computing, sustainable computing, granular computing, super-lightweight containers and WebAssembly, and swarm intelligence further broaden the research agenda. Finally, evaluation, benchmarking, and reproducibility—with standardized benchmarks and reproducible AI research results—remain critical to making progress in the field, and take on a new dimension when candidate designs are themselves generated and refined by AI agents, as in ADRS-style methodologies.

## The history of the workshop

This would be the eighth time of the workshop at Middleware and we want to build on our previous experience and continue to draw the attention of distributed systems researchers to this young research field and further drive the adoption and development of available technology.

There have been nine previous editions of this workshop:

* [WoAIS1](https://www.serverlesscomputing.org/woais1/): 20th ACM International Conference on Distributed and Event-based Systems,June 23, 2026 in hybrid location; virtual and in Lisbon, Portugal  
* [WoSC11](https://www.serverlesscomputing.org/wosc11/): 26th ACM/IFIP International Conference Middleware, Dec 25, 2024 in hybrid location; virtual and in Vanderbilt University, Nashville, TN, USA  
* [WoSC10](https://www.serverlesscomputing.org/wosc10/): 25th ACM/IFIP International Conference Middleware, Dec 2, 2024 in hybrid location; virtual and in The Hong Kong Polytechnic University, Hong Kong  
* [WoSC9](https://www.serverlesscomputing.org/wosc9/): 24th ACM/IFIP International Conference Middleware, Dec 11, 2023 in hybrid location; virtual and in Québec, Canada  
* [WoSC8](https://www.serverlesscomputing.org/wosc8/): 23rd ACM/IFIP International Conference Middleware, Nov 7, 2022 in hybrid location; virtual and in Québec, Canada  
* [WoSC7](https://www.serverlesscomputing.org/wosc7/): 22nd ACM/IFIP International Conference Middleware, Dec 7, 2021 in virtual location  
* [WoSC6](https://www.serverlesscomputing.org/wosc6/): 21st ACM/IFIP International Conference Middleware, Dec 8, 2020 in virtual location  
* [WosC5](https://www.serverlesscomputing.org/wosc5/): 20th ACM/IFIP International Conference Middleware, Dec 9, 2019 in UC Davis, CA, USA  
* [WoSC4](https://www.serverlesscomputing.org/wosc4/): 11th IEEE/ACM UCC / 5th IEEE/ACM BDCAT 2018, Zurich, Switzerland  
* [WoSC3](https://www.serverlesscomputing.org/wosc3/): IEEE CLOUD 2018, San Francisco, CA, USA  
* [WoSC2](https://www.serverlesscomputing.org/wosc2/): Middleware 2017, Las Vegas, NV, USA  
* [WoSC1](https://www.serverlesscomputing.org/wosc17/): ICDCS 2017, Atlanta, GA, USA

These are linked on the series' permanent web presence at: [https://www.serverlesscomputing.org/workshops/](https://www.serverlesscomputing.org/workshops/)

The organizers of this proposed workshop are the founding members of this workshop and have co-chaired previous iterations.

### Similar Workshops

WoAIS is the evolution of [WoSC](https://www.serverlesscomputing.org/workshops/) to combine serverless with emerging AI topics. WoSC was the first academic workshop dedicated to serverless computing. The [first edition of WoAIS](https://www.serverlesscomputing.org/woais1/) was co-located with DEBS 2026 in Lisbon, Portugal (June 23, 2026); this proposal is for the second edition.

In 2026, several adjacent serverless workshops are active. [SESAME 2026](https://sesame26.github.io/), the 4th Workshop on Serverless Systems, Applications and Methodologies, is co-located with EuroSys 2026 (April 27, 2026, Edinburgh, UK) and has explicitly expanded its scope to include serverless GenAI and LLM inference serving. [GraphSys 2026](https://graphsys.org/), the Workshop on Serverless, Extreme-Scale, and Sustainable Graph Processing Systems, is co-located with Euro-Par 2026 (August 24–25, 2026, Pisa, Italy). The [SEATED](https://edgeless-project.eu/seated/) Workshop on Serverless at the Edge (1st edition at ACM HPDC 2024 in Pisa, sponsored by the EU EDGELESS project) is relevant to the edge/IoT direction. The [WORDS](https://www.wordsworkshop.org/) Workshop on Resource Disaggregation and Serverless Computing has been periodically co-located with SOSP (most recently the 4th edition at SOSP 2023 in Koblenz, Germany).

Earlier related serverless workshops include [HiPS](https://highperformanceserverless.github.io/), the Workshop on High Performance Serverless Computing (co-located with ACM HPDC in 2021 and 2022), the First IEEE SERVICES Workshop on Serverless Computing [SWoSC](https://conferences.computer.org/services/2019/workshops/sc_workshop.html) (2019), and the regional European Symposium on Serverless Computing and Applications (ESSCA 2018), which was co-organized with WoSC4.

On the AI/ML systems side, venues such as [MLSys 2026](https://mlsys.org/) (Bellevue, WA, May 18–22, 2026), [EuroMLSys 2026](https://euromlsys.eu/) at EuroSys 2026 (Edinburgh, April 27, 2026), the AAAI 2026 [WMAC](https://multiagents.org/2026/) bridge program on LLM-based multi-agent collaboration, the [ICLR 2026 MemAgents](https://sites.google.com/view/memagent-iclr26/) workshop, the [ICLR 2026 Workshop on Multi-Agent Learning and Generative AI](https://iclr26-mal-gai.github.io/), and [AGENT 2026](https://conf.researchr.org/home/icse-2026/agent-2026) at ICSE 2026 address ML systems and agent algorithms. None of these, however, focus on the serverless substrate for AI workloads. A search of [WikiCFP](http://www.wikicfp.com/cfp/servlet/tool.search?q=serverless&year=a) and the workshops above confirms that, to the best of our knowledge, WoAIS remains the only workshop specifically at the intersection of serverless computing and AI/agentic workloads.

## A short description of the intended format of the workshop

Hybrid workshop (in-person and remote participants) with invited keynote speakers, paper presentations (pre-recorded videos as backup, live Q\&A), possible poster & demo session, and panel Q\&A.

## Review process

Submitted papers must have at most 6 pages of technical content, including text, figures, and appendices, but excluding any number of additional pages for bibliographic references. Note that submissions must be double-blind: authors’ names must not appear, and authors must make a good faith attempt to anonymize their submissions. Submitted papers must adhere to the formatting instructions of the ACM SIGPLAN style, which can be found on the ACM template page. The font size has to be set to 10pt.

We will use the HotCRP system in a way consistent with how Middleware workshops are using it.

## Tentative workshop paper submission and notification deadlines

* Submission:  September 17, 2026  
* Notification: October 12, 2026  
* Camera Ready: October 16, 2026  
* Author registration deadline: TBD  
* Conference: December 14, 2026

### Primary contacts of the organizing committee

Aleksander Slominski, IBM Research

### Estimated number of participants, length, and timetable of the workshop

We expect the workshop length and agenda to be similar to the previous iterations of the workshop, which included invited talks, paper presentations, and panel discussions. We will provide a final agenda once we know the number of invited talks and accepted papers.

Approximate attendance: 30-50 participants

## A preliminary list of PC members

Workshop co-chairs

* Paul Castro, IBM Research  
* Pedro García López, Universitat Rovira i Virgili  
* Vatche Isahagian, IBM Research  
* Aleksander Slominski, IBM Research  
* Vinod Muthusamy, IBM Research

Technical Program Committee (tentative)

* Alexandru Iosup, Vrije Universiteit Amsterdam  
* Ali Kanso, Microsoft  
* Amine Barrak, Oakland University  
* Cristina Abad, Escuela Superior Politécnica del \* Litoral (Ecuador)  
* Dennis Gannon, Indiana University & Formerly \* Microsoft Research  
* Eric Rozner, University of Colorado Boulder  
* Etienne Rivière, UCLouvain  
* Geoffrey Fox, Indiana University  
* Gul Agha, University of Illinois at Urbana-Champaign  
* Hans-Arno Jacobsen, MSRG (Middleware Systems \* Research Group)  
* Ian Foster, University of Chicago and Argonne \* National Laboratory  
* Josef Spillner, Zurich University of Applied Sciences  
* Kyungyong Lee, Kookmin University  
* Lucas Nussbaum, LORIA, France  
* Maciej Malawski, AGH University of Science and \* Technology, Poland  
* Maciej Pawlik, Academic Computer Centre CYFRONET of \* the University of Science and Technology in Cracow  
* Marc Sánchez Artigas, Universitat Rovira i Virgili  
* Per Persson, Ericsson Research  
* Peter Pietzuch, Imperial College  
* Rich Wolski, University of California, Santa Barbara  
* Rodric Rabbah, Nimbella and Apache OpenWhisk  
* Rodrigo Fonseca, Microsoft Research  
* Samuel Kounev, University of Wuerzburg  
* Tyler R. Caraza-Harter, University of \* Wisconsin-Madison  
* Višnja Križanović, Josip Juraj Strossmayer \* University of Osijek  
* Volker Hilt, Bell Labs (Nokia)  
* Wes Lloyd, University of Washington Tacoma

Steering Committee (tentative)

* Geoffrey Fox, Indiana University  
* Dennis Gannon, Indiana University & Formerly Microsoft Research  
* Arno Jacobsen, MSRG (Middleware Systems Research Group)

