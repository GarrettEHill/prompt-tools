# Dependabot PR Sweep — Notes

## Edge cases

- **Merge conflicts:** resolve minimally on the Dependabot branch; do not broad-refactor.
- **Major bumps:** often blocked pending migration — document and skip rather than force-merge.
- **Superseded PRs:** close older PR when a newer bump for the same dependency exists.
- **Flaky CI:** route to investigation-before-change before fix attempts.
- **Grouped monorepo bumps:** treat as one item only when manifests/lockfiles move together safely.
