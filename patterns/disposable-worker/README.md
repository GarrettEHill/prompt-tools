# Disposable Worker

Standalone prompt for handling exactly one work item in isolation.

## When to use

- spawning a Cursor subagent/task for one queue item
- handing off one item from a human coordinator
- testing per-item behavior before adopting the full sweep loop

## Files

- [`disposable-worker.md`](disposable-worker.md) — reusable worker prompt.
- [`compact-result-template.md`](compact-result-template.md) — return payload for coordinators.

## Related

- Coordinator loop: [`patterns/continuous-completion-model`](../continuous-completion-model/)
- Safety: [`primitives/git-github-safety`](../../primitives/git-github-safety/)
- Validation: [`primitives/validation-ladder`](../../primitives/validation-ladder/)
- Result schema: [`primitives/compact-result-schema`](../../primitives/compact-result-schema/)

## How to use

1. Paste `disposable-worker.md` into a subagent prompt or standalone task.
2. Provide the selected work item and minimal context.
3. Require the compact result template on completion.
