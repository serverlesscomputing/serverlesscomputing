# Workshop Proposal

## Title
11th International Workshop on Serverless Computing (WoSC11) part of ACM/IFIP Middleware 2025 in Vanderbilt University, Nashville, TN, USA (December 15-19)


## The names, affiliations and e-mail addresses of the organizing committee

### Paul Castro, IBM Research
Paul Castro, Ph.D. is a Research Staff Member at the IBM Watson Research Center. He has been active in research on mobile and pervasive computing, cloud infrastructure, wireless location systems, location databases, stream processing, and enterprise web applications and has been awarded several patents in these areas. He has worked on cloud services for supporting mobile applications running on various smartphone platforms. Work from his research in the area of multi-device application support was recently released as part of the IBM Bluemix Mobile Backend as a Service. He has earned two IBM Technical Achievement Awards for the IBM SmartCloud Web Meetings for mobile clients and the Intelligent Notification System. Most recently, he worked on IBM OpenWhisk for Bluemix, with a focus on mobile solutions.

### Pedro García López, University Rovira i Virgili
Pedro Garcia Lopez is full professor in Computer Science and Artificial Intelligence at Universitat Rovira i Virgili (URV).  He leads CLOUDLAB: Cloud and Distributed Systems  research group and he currently coordinates three large European research projects related to Serverless technologies (cloudstars.eu, neardata.eu, cloudskin.eu). His research topics are Serverless Computing, Big Data analytics, Cloud Computing, distributed systems, Cloud Storage, software architectures and middleware.

### Vatche Isahagian, IBM Research
Vatche Ishakian is a Research Staff Member in the AI Engineering group at the IBM Thomas J. Watson Research Center. He earned his PhD in Computer Science from Boston University under the supervision of Professor Azer Bestavros. His research interests include developing platforms and tools in support of AI cloud applications.

### Vinod Muthusamy, IBM Research
Vinod Muthusamy is a Research Staff Member in the Agentic AI Middleware group at the IBM Thomas J. Watson Research Center. His current research interests include LLM-based agents, AI middleware, agent orchestration, and all elements of the application lifecycle to build, monitor, and maintain robust AI applications.

### Aleksander Slominski, IBM Research
Aleksander Slominski is Research Staff Member in the Serverless Group at the IBM T.J. Watson Research Center. He is interested in development of applications for next generation Internet, Web Services, Orchestration, Components, AI, Workflows, and Clouds.

## Brief Technical Description

Over the last eleven years, Serverless Computing (Serverless) has gained an enthusiastic following in industry as a compelling paradigm for the deployment of cloud applications, and is enabled by the recent shift of enterprise application architectures to containers and microservices. Many of the major cloud vendors have released serverless platforms, including Amazon Lambda, Google Cloud Functions, Microsoft Azure Functions, IBM Cloud Functions. Open source projects are gaining popularity in providing serverless computing as a service.

Recently, Kubernetes gained popularity in enterprise and academia. Several open source projects, such as OpenFaaS and Knative, aim to provide developers with a serverless experience on top of Kubernetes by hiding low-level details. Auto-scalable multi-tenant Kubernetes deployments like Google Cloud Run or IBM Code Engine also overcome previous limitations of Serverless Functions like duration, networking, and higher granularity (more vCPUs).

