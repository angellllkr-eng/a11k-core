"""A11-K Reality Service — CPU-01 Reality Processing Cluster.

ADR-0005: Reality Is The Source Of Truth.
ADR-0002: A11-K Owns Certainty.

POST /a11k/reality/verify
GET  /a11k/reality/truth
GET  /a11k/reality/status
"""

from __future__ import annotations

from fastapi import FastAPI

app = FastAPI(title="A11-K Reality Service", version="1.0.0")

FACTS: list[dict] = []


@app.post("/a11k/reality/verify")
def verify_fact(claim: dict) -> dict:
    text = str(claim.get("claim", "")).strip()
    source = str(claim.get("source", "")).strip()

    if not text or not source:
        fact = {"claim": claim, "status": "REJECTED", "confidence": 0, "reason": "missing claim or source"}
        FACTS.append(fact)
        return fact

    confidence = 95 if source else 40
    status = "VERIFIED" if confidence >= 80 else "REJECTED"
    fact = {"claim": claim, "status": status, "confidence": confidence, "source": source}
    FACTS.append(fact)
    return fact


@app.get("/a11k/reality/truth")
def truth() -> dict:
    verified = [f for f in FACTS if f["status"] == "VERIFIED"]
    return {
        "facts": FACTS,
        "total": len(FACTS),
        "verified": len(verified),
        "truth_score": round(len(verified) / len(FACTS) * 100, 1) if FACTS else 0.0,
    }


@app.get("/a11k/reality/status")
def status() -> dict:
    return {"service": "reality-service", "cpu": "CPU-01", "status": "healthy"}
