# False-Positive Adjudication

Use when a scanner, linter, or CI check reports a finding that may not require a code fix.

## Workflow

1. Reproduce or inspect the finding live.
2. Identify the tool, rule, and claimed violation.
3. Compare with project policy and actual runtime behavior.
4. Classify the outcome:
   - **true positive** → hand off to disposable worker to implement fix
   - **false positive** → document narrow justification; close or suppress per policy
   - **policy disagreement** → blocked pending human decision
   - **tool/environment bug** → blocked with evidence

## Allowable suppression or closure

- objectively incorrect rule application
- documented project policy exception
- finding targets generated or third-party code handled by policy
- non-actionable environment limitation with evidence

## Not sufficient alone

- "too hard" or out of scope
- stylistic preference without policy
- broad rule disabling to avoid one fix
- silencing tests or checks without proving incorrectness

## Handoff

- true positive → [`disposable-worker`](../../patterns/disposable-worker/)
- ambiguous → [`investigation-before-change`](../../patterns/investigation-before-change/)
- record all outcomes with [`adjudication-record-template.md`](adjudication-record-template.md)
