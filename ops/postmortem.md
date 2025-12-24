# Postmortem: /health returning 503

## Summary
- 事象: `/health` が 503 を返し、監視対象として「ダウン」扱いとなった
- 期間: 2025-12-24 08:11 - 2025-12-24 08:11
- 影響: ヘルスチェックNG（想定: ロードバランサが切り離す）

## Detection
- Prometheus で `/metrics` の `http_requests_total` を確認し、503増加を検知

## Timeline (JST)
- 08:11 検知（/health が 503）
- 08:11 切り分け開始（ログ確認・環境変数確認）
- 08:11 FAIL_HEALTH=1 を特定
- 08:11 FAIL_HEALTH=0 に戻して再起動、復旧確認

## Root Cause
- `FAIL_HEALTH=1` の設定により `/health` が意図的に 503 となる実装

## Contributing Factors
- 失敗注入の手順/解除手順が一目で分かる場所にまとまっていなかった
- 503比率のアラート方針が未定義（検知が人手確認寄り）

## Resolution
- 環境変数を `FAIL_HEALTH=0` に戻し、コンテナ再起動で復旧

## What went well
- `docker compose logs` と `printenv` で素早く原因特定できた
- 復旧が単純で影響時間が短かった

## What went wrong
- 失敗注入の状態が外から分かりづらかった
- SLO/アラート基準がDraftで、運用判断が属人的になり得た

## Action Items
- [ ] Runbook に失敗注入の確認・解除・復旧確認手順を明記（Owner: sushi, Due: 2025-12-31）
- [ ] SLOに基づく可用性アラート方針（例の閾値）を決める（Owner: sushi, Due: 2025-12-31）
- [ ] 失敗注入が有効なときにログ/メトリクスで分かるサインを追加（Owner: sushi, Due: 2026-01-07）
