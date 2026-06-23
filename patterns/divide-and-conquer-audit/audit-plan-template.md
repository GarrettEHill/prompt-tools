# Audit Plan Template

Phase 2: for each scoped domain, define **how** it will be audited.

Append or fill one block per domain.

```text
## Audit Plan: <domain name>

Repository/project:
- <owner/repo or path>

Domain:
- <e.g. dependency-supply-chain>

Boundary:
- <directories, workflows, packages included/excluded>

Objective:
- <what risk or quality question this audit answers>

Evidence sources:
- <files, tools, APIs, issue searches>
- Examples:
  - gh issue list --label security
  - cargo audit / npm audit / osv-scanner
  - .github/workflows/*
  - Sonar open issues (ingest only)

Method:
1. <step>
2. <step>
3. <step>

Read-only checks:
- <commands that do not modify state>

Pass/fail criteria:
- pass: <what good looks like>
- fail: <what constitutes a finding>

Severity rubric:
- critical: <definition>
- high: <definition>
- medium: <definition>
- low: <definition>

Sonar overlap:
- ingest-existing | supplement | skip
- <how to avoid duplicate findings>

Existing issue search:
- <labels/keywords to find already-tracked work>

Output:
- compact auditor result with findings list
```

## Example: dependency-supply-chain

```text
## Audit Plan: dependency-supply-chain

Repository/project:
- GarrettEHill/Xyberus

Domain:
- dependency-supply-chain

Boundary:
- Cargo workspace manifests and lockfiles; GitHub Dependabot alerts if visible

Objective:
- Identify vulnerable, unpinned, or unmaintained dependencies.

Evidence sources:
- Cargo.toml, Cargo.lock
- gh api repos/GarrettEHill/Xyberus/dependabot/alerts (if permitted)
- cargo audit

Method:
1. List workspace crates and dependency sources.
2. Run cargo audit or equivalent.
3. Check for git deps, path overrides, yanked crates.
4. Cross-check open Dependabot PRs and security-labeled issues.

Read-only checks:
- cargo metadata
- cargo audit
- gh pr list --author app/dependabot --state open

Pass/fail criteria:
- pass: no known critical/high CVEs without documented exception
- fail: any critical/high CVE, unpinned risky dep, or abandoned dep on critical path

Severity rubric:
- critical: known exploited/vulnerable dep on production path
- high: known CVE without fix path
- medium: outdated dep with available safe upgrade
- low: minor version lag, no known CVE

Sonar overlap:
- supplement — Sonar may flag some SCA; dedupe by CVE/package

Existing issue search:
- labels: security, dependabot; keywords: CVE, vulnerability

Output:
- compact auditor result
```

## Example: static-analysis (Sonar ingest)

```text
## Audit Plan: static-analysis

Domain:
- static-analysis

Boundary:
- SonarQube/SonarCloud findings already posted to GitHub

Objective:
- Inventory open Sonar findings; do not re-run full static analysis unless needed.

Evidence sources:
- GitHub issues from Sonar
- Sonar PR/check annotations if visible

Method:
1. Search open issues for sonar, code smell, vulnerability, hotspot, bug.
2. Classify by severity and file/module.
3. Mark already-tracked vs gaps in coverage.

Read-only checks:
- gh issue list with search terms
- no local scanner unless Sonar API/GitHub issues unavailable

Sonar overlap:
- ingest-existing — primary source of truth

Output:
- compact auditor result listing ingested open findings and coverage gaps
```
