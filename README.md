# Wisecow – DevOps Assignment  
**Containerization • Kubernetes Deployment • TLS • CI/CD**

This repository contains my implementation of the Wisecow DevOps assignment.

The goal of the project is to:

- Containerize the Wisecow application  
- Deploy it into a Kubernetes cluster (Minikube/Kind)  
- Expose it as a Service  
- Implement CI/CD with GitHub Actions  
- (Challenge) Enable secure TLS communication using an Ingress  

---

# 📦 Application Overview

Wisecow is a simple bash-based web server that prints random “cow wisdom” using:

- `fortune-mod`
- `cowsay`
- `netcat-openbsd`

The server listens on **port 4499**.

Run locally (without Docker):

```bash
chmod +x wisecow.sh
./wisecow.sh
