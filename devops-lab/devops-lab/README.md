# devops-lab

A small notes API used as the practice app for learning DevOps layer by layer.

## Run locally
    python -m venv .venv && source .venv/bin/activate
    pip install -r requirements.txt
    python -m app.main

## Test
    pytest -v

## Endpoints
- GET /health
- GET /notes, POST /notes {"text": "..."}
- GET /notes/<id>, DELETE /notes/<id>

## Layers
- [x] L1 Source code and CI/CD (this repo + .github/workflows/ci.yml)
- [ ] L2 Containers and Orchestration
- [ ] L3 Cloud and Infrastructure
- [ ] L4 Infrastructure as code and automation
- [ ] L5 Observability and Reliability
- [ ] L6 Security and Compliance
- [ ] L7 Data and Dependencies
- [ ] L8 Production Operations and Recovery
