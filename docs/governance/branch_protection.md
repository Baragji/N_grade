# Branch Protection Policy for Phase 0 Foundation

## Branch Protection Rules
```yaml
required_status_checks:
  strict: true
  contexts:
    - ci
    - security
    - gate_validation
required_pull_request_reviews:
  required_approving_review_count: 2
  require_code_owner_reviews: true
```
- The `main` branch is the single source of truth for the autonomous AI coding system foundation.
- Protection rules enforce compliance, quality, and evidence generation requirements aligned to EU AI Act, ISO 42001, and GDPR commitments.
- All merges into `main` must demonstrate alignment with Phase 0 readiness criteria before advancing to Phase 1 planning.

## Required Status Checks
```bash
gh api \
  -X PUT \
  repos/:owner/:repo/branches/main/protection \
  --input .github/branch_protection_payload.json
```
- `ci` workflow must complete successfully, including linting, unit tests, and contract validation.
- `security` workflow must report zero high-severity issues prior to merge.
- `gate_validation` workflow must publish PASS status to evidence/validation/phase0_contract_validation.json.
- Status checks cannot be bypassed by administrators; waivers require documented approval stored in evidence/approvals/.

## Review Requirements
- Minimum of two code reviews from stakeholders identified in docs/strategy/charter.yaml.
- Reviewers must confirm evidence artifacts are updated, including g0_foundation.json and phase0_charter.json.
- Dismissed reviews are prohibited unless a follow-up approval is granted post-amendment.
- Review comments should capture compliance confirmations referencing EU AI Act, ISO 42001, and GDPR controls when relevant.

## Commit Signing and History
- All commits pushed to protected branches must be signed using verified GPG or SSH signatures.
- Force pushes to `main` are disabled to preserve evidence integrity and audit trails.
- Merge commits must reference associated gate validation reports and include links to evidence artifacts.
- Rewriting history on release branches requires documented approvals and is discouraged during Phase 0 stabilization.

## Required Branch Hygiene
- Feature branches must stay current with `main` prior to review; rebase or merge to resolve conflicts before requesting approval.
- Branch names should include ticket identifiers and phase context, e.g., `phase0/bootstrap-structure`.
- Stale branches older than 30 days trigger review by the Delivery Manager and may be archived.

## Automated Enforcement
- GitHub branch protection settings must enable required status checks, review counts, and signed commits.
- Workflows update evidence/governance/branch_protection_audit.json with nightly compliance status.
- scripts/validate_structure.py verifies branch protection documentation is present during CI runs.

## Incident Response
- In case of a failed check on `main`, revert commits within one hour and document the incident in evidence/state/audit_logs/.
- Notify Programme Sponsor, CTO, and Compliance Lead with remediation plan referencing relevant phases (Phase 0 through Phase 8).
- Post-incident reviews capture corrective actions and update this document when process changes are adopted.

## Continuous Improvement
- Branch protection policy reviewed monthly during steering cadence defined in charter.yaml.
- Feedback from Phase 1 and Phase 2 teams informs updates ensuring policy scales across later phases.
- Evidence of review cycles stored under evidence/governance/branch_protection_audit.json to support audits.
