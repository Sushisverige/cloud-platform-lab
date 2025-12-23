import logging
import os
import time

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, PlainTextResponse
from prometheus_client import CONTENT_TYPE_LATEST, Counter, Histogram, generate_latest

logging.basicConfig(level=logging.INFO, format='{"level":"%(levelname)s","msg":"%(message)s"}')
log = logging.getLogger("app")

REQUESTS = Counter("http_requests_total", "Total HTTP requests", ["method", "path", "status"])
LATENCY = Histogram("http_request_duration_seconds", "HTTP request latency", ["path"])

app = FastAPI(title="cloud-platform-lab")

@app.middleware("http")
async def metrics_middleware(request: Request, call_next):
    start = time.time()
    try:
        response = await call_next(request)
    except Exception as e:
        log.info(f'{{"event":"exception","error":"{type(e).__name__}"}}')
        raise
    finally:
        duration = time.time() - start
        path = request.url.path
        LATENCY.labels(path=path).observe(duration)
    REQUESTS.labels(
        method=request.method,
        path=request.url.path,
        status=str(response.status_code),
    ).inc()
    return response

@app.get("/health")
def health():
    if os.getenv("FAIL_HEALTH", "0") == "1":
        return JSONResponse({"status": "down"}, status_code=503)
    return {"status": "ok"}

@app.get("/hello")
def hello():
    return {"message": "hello from cloud-platform-lab"}

@app.get("/metrics")
def metrics():
    data = generate_latest()
    return PlainTextResponse(data.decode("utf-8"), media_type=CONTENT_TYPE_LATEST)
