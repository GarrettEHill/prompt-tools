# Regression Hunt Coordinator

Bisect-style regression investigation. **Read-only** until user approves a fix.

Extends [`investigation-before-change`](../investigation-before-change/investigation-before-change.md).

## Loop

1. Refresh live state
2. Capture symptom, repro steps, last-known-good signal
3. Narrow regression window via `git log`, tags, CI history
4. Spawn [`regression-worker`](regression-worker.md) per suspect commit range or hypothesis
5. Aggregate [`investigation-result-schema`](../../primitives/investigation-result-schema/investigation-result-schema.md)
6. Stop at root cause, blocked, or inconclusive with evidence

## Stop rules

- Root cause identified with evidence
- Regression window narrowed to ≤3 suspect commits
- Blocked: cannot reproduce, no git history, or missing CI logs
- 3 hypothesis failures → document blockers, hand off to CCM if fix needed

## Safety

Read-only bisect. No `git bisect run` with auto-commits unless user approves.
