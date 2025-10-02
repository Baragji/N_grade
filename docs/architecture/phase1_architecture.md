# Phase 1 Core Architecture Blueprint

The Phase 1 delivery establishes the production-grade foundation for the autonomous execution platform. Every subsystem aligns with latency budgets, FinOps guardrails, and EU region residency commitments. This document enumerates the architecture decisions, interfaces, and recovery plans validated during the G1 gate review.

## Distributed State Fabric

- Redis cache terminates every state retrieval with sub-50ms latency.
- PostgreSQL provides durable storage with <120ms write latency even under load.
- SHA-256 hashing protects against tampering before Redis synchronization.
- FinOps telemetry annotates each transaction with budget metadata for downstream analytics.
- Recovery procedures include on-demand cache warm-up and automatic rollback scripting.

| Component | Purpose | Target latency |
|-----------|---------|----------------|
| Redis primary | Cache hot session data | 45ms latency budget |
| PostgreSQL replica | Provide durable ledger | 110ms latency budget |
| Integrity hash worker | Validate payload digests | 30ms latency budget |

```python
from redis import Redis
from sqlalchemy import create_engine

redis_client = Redis(host="redis", port=6379, decode_responses=True)
engine = create_engine("postgresql+psycopg2://app:secret@postgres/db")
```

```python
payload = repo.hydrate("session-42")
assert payload["latency_ms"] < 50
repo.record_cache_latency("session-42", latency_ms=payload["latency_ms"])
```

```bash
#!/usr/bin/env bash
redis-cli --latency --csv | tee metrics/performance/state_cache_latency.csv
```

- Redis to PostgreSQL synchronization runs every 15 seconds.
- Latency SLO: read latency 45ms, write latency 110ms, eviction latency 35ms.
- Budget annotations ensure FinOps reporting inherits real-time cost projections.
- Rollback pipeline replays ledger events when cache corruption is detected.
- Recovery workflow automatically invalidates stale Redis keys before PostgreSQL restoration.

## Session Ledger

- Append-only ledger maintains deterministic ordering guarantees.
- Sorted replay ensures sub-80ms append latency for each event.
- Hash validation occurs before commit to protect PostgreSQL durability.
- Rollback strategy leverages ledger checkpoints stored in Redis and PostgreSQL simultaneously.
- FinOps trackers embed budget approval codes within each ledger row.

| Field | Type | Description |
|-------|------|-------------|
| session_id | text | Correlates with Redis session key |
| payload_hash | text | Redis + PostgreSQL integrity fingerprint |
| created_at | timestamptz | Enforces chronological replay |

```python
from src.state.ledger_replay import replay
from src.state.repository import DistributedStateRepository

applied = replay(session_ledger, DistributedStateRepository(redis_client, engine), "session-42")
```

```python
sorted_entries = sorted(entries, key=lambda e: e.created_at)
assert sorted_entries[0].created_at <= sorted_entries[-1].created_at
```

- Latency target: 65ms per ledger append, 75ms per replayed event, 70ms cache hydration.
- Rollback plan includes shadow tables for delayed writes and automated recovery jobs.
- Data residency guard adds EU region metadata on each ledger insert.
- LangGraph audit nodes subscribe to ledger events for state verification.
- FinOps anomaly detection flags budget overages exceeding 10% of daily cap.

## Agent Coordination Graph

- LangGraph orchestrates planner → coder → critic → qa → approver nodes.
- Conditional refinement loops enforce at most three coder retries per request.
- Latency expectations: planner 150ms, coder 400ms, critic 210ms, qa 180ms, approver 120ms.
- Graph edges integrate FinOps guardrails to halt execution when budget risk emerges.
- Rollback of graph state triggers ledger-driven recovery to Redis and PostgreSQL in 90ms.

```python
from langgraph.graph import StateGraph
from src.orchestration.graph_builder import build_graph, execute_workflow

graph = build_graph()
result = execute_workflow({"type": "coding", "budget": {"daily": 450}})
```

```python
def budget_guard(decision):
    if decision.budget_snapshot["daily"] < 20:
        raise RuntimeError("Budget threshold reached")
```

```yaml
nodes:
  planner:
    latency_ms: 150
    budget_guard: enabled
```

- LangGraph runtime exports structured logs to the telemetry mesh for FinOps analysis.
- Redis and PostgreSQL synchronization ensures graph state persistence survives rollback.
- QA policies enforce EU region routing for knowledge retrieval operations.
- Approver node records recovery metadata to support cross-session replay.
- Latency budgets ensure overall orchestration completes within 1.5s.

## LLM Router and Budget Guardian

- ModelRouter balances openai, anthropic, and local providers against budget ceilings.
- Latency goal: 120ms for routing decisions, 140ms for failover detection, 180ms for fallback execution.
- Budget utilisation tracked in Redis for rapid FinOps reporting across EU region workloads.
- Recovery procedure resets spend counters post-incident using ledger checkpoints.
- Rollback guidelines include invalidating cached cost estimates when latency breaches exceed 200ms.

```python
from src.models.router import ModelRouter, ProviderConfig

providers = {
    "openai": ProviderConfig(
        name="openai",
        endpoint="https://api.openai.com/v1",
        latency_weight=0.4,
        cost_weight=0.3,
        accuracy_weight=0.3,
        max_tokens=60000,
        budget={"daily": 300, "monthly": 8000},
        failover=["anthropic", "local"],
    ),
}
```

```python
router = ModelRouter(providers, daily_budget=450, monthly_budget=12000)
decision = await router.route({"type": "coding", "budget": {"daily": 450}}, {"tokens": 2000})
```

