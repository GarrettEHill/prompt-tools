# Dependency Review

PR-scoped dependency diff review.

## File

- [`dependency-review.md`](dependency-review.md)

## Scope

`Cargo.lock`, `package-lock`, `pnpm-lock`, `go.sum` changes in PR only.

## Checks

- new dependencies justified
- license flags
- known CVE signals (`cargo audit`, `npm audit` on diff scope if feasible)

Output via review-result-schema.
