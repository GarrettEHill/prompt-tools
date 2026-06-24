# Release Worker

Handle exactly one release slice. Do not pick the next slice.

## Scope lock

- One slice only (changelog, semver bump, breaking scan, migration notes, or release PR assembly).
- Do not expand beyond acceptance criteria for this slice.

## Steps

1. **Inspect live** — re-read release config, diff, and gate status.
2. **Confirm acceptance criteria** — define what "done" means for this slice.
3. **Implement** — smallest complete change for this slice only.
4. **Validate** — follow the [validation ladder](../../primitives/validation-ladder/validation-ladder.md).
5. **Retry** — up to 3 fix attempts after failed validation.
6. **PR** — open or update release PR if this slice produces committable work.
7. **Return compact result** — use the [compact result schema](../../primitives/compact-result-schema/compact-result-schema.md).

## Typical slices

| Slice | Output |
|-------|--------|
| `breaking-scan` | List of breaking API/config changes with severity |
| `changelog` | CHANGELOG.md / release notes entry |
| `semver-bump` | Version files updated consistently |
| `migration-notes` | Migration section in release notes |
| `release-pr` | Single PR bundling version + changelog + notes |

## Safety

Follow the [git/GitHub safety baseline](../../primitives/git-github-safety/git-github-safety.md).

Do not tag or publish releases unless explicitly requested.

## Return format

Return only the compact result. No full diffs or long logs.
