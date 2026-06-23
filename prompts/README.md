# Prompts

Lean bootstraps that **load** instructions from this repo at runtime.

## Audit pipeline

| Paste this | Loads |
|------------|-------|
| [`run-repository-audit.md`](run-repository-audit.md) | [`manifests/audit-manifest.md`](manifests/audit-manifest.md) → patterns, auditors, adapters |
| [`run-audit-remediation.md`](run-audit-remediation.md) | [`manifests/remediation-manifest.md`](manifests/remediation-manifest.md) → CCM patterns |

## Usage

1. Open **target repo** in Cursor.
2. Paste `run-repository-audit.md`; fill **Config** (3–6 lines).
3. Agent resolves `prompt_tools` (local clone best: `@prompt-tools/...`).
4. Agent loads manifest + phase files as it runs.
5. After audit, paste `run-audit-remediation.md` with handoff block.

## Why manifests

Keeps paste prompts small. Personas, schemas, and phase rules stay in `patterns/`, `auditors/`, `primitives/` — single source of truth.

## Resolve paths

```text
Local:  C:\Users\garre\prompt-tools\patterns\...
Remote: https://raw.githubusercontent.com/GarrettEHill/prompt-tools/main/patterns/...
```
