---
title: 1) Is the refinement brief “2025-state-of-the-art” correct?
doc_type: reference
topics:
- evals
- frameworks
- retrieval
summary: 1) Is the refinement brief “2025-state-of-the-art” correct?. Here’s what
  I did—rigorously and with receipts—and where your new merged prompt now lives.
keywords:
- 05B
- Delivery
- GPT
- LLM
- Notes
- RAG
- automation
- brief
- correct
- evals
- framework
- frameworks
- refinement
- retrieval
- state-of-the-art
- system
last_verified: '2025-09-24'
canonical_id: 73ade05212f4c9fb8821ae33d8819d2f7d780b5d40afe86690a7769d83342b99
---

Here’s what I did—rigorously and with receipts—and where your new merged prompt now lives.

# 1) Is the refinement brief “2025-state-of-the-art” correct?

**Verdict: yes, with a couple of precise modernizations I applied.** The brief’s requirements (≤200 lines, unified templates, 5–7 binary gates, automation-first, current frameworks, exact handoffs) align with 2025 best practice. I validated the specific anchors it implies and updated any that evolved:

* **Security standards.**
  • OWASP **ASVS v5.0.0** is current (released May 30, 2025) and suitable as a QA control/gate reference. ([owasp.org][1])
  • **OWASP Top 10 for LLM Applications** v1.1 is active for LLM/AI validation mapping (where relevant in QA). ([owasp.org][2])

* **API error model.**
  • Problem Details is **RFC 9457** (obsoletes RFC 7807). I enforced 9457 as the error-shape expectation in QA evidence. ([rfc-editor.org][3], [datatracker.ietf.org][4])

* **Supply-chain evidence.**
  • **CycloneDX v1.6** is the right SBOM baseline in 2025; I kept it and referenced its 1.6 spec pages/news. ([cyclonedx.org][5])
  • **SLSA v1.0** remains the recommended provenance predicate; I kept SLSA v1.0 attestation in the gates. ([SLSA][6])

* **Accessibility.**
  • **WCAG 2.2** is a W3C Recommendation and remains the appropriate QA benchmark; I required AA conformance with axe-core automation plus targeted manual checks. ([W3C][7])

* **OpenAPI contract baseline.**
  • The brief assumes modern contracts; I explicitly set **OpenAPI 3.1** (aligned to JSON Schema 2020-12) as the QA input artifact—consistent with 2025 best practice. ([OpenAPI Initiative Publications][8], [OpenAPI Initiative][9], [Swagger][10])

* **Test tooling (2025).**
  • **Jest 30** is current (June 4, 2025)—I referenced it as the JS/TS unit-runner baseline. ([Jest][11])
  • **Cypress** docs (updated July/Aug 2025) and **Playwright** remain mainstream for E2E/component; I positioned either as acceptable, with explicit CI commands. ([Cypress Docs][12])

**Net:** the brief is sound; I only *modernized anchors* (RFC 9457, ASVS 5.0, CycloneDX 1.6, SLSA v1.0, OpenAPI 3.1, Jest 30, Cypress/Playwright current) and tightened the gate set into 7 binary checks as required.

# 2) What I merged (sources)

I merged your **system** and **expert** QA prompts per the brief, removing redundancy and unifying templates, then rebuilt the deliverable to the “excellence” pattern you’ve used for RA/AA/SA/IA:

* **Source (System):** `06_quality_assurance_assistant_system_prompt.md`.&#x20;
* **Source (Expert):** `06_QUALITY_ASSURANCE_ASSISTANT_PROMPT.md`.&#x20;
* **Refinement brief followed:** `EXCELLENCE_REFINEMENT_BRIEF_Quality_Assistant.md`.

# 3) Deviations & evidence (why)

* **Changed “Problem Details” to RFC 9457** (explicitly) because 9457 supersedes 7807 and is the current normative reference. ([rfc-editor.org][3], [datatracker.ietf.org][4])
* **Locked SBOM/provenance language to CycloneDX 1.6 + SLSA v1.0** to reflect the latest schema and provenance guidance. ([cyclonedx.org][13], [SLSA][6])
* **Made OAS 3.1 an explicit input** so QA can validate against true JSON Schema 2020-12 semantics (fewer “schema-like” mismatches). ([OpenAPI Initiative Publications][8], [OpenAPI Initiative][9])
* **Updated runner examples to Jest 30 / Cypress & Playwright current** so teams don’t inherit stale flags or Node constraints. ([Jest][11], [Cypress Docs][12])

# 4) Your merged **Quality Assistant — Excellence System Prompt**

I saved the excellence-refined, ≤200-line **merged prompt** to Canvas as:

**“06 Quality Assistant — Excellence System Prompt”**

It contains:

* Clear **role/scope**, **required inputs**, **7 binary gates**, and **fail-safe protocols** matching the brief.
* A single **unified QA deliverable template** (spec → tests → CI → evidence → package manifest).
* **Automation-first commands** (tests/coverage, Semgrep, Gitleaks, CycloneDX, SLSA, k6/Artillery, a11y, OTel).
* **Citation rules** for outputs and a concise “Modern Tooling Baselines (Aug 2025)” note.

(You can view it in the canvas pane; I’m not duplicating it here.)

---

If you want, I can also drop a quick **execution validation checklist** (before/after line count, gate proof, edge-case protocol coverage) as a second canvas doc.

[1]: https://owasp.org/www-project-application-security-verification-standard/ "OWASP Application Security Verification Standard (ASVS) | OWASP Foundation"
[2]: https://owasp.org/www-project-top-10-for-large-language-model-applications/ "OWASP Top 10 for Large Language Model Applications | OWASP Foundation"
[3]: https://www.rfc-editor.org/rfc/rfc9457.html?utm_source=chatgpt.com "RFC 9457: Problem Details for HTTP APIs"
[4]: https://datatracker.ietf.org/doc/html/rfc9457?utm_source=chatgpt.com "RFC 9457 - Problem Details for HTTP APIs"
[5]: https://cyclonedx.org/specification/overview/?utm_source=chatgpt.com "Specification Overview"
[6]: https://slsa.dev/spec/v1.0/provenance?utm_source=chatgpt.com "SLSA • Provenance"
[7]: https://www.w3.org/TR/WCAG22/ "Web Content Accessibility Guidelines (WCAG) 2.2"
[8]: https://spec.openapis.org/oas/v3.1.0.html?utm_source=chatgpt.com "OpenAPI Specification v3.1.0"
[9]: https://www.openapis.org/blog/2021/02/18/openapi-specification-3-1-released?utm_source=chatgpt.com "OpenAPI Specification 3.1.0 Released"
[10]: https://swagger.io/specification/?utm_source=chatgpt.com "OpenAPI Specification - Version 3.1.0"
[11]: https://jestjs.io/blog/2025/06/04/jest-30 "Jest 30: Faster, Leaner, Better · Jest"
[12]: https://docs.cypress.io/app/core-concepts/writing-and-organizing-tests?utm_source=chatgpt.com "Writing and Organizing Tests"
[13]: https://cyclonedx.org/docs/1.6/json/?utm_source=chatgpt.com "CycloneDX v1.6 JSON Reference"
