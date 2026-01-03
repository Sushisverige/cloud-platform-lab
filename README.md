![ci](https://github.com/Sushisverige/cloud-platform-lab/actions/workflows/ci.yml/badge.svg)

# cloud-platform-lab

SRE/クラウド基盤の基礎実績として、ミニAPIを作成し、メトリクス公開 + Prometheusで収集し、運用ドキュメント（Runbook/SLO/Postmortem）まで揃えました。

## Features
- FastAPI: /health, /hello, /metrics
- Prometheus: metrics scrape
- CI: GitHub Actions (ruff + pytest)
- Ops docs: ops/runbook.md, ops/slo.md, ops/postmortem.md

## Run (local)
1) docker compose up --build
2) curl http://localhost:8000/health
3) curl http://localhost:8000/metrics | head
Prometheus: http://localhost:9090

## Failure injection
FAIL_HEALTH=1 docker compose up -d --force-recreate app
curl -i http://localhost:8000/health

## Compliance / Privacy / Ethics
- This repository is provided as a sample/portfolio.
- Do not process personal/confidential data without proper authorization and consent.
- Review docs/DATA_HANDLING.md and docs/ETHICS.md before any real-world use.
