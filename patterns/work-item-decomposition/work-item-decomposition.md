# Work Item Decomposition

Decompose broad work before assigning it to a disposable worker.

## Concrete item test

A work item is ready for one worker when it has:

- one primary outcome
- inspectable acceptance criteria
- bounded file/module scope
- known validation commands
- no unresolved design decision requiring human input
- completable in one worker context without switching goals

## Too-broad signals

- multiple unrelated modules
- unclear or conflicting acceptance criteria
- external dependency not yet available
- mixed work types (code + infra + docs epic)
- parent/umbrella issue without children

## Decomposition strategies

### Umbrella GitHub issues

- create child issues with acceptance criteria
- select the smallest unblocked child
- do not close parent until all children are complete

### Sonar/security findings

- scope to file/module/rule cluster
- split multi-location findings when fixes are independent

### Failing CI

- one failing job/check/root-cause cluster per item
- split when root causes differ

### Dependabot PRs

- one PR per worker unless policy defines safe grouping

### Documentation backlog

- one page/section/API surface per item

### Label normalization

- one issue per worker, or one explicit rule batch if policy allows

## Dependency ordering

Prefer items that:

1. unblock other items
2. reduce security/reliability risk
3. have the smallest blast radius
4. already have partial PRs or fixes in flight

## Parent/child closure

Never close a parent/umbrella item until all children and acceptance criteria are complete.
