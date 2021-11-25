---
title: Towards Federated Learning using FaaS Fabric
workshop: wosc6
authors:
  - name: Mohak Chadha
    affiliation: Technische Universität München, Garching (near Munich), Germany
    email: mohak.chadha@tum.de
  - name: Anshul Jindal
    affiliation: Technische Universität München, Garching (near Munich), Germany
    email: anshul.jindal@tum.de
  - name: Michael Gerndt
    affiliation: Technische Universität München, Garching (near Munich), Germany
    email: gerndt@in.tum.de
pdf: https://dl.acm.org/doi/10.1145/3429880.3430100
presentation:
  pdf: https://www.serverlesscomputing.org/wosc6/presentations/WoSC_2020_Presentation_P9.pdf
video:
  talk: https://www.youtube.com/embed/CjK4mevTTTc
---

Federated learning (FL) enables resource-constrained edge devices to learn a shared Machine Learning (ML) or Deep Neural Network (DNN) model, while keeping the training data local and providing privacy, security, and economic benefits. However, building a shared model for heterogeneous devices such as resource-constrained edge and cloud makes the efficient management of FL-clients challenging. Furthermore, with the rapid growth of FL-clients, the scaling of FL training process is also difficult.

In this paper, we propose a possible solution to these challenges: federated learning over a combination of connected Function-as-a-Service platforms, i.e., FaaS fabric offering a seamless way of extending FL to heterogeneous devices. Towards this, we present FedKeeper, a tool for efficiently managing FL over FaaS fabric. We demonstrate the functionality of FedKeeper by using three FaaS platforms through an image classification task with a varying number of devices/clients, different stochastic optimizers, and local computations (local epochs).