# Essential Prompt Engineering Guide for AI Coding Agents (Oct 2025 — GPT-5 / Claude Sonnet 4.5)

**Scope:** Agentic coding on **Claude Sonnet 4.5**, **GPT-5 (Thinking/Medium/High)**, **GPT-5-Codex** with **Copilot, Cursor, Trae, Codex, Zencoder**. Each claim has **[confidence]** and **model tags**.

---

## 0) Model Compatibility Matrix (summary)

* **Kernel prompt → plan (≤5 bullets) → diff-only patch → CI gates**: **[HIGH]** **(GPT-5 ✅ | Sonnet 4.5 ✅ | Codex ✅)**. Supported by Copilot's agent Issue→PR VM workflow & Sonnet 4.5 SWE-bench runs using simple scaffold + tools.
* **Unified diff as edit format**: **[HIGH] (2025 evidence + tool support)** **(GPT-5 ✅ | Sonnet 4.5 ✅ | Codex ✅)**. Aider enforces diff for GPT-5; community IDEs and agent frameworks increasingly default to patch flows. Replication to Sonnet 4.5/GPT-5 is **partially** documented (see Q1).
* **Fail-to-Pass test loop + PR evidence**: **[HIGH]** **(GPT-5 ✅ | Sonnet 4.5 ✅ | Codex ✅)**. Matches SWE-bench Live/Pro methodology & Copilot agent docs.
* **Keep system/context concise; target retrieval vs "paste the repo"**: **[MEDIUM]** **(GPT-5 ✅ | Sonnet 4.5 ✅ | Codex ✅)**. Long-context coding studies still show mid-context degradation; use RAG/file-pinning.

---

## 1) Core Prompt Structure (validated for 2025 models)

* **Skeleton:** *Task → Context (paths, constraints) → DoD → Plan (≤5 bullets; wait) → Diff-only patch → Run tests/lint/build; iterate until green → PR note (why/risks)*. **[HIGH]** **(GPT-5 ✅ | Sonnet 4.5 ✅ | Codex ✅)**. Mirrors Copilot agent VM flow; Anthropic reports Sonnet 4.5 top SWE-bench with simple "bash+edit" scaffold.
* **Context discipline:** Point the agent to **only touched files + nearest docs**; avoid dumping whole repos—even with large windows (GPT-5 ~400k, Sonnet 4.5 ~200k/1M option). **[MEDIUM]** **(GPT-5 ✅ | Sonnet 4.5 ✅ | Codex ✅)**.

---

## 2) Phrases/Commands that Enforce Quality (tool-aware)

* **Plan-then-patch:** "**Propose plan (≤5 bullets), then wait. After approval, return a single valid unified diff (`---/+++`, `@@`) and nothing else.**" **[HIGH]** **(GPT-5 ✅ | Sonnet 4.5 ✅ | Codex ✅)**. Aider+community patterns; diff flows are natively supported/applied in many agents/IDEs.
* **Test & CI gate:** "**Run tests/lint/build; iterate until green; include a brief logs excerpt in PR.**" **[HIGH]** **(GPT-5 ✅ | Sonnet 4.5 ✅ | Codex ✅)**. SWE-bench Live/Pro & Copilot agent guides.
* **Touch limits:** "**Edit only referenced files; no stray folders; smallest possible diff.**" **[MEDIUM]** **(GPT-5 ✅ | Sonnet 4.5 ✅ | Codex ✅)**. Multiple Cursor/community threads show failures when not enforced.
* **Commit hygiene:** **Conventional Commits** for title/body. **[MEDIUM]** **(GPT-5 ✅ | Sonnet 4.5 ✅ | Codex ✅)**. Widely used in 2025 agent PR demos.

---

## 3) Testing & Verification (2025)

* **Fail-to-Pass first:** require at least one failing test that goes green; keep regressions green. **[HIGH]** **(GPT-5 ✅ | Sonnet 4.5 ✅ | Codex ✅)**. SWE-bench Live/Pro reflect this loop.
* **Benchmark alignment:** 2025 leaderboards show **Sonnet 4.5** and **GPT-5/Codex** at the top on SWE-bench Verified/Live/Pro with agentic scaffolds. **[HIGH]**.

---

## 4) Requirement Compliance (DoD + security)

* **Inline DoD table** the agent must echo ✅/❌ in PR. **[MEDIUM]** **(All ✅)**. Matches Copilot tutorials & org pilots.
* **Security prompts (enterprise):** "Never print secrets; enable **GitHub Secret Scanning/Protection**; pin GH Actions by SHA; run SAST/dep scans; vet new deps with **OpenSSF Scorecard**; follow **OWASP LLM Top-10** (especially LLM01 Prompt Injection & insecure output handling)." **[HIGH]** **(All ✅)**.

---

## 5) Production-Ready Deliverables (checklist)

* **Must include:** (a) **Unified diff** (multi-file), (b) **tests pass** + logs snippet/coverage delta, (c) **lint/format clean**, (d) **short PR rationale**, (e) **Conventional Commit** title. **[HIGH]** **(All ✅)**. Backed by Copilot agent docs & 2025 tool patterns.

