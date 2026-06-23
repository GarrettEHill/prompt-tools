# Full Repository Audit — Domain Catalog

Persona-based audit runs organized by [**class**](../../auditors/persona-classes.md). See [`persona-catalog.md`](../../auditors/persona-catalog.md).

## Recommended classes

| Class | When to include |
|-------|-----------------|
| ingest | always if Sonar/static analysis active |
| security | always |
| infrastructure | if CI, compose, deploy, or DB present |
| architecture | if monorepo, FFI, or schemas present |
| quality | if tests or vision/sim pipelines present |
| contracts | always (docs + requirements + API if applicable) |
| safety-critical | robotics/real-time control only |
| compliance | shipped OSS artifacts |

## Recommended auditor runs

| Run | Personas | Class(es) | Boundary |
|-----|----------|-----------|----------|
| 1 | `static-analysis-ingest` | ingest | repo-wide |
| 2 | `dependency-supply-chain` | security | manifests + lockfiles |
| 3 | `secrets-hygiene` | security | env, config sample |
| 4 | `ci-cd`, `secrets-hygiene` | security, infrastructure | `.github/workflows/` |
| 5 | `container-runtime-hardening` | infrastructure | compose, deploy |
| 6 | `auth-session` | security | auth (skip if N/A) |
| 7 | `test-quality`, `architecture-boundaries` | quality, architecture | main source |
| 8 | `requirements-traceability` | contracts | normative docs |
| 9 | `documentation-accuracy` | contracts | README + docs |
| 10 | `license-compliance` | compliance | LICENSE + deps |

Add specialized runs from catalog: `network-segmentation-policy`, `realtime-safety-authority`, `mcp-server-safety`, `schema-contract-drift`, `youth-platform-privacy`, etc.

## When to skip

Document skipped classes/personas in the executive report with reason.
