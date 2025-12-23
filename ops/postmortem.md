# Postmortem: /health returning 503

## Summary
- 事象: /health が 503 を返し、監視対象として「ダウン」扱いとなった
- 期間: 2025-12-24 08:11 - 2025-12-24 08:11
- 影響: ヘルスチェックNG（想定: ロードバランサが切り離す）

## Detection
- Prometheusで /metrics の http_requests_total と 503増加を確認

## Root Cause
- FAIL_HEALTH=1 の設定により /health が意図的に 503 となる実装

## Resolution
- 環境変数を FAIL_HEALTH=0 に戻し、コンテナ再起動で復旧

## Action Items
- 設定変更時の手順を runbook に明記
- 監視: 503比率のアラート閾値を決める（今後）
