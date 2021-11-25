---
title: "ACE: Just-in-time Serverless Software Component Discovery Through Approximate Concrete Execution"
authors:
  - name: Anthony Byrne
    email: abyrne19@bu.edu
    affiliation: Boston University
  - name: Shripad Nadgowda
    email: nadgowda@us.ibm.com
    affiliation: IBM T.J. Watson Research Center
  - name: Ayse K. Coskun
    email: acoskun@bu.edu
    affiliation: Boston University
pdf: https://dl.acm.org/doi/10.1145/3429880.3430098
presentation:
  pdf: https://www.serverlesscomputing.org/wosc6/presentations/p7.pdf
  pptx: https://www.serverlesscomputing.org/wosc6/presentations/p7.pptx
video:
  talk: https://www.youtube.com/embed/mctma7mcLCs
---

While much of the software running on today's serverless platforms is written in easily-analyzed high-level interpreted languages, many performance-conscious users choose to deploy their applications as container-encapsulated compiled binaries on serverless container platforms such as AWS Fargate or Google Cloud Run. Modern CI/CD workflows make this deployment process nearly-instantaneous, leaving little time for in-depth manual application security reviews. This combination of opaque binaries and rapid deployment prevents cloud developers and platform operators from knowing if their applications contain outdated, vulnerable, or legally-compromised code. This paper proposes Approximate Concrete Execution (ACE), a just-in-time binary analysis technique that enables automatic software component discovery for serverless binaries. Through classification and search engine experiments with common cloud software packages, we find that ACE scans binaries 5.2x faster than a state-of-the-art binary analysis tool, minimizing the impact on deployment and cold-start latency while maintaining comparable recall.