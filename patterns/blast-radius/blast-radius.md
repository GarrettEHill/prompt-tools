# Blast Radius Analysis

Read-only. User supplies `target` (file, module, API symbol).

## Analyze

1. Direct dependents (imports, callers, routes)
2. Tests covering target
3. Deploy/config surfaces affected
4. Docs referencing target
5. Downstream packages/services

## Use

- [`architecture-boundaries`](../auditors/architecture-boundaries/) lens
- [`test-quality`](../auditors/test-quality/) lens

## Output

[`blast-radius-template.md`](blast-radius-template.md) filled in.

No code changes.
