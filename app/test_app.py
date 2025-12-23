from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_health_ok():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"

def test_metrics_exists():
    r = client.get("/metrics")
    assert r.status_code == 200
    assert "http_requests_total" in r.text
