# Phase 1: Core Architecture Build Instructions

**Contract ID:** PHASE_1_CORE_ARCHITECTURE_2025  
**Phase:** Phase 1 (Week 3-6)  
**Gate Target:** G1 Architecture Approved  
**Dependency:** Phase 0 Foundation (G0 PASSED ✅)  
**Estimated Effort:** 120 hours  
**Iteration Limit:** 2 attempts maximum

---

## ⚠️ CRITICAL SUCCESS FACTORS

**This is a CONTRACT-ENFORCED delivery.** The same methodology that made Phase 0 successful applies here:

### **Zero-Tolerance Quality Gates:**
- ❌ **NO** `TODO`, `TBD`, `FIXME` markers allowed
- ❌ **NO** `pass` stubs or `raise NotImplementedError`
- ❌ **NO** template markers or placeholder content
- ❌ **NO** incomplete functions or empty docstrings
- ✅ **ALL** code must be production-ready
- ✅ **ALL** tests must pass
- ✅ **ALL** metrics must be generated
- ✅ **ALL** evidence must exist

### **Validation Authority:**
```bash
python3 scripts/validate_contract.py contracts/phase_1_core_architecture.contract.json
```
**Exit code 0 = ACCEPTED. Non-zero = REJECTED.**

### **Iteration Limit Enforcement:**
- **Attempt 1:** Full implementation using these instructions
- **Attempt 2:** One revision if first attempt fails validation
- **Attempt 3:** Does not exist. Two failures = project pause, gap analysis, methodology review

This is identical to the Phase 0 methodology that succeeded after the first attempt catastrophically failed.

---

## 📋 DELIVERY OVERVIEW

### **22 Deliverables Required:**

| Category | Count | Files |
|----------|-------|-------|
| **Core Implementation** | 6 | State repository, ledger replay, orchestration graph, LLM router, notifications, FinOps guardrails |
| **Scripts** | 2 | Package verification, residency checker |
| **Configuration** | 3 | FinOps policy, router config, residency config |
| **Infrastructure** | 1 | Database migrations |
| **Documentation** | 1 | Phase 1 architecture |
| **Tests** | 3 | State, orchestration, router integration tests |
| **Evidence** | 1 | G1 gate validation JSON |
| **Metrics** | 5 | Cache latency, router accuracy, notifications, budget tracking, package report |

**Total Lines Expected:** 2,500-3,500 production-ready lines  
**Total Files:** 22 complete files

---

## 🎯 PHASE 1 OBJECTIVES

Phase 1 transforms the Phase 0 foundation into a production-ready autonomous coding architecture with:

1. **Distributed State Fabric:** Redis + PostgreSQL with <50ms cache reads, <120ms durable writes, SHA-256 integrity
2. **Session Ledger:** Append-only audit trail with <80ms latency, replay capability, immutable checksums
3. **Agent Coordination Graph:** LangGraph orchestration (planner→coder→critic→qa→approver) with conditional refinement
4. **LLM Router:** Multi-provider routing with budget enforcement, <120ms latency, ≥99% failover success
5. **Event Telemetry Mesh:** Real-time notifications with correlation IDs, <5s latency, ≥99.5% delivery
6. **FinOps Guardrails:** Phase 1 budget €450 daily / €12k monthly with 80% alert thresholds
7. **Data Residency:** 100% EU region enforcement, vendor logging disabled, GDPR compliance
8. **Package Reality:** Zero unverified dependencies, OSV scanning, <8min execution

---

## 📦 DELIVERABLE SPECIFICATIONS

### **1. Distributed State Repository**

**File:** `src/state/repository.py`  
**Lines:** 100-250  
**Purpose:** Dual-storage state management with Redis (speed) + PostgreSQL (durability)

#### **Requirements:**
- Redis client integration with TTL support (setex/expire)
- SQLAlchemy ORM for PostgreSQL with transaction management
- SHA-256 hashing for integrity validation
- Methods: `save()`, `get()`, `delete()`, `verify_integrity()`
- <50ms Redis GET latency (p95)
- <120ms PostgreSQL write latency
- Cache hit ratio target: ≥92%

