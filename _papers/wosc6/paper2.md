---
title: Implications of Public Cloud Resource Heterogeneity for Inference Serving
workshop: wosc6
authors:
  - name: Jashwant Raj Gunasekaran
    email: jashwant@psu.edu
    affiliation: The Pennsylvania State University
  - name: Cyan Subhra Mishra
    email: cyan@psu.edu
    affiliation: The Pennsylvania State University
  - name: Prashanth Thinakaran
    email: prashanth@psu.edu
    affiliation: The Pennsylvania State University
  - name: Mahmut Taylan Kandemir
    email: mtk2@psu.edu
    affiliation: The Pennsylvania State University
  - name: Chita R. Das
    email: cxd12@psu.edu
    affiliation: The Pennsylvania State University
pdf: "https://dl.acm.org/doi/10.1145/3429880.3430093"
presentation:
  pdf: https://www.serverlesscomputing.org/wosc6/presentations/p2.pdf
video:
  talk: https://www.youtube.com/embed/oYYPbglFZlg
---

We are witnessing an increasing trend towards using Machine Learning (ML) based prediction systems, spanning across different application domains, including product recommendation systems, personal assistant devices, facial recognition, etc. These applications typically have diverse requirements in terms of accuracy and response latency, that have a direct impact on the cost of deploying them in a public cloud. Furthermore, the deployment cost also depends on the type of resources being procured, which by themselves are heterogeneous in terms of provisioning latencies and billing complexity. Thus, it is strenuous for an inference serving system to choose from this confounding array of resource types and model types to provide low-latency and cost-effective inferences. In this work we quantitatively characterize the cost, accuracy and latency implications of hosting ML inferences on different public cloud resource offerings. Our evaluation shows that, prior work does not solve the problem from both dimensions of model and resource heterogeneity. Hence, we argue that to address this problem, we need to holistically solve the issues that arise when trying to combine both model and resource heterogeneity towards optimizing for application constraints. Towards this, we discuss the design and implications of a self-managed inference serving system, which can optimize the application requirements based on public cloud resource characteristics.