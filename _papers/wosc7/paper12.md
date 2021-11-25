---
title: "The Serverless Application Analytics Framework: Enabling Design Trade-off Evaluation for Serverless Software"
authors:
  - name: Robert Cordingly
    affiliation: School of Engineering and Technology, University of Washington, Tacoma WA USA
    email: rcording@uw.edu
  - name: Hanfei Yu
    affiliation: School of Engineering and Technology, University of Washington, Tacoma WA USA
    email: hanfeiyu@uw.edu
  - name: Varik Hoang
    affiliation: School of Engineering and Technology, University of Washington, Tacoma WA USA
    email: varikmp@uw.edu
  - name: Zohreh Sadeghi
    affiliation: School of Engineering and Technology, University of Washington, Tacoma WA USA
    email: zsadeghi@uw.edu
  - name: David Foster
    affiliation: School of Engineering and Technology, University of Washington, Tacoma WA USA
    email: davidf94@uw.edu
  - name: David Perez
    affiliation: School of Engineering and Technology, University of Washington, Tacoma WA USA
    email: daperez@uw.edu
  - name: Rashad Hatchett
    affiliation: School of Engineering and Technology, University of Washington, Tacoma WA USA
    email: rhatch26@uw.edu
  - name: Wes Lloyd
    affiliation: School of Engineering and Technology, University of Washington, Tacoma WA USA
    email: wlloyd@uw.edu
pdf: https://dl.acm.org/doi/10.1145/3429880.3430103
presentation:
  pdf: https://www.serverlesscomputing.org/wosc6/presentations/p12.pdf
  pptx: https://www.serverlesscomputing.org/wosc6/presentations/p12.pptx
video:
  lightning: https://youtu.be/i_s91P72pRE
  talk: https://www.youtube.com/embed/oRDkHdapmg4
---

To help better understand factors that impact performance on Function-as-a-Service (FaaS) platforms we have developed the Serverless Application Analytics Framework (SAAF). SAAF provides a reusable framework supporting multiple programming languages that developers can integrate into a function's package for deployment to multiple commercial and open source FaaS platforms. SAAF improves the observability of FaaS function deployments by collecting forty-eight distinct metrics to enable developers to profile CPU and memory utilization, monitor infrastructure state, and observe platform scalability. In this paper, we describe SAAF in detail and introduce supporting tools highlighting important features and how to use them. Our client application, FaaS Runner, provides a tool to orchestrate workloads and automate the process of conducting experiments across FaaS platforms. We provide a case study demonstrating the integration of SAAF into an existing open source image processing pipeline built for AWS Lambda. Using FaaS Runner, we automate experiments and acquire metrics from SAAF to profile each function of the pipeline to evaluate performance implications. Finally, we summarize contributions using our tools to evaluate implications of different programming languages for serverless data processing, and to build performance models to predict runtime for serverless workloads.