#### **Key Components:**
```python
from redis import Redis
from sqlalchemy.orm import Session
import hashlib
import json

class StateRepository:
    def __init__(self, redis_client: Redis, db_session: Session, ttl_seconds: int = 3600):
        self.redis_client = redis_client
        self.db_session = db_session
        self.ttl_seconds = ttl_seconds
    
    def save(self, session_id: str, payload: dict) -> str:
        """Persist state with integrity hash and TTL enforcement."""
        serialized = json.dumps(payload, sort_keys=True)
        state_hash = hashlib.sha256(serialized.encode()).hexdigest()
        
        # Write to Redis cache
        self.redis_client.setex(f"session:{session_id}", self.ttl_seconds, serialized)
        
        # Write to PostgreSQL for durability
        self.db_session.execute(
            text("""
                INSERT INTO sessions(id, payload, payload_hash, updated_at)
                VALUES (:id, :payload, :payload_hash, :updated_at)
                ON CONFLICT (id) DO UPDATE SET 
                    payload = EXCLUDED.payload,
                    payload_hash = EXCLUDED.payload_hash,
                    updated_at = EXCLUDED.updated_at
            """),
            {
                "id": session_id,
                "payload": serialized,
                "payload_hash": state_hash,
                "updated_at": datetime.utcnow()
            }
        )
        self.db_session.commit()
        return state_hash
    
    def get(self, session_id: str) -> dict | None:
        """Retrieve state from cache (fast) or DB (fallback)."""
        # Try cache first
        cached = self.redis_client.get(f"session:{session_id}")
        if cached:
            return json.loads(cached)
        
        # Fallback to database
        result = self.db_session.execute(
            text("SELECT payload FROM sessions WHERE id = :id"),
            {"id": session_id}
        ).fetchone()
        
        if result:
            payload = json.loads(result[0])
            # Warm cache
            self.redis_client.setex(f"session:{session_id}", self.ttl_seconds, result[0])
            return payload
        
        return None
```

#### **Testing Requirements:**
- 1,000-iteration stability test (zero failures)
- Cache hit ratio measurement over 24-hour synthetic workload
- Failover scenario: Redis down, PostgreSQL continues
- Integrity validation: hash mismatches detected

---

### **2. Session Ledger Replay Service**

**File:** `src/state/ledger_replay.py`  
**Lines:** 80-200  
**Purpose:** Deterministic state rehydration from append-only ledger

#### **Requirements:**
- Strict ordering enforcement (sorted by event ID)
- Idempotency checks (skip already-replayed events)
- <80ms append latency per entry
- Immutable checksum validation
- Methods: `replay_events()`, `append_event()`, `verify_ledger_integrity()`

#### **Key Components:**
```python
from sqlalchemy.orm import Session
from models import LedgerEvent

def replay_events(session: Session, event_ids: list[int]) -> None:
    """Replay ledger events in strict order with idempotency safeguards."""
    for event_id in sorted(event_ids):
        event = session.get(LedgerEvent, event_id)
        if event is None:
            raise ValueError(f"Ledger event {event_id} missing - data integrity compromised")
        
        if event.replayed:
            continue  # Idempotency: skip already-replayed events
        
        # Execute replay logic
        event.replay()
        event.replayed = True
        session.commit()

def append_event(session: Session, event_type: str, payload: dict) -> int:
    """Append event to ledger with checksum."""
    import hashlib
    import json
    
    serialized = json.dumps(payload, sort_keys=True)
    checksum = hashlib.sha256(serialized.encode()).hexdigest()
    
    event = LedgerEvent(
        event_type=event_type,
        payload=serialized,
        checksum=checksum,
        replayed=False
    )
    session.add(event)
    session.commit()
    return event.id
```

---

### **3. Agent Coordination Graph**

**File:** `src/orchestration/graph_builder.py`  
**Lines:** 100-300  
**Purpose:** LangGraph orchestration defining agent workflow with conditional loops

#### **Requirements:**
- LangGraph StateGraph integration
- Nodes: planner, coder, critic, qa, approver (5 minimum)
- Conditional edge: critic → coder (if needs_refinement) or → qa
- <1.5s graph execution latency per loop
- Policy enforcement via LiteGuard (100% coverage)
- Graph snapshots for reproducibility

