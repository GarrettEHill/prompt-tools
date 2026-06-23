# Remote review bootstrap — PR review

```yaml
repo: <owner/repo>
pr: <number>
reviewers: []   # optional; auto-select if empty
```

Fetch `{base}prompts/manifests/review-pr-manifest.md` and listed files.

Execute [`patterns/pr-review/pr-review-coordinator.md`] on PR diff. Read-only.

**Begin:** `gh pr view`, `gh pr diff`, then review.
