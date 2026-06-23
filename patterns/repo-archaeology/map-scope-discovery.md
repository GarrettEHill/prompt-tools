# Map Scope Discovery

Infer map boundaries from repo layout:

| Signal | Map run |
|--------|---------|
| `src/`, `crates/`, `packages/` | api-surface + data-flow |
| `compose/`, `deploy/`, Dockerfiles | deploy-topology |
| `.github/workflows/` | deploy-topology (CI path) |
| `docs/`, README | api-surface (documented surface) |

Skip `node_modules/`, `target/`, `.git/`, vendored trees.

Output `map_runs` table with boundary + mappers.
