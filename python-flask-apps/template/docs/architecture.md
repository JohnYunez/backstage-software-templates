# Architecture

This application is a lightweight REST API built with Flask.

## Endpoints

- `/api/v1/${{values.api_path}}`: Returns a JSON object with a greeting, current server time, hostname, and an environment variable.
- `/api/v1/healthz`: Returns a simple health check status.

## Service endpoint

To get the url exposed by the load balancer, run:
```bash
echo "http://$(kubectl get svc -n ${{values.component_name}}-${{values.environment}} -o jsonpath={.items[].status.loadBalancer.ingress[0].hostname}):5000/api/v1/${{values.api_path}}"
```

## Images

[Dockerhub/johnyunez/${{values.component_name}}](https://hub.docker.com/repository/docker/johnyunez/${{values.component_name}})

## Components

- **Flask**: Web framework for Python.
- **Docker** (optional): For containerized deployment.
- **Environment Variables**: Reads `INFRA_DATA` and sets `APP_ENV` for configuration.

## Sequence Diagram

```mermaid
sequenceDiagram
    Client->>API: GET /api/v1/${{values.api_path}}
    API->>System: Get time, hostname, env
    API-->>Client: JSON response

    Client->>API: GET /api/v1/healthz
    API-->>Client: {"status": "up"}
```