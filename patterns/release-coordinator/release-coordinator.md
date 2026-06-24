# Release Coordinator

Operate as a coordinator for a **version cut**. Output is **ship decision + release PR bundle**, not an open-ended backlog.

Distinct from audit: audit finds health gaps; Ship answers **can we tag vX.Y.Z today**.

## Coordinator responsibilities

1. Refresh live project state.
2. Load release config (`version`, `base_ref`, optional `previous_tag`).
3. Run release gate via [`release-checklist.md`](release-checklist.md) → [`ship-gate-schema`](../../primitives/ship-gate-schema/ship-gate-schema.md).
4. If `no-ship` or `blocked`, document blockers and hand off to CCM — stop.
5. Generate rollback plan (read-only) via [`rollback-plan`](../rollback-plan/).
6. Build prioritized slice queue:
   - breaking-change scan
   - changelog / release notes
   - semver bump (if not user-supplied)
   - migration notes
   - release PR assembly
7. Spawn a fresh [`release-worker`](release-worker.md) per slice.
8. After each slice, keep compact coordinator note only.
9. Open or update release PR when slices complete.
10. Final go/no-go: gates still pass + release PR ready for human merge/tag.

## Worker responsibilities

Each worker handles exactly one slice per [`release-worker.md`](release-worker.md).

## Continuous loop

```text
refresh → ship gate → (stop if no-ship) → rollback plan → slice queue → worker → compact result → next slice
```

## Stop rules

Stop when:

- ship gate fails (hand off to CCM)
- all release slices complete and release PR is ready
- baseline validation broken unrelated to release
- auth/tooling unavailable
- 3 slice failures hit retry limit

## Safety rules

- Do not tag or publish without explicit user request.
- Do not ship with open `audit-finding` issues unless documented exception.
- Merge release PR through GitHub after validation.
- Prefer single release PR bundling version + changelog + notes.

## Handoff to CCM

When ship gate fails, output:

```yaml
handoff:
  ccm_queue: [<issue ids from blockers>]
  recommended_action: "Run bootstrap-remediate or failing-ci adapter, then re-run ship gate"
```

## Final report

When the loop stops, produce a concise report:

- target version and verdict (ship / no-ship / release-pr-ready)
- gates evaluated
- rollback plan location
- release PR URL
- blockers and CCM handoff if any