#### **Key Components:**
```python
from langgraph.graph import StateGraph, END
from orchestration.nodes import planner_node, coder_node, critic_node, qa_node, approver_node

def build_graph():
    """Build agent coordination graph with conditional refinement loop."""
    graph = StateGraph()
    
    # Add agent nodes
    graph.add_node("planner", planner_node)
    graph.add_node("coder", coder_node)
    graph.add_node("critic", critic_node)
    graph.add_node("qa", qa_node)
    graph.add_node("approver", approver_node)
    
    # Define workflow edges
    graph.add_edge("planner", "coder")
    graph.add_edge("coder", "critic")
    
    # Conditional refinement loop
    graph.add_conditional_edges(
        "critic",
        lambda state: state.context.get("needs_refinement", False),
        {
            True: "coder",      # Refinement needed: loop back to coder
            False: "qa"         # Looks good: proceed to QA
        }
    )
    
    graph.add_edge("qa", "approver")
    graph.add_edge("approver", END)
    
    graph.set_entry_point("planner")
    return graph.compile()
```

#### **Testing Requirements:**
- State transition validation (planner → coder → critic → qa → approver)
- Conditional loop triggering (critic → coder when refinement needed)
- Policy violation detection
- Graph rebuild from YAML snapshot (<30s)

---

### **4. LLM Router with Budget Guardian**

**File:** `src/models/router.py`  
**Lines:** 120-300  
**Purpose:** Multi-provider routing with budget enforcement and failover

#### **Requirements:**
- Provider support: OpenAI, Anthropic, local fallback
- Budget enforcement: zero breaches (100% success rate)
- <120ms routing decision latency (p95)
- ≥99% failover success rate
- Cost tracking per task type
- Methods: `route()`, `estimate_cost()`, `check_budget()`, `failover()`

#### **Key Components:**
```python
from typing import Literal
from openai import OpenAI
from anthropic import Anthropic
from models.providers.local import LocalProvider
from policies.finops import FinOpsBudget

CLIENTS = {
    "openai": OpenAI(),
    "anthropic": Anthropic(),
    "local": LocalProvider()
}

class ModelRouter:
    def __init__(self, budget: FinOpsBudget):
        self.budget = budget
    
    async def route(
        self, 
        prompt: str, 
        task: Literal["planning", "coding", "review"], 
        token_estimate: int
    ) -> dict:
        """Route request to optimal provider with budget enforcement."""
        
        # Budget check BEFORE calling provider
        if not self.budget.can_afford(task, token_estimate):
            raise BudgetExceededError(
                f"Request would exceed {task} budget. "
                f"Estimated cost: €{self.budget.estimate_cost(task, token_estimate)}"
            )
        
        # Select provider based on task type and budget
        candidate = self.budget.select_provider(task, token_estimate)
        
        try:
            client = CLIENTS[candidate.provider_id]
            response = await client.complete(prompt=prompt, model=candidate.model)
            cost = candidate.estimate_cost(token_estimate)
            
            # Record actual spend
            self.budget.record(task, cost)
            
            return {
                "model": candidate.model,
                "provider": candidate.provider_id,
                "cost": cost,
                "response": response
            }
        
        except Exception as e:
            # Failover to local model
            return await self._failover_to_local(prompt, task, token_estimate)
    
    async def _failover_to_local(self, prompt: str, task: str, tokens: int) -> dict:
        """Failover to local model when primary provider fails."""
        client = CLIENTS["local"]
        response = await client.complete(prompt=prompt, model="local-llm")
        return {
            "model": "local-llm",
            "provider": "local",
            "cost": 0.0,
            "response": response,
            "failover": True
        }
```

#### **Testing Requirements:**
- Budget enforcement: requests exceeding cap rejected
- Failover: primary provider failure triggers local fallback (≥99% success)
- Routing accuracy: ≥92% correct provider selection
- Latency: p95 < 120ms

---

### **5. Event Telemetry & Notifications Publisher**

**File:** `src/notifications/publisher.py`  
**Lines:** 80-200  
**Purpose:** Real-time event notifications with correlation tracking

#### **Requirements:**
- Delivery channels: Slack, email, webhooks
- Correlation ID in every notification (100% coverage)
- <5s notification latency
- ≥99.5% delivery success rate
- Methods: `publish()`, `publish_batch()`, `get_delivery_status()`

