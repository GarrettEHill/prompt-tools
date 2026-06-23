# Example Final Reports

## Sonar cleanup sweep (partial)

```markdown
# Sweep Final Report

## Run summary
- **Goal:** Fix actionable Sonar findings posted on GitHub
- **Repository:** GarrettEHill/Xyberus
- **Outcome:** partial
- **Stop reason:** 3 items hit retry limit

## Work processed
| Order | Item | Status | Summary |
|-------|------|--------|---------|
| 1 | #201 hotspot auth | completed | Narrowed input validation; merged PR #512 |
| 2 | #198 duplication util | completed | Extracted helper; merged PR #513 |
| 3 | #195 coverage gap | blocked | Flaky integration test blocked verification |

## PR outcomes
- **Opened:** 2
- **Merged:** 2
- **Left open:** 0

## Issue/finding outcomes
- **Closed:** 2
- **Updated:** 1
- **Unresolved:** 1

## Validation
- **Commands run:** `cargo test -p auth`, `cargo test --workspace --locked`, Sonar check
- **Failures/retries:** item #195 failed 3 validation attempts

## Blockers
- **Per-item:** #195 coverage fix blocked by flaky integration test
- **Global:** none

## Patterns observed
- **Repeated failure types:** integration test timing sensitivity
- **Repo-wide issues discovered:** none

## Recommended follow-up
- Fix flaky integration test in separate item
- Re-queue #195 after test stabilization
```

## Dependabot sweep (completed)

```markdown
# Sweep Final Report

## Run summary
- **Goal:** Merge actionable open Dependabot PRs
- **Repository:** org/service
- **Outcome:** completed
- **Stop reason:** queue empty

## Work processed
| Order | Item | Status | Summary |
|-------|------|--------|---------|
| 1 | PR #42 serde patch | completed | Merged after workspace tests |
| 2 | PR #43 actions bump | completed | Merged after actionlint + CI |

## PR outcomes
- **Opened:** 0
- **Merged:** 2
- **Left open:** 1 major bump left blocked

## Issue/finding outcomes
- **Closed:** 0
- **Updated:** 0
- **Unresolved:** 1 major bump needs migration

## Validation
- **Commands run:** `cargo test --workspace --locked`, `actionlint`, GitHub checks
- **Failures/retries:** none

## Blockers
- **Per-item:** PR #44 major bump — breaking API change
- **Global:** none

## Recommended follow-up
- Create migration issue for PR #44
```
