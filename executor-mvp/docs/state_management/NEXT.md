# Next Up (≤3 items)
1) **Should:** Harden test coverage thresholds and add API happy-path tests.  
   **DoD:** coverage ≥80% lines/branches on `src/**`; `/api/execute` happy-path integration test passes with mocked provider.
2) **Could:** Add CODEOWNERS and enforce required reviews in GitHub.  
   **DoD:** PRs require approvals; ownership documented.
3) **Could:** Add JUnit reporter to Vitest and publish `junit.xml` artifact.  
   **DoD:** CI uploads `junit.xml`; PRs show test results inline.
