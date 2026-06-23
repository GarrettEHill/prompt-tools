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

Map domains to personas in [`auditors/persona-catalog.md`](../../auditors/persona-catalog.md). Select domains that apply; skip irrelevant ones with reason.

| Domain | Persona(s) | Examples of what it covers |
|--------|------------|---------------------------|
| `static-analysis` | `static-analysis-ingest` | Sonar — **ingest, don't duplicate** |
| `dependency-supply-chain` | `dependency-supply-chain` | CVEs, unpinned deps, Dependabot |
| `secrets-hygiene` | `secrets-hygiene` | hardcoded secrets, CI secret usage |
| `auth-session` | `auth-session` | auth flows, session/token handling |
| `ci-cd` | `ci-cd` (+ `secrets-hygiene` optional) | workflow permissions, pinning |
| `test-quality` | `test-quality` | coverage gaps, flaky patterns |
| `architecture-boundaries` | `architecture-boundaries` | coupling, circular deps |
| `documentation-accuracy` | `documentation-accuracy` | README commands, API docs |
| `configuration-drift` | `secrets-hygiene` | env templates, prod config in repo |
| `error-handling-observability` | `test-quality` (partial) | panic paths, swallowed errors |

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
- Each scope item maps to one or more **personas** and one or more **auditor runs** (see [`persona-composition.md`](../../auditors/persona-composition.md)).
- If a domain is too broad, split it (e.g. `ci-cd` → `workflow-security` + `workflow-correctness`).
- Record skipped domains and why.

## Concrete section test

A scope item is ready for planning when:

- [ ] domain name and boundary are clear
- [ ] rationale ties to repo structure or risk
- [ ] small enough for one auditor OR split is documented
- [ ] Sonar overlap strategy is explicit (`full-audit` vs `ingest-existing`)
