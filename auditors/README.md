# Auditor Personas

Focused, composable audit specialties. Each persona is a concise prompt that flavors [`disposable-auditor`](../../patterns/disposable-auditor/).

## Concept

```text
coordinator
  → spawns disposable auditor #1 with personas [ci-cd]
  → spawns disposable auditor #2 with personas [dependency-supply-chain, secrets-hygiene]
  → spawns disposable auditor #3 with personas [static-analysis-ingest]
```

- **N auditors** = N tight parallel or serial runs
- **X personas each** = combined expertise without one mega-prompt
- Each persona stays small and refinable independently

## Files

- [`persona-catalog.md`](persona-catalog.md) — all personas and compatibility
- [`persona-composition.md`](persona-composition.md) — how coordinators combine personas

## Personas

| Persona | Path |
|---------|------|
| Static analysis ingest | [`static-analysis-ingest/persona.md`](static-analysis-ingest/persona.md) |
| Dependency supply chain | [`dependency-supply-chain/persona.md`](dependency-supply-chain/persona.md) |
| Secrets hygiene | [`secrets-hygiene/persona.md`](secrets-hygiene/persona.md) |
| CI/CD | [`ci-cd/persona.md`](ci-cd/persona.md) |
| Test quality | [`test-quality/persona.md`](test-quality/persona.md) |
| Documentation accuracy | [`documentation-accuracy/persona.md`](documentation-accuracy/persona.md) |
| Architecture boundaries | [`architecture-boundaries/persona.md`](architecture-boundaries/persona.md) |
| Auth & session | [`auth-session/persona.md`](auth-session/persona.md) |

## Where personas belong

| Type | Location | Example |
|------|----------|---------|
| Persona | `auditors/<name>/persona.md` | ci-cd checks |
| Auditor shell | `patterns/disposable-auditor/` | read-only behavior |
| Coordinator | `patterns/divide-and-conquer-audit/` | spawn plan |
| Project config | `adapters/full-repository-audit/` | which personas for this repo |
