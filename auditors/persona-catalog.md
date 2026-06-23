# Persona Catalog

Organized by [**class**](persona-classes.md). See [`classes/`](classes/) for class indexes.

## By class

### ingest

| Persona | Focus | Typical boundary |
|---------|-------|------------------|
| `static-analysis-ingest` | Sonar/GitHub findings ingest | repo-wide |

### security

| Persona | Focus | Typical boundary |
|---------|-------|------------------|
| `dependency-supply-chain` | CVEs, pins, Dependabot | manifests, lockfiles |
| `secrets-hygiene` | hardcoded secrets, CI exposure | workflows, env, src sample |
| `auth-session` | auth flows, tokens, sessions | auth modules |
| `mcp-server-safety` | MCP tool surface, session storage | MCP server src |
| `plugin-trust-boundary` | plugin URLs, capability tickets | plugins/, orchestrator |
| `youth-platform-privacy` | student/guest PII minimization | auth, public routes |

### infrastructure

| Persona | Focus | Typical boundary |
|---------|-------|------------------|
| `ci-cd` | workflow permissions, pinning | `.github/workflows/` |
| `container-runtime-hardening` | caps, privileged, image pins | compose, Dockerfiles |
| `network-segmentation-policy` | zones, nft, gateway topology | compose, firewall, docs |
| `ipc-socket-security` | UDS permissions, exposure | sockets, `/run/` paths |
| `database-migration-hygiene` | migrations, schema drift | migrations/, ORM |
| `observability-readiness` | logs, metrics, health | services, deploy |

### architecture

| Persona | Focus | Typical boundary |
|---------|-------|------------------|
| `architecture-boundaries` | coupling, cycles, layers | `src/`, crates |
| `monorepo-package-boundaries` | workspace package graph | packages/, workspace root |
| `ffi-embed-boundary` | C ABI, panic, ownership | `ffi/`, cbindgen |
| `schema-contract-drift` | schema ↔ codegen ↔ runtime | schemas/, generated |

### quality

| Persona | Focus | Typical boundary |
|---------|-------|------------------|
| `test-quality` | critical gaps, flaky tests | `src/`, tests |
| `vision-pipeline-parity` | sim vs robot tuning | sim/, teamcode |

### contracts

| Persona | Focus | Typical boundary |
|---------|-------|------------------|
| `documentation-accuracy` | README/docs vs reality | README, docs |
| `requirements-traceability` | normative docs vs impl | DESIGN, checklists |
| `openapi-api-surface` | spec vs routes, auth | OpenAPI, API routes |

### safety-critical

| Persona | Focus | Typical boundary |
|---------|-------|------------------|
| `realtime-safety-authority` | watchdog, E-stop, authority | control/safety code |

### compliance

| Persona | Focus | Typical boundary |
|---------|-------|------------------|
| `license-compliance` | dependency licenses | LICENSE, lockfiles |

## Project → class shortcuts

| Project type | Suggested classes |
|--------------|-------------------|
| Network control plane (Xyberus) | ingest, security, infrastructure, contracts |
| Robotics motion (RustySpark) | ingest, safety-critical, architecture, quality |
| Plugin monorepo (Sendarr) | ingest, security, architecture, contracts, infrastructure |
| Student web app (Daily Games) | ingest, security, infrastructure, contracts |
| MCP server | security, contracts |
| FTC vision (ViDAR) | quality, contracts |

## Default full-repo run plan (12 auditors)

| Run | Personas | Boundary |
|-----|----------|----------|
| 1 | `static-analysis-ingest` | repo-wide |
| 2 | `dependency-supply-chain` | manifests + lockfiles |
| 3 | `secrets-hygiene` | env, config, src sample |
| 4 | `ci-cd`, `secrets-hygiene` | `.github/workflows/` |
| 5 | `container-runtime-hardening` | compose, deploy, Dockerfiles |
| 6 | `auth-session` | auth modules (skip if N/A) |
| 7 | `test-quality`, `architecture-boundaries` | main source |
| 8 | `requirements-traceability` | normative docs |
| 9 | `documentation-accuracy` | README + docs |
| 10 | `openapi-api-surface` | API layer (skip if N/A) |
| 11 | `license-compliance` | LICENSE + deps |
| 12 | `observability-readiness` | services (skip if N/A) |

Add specialized runs per project: `network-segmentation-policy`, `realtime-safety-authority`, `mcp-server-safety`, etc.

Adjust per [`persona-composition.md`](persona-composition.md).

## Pairing quick reference

| Persona | Pairs well with |
|---------|-----------------|
| `dependency-supply-chain` | `secrets-hygiene` |
| `ci-cd` | `secrets-hygiene`, `container-runtime-hardening` |
| `container-runtime-hardening` | `network-segmentation-policy` |
| `test-quality` | `architecture-boundaries`, `realtime-safety-authority` |
| `schema-contract-drift` | `monorepo-package-boundaries`, `openapi-api-surface` |
| `mcp-server-safety` | `secrets-hygiene` |
| `plugin-trust-boundary` | `schema-contract-drift` |
| `auth-session` | `youth-platform-privacy`, `openapi-api-surface` |
