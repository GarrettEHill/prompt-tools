# Codemod Coordinator

Coordinate mechanical codemods with per-chunk validation.

Uses migration-sweep discipline. Default: one module/directory per worker.

## Loop

1. Plan codemod chunks via work-item-decomposition
2. Spawn [`codemod-worker`](codemod-worker.md) per chunk
3. Validate; rollback chunk on failure
4. Aggregate PRs or single rolling PR per config
