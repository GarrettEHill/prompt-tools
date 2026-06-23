# Full Repository Audit — Domain Catalog

Persona-based audit runs. See [`auditors/persona-catalog.md`](../../auditors/persona-catalog.md) for composition rules.

| Domain | Persona | Sonar overlap |
|--------|---------|---------------|
| `static-analysis` | `static-analysis-ingest` | **Primary Sonar domain** — ingest only |
| `dependency-supply-chain` | `dependency-supply-chain` | Partial SCA |
| `secrets-hygiene` | `secrets-hygiene` | Partial secret detection |
| `auth-session` | `auth-session` | Partial hotspots |
| `ci-cd` | `ci-cd` + `secrets-hygiene` | Minimal |
| `test-quality` | `test-quality` | Coverage only |
| `architecture-boundaries` | `architecture-boundaries` | Partial coupling |
| `documentation-accuracy` | `documentation-accuracy` | None |
| `configuration-drift` | `secrets-hygiene` | Minimal |
| `error-handling-observability` | `test-quality` (partial) | Partial bug rules |

## Recommended auditor runs

| Run | Personas | Boundary |
|-----|----------|----------|
| 1 | `static-analysis-ingest` | repo-wide issue ingest |
| 2 | `dependency-supply-chain` | manifests + lockfiles |
| 3 | `secrets-hygiene` | env templates, config sample |
| 4 | `ci-cd`, `secrets-hygiene` | `.github/workflows/` |
| 5 | `auth-session` | auth modules (skip if N/A) |
| 6 | `test-quality`, `architecture-boundaries` | main source tree |
| 7 | `documentation-accuracy` | README + docs |

Adjust N runs by repo size — split or merge per [`persona-composition.md`](../../auditors/persona-composition.md).

## When to skip

Document skipped personas/runs in the executive report with reason.
