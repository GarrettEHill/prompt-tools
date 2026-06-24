# Label Policy Enforcement

Recurring enforcement of issue label taxonomy.

Extends [`issue-label-normalization`](../../adapters/issue-label-normalization/domain-adapter.md) for scheduled sweeps.

## Mode

- `audit`: report mismatches
- `fix`: CCM queue per mismatch (user approves `gh issue edit`)

Requires policy template before run.
