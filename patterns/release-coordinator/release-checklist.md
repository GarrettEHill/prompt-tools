# Release Checklist (coordinator phase)

Run before assembling the release PR bundle.

1. Execute [`ship-checklist`](../ship-checklist/ship-checklist.md).
2. If `verdict` is not `ship`, stop and hand off blockers to CCM — do not cut release.
3. Generate [`rollback-plan`](../rollback-plan/rollback-plan.md) artifact.
4. Proceed to release slices only when gates pass.

See [`gate-template.md`](../ship-checklist/gate-template.md) for the filled checklist.
