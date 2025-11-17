Wisecow – DevOps Assignment

Containerization • Kubernetes Deployment • TLS • CI/CD • Zero-Trust Security

This repository contains my full implementation of the Wisecow DevOps assignment.

The goal of the project is to:

Containerize the Wisecow application

Deploy it into a Kubernetes cluster

Expose it as a Kubernetes Service

Implement CI/CD using GitHub Actions (Docker build + push + deploy)

(Challenge) Enable secure TLS communication using an Ingress

(Optional Challenge) Apply a Zero-Trust KubeArmor Policy
Application Overview

Wisecow is a simple bash-based web server that prints random “cow wisdom” using:

fortune-mod

cowsay

netcat-openbsd

The server listens on port 4499.

Run locally (without Docker):
  chmod +x wisecow.sh
  ./wisecow.sh
Open:
  http://localhost:4499

Dockerization
The application is containerized using the Dockerfile in this repository:
    FROM ubuntu:22.04

RUN apt-get update && \
    apt-get install -y cowsay fortune netcat-openbsd && \
    apt-get clean

WORKDIR /app
COPY wisecow.sh .
RUN chmod +x wisecow.sh

CMD ["./wisecow.sh"]


Build and run:
    docker build -t wisecow .
    docker run -p 4499:4499 wisecow


☸️ Kubernetes Deployment

All manifests are in the k8s/ directory.

✔ Deployment (deployment.yaml)

2 replicas

Uses Docker Hub image: othmaneberrouyne/wisecow:latest

✔ Service (service.yaml)

Type: ClusterIP

Exposes port 80 internally

Forwards to container port 4499

✔ Ingress (ingress.yaml)

Since my environment uses Traefik (k3s default):

annotations:
  traefik.ingress.kubernetes.io/router.entrypoints: web
spec:
  ingressClassName: traefik


To access the application:

curl http://wisecow.local


(Local DNS added in /etc/hosts.)


CI/CD (GitHub Actions)

File: .github/workflows/ci-cd.yaml

Pipeline tasks:

Build Docker image

Push to Docker Hub

Deploy automatically to Kubernetes using:

KUBE_CONFIG

DOCKER_USERNAME

DOCKER_PASSWORD

This enables Continuous Deployment on every push to main.

🔐 TLS

Ingress is compatible with Traefik TLS.
(If cert-manager is installed, TLS can be enabled easily.)

💻 Problem Statement 2 — Automation Scripts

Located in the scripts/ directory.

✔ System Health Monitor (Bash)

Monitors:

CPU usage

Memory usage

Disk space

Running processes

Logs alerts when thresholds are exceeded.

✔ Application Health Checker (Python)

Sends HTTP request to a target URL and prints:

UP (200 OK)

DOWN (error code or no response)

🛡️ Problem Statement 3 — Zero-Trust Policy (KubeArmor)

KubeArmor installed using Helm:

helm install kubearmor kubearmor/kubearmor --namespace kube-system


Policy file:
k8s/kubearmor-policy.yaml
