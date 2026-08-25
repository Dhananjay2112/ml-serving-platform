# Production ML Model Serving Platform

An end-to-end MLOps pipeline: train a model, track it with MLflow, serve it via FastAPI,
containerize it, provision infrastructure with Terraform, deploy to Kubernetes (EKS) via
GitOps (ArgoCD), and monitor it with Prometheus + Grafana.

## Why this project exists

Most "ML projects" stop at a Jupyter notebook. This one is scoped to demonstrate the full
path a model takes to become a reliable production service — the actual job of an
MLOps/DevOps engineer:

1. **Model training & tracking** — reproducible training runs, versioned artifacts
2. **Serving** — a real API, not a notebook cell
3. **Containerization** — Docker image, built and scanned in CI
4. **Infrastructure as Code** — Terraform provisions the cluster, nobody clicks in a console
5. **CI** — GitHub Actions lints, tests, builds, and pushes the image
6. **CD via GitOps** — ArgoCD syncs the cluster to match the Git repo, not a manual `kubectl apply`
7. **Observability** — Prometheus scrapes both infra and model-serving metrics; Grafana visualizes them
8. **Resilience** — Horizontal Pod Autoscaler + load testing to prove it scales
9. **Security** — secrets pulled from AWS Secrets Manager, least-privilege IAM

## Architecture

```
 Data/Model Training (model/train.py + MLflow)
              |
              v
   FastAPI serving app (app/main.py) --- Dockerfile --- ECR
              |
              v
   Terraform (infra/terraform) provisions VPC + EKS + ECR
              |
              v
   GitHub Actions CI (.github/workflows/ci.yml)
        build -> test -> push image to ECR
              |
              v
   ArgoCD (argocd/application.yaml) watches this repo's helm/ dir
        auto-syncs Helm release to EKS
              |
              v
   Prometheus + Grafana (monitoring/) scrape latency, error rate,
        and a model-specific metric (prediction distribution)
```

## Repo layout

```
model/          training script + requirements (MLflow tracked)
app/            FastAPI serving app + Dockerfile
infra/terraform/ VPC, EKS cluster, ECR repo
helm/           Helm chart for the serving app (deployment, service, HPA)
argocd/         ArgoCD Application manifest (GitOps entrypoint)
.github/workflows/ CI pipeline
monitoring/     Prometheus ServiceMonitor + Grafana dashboard JSON
docs/           architecture notes, decisions, day-by-day log
```

## Running locally

```bash
cd model && pip install -r requirements.txt && python train.py
cd ../app && pip install -r requirements.txt && uvicorn main:app --reload
curl -X POST localhost:8000/predict -H "Content-Type: application/json" -d '{"features":[0.1,0.2,0.3,0.4]}'
```

## Day-by-day log

See `docs/PROGRESS.md` — updated with a commit each day covering what was built and why.

## Status

Scaffold created. Follow the 15-day plan in `docs/PROGRESS.md` to fill in each stage in order —
train → serve → containerize → provision → deploy → observe → harden.