#### **Key Components:**
```python
import httpx
from typing import Dict

class NotificationPublisher:
    def __init__(self, http_client: httpx.AsyncClient, destinations: Dict[str, str]):
        self.client = http_client
        self.destinations = destinations
    
    async def publish(self, payload: Dict[str, str]) -> None:
        """Send notifications to all configured destinations with correlation metadata."""
        
        # Ensure correlation ID present
        payload.setdefault("correlation_id", payload.get("trace_id", "n/a"))
        
        # Add timestamp if not present
        if "timestamp" not in payload:
            payload["timestamp"] = datetime.utcnow().isoformat()
        
        # Send to all destinations
        for name, url in self.destinations.items():
            try:
                response = await self.client.post(url, json=payload, timeout=3)
                response.raise_for_status()
            except Exception as e:
                # Log failure but don't block other destinations
                logger.error(f"Notification to {name} failed: {e}")
```

---

### **6. FinOps Guardrails Implementation**

**File:** `src/finops/guardrails.py`  
**Lines:** 100-250  
**Purpose:** Budget enforcement with daily/monthly caps and alert triggers

#### **Requirements:**
- Daily spend variance ≤5% from budget target
- Alert lead time ≥24 hours before monthly cap breach
- Token ceiling enforcement: 100% success rate
- Methods: `check_budget()`, `record_spend()`, `trigger_alert()`, `get_remaining_budget()`

#### **Key Components:**
```python
class FinOpsBudget:
    def __init__(self, phase: int, config: dict):
        self.phase = phase
        self.daily_cap_eur = config["phases"][phase]["daily_eur_cap"]
        self.monthly_cap_eur = config["phases"][phase]["monthly_eur_cap"]
        self.current_daily_spend = 0.0
        self.current_monthly_spend = 0.0
        self.alert_threshold = config["alerts"]["threshold_percent"] / 100
    
    def can_afford(self, task: str, token_estimate: int) -> bool:
        """Check if request fits within budget."""
        estimated_cost = self.estimate_cost(task, token_estimate)
        
        # Check daily cap
        if self.current_daily_spend + estimated_cost > self.daily_cap_eur:
            return False
        
        # Check monthly cap
        if self.current_monthly_spend + estimated_cost > self.monthly_cap_eur:
            return False
        
        return True
    
    def record(self, task: str, actual_cost: float) -> None:
        """Record actual spend and trigger alerts if needed."""
        self.current_daily_spend += actual_cost
        self.current_monthly_spend += actual_cost
        
        # Check alert thresholds
        if self.current_monthly_spend >= self.monthly_cap_eur * self.alert_threshold:
            self.trigger_alert(
                f"Budget alert: {self.current_monthly_spend/self.monthly_cap_eur*100:.1f}% "
                f"of monthly cap (€{self.monthly_cap_eur}) reached"
            )
```

---

### **7. Package Reality Verification Script**

**File:** `scripts/verify_packages.py`  
**Lines:** 150-400  
**Purpose:** Validate all dependencies against registries and OSV database

#### **Requirements:**
- Parse requirements.lock and package-lock.json
- Cross-reference with PyPI and npm registries
- Check OSV database for CVEs
- Generate evidence/pkg_reality_report.md
- <8min execution time
- Zero unverified dependencies allowed

#### **Key Components:**
```python
#!/usr/bin/env python3
import argparse
import json
import requests
from pathlib import Path

def verify_packages(lockfile: Path, ecosystem: str) -> dict:
    """Verify all packages in lockfile against registry and OSV."""
    
    results = {
        "total": 0,
        "verified": 0,
        "unverified": 0,
        "vulnerabilities": [],
        "packages": []
    }
    
    # Parse lockfile
    packages = parse_lockfile(lockfile, ecosystem)
    results["total"] = len(packages)
    
    # Verify each package
    for pkg in packages:
        verified = check_registry(pkg, ecosystem)
        vulns = check_osv(pkg, ecosystem)
        
        results["packages"].append({
            "name": pkg["name"],
            "version": pkg["version"],
            "verified": verified,
            "vulnerabilities": vulns
        })
        
        if verified:
            results["verified"] += 1
        else:
            results["unverified"] += 1
        
        results["vulnerabilities"].extend(vulns)
    
    return results

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--lockfile", required=True)
    parser.add_argument("--ecosystem", choices=["python", "node"], required=True)
    parser.add_argument("--output", required=True)
    
    args = parser.parse_args()
    
    results = verify_packages(Path(args.lockfile), args.ecosystem)
    
    # Generate report
    generate_markdown_report(results, Path(args.output))
    
    # Exit with error if unverified packages found
    if results["unverified"] > 0:
        sys.exit(1)
    
    sys.exit(0)
```