Serverless on the cloud is a mature research area with many conferences accepting papers on this topic. In the spirit of having this workshop serve as a venue for future and exploratory research directions, we will be evolving the workshop to include hybrid cloud environments, as well as edge and IoT devices. These next-gen computing architectures are becoming more common but have little support from serverless platforms and bring new challenges to old concerns such as resource optimization, scaling, cost, monitoring, and ease of use. The serverless experience becomes an essential topic for emerging topics such as DevOps and [Platform Engineering](https://platformengineering.org/) in industry and will be critical to the success of next-gen computing.

Building on the recent advances in generative AI, including Large Language Models (LLMs) and other types of Foundations Models (FMs), the workshop also plans to explore the use of hybrid serverless platforms to fine-tune, serve, and manage the lifecycle of LLMs with a focus on aspects such as use cases, resource allocations, optimizations, and using AI to improve serverless experience.

Emerging applications such as AI agents present interesting serverless workloads patterns. These agentic solutions are characterized by multiple LLM calls to process user requests and construct dynamic plans, unpredictable orchestrations of API calls, and invocations of deterministic code and AI models to reflect on API responses and make progress towards a goal. They may be triggered by events, run quickly for a few seconds or autonomously for days, and communicate with other agents. These applications resurface known serverless challenges in a new setting, including cold start, state management, and resource allocation. They also raise new challenges such as mixed GPU and CPU workloads, applications with stochastic plans, bursty long running processes, inter-process communication, and integrations with agentic programming models such as LangGraph and Crew AI.

This workshop brings together researchers and practitioners to discuss their experiences and thoughts on future directions of serverless research.

### Interest to the Research Community

Serverless architectures offer different tradeoffs in terms of control, cost, and flexibility compared to distributed applications built on an Infrastructure as a Service (IaaS) substrate. For example, a serverless architecture requires developers to more carefully consider the resources used by their code (time to execute, memory used, etc.) when modularizing their applications. This is in contrast to concerns around latency, scalability, and elasticity, which is where significant development effort has traditionally been spent when building cloud services. In addition, tools and techniques to monitor and debug applications aren't applicable in serverless architectures, and new approaches are needed. As well, test and development pipelines may need to be adapted. Another decision that developers face is the appropriateness of the serverless ecosystem to their application requirements. A rich ecosystem of services built into the platform is typically easier to compose and would offer better performance. However, composing external services may be unavoidable, and in such cases, many of the benefits of serverless disappear, including performance and availability guarantees. This presents an important research challenge, and it is not clear how existing results and best practices, such as workflow composition research, can be applied to composition in a serverless environment.
Finally, an intriguing area of research lies in the emergence of innovative FaaS runtimes tailored to various application domains. The investigation of serverless FaaS is not limited to low-latency HPC scenarios; it is also being explored in edge computing environments. Moreover, FaaS is serving as a source of inspiration for groundbreaking interactive burst-parallel extreme data analytics environments in the Cloud. Additionally, serverless AI services are expected to present formidable research objectives in the coming years.

## The history of the workshop

This would be the fifth time of the workshop at Middleware and we want to build on our previous experience and continue to draw the attention of distributed systems researchers to this young research field and further drive the adoption and development of available technology.

There have been nine previous editions of this workshop:
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

These are linked on the series' permanent web presence at: https://www.serverlesscomputing.org/workshops/

The organizers of this proposed workshop are the founding members of this workshop and have co-chaired previous iterations.

### Similar Workshops

WoSC is the first academic workshop dedicated to Serverless Computing. As far as we know, in 2025, there is only one similar workshop [GraphSys 2025](https://graphsys.org/): The Third Workshop on Serverless, Extreme-Scale, and Sustainable Graph Processing Systems that is co-located with Europar 2025 (August 25, 2025, Dresden, Germany). In 2024, there were two other serverless workshops: [SESAME 2024](https://sesame2024.github.io/) Workshop on SErverless Systems, Applications and MEthodologies (co-located with EuroSys 2024) 
and [WORDS 2023](https://www.wordsworkshop.org/) The Fourth Workshop On Resource Disaggregation and Serverless Computing (in conjunction with SOSP 2023).
In previous years there were few serverless workshops co-located with the conferences such as [HiPS 2022](https://highperformanceserverless.github.io/) Workshops on High Performance Serverless Computing (in conjunction with ACM HPDC) in 2021 and 2022, then in 2019 The First IEEE SERVICES Workshop on Serverless Computing [SWoSC](https://conferences.computer.org/services/2019/workshops/sc_workshop.html) and a regional workshop - European Symposium on Serverless Computing and Applications [ESSCA 2018](http://essca2018.servicelaboratory.ch/)  that was co-organized with WoSC4 in 2018. Checking with [WikiCFP](http://www.wikicfp.com/cfp/servlet/tool.search?q=serverless&year=a) are the only similar workshops.

##  A short description of the intended format of the workshop

Hybrid workshop (in-person and remote participants) with invited keynote speakers, paper presentations (pre-recorded videos as backup, live Q&A), possible poster & demo session, and panel Q&A.

## Review process

Submitted papers must have at most 6 pages of technical content, including text, figures, and appendices, but excluding any number of additional pages for bibliographic references. Note that submissions must be double-blind: authors’ names must not appear, and authors must make a good faith attempt to anonymize their submissions. Submitted papers must adhere to the formatting instructions of the ACM SIGPLAN style, which can be found on the ACM template page. The font size has to be set to 10pt.

We will use the HotCRP system in a way consistent with how Middleware workshops are using it.

## Tentative workshop paper submission and notification deadlines

* Submission:  September 24, 2025
* Notification: October 19, 2025
* Camera Ready: October 27, 2025
* Author registration deadline: TBD
* Conference: December 15, 2024

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
* Cristina Abad, Escuela Superior Politécnica del * Litoral (Ecuador)
* Dennis Gannon, Indiana University & Formerly * Microsoft Research
* Eric Rozner, University of Colorado Boulder
* Geoffrey Fox, Indiana University
* Gul Agha, University of Illinois at Urbana-Champaign
* Hans-Arno Jacobsen, MSRG (Middleware Systems * Research Group)
* Ian Foster, University of Chicago and Argonne * National Laboratory
* Josef Spillner, Zurich University of Applied Sciences
* Kyungyong Lee, Kookmin University
* Lucas Nussbaum, LORIA, France
* Maciej Malawski, AGH University of Science and * Technology, Poland
* Maciej Pawlik, Academic Computer Centre CYFRONET of * the University of Science and Technology in Cracow
* Marc Sánchez Artigas, Universitat Rovira i Virgili
* Per Persson, Ericsson Research
* Peter Pietzuch, Imperial College
* Rich Wolski, University of California, Santa Barbara
* Rodric Rabbah, Nimbella and Apache OpenWhisk
* Rodrigo Fonseca, Microsoft Research
* Samuel Kounev, University of Wuerzburg
* Tyler R. Caraza-Harter, University of * Wisconsin-Madison
* Višnja Križanović, Josip Juraj Strossmayer * University of Osijek
* Volker Hilt, Bell Labs (Nokia)
* Wes Lloyd, University of Washington Tacoma


Steering Committee (tentative)
* Geoffrey Fox, Indiana University
* Dennis Gannon, Indiana University & Formerly Microsoft Research
* Arno Jacobsen, MSRG (Middleware Systems Research Group)
