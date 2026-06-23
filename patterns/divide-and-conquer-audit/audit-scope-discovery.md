# Audit Scope Discovery

Phase 1: identify **what** needs to be audited before defining **how**.

## Goal

Produce a bounded list of audit domains/sections appropriate for the repository, beyond what SonarQube already covers.

## Discovery inputs

Inspect live:

- repository layout (languages, apps, services, infra folders)
- `package.json`, `Cargo.toml`, `pyproject.toml`, `go.mod`, etc.
- `.github/workflows/`, CI config
- `Dockerfile`, `docker-compose`, deploy config (read-only)
- docs, README, API specs
- dependency manifests and lockfiles
- existing GitHub issues, labels, and Sonar-posted findings
- security policy, CONTRIBUTING, CODEOWNERS

## Default audit domain catalog

Select domains that apply; skip irrelevant ones with reason.

| Domain | Examples of what it covers |
|--------|---------------------------|
| `static-analysis` | SonarQube/SonarCloud, linters — **reference, don't duplicate** |
| `dependency-supply-chain` | outdated deps, known CVEs, unpinned deps, Dependabot posture |
| `secrets-hygiene` | hardcoded secrets, `.env` patterns, CI secret usage |
| `auth-session` | auth flows, session handling, token storage |
| `input-validation` | injection surfaces, unsafe deserialization |
| `ci-cd` | workflow correctness, permissions, caching, required checks |
| `test-quality` | coverage gaps, missing critical paths, flaky patterns |
| `architecture-boundaries` | coupling, circular deps, module layering |
| `error-handling-observability` | logging, metrics, error propagation |
| `documentation-accuracy` | README commands, API docs vs code |
| `configuration-drift` | env-specific config, feature flags, prod settings |
| `performance-hotspots` | obvious N+1, blocking I/O, unbounded growth |
| `license-compliance` | dependency licenses, header requirements |
| `access-control` | IAM-ish patterns in code, RBAC gaps |
| `data-protection` | PII handling, retention, encryption at rest/transit |

## Output: audit scope list

```yaml
audit_scope:
  - domain: dependency-supply-chain
    rationale: "Rust workspace with multiple crates and lockfile"
    priority: high
  - domain: ci-cd
    rationale: "12 GitHub Actions workflows"
    priority: high
  - domain: static-analysis
    rationale: "SonarCloud active — ingest, don't re-audit from scratch"
    priority: medium
    mode: ingest-existing
```

## Rules

- **Sonar is not the whole audit.** Include it as one domain in `ingest-existing` mode when Sonar is already running.
- Each domain must be concretely bounded — one disposable auditor per domain (or per sub-section if large).
- If a domain is too broad, split it (e.g. `ci-cd` → `workflow-security` + `workflow-correctness`).
- Record skipped domains and why.

## Concrete section test

A scope item is ready for planning when:

- [ ] domain name and boundary are clear
- [ ] rationale ties to repo structure or risk
- [ ] small enough for one auditor OR split is documented
- [ ] Sonar overlap strategy is explicit (`full-audit` vs `ingest-existing`)
