# Compact Mapper Result

Return to map coordinator after each section.

```yaml
map_section:
  boundary: string
  mappers: [string]
  status: completed | blocked | partial
summary: string
modules:
  - id: MAP-001
    name: string
    path: string
    role: string
    summary: string
open_questions: [string]
blocked: { reason: null | string }
```

One screenful max. Full map assembled at aggregation phase.
