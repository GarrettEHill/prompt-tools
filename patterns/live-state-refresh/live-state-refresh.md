# Live State Refresh

Refresh live project state before starting and between sweep iterations.

## Refresh layers

### 1. Environment

- `gh auth status`
- required CLIs available
- correct repo clone/path
- network/API availability

### 2. Git hygiene

- current branch
- `git status` — respect unrelated user changes
- sync `main` from origin
- confirm not in accidental detached state

### 3. GitHub live state

- open PRs relevant to the goal
- open issues, labels, and checks
- failing Actions/workflows
- branch protection context

### 4. Baseline health

- run minimal repo validation command(s)
- stop if baseline is globally broken

### 5. Safety decision

- safe to continue?
- blocked by secrets/production risk?
- should route to investigate-only mode?

## Output

Produce a compact current-state snapshot:

```markdown
**Branch:** main (clean | dirty — user changes present)
**Auth/tooling:** ok | blocked
**Open relevant items:** <count + brief list>
**Baseline validation:** pass | fail | not run
**Recommendation:** continue | stop | investigate-only
```

## Stop conditions

Stop or do not start the sweep when refresh reveals:

- auth/tooling unavailable
- unrelated user changes at risk
- baseline validation broken globally
- continuing would require secrets or production changes
