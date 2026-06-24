# Migration Sweep Coordinator

CCM-style coordinator for framework/API migrations.

## Loop

1. Refresh live state
2. Load migration plan from [`adapters/framework-upgrade`](../../adapters/framework-upgrade/domain-adapter.md)
3. Build queue of migration units per [`migration-unit-template.md`](migration-unit-template.md)
4. Spawn [`migration-worker`](migration-worker.md) per unit
5. Validate per [`validation-ladder`](../../primitives/validation-ladder/validation-ladder.md)
6. Hand off blockers to CCM

Parallel to [`continuous-completion-model`](../continuous-completion-model/continuous-completion-model.md).
