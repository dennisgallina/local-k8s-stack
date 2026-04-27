# local-k8s-stack

A local Kubernetes stack running a Python Flask API, built and pushed via GitHub Actions CI pipeline.

## Stack

- **App**: Python Flask
- **Container**: Docker
- **Orchestration**: Kubernetes (kind)
- **Manifests**: Kustomize
- **CI**: GitHub Actions → GitHub Container Registry (ghcr.io)

## Architecture

GitHub Push
│
▼
GitHub Actions (CI)
│
├── docker build
└── docker push → ghcr.io
Local:
kubectl apply -k k8s/base/
│
├── Deployment (2 replicas)
└── Service (ClusterIP)
## Prerequisites

- Docker
- kind
- kubectl

## Run locally

```bash
# Create cluster
kind create cluster --name local-k8s-stack

# Load image
kind load docker-image local-k8s-stack:0.1.0 --name local-k8s-stack

# Deploy
kubectl apply -k k8s/base/

# Test
kubectl port-forward service/flask-app 8080:80
curl http://localhost:8080/health
curl http://localhost:8080/info
```

## Endpoints

| Endpoint | Description |
|----------|-------------|
| `/health` | Liveness probe — returns `{"status": "ok"}` |
| `/info`   | App metadata — version and environment |
