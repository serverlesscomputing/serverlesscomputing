---
title: Resource Management for Cloud Functions with Memory Tracing, Profiling and Autotuning
authors:
  - name: Josef Spillner
    email: josef.spillner@zhaw.ch
    affiliation: Zurich University of Applied Sciences, Winterthur, Switzerland
pdf: "https://dl.acm.org/doi/abs/10.1145/3429880.3430094"
presentation:
  pdf: https://www.serverlesscomputing.org/wosc6/presentations/faasmemautotuning-slides.pdf
video:
  lightning: https://www.youtube.com/watch?v=qOc64o68rI8
  talk: https://www.youtube.com/embed/ESb-DKQDOwo
---

Application software provisioning evolved from monolithic designs towards differently designed abstractions including serverless applications. The promise of that abstraction is that developers are free from infrastructural concerns such as instance activation and autoscaling. Today's serverless architectures based on FaaS are however still exposing developers to explicit low-level decisions about the amount of memory to allocate for the respective cloud functions. In many cases, guesswork and ad-hoc decisions determine the values a developer will put into the configuration. We contribute tools to measure the memory consumption of a function in various Docker, OpenFaaS and GCF/GCR configurations over time and to create trace profiles that advanced FaaS engines can use to autotune memory dynamically. Moreover, we explain how pricing forecasts can be performed by connecting these traces with a FaaS characteristics knowledge base.