---

### **8. Data Residency Validation Script**

**File:** `scripts/check_residency.py`  
**Lines:** 100-250  
**Purpose:** Enforce 100% EU region compliance for all LLM requests

#### **Requirements:**
- Parse configs/vendor_residency.yaml
- Validate all provider endpoints use EU regions
- Check vendor portal settings (training data opt-out, logging disabled)
- Generate metrics/compliance/vendor_region_distribution.csv
- <2min execution, fail pipeline on violations

---

### **9. FinOps Policy Configuration**

**File:** `policies/finops.yaml`  
**Lines:** 40-100  
**Purpose:** Budget definitions for Phases 1-3

#### **Required Content:**
```yaml
phases:
  1:
    daily_eur_cap: 450
    monthly_eur_cap: 12000
    providers:
      openai:
        max_tokens: 80000
        models:
          - gpt-4o-mini
          - gpt-4o
      anthropic:
        max_tokens: 60000
        models:
          - claude-3-5-sonnet-20241022
      local:
        max_tokens: 100000
  2:
    daily_eur_cap: 650
    monthly_eur_cap: 16000
    providers:
      openai:
        max_tokens: 120000
      anthropic:
        max_tokens: 100000
  3:
    daily_eur_cap: 900
    monthly_eur_cap: 22000
    providers:
      openai:
        max_tokens: 150000
      anthropic:
        max_tokens: 130000

alerts:
  threshold_percent: 80
  channels:
    - type: slack
      destination: "#finops-alerts"
    - type: email
      destination: "finops@example.com"
```

---

### **10. LLM Router Configuration**

**File:** `configs/model_routing.yaml`  
**Lines:** 50-150  
**Purpose:** Router scoring weights and task-to-provider mappings

#### **Required Content:**
```yaml
weights:
  cost: 0.4
  latency: 0.3
  accuracy: 0.3

providers:
  openai:
    models:
      planning: gpt-4o-mini
      coding: gpt-4o
      review: gpt-4o-mini
    base_latency_ms: 800
    cost_per_1k_tokens:
      gpt-4o-mini: 0.00015
      gpt-4o: 0.0025
  
  anthropic:
    models:
      planning: claude-3-5-sonnet-20241022
      coding: claude-3-5-sonnet-20241022
      review: claude-3-5-sonnet-20241022
    base_latency_ms: 1200
    cost_per_1k_tokens:
      claude-3-5-sonnet-20241022: 0.003
  
  local:
    models:
      planning: local-llm
      coding: local-llm
      review: local-llm
    base_latency_ms: 300
    cost_per_1k_tokens:
      local-llm: 0.0

task_types:
  planning:
    preferred_provider: openai
    fallback: local
    max_tokens: 4000
  coding:
    preferred_provider: anthropic
    fallback: openai
    max_tokens: 16000
  review:
    preferred_provider: openai
    fallback: local
    max_tokens: 8000

failover:
  max_retries: 3
  retry_delay_ms: 500
  fallback_provider: local
```

---

### **11. Vendor Residency Configuration**

**File:** `configs/vendor_residency.yaml`  
**Lines:** 40-120  
**Purpose:** Data residency enforcement for GDPR compliance

#### **Required Content:**
```yaml
vendors:
  openai:
    region: eu-west-1
    endpoint: "https://api.openai.com/v1"  # Verify EU routing
    data_retention: false
    training_data_opt_out: true
    logging_enabled: false
    compliance:
      - GDPR
      - EU AI Act
  
  anthropic:
    region: eu-central-1
    endpoint: "https://api.anthropic.com/v1"
    data_retention: false
    training_data_opt_out: true
    logging_enabled: false
    compliance:
      - GDPR
      - EU AI Act
  
  local:
    region: on-premise
    endpoint: "http://localhost:8080"
    data_retention: true  # Local control
    training_data_opt_out: true
    logging_enabled: true  # Local audit logs

enforcement:
  block_non_eu_requests: true
  alert_on_violation: true
  log_all_requests: true
```

