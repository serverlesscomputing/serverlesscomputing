---
title: Proactive Serverless Function Resource Management
workshop: wosc6
authors:
  - name: Erika Hunhof
    affiliation: CU Boulder
  - name: Shazal Irshad
    affiliation: CU Boulder
  - name: Vijay Thurimella
    affiliation: Thrive, Inc
  - name: Ali Tariq
    affiliation: CU Boulder
  - name: Eric Rozner
    affiliation: CU Boulder
pdf: https://dl.acm.org/doi/10.1145/3429880.3430102
presentation:
  pdf: https://www.serverlesscomputing.org/wosc6/presentations/p11.pdf
  pptx: https://www.serverlesscomputing.org/wosc6/presentations/p11.ppt
video:
  talk: https://www.youtube.com/embed/fMQvhkuqnmc
---

This paper introduces a new primitive to serverless language runtimes called freshen. With freshen, developers or providers specify functionality to perform before a given function executes. This proactive technique allows for overheads associated with serverless functions to be mitigated at execution time, which improves function responsiveness. We show various predictive opportunities exist to run freshen within reasonable time windows. A high-level design and implementation are described, along with preliminary results to show the potential benefits of our scheme.