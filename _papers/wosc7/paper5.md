---
title: Evaluation of Network File System as a Shared Data Storage in Serverless Computing
authors:
  - name: Jaeghang Choi
    email: chl8273@kookmin.ac.kr
    affiliation: Dept. of Computer Science, Kookmin Univ., Seoul, S. Korea
  - name: Kyungyong Lee
    email: leeky@kookmin.ac.kr
    affiliation: Dept. of Computer Science, Kookmin Univ., Seoul, S. Korea
pdf: https://dl.acm.org/doi/10.1145/3429880.3430096
presentation:
  pdf: https://www.serverlesscomputing.org/wosc6/presentations/[WOSC%202020]%20Evaluation%20of%20Network%20File%20System%20as%20a%20Shared%20Data%20Storage%20in%20Serverless%20Computing.pdf
video:
  talk: https://www.youtube.com/embed/pjNrI1x_4UM
---

Fully-managed cloud and Function-as-a-Service (FaaS) services allow the wide adoption of serverless computing for various cloud-native applications. Despite the many advantages that serverless computing provides, no direct connection support exists between function run-times, and it is a barrier for data-intensive applications. To overcome this limitation, the leading cloud computing vendor Amazon Web Services (AWS) has started to support mounting the network file system (NFS) across different function run-times. This paper quantitatively evaluates the performance of accessing NFS storage from multiple function run-times and compares the performance with other methods of sharing data among function run-times. Despite the great qualitative benefits of the approach, the limited I/O bandwidth of NFS storage can become a bottleneck, especially when the number of concurrent access from function run-times increases.