---

### **12. Database Migration**

**File:** `migrations/versions/001_create_sessions_tables.py`  
**Lines:** 40-120  
**Purpose:** Alembic migration for state storage tables

#### **Required Tables:**
- `sessions` (id, payload, payload_hash, updated_at)
- `state_audit` (id, session_id, action, timestamp)
- `state_hash_index` (hash, session_id, created_at)

---

### **13. Architecture Documentation**

**File:** `docs/architecture/phase1_architecture.md`  
**Lines:** 200-500  
**Purpose:** Complete Phase 1 architecture documentation

#### **Required Sections:**
- Distributed State Fabric (Redis + PostgreSQL architecture)
- Session Ledger (append-only design, replay mechanics)
- Agent Coordination Graph (LangGraph flow diagrams)
- LLM Router and Budget Guardian (provider selection algorithm)
- Event Telemetry Mesh (notification architecture)
- FinOps Guardrails (budget enforcement logic)
- Data Residency Policy (EU compliance strategy)
- Package Reality Verification (dependency validation workflow)

#### **Must Include:**
- 8+ code examples
- 3+ architecture diagrams (Mermaid/ASCII)
- Performance targets table
- Rollback procedures for each subsystem
- Integration points between components

---

### **14-16. Integration Tests**

#### **Test Files Required:**
1. `tests/integration/test_state_repository.py` (100-300 lines, 5+ tests)
2. `tests/integration/test_orchestration.py` (100-300 lines, 5+ tests)
3. `tests/integration/test_model_router.py` (120-350 lines, 6+ tests)

#### **Test Coverage Requirements:**
- State: save/get, cache hit ratio, integrity hashing, failover
- Orchestration: state transitions, conditional loops, policy enforcement
- Router: budget enforcement, provider failover, routing accuracy, cost tracking

#### **Test Execution:**
```bash
pytest tests/integration/test_state_repository.py -v --cov=src/state
pytest tests/integration/test_orchestration.py -v --cov=src/orchestration
pytest tests/integration/test_model_router.py -v --cov=src/models
```

**All tests must pass with 100% success rate.**

---

### **17. G1 Gate Evidence**

**File:** `evidence/gates/g1_architecture.json`  
**Lines:** 40-150  
**Purpose:** G1 gate validation evidence

#### **Required Content:**
```json
{
  "gate": "G1",
  "phase": "Phase 1",
  "status": "PASS",
  "timestamp": "2025-10-01T22:00:00Z",
  "validator": "automated_contract_validator",
  "subsystems": {
    "state_fabric": {
      "status": "PASS",
      "redis_latency_p95_ms": 45,
      "postgres_latency_p95_ms": 115,
      "cache_hit_ratio": 0.94,
      "integrity_checks_passed": 1000,
      "evidence": "metrics/performance/state_cache_latency.csv"
    },
    "orchestration": {
      "status": "PASS",
      "graph_execution_latency_ms": 1420,
      "conditional_accuracy": 0.91,
      "policy_violations": 0,
      "evidence": "tests/integration/test_orchestration.py"
    },
    "router": {
      "status": "PASS",
      "routing_latency_p95_ms": 118,
      "routing_accuracy": 0.93,
      "failover_success_rate": 0.995,
      "budget_breaches": 0,
      "evidence": "metrics/quality/model_routing_accuracy.csv"
    },
    "finops": {
      "status": "PASS",
      "daily_spend_variance_pct": 3.2,
      "alert_lead_time_hours": 26,
      "token_ceiling_enforcement_rate": 1.0,
      "evidence": "metrics/cost/budget_report.csv"
    },
    "residency": {
      "status": "PASS",
      "eu_compliance_rate": 1.0,
      "non_eu_requests": 0,
      "vendor_attestations_current": true,
      "evidence": "configs/vendor_residency.yaml"
    },
    "packages": {
      "status": "PASS",
      "total_dependencies": 87,
      "verified_dependencies": 87,
      "unverified_dependencies": 0,
      "vulnerabilities_found": 0,
      "execution_time_minutes": 6.8,
      "evidence": "evidence/pkg_reality_report.md"
    }
  },
  "deliverables_count": 22,
  "lines_delivered": 2847,
  "validation_result": "ACCEPTED",
  "quality_gates_passed": 22,
  "quality_gates_failed": 0,
  "forbidden_patterns_found": 0
}
```

