# Continuous Completion Model

Operate as a coordinator with disposable workers.

The goal is to continue processing work items until the queue is complete, blocked, or the stop rules are triggered. Do not stop after one successful item.

## Coordinator Responsibilities

The main agent is only the coordinator.

It must:

1. Refresh live project state before starting.
2. Build a prioritized queue of actionable work items.
3. Select exactly one concrete work item at a time.
4. Spawn a fresh worker/subagent/isolated task context for that one item.
5. Give the worker only the minimal context needed:

   - repository/project
   - selected work item
   - relevant parent/umbrella context
   - validation requirements
   - safety rules
   - retry limits

6. After the worker finishes, discard the worker context.
7. Keep only a compact coordinator note:

   - work item ID/title
   - files/modules changed
   - PR/branch/result
   - tests/validation run
   - merge/close status
   - blocker or follow-up, if any

8. Refresh live state again.
9. Rebuild the queue.
10. Continue with the next item.

Do not allow the coordinator context to accumulate full diffs, long logs, repeated analysis, or implementation details from prior workers.

If real subagents are unavailable, simulate this by treating each iteration as an isolated worker task and summarizing only the compact result before continuing.

## Worker Responsibilities

Each worker handles exactly one selected work item.

The worker must:

1. Inspect the selected item live.
2. Confirm scope and acceptance criteria.
3. Identify affected files/modules/tests.
4. Implement the smallest complete fix.
5. Add or update focused tests/proofs.
6. Run the required validation.
7. Retry fixes up to the allowed limit.
8. Open a PR if the item is resolved.
9. Merge only after validation passes and the PR is mergeable.
10. Close or update the work item only if the merged work fully satisfies it.
11. Return a compact result to the coordinator.

The worker must not continue to another unrelated item.

## Continuous Loop

Repeat this cycle:

1. Refresh live state.
2. Build or update the queue.
3. Select the next dependency-ordered actionable item.
4. Spawn a fresh worker for that item.
5. Worker implements, validates, PRs, merges, and closes if complete.
6. Coordinator records compact result.
7. Discard worker context.
8. Sync back to clean current main.
9. Continue.

## Stop Rules

Stop only when:

- all actionable work is complete
- all remaining work is blocked
- the umbrella/parent goal is genuinely complete
- baseline validation is broken
- auth/tooling/environment is unavailable
- continuing would require secrets or risky production changes
- retry/failed-item limits are hit

## Retry Rules

Each work item gets at most 3 fix attempts.

A fix attempt means making a code/config/test/workflow change after a failed validation run.

If the item still fails after 3 fix attempts:

1. Leave it unresolved.
2. Do not merge.
3. Document the blocker.
4. Return the failure to the coordinator.
5. Continue to the next unblocked item if safe.

If 3 separate work items hit the 3-attempt limit, stop the entire sweep and produce a final report.

## Safety Rules

Always:

- start from clean current main
- respect existing user changes
- avoid destructive git commands
- avoid force-push
- avoid broad unrelated refactors
- avoid changing secrets, credentials, or production deployment settings
- preserve existing behavior unless the selected item requires changing it
- verify before merging
- merge through GitHub
- sync main after each merge
- refresh live state between iterations

Never:

- assume prior chat state is current
- merge without validation
- close an umbrella issue unless all child/acceptance criteria are complete
- suppress or paper over incomplete runtime behavior
- continue blindly after global repo/tooling failure

## Final Report

When the loop stops, produce a concise report:

- goal completed or left open
- work items processed in order
- PRs opened
- PRs merged
- items closed
- items left unresolved
- blockers encountered
- validation commands run
- repeated failure patterns
- repo-wide issues discovered
- recommended follow-up work
