---
title: Active-Standby for High-Availability in FaaS
authors:
  - name: Yasmina Bouizem
    affiliation: Univ Tlemcen, LRIT, Univ Rennes, Inria
  - name: Djawida Dib
    affiliation: Univ Tlemcen, LRIT
  - name: Nikos Parlavantzas
    affiliation: INSA Rennes, IRISA
  - name: Christine Morin
    affiliation: Univ Rennes, Inria
pdf: https://dl.acm.org/doi/10.1145/3429880.3430097
presentation:
  pdf: https://www.serverlesscomputing.org/wosc6/presentations/P6-WoSC6_Active%20Standby%20for%20High%20Availability%20in%20FaaS.pdf
video:
  talk: https://www.youtube.com/embed/mfWqxRODZw0
---

Serverless computing is becoming more and more attractive for cloud solution architects and developers. This new computing paradigm relies on Function-as-a-Service (FaaS) platforms that enable deploying functions without being concerned with the underlying infrastructure. An important challenge in designing FaaS platforms is ensuring the availability of deployed functions. Existing FaaS platforms address this challenge principally through retrying function executions. In this paper, we propose and implement an alternative fault-tolerance approach based on active-standby failover. Results from an experimental evaluation show that our approach increases availability and performance compared to the retry-based approach.