class Templates:

    @staticmethod
    def readme():

        return """
# OptiMind AI - Production Deployment Package

This package contains the files necessary to deploy your optimized model in a production environment.

## Quick Start

### 1. Local / Docker Compose
Run the following command to build the image and start the service locally:
```bash
docker-compose up --build
```
The service will be available at `http://localhost:8000`.

### 2. Kubernetes
Deploy to a Kubernetes cluster using the provided manifests:
```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

### 3. Nginx Reverse Proxy
To configure Nginx as a reverse proxy, copy `nginx.conf` to your server's Nginx configuration directory.
""".strip()
