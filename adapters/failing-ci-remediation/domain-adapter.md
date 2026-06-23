## Domain Adapter: Failing CI Remediation

Repository/project:
- `<owner/repo>`

Goal:
- Identify, fix, and verify failing CI jobs/checks until required checks are green.

Work queue discovery:
- recent failing workflow runs on `main` and open PRs
- required checks on open PRs via `gh pr checks`
- `gh run list`, Actions annotations, and job logs
- classify main-branch regression vs PR-specific failure

Selection order:
1. required checks failing on `main`
2. required checks failing on merge-ready PRs
3. non-required but high-signal failures
4. flaky/low-confidence failures after investigation

A work item is concrete when:
- one failing job/check/root-cause cluster per worker
- split multi-job failures when root causes differ

If an item is too broad:
- decompose by job, workflow, or failing test file
- route flaky failures to investigation first

Validation requirements:
- reproduce with focused command when possible
- run affected test suite
- run repo-standard CI-equivalent commands locally
- wait for GitHub checks when local reproduction is insufficient

Completion criteria:
- target check green on the correct branch/PR
- root cause addressed, not masked
- flaky tests fixed or quarantined per project policy

Special safety rules:
- do not disable checks to "fix" CI without explicit project policy
- do not weaken assertions without proving incorrectness
- prefer root-cause fixes over retry-only behavior

Final report must include:
- main vs PR failures remediated
- checks still failing
- flaky tests discovered
- workflows/jobs touched
