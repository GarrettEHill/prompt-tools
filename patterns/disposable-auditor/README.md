# Disposable Auditor

Generic read-only audit worker shell. **Flavor** it with one or more auditor personas from [`auditors/`](../../auditors/).

## When to use

- as the base for every audit section spawned by [`divide-and-conquer-audit`](../divide-and-conquer-audit/)
- standalone for a single scoped audit pass

## Files

- [`disposable-auditor.md`](disposable-auditor.md) — base shell (behavior, safety, return format)
- Persona composition: [`auditors/persona-composition.md`](../../auditors/persona-composition.md)
- Persona catalog: [`auditors/persona-catalog.md`](../../auditors/persona-catalog.md)

## Spawn recipe

```text
disposable-auditor.md
+ <one or more persona.md files>
+ audit plan entry (boundary, tools, overrides)
+ audit-finding-schema
```

## Related

- [`primitives/audit-finding-schema`](../../primitives/audit-finding-schema/)
- [`patterns/divide-and-conquer-audit`](../divide-and-conquer-audit/)
