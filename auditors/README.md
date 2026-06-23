# Auditor Personas

Focused, composable audit specialties. Each persona flavors [`disposable-auditor`](../../patterns/disposable-auditor/).

## Organization

Personas are grouped by **class** for long-term management:

- [`persona-classes.md`](persona-classes.md) — taxonomy and selection by class
- [`classes/`](classes/) — index per class (security, infrastructure, …)
- [`persona-catalog.md`](persona-catalog.md) — full catalog with project shortcuts
- [`persona-composition.md`](persona-composition.md) — combine 1–3 personas per run

Paths stay flat: `auditors/<persona>/persona.md`.

## Concept

```text
coordinator
  → audit plan: classes [security, infrastructure] → expand to personas
  → auditor run 1: [ci-cd, secrets-hygiene]
  → auditor run 2: [container-runtime-hardening, network-segmentation-policy]
```

- **24 personas** across **8 classes**
- **N auditors** × **1–3 personas** each = tight, valuable runs

## Classes

| Class | Count | Index |
|-------|-------|-------|
| ingest | 1 | [`classes/ingest.md`](classes/ingest.md) |
| security | 6 | [`classes/security.md`](classes/security.md) |
| infrastructure | 6 | [`classes/infrastructure.md`](classes/infrastructure.md) |
| architecture | 4 | [`classes/architecture.md`](classes/architecture.md) |
| quality | 2 | [`classes/quality.md`](classes/quality.md) |
| contracts | 3 | [`classes/contracts.md`](classes/contracts.md) |
| safety-critical | 1 | [`classes/safety-critical.md`](classes/safety-critical.md) |
| compliance | 1 | [`classes/compliance.md`](classes/compliance.md) |

## Where things belong

| Type | Location | Example |
|------|----------|---------|
| Persona | `auditors/<name>/persona.md` | `ci-cd` |
| Class index | `auditors/classes/<class>.md` | `security` |
| Auditor shell | `patterns/disposable-auditor/` | read-only behavior |
| Coordinator | `patterns/divide-and-conquer-audit/` | spawn plan |
| Project config | `adapters/full-repository-audit/` | class/persona selection |
