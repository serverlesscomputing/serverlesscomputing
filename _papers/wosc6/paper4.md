---
title: An Evaluation of Serverless Data Processing Frameworks
workshop: wosc6
authors:
  - name: Sebastian Werner
    email: sw@ise.tu-berlin.de
    affiliation: ISE, TU Berlin, Berlin, Germany
  - name: Richard Girke
    email: rg@ise.tu-berlin.de
    affiliation: ISE, TU Berlin, Berlin, Germany
  - name: Jörn Kuhlenkamp
    email: jk@ise.tu-berlin.de
    affiliation: ISE, TU Berlin, Berlin, Germany
pdf: https://dl.acm.org/doi/abs/10.1145/3429880.3430095
presentation:
  pdf: https://www.serverlesscomputing.org/wosc6/presentations/p4.pdf
video:
  lightning: https://youtu.be/KAmJo2IHhCo
  talk: https://www.youtube.com/embed/qPrplH3ut50
---

Serverless computing is a promising cloud execution model that significantly simplifies cloud users’ operational concerns by offering features such as auto-scaling and a pay-as-you-go cost model. Consequently, serverless systems promise to provide an excellent fit for ad-hoc data processing. Unsurprisingly, numerous serverless systems/frameworks for data processing emerged recently from research and industry. However, systems researchers, decision-makers, and data analysts are unaware of how these serverless systems compare to each other. In this paper, we identify existing serverless frameworks for data processing. We present a qualitative assessment of different system architectures and an experiment-driven quantitative comparison, including performance, cost, and usability using the TPC-H benchmark. Our results show that the three publicly available serverless data processing frameworks outperform a comparatively sized Apache Spark cluster in terms of performance and cost for ad-hoc queries on cold data.