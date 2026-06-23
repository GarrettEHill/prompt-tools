# Mapper Composition

- 1 map section per coordinator run
- 1–2 mappers per run
- boundary from map plan (e.g. `src/`, `deploy/`, `docs/`)

```yaml
map_runs:
  - boundary: src/
    mappers: [api-surface-mapper, data-flow-mapper]
  - boundary: compose/ deploy/
    mappers: [deploy-topology-mapper]
```
