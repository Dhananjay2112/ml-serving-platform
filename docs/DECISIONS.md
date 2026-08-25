# Key Decisions (and how to talk about them in an interview)

**Why GitOps (ArgoCD) instead of `kubectl apply` in CI?**
CI shouldn't have direct write access to the cluster. With GitOps, CI only pushes an image
and updates a Git file (the image tag in `values.yaml`); ArgoCD is the only thing that
talks to the cluster, and it continuously reconciles - so drift gets corrected automatically
and every deployed state is traceable to a commit.

**Why Terraform for EKS instead of `eksctl` or console clicks?**
Reproducibility and review. Infra changes go through the same PR process as code changes,
and the whole environment can be destroyed and rebuilt from source.

**Why spot instances / single NAT gateway?**
Explicitly a portfolio-project cost decision, not a production one - and worth saying so
out loud in an interview. Shows you understand the trade-off (cost vs. availability) rather
than not knowing it exists.

**Why expose Prometheus metrics from the app itself (not just infra metrics)?**
Infra metrics (CPU, memory) tell you the pod is alive. They don't tell you the model is
still making good predictions. Tracking prediction distribution over time is a cheap first
step toward detecting model/data drift in production - a real MLOps concern, not just DevOps.

**What would you change for real production use?**
- Multi-AZ NAT gateways, not single
- Argo Image Updater or a bot commit instead of manually editing values.yaml in CI
- A model registry promotion gate (staging -> production) instead of always pointing at
  `models:/serving-model/Production`
- Canary or blue-green rollout via Argo Rollouts instead of a plain Deployment
