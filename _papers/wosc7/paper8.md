---
title: "Serverless Isn't Server-Less: Measuring and Exploiting Resource Variability on Cloud FaaS Platforms"
authors:
  - name: Samuel Ginzburg and Michael J. Freedman
    affiliation: Princeton University
pdf: https://dl.acm.org/doi/10.1145/3429880.3430098
presentation:
  pdf: https://www.serverlesscomputing.org/wosc6/presentations/p8.pdf
video:
  talk: https://www.youtube.com/embed/a0l1yismd8M
---

Serverless computing in the cloud, or functions as a service (FaaS), poses new and unique systems design challenges. Serverless offers improved programmability for customers, yet at the cost of increased design complexity for cloud providers. One such challenge is effective and consistent resource management for serverless platforms, the implications of which we explore in this paper. In this paper, we conduct one of the first detailed in situ measurement studies of performance variability in AWS Lambda. We show that the observed variations in performance are not only significant, but stable enough to exploit. We then design and evaluate an end-to-end system that takes advantage of this resource variability to exploit the FaaS consumption-based pricing model, in which functions are charged based on their fine-grain execution time rather than actual low-level resource consumption. By using both light-weight resource probing and function execution times to identify attractive servers in serverless platforms, customers of FaaS services can cause their functions to execute on better performing servers and realize a cost savings of up to 13% in the same AWS region.