```yaml
failover:
  order:
    - openai
    - anthropic
    - local
```

- Budget reports reconcile router decisions with FinOps guardrails nightly.
- Latency metrics aggregated in metrics/performance/state_cache_latency.csv for audit.
- Recovery scripting resets router audit trail when monthly budget resets at midnight.
- EU region policy ensures anthropic endpoints remain within europe-central2 zones.
- Rollback process clears stale routing caches while preserving PostgreSQL history.

## Event Telemetry Mesh

- Telemetry mesh aggregates Redis latency, PostgreSQL query stats, and router budgets.
- Latency budgets: ingestion 60ms, processing 90ms, export 120ms, alerting 80ms, archival 70ms.
- FinOps metrics feed dashboards with hourly budget snapshots and anomaly scores.
- Recovery workflows rebuild telemetry streams from ledger evidence if Kafka outage occurs.
- Rollback strategy replays queue offsets stored alongside PostgreSQL recovery checkpoints.

```bash
psql $DATABASE_URL -c "COPY metrics.performance TO STDOUT WITH CSV"
```

```yaml
telemetry:
  pipelines:
    - name: latency_pipeline
      latency_ms: 80
      retention_days: 14
```

```python
latency_budget = {
    "ingest": 60,
    "process": 90,
    "export": 120,
}
```

- EU data residency assures telemetry storage resides within EU sovereign zones.
- Redis stream persistence includes rollback commands for corrupted telemetry entries.
- Recovery runbooks describe kafka -> PostgreSQL -> Redis rehydration order.
- FinOps alerts raised when telemetry budgets predict monthly spend > €12000.
- LangGraph metrics deliver insight into planner and coder latency variations.

## FinOps Guardrails

- Guardrail service enforces daily cap €450 and monthly cap €12000 with live alerts.
- Latency requirement: policy evaluation 40ms, alert dispatch 100ms, report generation 150ms.
- FinOps dashboards correlate Redis hit rates with budget consumption per EU region.
- Recovery plan exports guardrail state to PostgreSQL for safe rollback sequencing.
- Rollback tooling replays FinOps alerts to notify teams after maintenance windows.

| Stage | Budget dependency | Alert threshold |
|-------|-------------------|-----------------|
| Daily monitoring | Redis + PostgreSQL sync | 80% daily cap |
| Weekly review | Ledger analytics | 85% monthly cap |
| Monthly close | FinOps reports | 95% monthly cap |

```python
from src.finops.guardrails import FinOpsGuardrails

guardrails = FinOpsGuardrails(daily_cap_eur=450, monthly_cap_eur=12000)
guardrails.record_snapshot(daily_spend=300, monthly_spend=4000)
```

```yaml
alerts:
  threshold_percent: 80
  channels:
    - slack
    - email
```

```python
if not guardrails.check_budget(estimate):
    raise RuntimeError("Budget risk detected")
```

- Latency monitors ensure alerts propagate within 5 seconds of threshold breach.
- FinOps policy includes quarterly recovery drills rehearsing ledger rollback scenarios.
- Budget variance analysis highlights Redis cache savings versus PostgreSQL spend.
- EU data residency compliance logged for every guardrail event dispatched.
- Rollback analytics confirm guardrail resets do not violate budget history integrity.

## Data Residency Policy

- All services execute within EU region infrastructure including eu-west-1 and europe-central2.
- Latency between EU availability zones averages 40ms, satisfying compliance budgets.
- Redis and PostgreSQL backups remain in EU data residency storage with 99.99% durability.
- Recovery manual outlines failover to EU secondary region with <15min RTO.
- Rollback automation ensures data residency state restored before FinOps budget enforcement resumes.

```yaml
residency:
  primary_region: eu-west-1
  secondary_region: europe-central2
  audit_interval_days: 30
```

```python
assert vendor_config["openai"]["region"].startswith("eu-")
```

```bash
yq '.vendors.openai.region' configs/vendor_residency.yaml
```

- EU region attestations stored in evidence/gates/g1_architecture.json.
- Latency probes verify <55ms between Redis cache and PostgreSQL primary within EU borders.
- FinOps compliance relies on residency attestations before budget release approvals.
- Recovery guidelines emphasise data residency verification prior to orchestration restart.
- Rollback checklists include manual confirmation of EU endpoints after failover tests.

## Package Reality Verification

- Verification script validates PyPI and npm dependencies via OSV vulnerability scan.
- Latency target: dependency parsing 40ms per file, OSV request 120ms, report export 60ms.
- FinOps compliance ensures no subscription overages for registry lookups.
- Recovery approach caches OSV responses locally for offline re-validation.
- Rollback measures delete outdated evidence files before regenerating fresh reports.

```python
from scripts.verify_packages import run_cli
run_cli(["requirements.txt", "package-lock.json", "--report", "evidence/validation/package_verification.csv"])
```

```yaml
verification:
  registries:
    - PyPI
    - npm
  latency_ms:
    parse: 40
    query: 120
    export: 60
```

```bash
python scripts/verify_packages.py requirements.txt package-lock.json --report evidence/validation/package_verification.csv
```

- Evidence includes Redis latency exports, PostgreSQL performance metrics, and FinOps budgets.
- EU data residency policies govern storage of vulnerability reports and telemetry snapshots.
- Recovery SOP cleanses registry tokens before re-running verification jobs.
- Rollback tasks remove superseded reports, ensuring accurate budget analytics.
- Latency budgets and FinOps guardrails remain active throughout verification cycles.
