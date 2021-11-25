---
title: Bringing scaling transparency to Proteomics applications with serverless computing
authors:
  - name: Mariano Ezequiel Mirabelli
    affiliation: Universitat Rovira i Virgili, Tarragona, Spain
    email: mmirabelli@uoc.edu
  - name: Pedro García-López
    affiliation: Universitat Rovira i Virgili, Tarragona, Spain
    email: pedro.garcia@urv.cat
  - name: Gil Vernik
    affiliation: IBM Israel, Haifa, Israel
    email: gilv@il.ibm.com
pdf: https://dl.acm.org/doi/10.1145/3429880.3430101
presentation:
  pdf: https://www.serverlesscomputing.org/wosc6/presentations/WOSC%20[2020]%20Bringing%20scaling%20transparency%20to%20Proteomics%20applications%20with%20serverless%20computing.pdf
video:
  talk: https://www.youtube.com/embed/4GSQRNgdF0A
---

Scaling transparency means that applications can expand in scale without changes to the system structure or the application algorithms. Serverless Computing's inherent auto-scaling support and fast function launching is ideally suited to support scaling transparency in different domains.

In particular, Proteomic applications could considerably benefit from scaling transparency and serverless technologies due to their high concurrency requirements. Therefore, the auto-provisioning nature of serverless platforms makes this computing model an alternative to satisfy dynamically the resources required by protein folding simulation processes. However, the transition to these architectures must face challenges: they should show comparable performance and cost to code running in Virtual Machines (VMs).

In this article, we demonstrate that Proteomics applications implemented with the Replica Exchange algorithm can be moved to serverless settings guaranteeing scaling transparency. We also validate that we can reduce the total execution time by around forty percent with comparable cost to cluster technologies (Work Queue) over VMs.