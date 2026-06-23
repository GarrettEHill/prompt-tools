# Stop/Blocker Decision Tree

Use at runtime after each worker result or failed preflight.

## Decision flow

```text
Worker/pre-flight result
        |
        v
  Global blocker? ----yes----> STOP SWEEP + final report
   (auth, baseline,
    secrets risk,
    user-change conflict)
        | no
        v
  Item blocked? ----yes----> Record blocker
        |                    Skip item if safe
        |                    Continue queue
        v
  Retry limit hit? ---yes----> Record failure
        |                    Increment failed-item count
        |                    Continue if count < 3 items
        v
  3 items at retry limit? -> STOP SWEEP + final report
        |
        v
  Item needs investigation? -> Route to investigation pattern
        |
        v
  Item too broad? ----------> Route to decomposition pattern
        |
        v
  Continue with next item
```

## Item-level blockers

Skip the item and continue when safe:

- missing info or access for this item only
- 3 fix attempts exhausted for this item
- scope too broad — needs decomposition first
- flaky or unreproducible — needs investigation first
- merge blocked by conflicts requiring human decision

## Global blockers

Stop the entire sweep:

- `gh auth status` or required tooling unavailable
- baseline validation broken on unrelated changes
- continuing requires secrets or production changes
- unrelated local user changes would be overwritten
- 3 separate work items have hit the 3-attempt retry limit

## CCM thresholds

- **Per item:** at most 3 fix attempts after failed validation.
- **Per sweep:** if 3 separate items hit the retry limit, stop and produce a final report.

## Continue conditions

Safe to continue when:

- next item is independent of the failed/blocked item
- safety rules still satisfied
- global failure count is below the sweep stop threshold
- live state refresh passes
