# Failing CI Remediation — Notes

## Main vs PR failures

- **Main regression:** fix on `main` via PR from a fix branch; higher priority.
- **PR-specific:** remediate on the existing PR branch when possible.

## Common routes

- deterministic test failure → disposable worker
- intermittent failure → investigation-before-change
- infrastructure/auth failure → blocked global or item blocker

## Anti-patterns

- disabling required checks
- `@Ignore` / `skip` without justification
- merging with unrelated fixes bundled in
