"""A11-K Security Service — ADR-0011: Security By Default.

Every service must expose /health /ready /metrics /audit.

GET /a11k/security/health
GET /a11k/security/audit
GET /a11k/security/status
"""

from __future__ import annotations

from fastapi import FastAPI

app = FastAPI(title="A11-K Security Service", version="1.0.0")

AUDIT_LOG: list[dict] = []


@app.get("/a11k/security/health")
def health() -> dict:
    return {"status": "healthy", "service": "security-service"}


@app.get("/a11k/security/ready")
def ready() -> dict:
    return {"ready": True}


@app.get("/a11k/security/metrics")
def metrics() -> dict:
    return {"audit_entries": len(AUDIT_LOG), "incidents_open": 0}


@app.get("/a11k/security/audit")
def audit() -> dict:
    return {"entries": AUDIT_LOG[-50:], "total": len(AUDIT_LOG)}


@app.post("/a11k/security/audit")
def log_event(item: dict) -> dict:
    AUDIT_LOG.append(item)
    return {"logged": True, "total": len(AUDIT_LOG)}


@app.get("/a11k/security/status")
def status() -> dict:
    return {"service": "security-service", "status": "healthy"}
