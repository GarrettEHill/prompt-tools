# Full Repository Audit — Domain Catalog

How each domain relates to SonarQube and what it adds.

| Domain | Sonar overlap | Audit adds |
|--------|---------------|------------|
| `static-analysis` | **Primary Sonar domain** | Ingest open Sonar issues; gap-check for unscanned paths |
| `dependency-supply-chain` | Partial (SCA rules) | CVE audit, unpinned deps, Dependabot posture, yanked crates |
| `secrets-hygiene` | Partial (secret detection) | `.env` patterns, CI secret usage, git history signals |
| `auth-session` | Partial (security hotspots) | End-to-end auth flow review, session/token handling |
| `ci-cd` | Minimal | Workflow permissions, action pinning, required checks, deploy safety |
| `test-quality` | Coverage metrics only | Missing critical tests, flaky patterns, untested error paths |
| `architecture-boundaries` | Partial (coupling rules) | Module layering, circular deps, forbidden imports |
| `documentation-accuracy` | None | README commands, API docs vs implementation |
| `configuration-drift` | Minimal | env templates, feature flags, prod-only config in repo |
| `error-handling-observability` | Partial (bug rules) | panic paths, swallowed errors, missing structured logs |

## Recommended audit order

1. `static-analysis` (ingest Sonar — establishes baseline)
2. `dependency-supply-chain`
3. `secrets-hygiene`
4. `ci-cd`
5. `auth-session` (if applicable)
6. `test-quality`
7. `architecture-boundaries`
8. `documentation-accuracy`
9. `error-handling-observability`
10. `configuration-drift`

## When to skip

Document skipped domains in the executive report with reason.
