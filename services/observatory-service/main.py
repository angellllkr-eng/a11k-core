"""A11-K Observatory Service — ADR-0013: Observatory Is Mandatory.

Consumes ALL events. Produces ALERT_CREATED, SYSTEM_DEGRADED, SYSTEM_HEALTHY.

GET /a11k/observatory/telemetry
GET /a11k/observatory/status
"""

from __future__ import annotations

from fastapi import FastAPI

app = FastAPI(title="A11-K Observatory Service", version="1.0.0")

TELEMETRY: list[dict] = []


@app.post("/a11k/observatory/ingest")
def ingest(event: dict) -> dict:
    TELEMETRY.append(event)
    # v1: simple degradation detection
    if event.get("event_type") in ("SYSTEM_DEGRADED", "INCIDENT_REPORTED"):
        return {"ingested": True, "alert": "ALERT_CREATED"}
    return {"ingested": True}


@app.get("/a11k/observatory/telemetry")
def telemetry() -> dict:
    return {"events": TELEMETRY[-100:], "total": len(TELEMETRY)}


@app.get("/a11k/observatory/status")
def status() -> dict:
    return {"service": "observatory-service", "status": "healthy", "events_captured": len(TELEMETRY)}
