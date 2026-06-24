# Framework Upgrade Domain Adapter

Plug-in for migration-sweep.

## Responsibilities

- Define migration units from framework version delta
- Map breaking changes to scoped file sets
- Default validation commands per stack

## Config

```yaml
framework: <name>
from_version: string
to_version: string
unit_strategy: directory | module | feature-flag
```
