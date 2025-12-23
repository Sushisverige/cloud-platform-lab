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
