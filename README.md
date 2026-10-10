# A11-K Core — The CPU Civilization

**A11-K is not a business. A11-K is the computational nervous system.**

Purpose: Observe · Verify · Think · Remember · Protect · Decide.

Its citizens are CPUs. Every processor acts as a verification engine.

## CPU Departments

| CPU | Cluster | Output |
|-----|---------|--------|
| CPU-01 | Reality Processing | Truth |
| CPU-02 | Knowledge | Understanding |
| CPU-03 | Risk | Protection |
| CPU-04 | Executive | Decision |

## Services

```
services/
├── reality-service/    # fact verification, evidence intake, source scoring
├── knowledge-service/  # knowledge graph, memory, pattern recognition
├── risk-service/       # threat detection, simulation, recovery planning
├── executive-service/  # prioritization, resource allocation, decision registry
├── governance-service/ # repository governance, ADR enforcement
├── security-service/   # auth, audit, incident response
└── observatory-service/ # telemetry, health, alerts (consumes all events)
```

## Canonical Events Produced

FACT_VERIFIED · FACT_REJECTED · CONTRADICTION_FOUND · KNOWLEDGE_CREATED ·
RISK_DETECTED · RISK_ESCALATED · RISK_MITIGATED · RISK_CLOSED ·
DECISION_CREATED · DECISION_APPROVED · MISSION_CREATED ·
DIRECTIVE_CREATED · ALERT_CREATED · SYSTEM_DEGRADED · SYSTEM_HEALTHY

## Rule (ADR-0002)

Every A11-K capability must answer: **Does this increase certainty?** If not: Reject.

## Monorepo Home

Full scaffold: [robot-cpu-platform](https://github.com/angellllkr-eng/robot-cpu-platform)
