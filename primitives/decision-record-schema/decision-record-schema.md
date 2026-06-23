# Decision Record Schema

```yaml
id: DEC-001
title: string
status: documented | implicit | disputed | unknown
source: ADR | DESIGN.md | comment | code-structure | PR
location: path or link
decision: string
rationale: string
consequences: string
related_modules: [string]
```

## Register output

```yaml
decision_register:
  - <decision records>
implicit_decisions: [<needs ADR>]
```
