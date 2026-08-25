# Progress Log

Commit against this daily — each entry should correspond to a real commit with working code,
not just notes. This log is also your interview cheat sheet: read it back before a call.

- [ ] **Day 1** — Repo scaffold, dataset chosen, problem framed (classification/regression + why)
- [ ] **Day 2** — Baseline model trained, MLflow tracking wired up, first run logged
- [ ] **Day 3** — FastAPI `/predict` endpoint wraps the model, loads it from MLflow artifact
- [ ] **Day 4** — Dockerfile for the app, image builds and runs locally, basic tests pass
- [ ] **Day 5** — Terraform: VPC module applied, state backend configured (S3 + DynamoDB lock)
- [ ] **Day 6** — Terraform: EKS cluster + ECR repo applied, cluster reachable via kubectl
- [ ] **Day 7** — GitHub Actions: lint + test job running on PR
- [ ] **Day 8** — GitHub Actions: build + push image to ECR on merge to main
- [ ] **Day 9** — Helm chart written for the serving app (deployment, service)
- [ ] **Day 10** — ArgoCD installed on cluster, Application manifest applied, auto-sync verified
- [ ] **Day 11** — Prometheus + Grafana installed, latency/error-rate dashboard live
- [ ] **Day 12** — Centralized logging wired up (ELK or CloudWatch), can trace one request end-to-end
- [ ] **Day 13** — HPA configured, load test run (k6/Locust), scaling behavior captured (screenshot/graph)
- [ ] **Day 14** — Secrets moved to AWS Secrets Manager, IAM roles scoped to least privilege
- [ ] **Day 15** — Architecture diagram finalized, README polished, short demo recorded

## Notes template (fill in as you go)

### Day N — <date>
- What I built:
- Why I made this choice (vs alternatives):
- What broke / what I learned:
- Next:
