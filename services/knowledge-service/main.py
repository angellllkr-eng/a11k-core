"""A11-K Knowledge Service — CPU-02 Knowledge Cluster.

ADR-0006: Knowledge Must Be Preserved.

POST /a11k/knowledge/store
GET  /a11k/knowledge/graph
GET  /a11k/knowledge/status
"""

from __future__ import annotations

from fastapi import FastAPI

app = FastAPI(title="A11-K Knowledge Service", version="1.0.0")

ENTITIES: list[dict] = []


@app.post("/a11k/knowledge/store")
def store(entity: dict) -> dict:
    record = {
        "id": entity.get("id", f"ent-{len(ENTITIES)+1}"),
        "type": entity.get("type", "unknown"),
        "title": entity.get("title", ""),
        "source": entity.get("source", ""),
        "relationships": entity.get("relationships", []),
    }
    ENTITIES.append(record)
    return record


@app.get("/a11k/knowledge/graph")
def graph() -> dict:
    return {"entities": ENTITIES, "total": len(ENTITIES)}


@app.get("/a11k/knowledge/status")
def status() -> dict:
    return {"service": "knowledge-service", "cpu": "CPU-02", "status": "healthy"}
