# Runbook: cloud-platform-lab

## 症状: /health が 503
### 1) 影響確認
- curl -i http://localhost:8000/health

### 2) ログ確認
- docker compose logs -f app

### 3) 設定確認
- docker compose exec app printenv | grep FAIL_HEALTH

### 4) 復旧
- FAIL_HEALTH=0 に戻して再起動
  - docker compose up -d --force-recreate app
