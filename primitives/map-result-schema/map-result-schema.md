# Map Result Schema

## Module / area entry

```yaml
id: MAP-001
name: string
path: string
role: entrypoint | library | service | infra | docs | test
summary: string
entrypoints: [string]
depends_on: [string]
depended_on_by: [string]
key_files: [string]
risks: [string]
mapper: api-surface | data-flow | deploy-topology
```

## Aggregated map artifact

```yaml
repo: owner/repo
generated: date
reading_order: [path, path, ...]
modules: [<module entries>]
data_flows: [{from, to, via}]
deploy_surfaces: [{name, path, type}]
open_questions: [string]
```

## Rules

- Read-only observations only
- Cite file paths as evidence
- No full file dumps
