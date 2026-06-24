# Ship Gate Checklist Template

Fill per release candidate. Required gates must pass for `verdict: ship`.

## Release metadata

| Field | Value |
|-------|-------|
| Version | |
| Base ref | |
| Candidate SHA | |
| Release owner | |
| Date | |

## Required gates

| Gate ID | Name | Status | Evidence |
|---------|------|--------|----------|
| `ci-green` | Required CI/checks green on candidate | | `gh pr checks` / `gh run list` |
| `audit-clear` | No open `audit-finding` issues | | `gh issue list --label audit-finding` |
| `changelog` | Changelog/release notes updated | | diff vs prior tag |
| `breaking-changes` | Breaking changes documented | | semver scan + migration notes |
| `migrations` | DB/config migrations noted | | migration files + rollback refs |
| `deprecations` | Deprecations handled or deferred with issue | | grep / issue refs |

## Optional gates (warn only)

| Gate ID | Name | Status | Evidence |
|---------|------|--------|----------|
| `docs-sync` | User-facing docs match release | | |
| `security-scan` | Latest security scan clean | | Sonar / cargo audit |
| `smoke-test` | Deploy smoke passed | | |

## Verdict

- [ ] **ship** — all required gates pass
- [ ] **no-ship** — one or more required gates fail
- [ ] **blocked** — cannot evaluate (document why)

## Blockers

1.

## Handoff to CCM

Issue ids / check names to remediate before re-running ship gate:
