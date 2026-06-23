# Persona Catalog

| Persona | Focus | Typical boundary | Pairs well with |
|---------|-------|------------------|-----------------|
| `static-analysis-ingest` | Ingest Sonar/GitHub findings | repo-wide ingest | — (usually solo) |
| `dependency-supply-chain` | CVEs, pins, Dependabot | manifests, lockfiles | `secrets-hygiene` |
| `secrets-hygiene` | hardcoded secrets, CI exposure | workflows, env templates, src | `ci-cd`, `dependency-supply-chain` |
| `ci-cd` | workflow permissions, pinning | `.github/workflows/` | `secrets-hygiene` |
| `test-quality` | critical gaps, flaky patterns | `src/`, test dirs | `architecture-boundaries` |
| `documentation-accuracy` | README/docs vs reality | `docs/`, README | — (usually solo) |
| `architecture-boundaries` | coupling, cycles, layers | `src/`, packages | `test-quality` |
| `auth-session` | auth flows, tokens, sessions | auth modules, middleware | `secrets-hygiene` |

## Default full-repo run plan (8 auditors)

| Run | Personas | Boundary |
|-----|----------|----------|
| 1 | `static-analysis-ingest` | repo-wide |
| 2 | `dependency-supply-chain` | manifests + lockfiles |
| 3 | `secrets-hygiene` | env templates, config, sample of src |
| 4 | `ci-cd`, `secrets-hygiene` | `.github/workflows/` |
| 5 | `auth-session` | auth/session modules (skip if N/A) |
| 6 | `test-quality`, `architecture-boundaries` | main source tree |
| 7 | `documentation-accuracy` | README + docs |
| 8 | `test-quality` | integration/e2e tests only (if present) |

Adjust run count by repo size — merge or split per [`persona-composition.md`](persona-composition.md).

## Compatibility matrix

|  | deps | secrets | ci-cd | sonar | tests | docs | arch | auth |
|--|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| deps | — | ✓ | · | ✓ | · | · | · | · |
| secrets | ✓ | — | ✓ | · | · | · | · | ✓ |
| ci-cd | · | ✓ | — | · | · | · | · | · |
| sonar | ✓ | · | · | — | · | · | · | · |
| tests | · | · | · | · | — | · | ✓ | · |
| docs | · | · | · | · | · | — | · | · |
| arch | · | · | · | · | ✓ | · | — | · |
| auth | · | ✓ | · | · | · | · | · | — |

✓ = good pair · = neutral / split preferred
