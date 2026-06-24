## Domain Adapter: Semver Release

Repository/project:
- `<owner/repo>`

Goal:
- Evaluate release readiness, assemble release PR bundle, output go/no-go for vX.Y.Z.

Work queue discovery:
- User-supplied `version:` (required or infer from conventional commits)
- Open `audit-finding` issues
- Required CI status on `main` / release branch
- Diff since last tag (`git describe --tags --abbrev=0`)

Selection order:
1. Ship gate (all required gates)
2. Rollback plan generation (read-only)
3. Breaking-change scan
4. Changelog / release notes
5. Semver bump across version files
6. Migration notes
7. Release PR assembly

Validation requirements:
- [`ship-checklist`](../../patterns/ship-checklist/ship-checklist.md) → all required gates pass
- repo-standard validation (`make validate`, preflight, project CI equivalent)
- changelog includes target version
- breaking changes documented for major/minor bumps

Completion criteria:
- `ship-gate-schema` verdict is `ship` or documented `no-ship` with blockers
- rollback plan artifact produced before release PR
- release PR opened with version + changelog + notes (when gates pass)
- no tag/publish unless user explicitly requests

Special safety rules:
- do not ship with open `audit-finding` issues
- do not disable CI checks to pass ship gate
- hand off blockers to CCM via `bootstrap-remediate.md`
- read-only rollback plan — no deploy actions

Config:

```yaml
repo: <owner/repo>
version: 1.2.0              # target semver
base_ref: main              # branch to release from
previous_tag: v1.1.0        # optional; infer if omitted
required_gates:               # optional override
  - ci-green
  - audit-clear
  - changelog
  - breaking-changes
  - migrations
  - deprecations
```

Final report must include:
- ship verdict and gate table
- rollback plan summary
- release PR URL (if opened)
- CCM handoff queue (if no-ship)