---

## 6) Getting Started (realistic for GPT-5/Sonnet 4.5)

1. Start with **1–2 file tickets** & **diff-only output**.
2. Add **DoD** to issues; turn on **Secret Protection**, **Dependabot**, **Scorecard**; pin Actions by SHA.
3. Use **plan→approve→diff**; after **2 failed iterations, pause and hand-edit**, then resume. **[HIGH]**.

---

## 7) Troubleshooting (2025 tools)

* **Patch won't apply (Cursor/Copilot):** ask for **regenerated diff with more context** or use 3-way apply/fuzzy patcher; Cursor "apply" regressions are known. **[MEDIUM]**.
* **Agent loops / fake tool calls:** reduce scope to single file; enforce fail-then-fix; forbid unknown binaries (e.g., `applypatch` reports). **[MEDIUM]**.
* **Hallucinated APIs:** constrain to touched paths & repo docs; reject unknown symbols. **[MEDIUM]**.

---

## 8) Limitations (explicit)

* **Unified diff 61%→20% gain replication:** **No peer-reviewed replication on GPT-5/Sonnet 4.5 yet**; Aider now **enforces diffs for GPT-5** and community usage is high, but we **extrapolate** the exact lift from GPT-4-Turbo era. **[MEDIUM]**.
* **Context windows (2025):** GPT-5 docs cite ~**400k**; Sonnet 4.5 **~200k** (with **1M option**). Practical effective windows may be lower in some UIs; RAG/file-pinning still recommended. **[MEDIUM]**.

---

## Model-Specific Best Practices

### GPT-5 / GPT-5-Codex
* Use **shorter system prompts** + **strict tool envelopes** (e.g., `apply_patch`)
* Codex guide notes **different prompting** vs base GPT-5
* **Plan-before-edit still useful**, but Codex tends to self-plan aggressively
* **[HIGH]** confidence

### Claude Sonnet 4.5
* Validated on SWE-bench with **simple scaffold, bash+file-edit**
* Prompts that **emphasize heavy tool use + write tests first**
* Performs best with explicit tool/command structure
* **[HIGH]** confidence

### Tool-Specific Notes

**Copilot (agent mode):**
* Obeys Issue→PR VM flow
* Your prompt **can't override** VM/session steps
* Deliver diffs/PR notes
* **[HIGH]** confidence

**Cursor:**
* Supports apply/patch flows
* Some builds show **apply regressions**—be ready to regenerate diffs
* **[MEDIUM]** confidence

**Trae/Zencoder/Codex:**
* Use **tool envelopes** and diffs
* Codex explicitly documents **different prompting** for GPT-5-Codex
* **[MEDIUM]** confidence

---

## COPY-PASTE STARTER PROMPT (tool-agnostic, 2025-ready)

```
ROLE: Senior Implementation Agent

CONTEXT: Change touches only [specific file paths]; project uses tests/lint/build & Conventional Commits.

DEFINITION OF DONE:
1. Tests added/updated + all pass
2. Lint/format clean
3. Minimal diff (no stray files)
4. PR note with "what/why/risks"

WORKFLOW:
Step 1 - PLAN FIRST: Output ≤5 bullets, then WAIT for approval.

Step 2 - ON APPROVAL: Return ONLY a valid unified diff (---/+++, @@) for all files.
- NO prose, NO explanations in the diff output
- Multi-file diffs allowed

Step 3 - TEST: Run tests/lint/build; iterate until green
- Include a short logs excerpt showing pass status

Step 4 - PR NOTE: Brief description covering:
- What changed
- Why (problem being solved)
- Any risks or trade-offs

SECURITY REQUIREMENTS:
- Never print secrets
- Follow OWASP LLM Top-10
- New deps must pass OpenSSF Scorecard
- GitHub Actions pinned by SHA

CONSTRAINTS:
- Edit ONLY referenced files
- No stray folders or files
- Smallest possible diff
- Use Conventional Commits format for title
```

---

## Quick Reference: Confidence Levels

* **[HIGH]:** Tool maintainer docs/blogs, official docs, peer-reviewed/recognized benchmarks
* **[MEDIUM]:** Broad community consensus threads, reputable tech blogs/tutorials
* **[LOW]:** Individual posts or vendor case studies lacking independent replication

---

## Context Window Guidelines (2025)

* **GPT-5:** ~400k tokens
* **Claude Sonnet 4.5:** ~200k tokens (1M option available)
* **Best Practice:** Use targeted retrieval (RAG, file-pinning, nearest neighbors) rather than dumping entire repos
* Long-context studies still show mid-context degradation

---

## SWE-bench Performance (Oct 2025)

Current leaderboard leaders using these techniques:
* Claude Sonnet 4.5 (top performer with simple scaffold)
* GPT-5 / GPT-5-Codex (top tier)
* Best results from agents using Fail-to-Pass iteration loops

---

**Last Updated:** October 2025  
**Version:** 1.0 (GPT-5/Sonnet 4.5 optimized)