# Compact Result Schema

Return this structure from every worker or investigation run.

## Schema

```yaml
work_item:
  id: string          # issue number, PR number, check id, finding id
  title: string
  type: issue | pr | check | finding | doc | label-task
status: completed | blocked | failed | needs-follow-up | investigate
summary: string     # one-line outcome
changes:
  files: [string]
  modules: [string]
validation:
  commands:
    - cmd: string
      status: pass | fail | skipped
pr:
  url: string | null
  opened: bool
  merged: bool
work_tracking:
  closed: bool
  comments_added: bool
blocker:
  reason: string | null
  retry_attempts: 0-3
follow_up:
  recommended_action: string | null
```

## Markdown form

```markdown
**Item:** #123 — Fix clippy lint in auth module
**Status:** completed
**Summary:** Removed redundant clone; clippy and module tests pass.
**Changes:** src/auth.rs
**Validation:** `cargo test -p auth` pass; `cargo clippy -p auth` pass
**PR:** https://github.com/org/repo/pull/456 (merged)
**Closed:** yes
```

## Rules

- Stable field names across all patterns.
- No full diffs, stack traces, or long logs.
- Supports investigate-only outcomes (`status: investigate`).
- Coordinator keeps only this payload between iterations.

## Examples

### Success

```yaml
work_item: { id: "42", title: "Merge Dependabot bump for serde", type: pr }
status: completed
summary: "Merged after workspace tests and required checks passed."
changes: { files: ["Cargo.lock"], modules: ["deps"] }
validation:
  commands:
    - { cmd: "cargo test --workspace --locked", status: pass }
pr: { url: "https://github.com/org/repo/pull/42", opened: true, merged: true }
work_tracking: { closed: false, comments_added: false }
blocker: { reason: null, retry_attempts: 0 }
follow_up: { recommended_action: null }
```

### Blocked

```yaml
work_item: { id: "88", title: "Major bump requires API migration", type: pr }
status: blocked
summary: "Major version bump needs human design decision."
changes: { files: [], modules: [] }
validation:
  commands:
    - { cmd: "cargo test --workspace --locked", status: fail }
pr: { url: "https://github.com/org/repo/pull/88", opened: true, merged: false }
work_tracking: { closed: false, comments_added: true }
blocker: { reason: "Breaking API changes beyond auto-fix scope", retry_attempts: 3 }
follow_up: { recommended_action: "Create migration issue and leave PR open" }
```

### Investigation handoff

```yaml
work_item: { id: "ci-991", title: "Flaky integration test on main", type: check }
status: investigate
summary: "Failure intermittent; likely environment timing issue."
changes: { files: [], modules: ["integration"] }
validation:
  commands:
    - { cmd: "npm test -- integration/api.test.ts", status: fail }
pr: { url: null, opened: false, merged: false }
work_tracking: { closed: false, comments_added: false }
blocker: { reason: "Flaky reproduction", retry_attempts: 0 }
follow_up: { recommended_action: "Route to implement worker with quarantine or retry fix" }
```
