"""A11-K Governance Service — repository and ADR enforcement.

ADR-0010: Repository Creation Governance.

POST /a11k/governance/repo
GET  /a11k/governance/repos
GET  /a11k/governance/status
"""

from __future__ import annotations

from fastapi import FastAPI

app = FastAPI(title="A11-K Governance Service", version="1.0.0")

REPOS: list[dict] = []


@app.post("/a11k/governance/repo")
def register_repo(item: dict) -> dict:
    # Zero Operational Law check
    certainty = bool(item.get("increases_certainty"))
    value = bool(item.get("increases_value"))
    if not certainty and not value:
        return {"status": "REJECTED", "reason": "passes neither A11-K nor MindReply test", "action": "archive/merge/delete"}
    repo = {
        "name": item.get("name", ""),
        "owner": item.get("owner", ""),
        "purpose": item.get("purpose", ""),
        "domain": "a11k" if certainty else "mindreply",
        "status": "active",
    }
    REPOS.append(repo)
    return repo


@app.get("/a11k/governance/repos")
def repos() -> dict:
    return {"repositories": REPOS, "total": len(REPOS)}


@app.get("/a11k/governance/status")
def status() -> dict:
    return {"service": "governance-service", "status": "healthy"}
