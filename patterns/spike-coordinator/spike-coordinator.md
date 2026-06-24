# Spike Coordinator

Time-boxed exploration: options, evidence, recommendation. **Explicit no-merge default.**

## Loop

1. Define question and time box
2. Optional: repo-archaeology or blast-radius input
3. Spawn [`spike-worker`](spike-worker.md) per option or evidence gather
4. Output [`decision-record-schema`](../../primitives/decision-record-schema/decision-record.md)
5. Optional: promote follow-ups to issues/CCM — no production commits

## Rules

- `no_commit: true` unless user explicitly overrides
- Options matrix required
