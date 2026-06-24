# Ship Checklist

Read-only release gate evaluation. Answers **are we allowed to ship vX.Y.Z today** — distinct from cutting the release.

## When to use

- Before tagging or publishing a release
- As input to [`release-coordinator`](../release-coordinator/)
- After audit remediation, before semver bump

## Steps

1. **Live refresh** — sync base ref; confirm candidate SHA.
2. **Load config** — required/optional gate lists (defaults below).
3. **Evaluate each gate** — run closest command or query GitHub live.
4. **Record evidence** — URLs, issue numbers, command outcomes.
5. **Compute verdict** — per [`ship-gate-schema`](../../primitives/ship-gate-schema/ship-gate-schema.md).
6. **Handoff** — if `no-ship`, list blockers for CCM remediation.

## Default required gates

| Gate ID | Check |
|---------|-------|
| `ci-green` | Required checks green on `main` (or release branch) |
| `audit-clear` | Zero open issues with label `audit-finding` |
| `changelog` | `CHANGELOG.md` or release notes include this version |
| `breaking-changes` | Major/minor bump has documented breaking changes |
| `migrations` | New migrations have up/down or rollback notes |
| `deprecations` | No undeclared deprecations in release diff |

## Default optional gates

| Gate ID | Check |
|---------|-------|
| `docs-sync` | README/docs updated for user-visible changes |
| `security-scan` | Latest supply-chain / static scan clean |
| `smoke-test` | Post-deploy smoke evidence if applicable |

## Configurable overrides

```yaml
required_gates: [ci-green, audit-clear, changelog]
optional_gates: [docs-sync]
base_ref: main
version: 1.2.0
```

## Output

Fill [`gate-template.md`](gate-template.md) and emit [`ship-gate-schema`](../../primitives/ship-gate-schema/ship-gate-schema.md).

No version bumps, tags, or deploys in this pattern.
