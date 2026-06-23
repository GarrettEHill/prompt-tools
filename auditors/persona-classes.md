# Persona Classes

Personas are grouped by **class** for long-term management. Paths stay flat (`auditors/<name>/persona.md`); class indexes live in [`classes/`](classes/).

## Why classes

- pick personas by risk domain, not alphabet
- adapters can say "run all `security` + `infrastructure` classes"
- new personas have an obvious home
- catalog and compatibility matrices stay readable at scale

## Class index

| Class | Index | Personas |
|-------|-------|----------|
| `ingest` | [`classes/ingest.md`](classes/ingest.md) | ingest external scanner output |
| `security` | [`classes/security.md`](classes/security.md) | secrets, deps, auth, MCP, plugins, youth privacy |
| `infrastructure` | [`classes/infrastructure.md`](classes/infrastructure.md) | CI/CD, containers, network, IPC, DB, observability |
| `architecture` | [`classes/architecture.md`](classes/architecture.md) | boundaries, monorepo, FFI, schema drift |
| `quality` | [`classes/quality.md`](classes/quality.md) | tests, vision/sim parity |
| `contracts` | [`classes/contracts.md`](classes/contracts.md) | docs accuracy, requirements traceability, OpenAPI |
| `safety-critical` | [`classes/safety-critical.md`](classes/safety-critical.md) | real-time robotics/control safety |
| `compliance` | [`classes/compliance.md`](classes/compliance.md) | licenses, regulatory-adjacent checks |

## Selecting by class

```yaml
audit_plan:
  classes: [security, infrastructure, contracts]
  exclude_personas: [youth-platform-privacy]  # N/A for this repo
```

Coordinator expands classes → persona list via class index, then applies [`persona-composition.md`](persona-composition.md).

## Adding a new persona

1. Create `auditors/<persona-name>/persona.md`
2. Add `**Class:** <class>` at top of persona
3. Register in class index under `classes/<class>.md`
4. Add row to [`persona-catalog.md`](persona-catalog.md)

## Class pairs (common auditor runs)

| Run theme | Classes / personas |
|-----------|-------------------|
| Security baseline | `security`: deps + secrets + auth |
| Deploy hardening | `infrastructure`: ci-cd + container-runtime-hardening |
| Xyberus-style network | `infrastructure`: network-segmentation-policy + container-runtime-hardening |
| Monorepo API app | `architecture` + `contracts`: schema-contract-drift + openapi-api-surface |
| FTC / robotics | `safety-critical` + `quality`: realtime-safety-authority + test-quality |
| MCP server | `security`: mcp-server-safety + secrets-hygiene |
| Student platform | `security` + `contracts`: youth-platform-privacy + auth-session |