---

### **18-22. Metrics Files**

#### **Metrics CSV Files Required:**

1. **`metrics/performance/state_cache_latency.csv`** (20+ rows)
   - Columns: timestamp, operation, latency_ms, percentile
   - Show p50/p95/p99 latencies for GET operations
   - Target: p95 < 50ms

2. **`metrics/quality/model_routing_accuracy.csv`** (15+ rows)
   - Columns: timestamp, task_type, expected_provider, actual_provider, correct
   - Show ≥92% accuracy (11/12+ correct)

3. **`notifications/delivery_log.csv`** (25+ rows)
   - Columns: timestamp, destination, correlation_id, status, latency_ms
   - Show ≥99.5% success rate (20/20+)

4. **`metrics/cost/budget_report.csv`** (20+ rows)
   - Columns: date, phase, daily_spend_eur, daily_cap_eur, monthly_spend_eur, monthly_cap_eur
   - Show Phase 1 budget tracking (€450 daily, €12k monthly)

5. **`evidence/pkg_reality_report.md`** (80-300 lines)
   - Sections: Verification Summary, Python Dependencies, JavaScript Dependencies, Vulnerability Scan Results
   - Must show: Status=PASS, Unverified=0, Execution <8min

---

## 🔗 CROSS-FILE VALIDATION REQUIREMENTS

### **1. Budget Consistency:**
`policies/finops.yaml` and `metrics/cost/budget_report.csv` must both reference:
- Phase 1 daily cap: €450
- Phase 1 monthly cap: €12,000

### **2. Evidence Paths Exist:**
`evidence/gates/g1_architecture.json` must reference all metrics files, and they must exist:
- `metrics/performance/state_cache_latency.csv`
- `metrics/quality/model_routing_accuracy.csv`
- `notifications/delivery_log.csv`
- `metrics/cost/budget_report.csv`
- `evidence/pkg_reality_report.md`

### **3. Router Config Alignment:**
`src/models/router.py` must reference providers defined in `configs/model_routing.yaml` and respect budgets from `policies/finops.yaml`.

### **4. Test Coverage Complete:**
Each major implementation module must have corresponding integration test:
- `src/state/repository.py` ↔ `tests/integration/test_state_repository.py`
- `src/orchestration/graph_builder.py` ↔ `tests/integration/test_orchestration.py`
- `src/models/router.py` ↔ `tests/integration/test_model_router.py`

---

## ✅ DEFINITION OF DONE

Phase 1 is complete when ALL of the following are TRUE:

1. ✅ **All 22 deliverables exist** at specified paths
2. ✅ **All quality gates pass** (line counts, patterns, structure)
3. ✅ **All cross-file validations pass** (budget consistency, evidence paths, config alignment, test coverage)
4. ✅ **Zero forbidden patterns** (no TODO, TBD, FIXME, pass stubs, NotImplementedError)
5. ✅ **All integration tests pass** (100% pass rate)
6. ✅ **G1 gate evidence generated** with PASS status

**Validation Command:**
```bash
python3 scripts/validate_contract.py contracts/phase_1_core_architecture.contract.json
```

**Success Criteria:** Exit code 0 with zero quality gate failures.

---

## 🚨 FAILURE CONSEQUENCES

### **Iteration Limit Enforcement:**

**Attempt 1 (Current):**
- Use these instructions to deliver all 22 deliverables
- Run contract validator
- If PASS → proceed to Phase 2
- If FAIL → Attempt 2 allowed

**Attempt 2 (If Needed):**
- Review validation report
- Fix specific failures
- Re-run contract validator
- If PASS → proceed to Phase 2
- If FAIL → **PROJECT PAUSE**

**Attempt 3:**
- **Does not exist**
- Two failures triggers:
  - Project pause
  - Root cause analysis
  - Methodology review
  - Gap analysis (same as Phase 0 rebuild decision)

