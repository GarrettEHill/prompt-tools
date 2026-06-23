# Existing PR Remediation

Remediate open pull requests instead of creating duplicate branches/PRs.

## Files

- [`existing-pr-remediation.md`](existing-pr-remediation.md) — PR-native worker prompt.
- [`pr-remediation-checklist.md`](pr-remediation-checklist.md) — copy-paste checklist.

## When to use

- open Dependabot PRs
- PRs with failing checks
- PRs with review comments or merge conflicts
- PRs needing update/rebase before merge

## Related

- [`patterns/disposable-worker`](../disposable-worker/)
- [`adapters/dependabot-pr-sweep`](../../adapters/dependabot-pr-sweep/)
- [`adapters/failing-ci-remediation`](../../adapters/failing-ci-remediation/)
