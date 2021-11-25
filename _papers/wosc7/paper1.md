---
title: Temporal Performance Modelling of Serverless Computing Platforms
tags:
  - wosc7
authors:
  - name: N. Mahmoudi
    email: nmahmoud@ualberta.ca
    affiliation: Dept. of Electrical and Computer Engineering, University of Alberta, Edmonton, AB, Canada
  - name: H. Khazaei
    email: hkh@yorku.ca
    affiliation: Dept. of Electrical Engineering and Computer Science, York University, Toronto, ON, Canada
pdf: "https://dl.acm.org/doi/10.1145/3429880.3430092"
presentation:
  pdf: https://www.serverlesscomputing.org/wosc6/presentations/p1.pdf
  pptx: https://www.serverlesscomputing.org/wosc6/presentations/p1.pptx
video:
  lightning: https://youtu.be/E5KigIq0Z1E
  talk: https://www.youtube.com/embed/9r3j_1B5t8c
---

Analytical performance models have been shown very efficient in analyzing, predicting, and improving the performance of distributed computing systems. However, there is a lack of rigorous analytical models for analyzing the transient behaviour of serverless computing platforms, which is expected to be the dominant computing paradigm in cloud computing. Also, due to its unique characteristics and policies, performance models developed for other systems cannot be directly applied to modelling these systems. In this work, we propose an analytical performance model that is capable of predicting several key performance metrics for serverless workloads using only their average response time for warm and cold requests. The introduced model uses realistic assumptions, which makes it suitable for online analysis of real-world platforms. We validate the proposed model through extensive experimentation on AWS Lambda. Although we focus primarily on AWS Lambda due to its wide adoption in our experimentation, the proposed model can be leveraged for other public serverless computing platforms with similar auto-scaling policies, e.g., Google Cloud Functions, IBM Cloud Functions, and Azure Functions.