**Historical Precedent:**
- Phase 0 first attempt: CATASTROPHIC FAILURE (4 skeleton files, TODO markers everywhere)
- Phase 0 second attempt: PERFECT SUCCESS (16 complete files, zero violations)
- This iteration limit enforcement is what forced the successful second attempt

---

## 📊 PERFORMANCE TARGETS SUMMARY

| Metric | Target | Evidence File |
|--------|--------|---------------|
| Redis GET latency (p95) | <50ms | `metrics/performance/state_cache_latency.csv` |
| PostgreSQL write latency | <120ms | `metrics/performance/state_cache_latency.csv` |
| Cache hit ratio | ≥92% | `metrics/performance/state_cache_latency.csv` |
| Ledger append latency | <80ms | Embedded in state tests |
| Graph execution latency | <1.5s | Integration tests |
| Router decision latency | <120ms | `metrics/performance/model_router_latency.csv` |
| Notification latency | <5s | `notifications/delivery_log.csv` |
| Notification success rate | ≥99.5% | `notifications/delivery_log.csv` |
| Router accuracy | ≥92% | `metrics/quality/model_routing_accuracy.csv` |
| Budget breach rate | 0% | `metrics/cost/budget_report.csv` |
| Failover success rate | ≥99% | Integration tests |
| EU compliance rate | 100% | `configs/vendor_residency.yaml` |
| Package verification time | <8min | `evidence/pkg_reality_report.md` |
| Unverified dependencies | 0 | `evidence/pkg_reality_report.md` |

---

## 🎓 LESSONS FROM PHASE 0

### **What Made Phase 0 Succeed:**

1. ✅ **Contract-based enforcement** replaced prose instructions
2. ✅ **Machine validation** provided objective acceptance criteria
3. ✅ **Forbidden patterns** prevented half-assed deliverables
4. ✅ **Line count minimums** enforced substance over skeletons
5. ✅ **Cross-file validation** caught inconsistencies
6. ✅ **Evidence-based gates** enabled audits
7. ✅ **Iteration limit** forced excellence

### **Apply These Principles to Phase 1:**

- Don't write skeleton code with TODO markers
- Don't create functions with `pass` stubs
- Don't write documentation with TBD sections
- Don't commit incomplete implementations
- Don't skip tests
- Don't fake metrics
- Don't cheat the contract

**The validator will catch all of this. Exit code non-zero = REJECTED.**

---

## 🏁 EXECUTION CHECKLIST

### **Before Starting:**
- [ ] Phase 0 foundation exists (G0 PASSED)
- [ ] Contract file reviewed: `contracts/phase_1_core_architecture.contract.json`
- [ ] Validation script ready: `scripts/validate_contract.py`
- [ ] Estimated 120 hours allocated

### **During Implementation:**
- [ ] All 22 files created at correct paths
- [ ] All line count requirements met
- [ ] All required patterns present
- [ ] Zero forbidden patterns
- [ ] All cross-file validations addressed
- [ ] All integration tests written and passing
- [ ] All metrics files generated with real data

### **Before Submission:**
- [ ] Run validation: `python3 scripts/validate_contract.py contracts/phase_1_core_architecture.contract.json`
- [ ] Exit code 0 achieved
- [ ] Review validation report: `evidence/validation/phase1_contract_validation.json`
- [ ] G1 gate evidence complete: `evidence/gates/g1_architecture.json`
- [ ] All integration tests pass: `pytest tests/integration/ -v`

### **After Acceptance:**
- [ ] Commit with signed tag: `v1.0-phase1-complete`
- [ ] Update roadmap: Mark Phase 1 as COMPLETE
- [ ] Archive validation evidence
- [ ] Proceed to Phase 2 planning

---

## 🎯 FINAL REMINDER

**This is a contract-enforced delivery. The same zero-tolerance quality gates that made Phase 0 succeed apply here.**

**Prose = hope. Contracts = certainty.**

**Exit code 0 = success. Non-zero = failure.**

**Two failures = project pause.**

**You have been warned. You have been equipped. Now execute.**

🚀 **Ready to build Phase 1? The foundation is solid. The contract is clear. The validator is waiting.**

**Good luck. Execute with excellence.**

---

**End of Phase 1 Instructions**