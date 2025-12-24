# Runbook: cloud-platform-lab

## 目的
`/health` が 503 を返す状況を素早く切り分け・復旧する。

## 症状
- `/health` が 503 を返す

## 影響
- ヘルスチェックNG（ロードバランサ/監視がある前提ではアラート・切り離し対象）

## 想定原因（まず疑う順）
1. 失敗注入（`FAIL_HEALTH=1`）が有効
2. アプリプロセス異常 / コンテナ再起動ループ
3. 設定ミス（環境変数/composeの差分）

## まず5分でやる（切り分け）
```bash
curl -i http://localhost:8000/health
docker compose ps
docker compose logs --tail=200 app
```

## 手順
### 1) 影響確認
```bash
curl -i http://localhost:8000/health
```

### 2) ログ確認
```bash
docker compose logs -f app
```

### 3) 設定確認（失敗注入の有無）
```bash
docker compose exec app printenv | grep FAIL_HEALTH || true
```

### 4) 復旧（失敗注入を解除して再起動）
```bash
FAIL_HEALTH=0 docker compose up -d --force-recreate app
```

## 復旧確認
```bash
