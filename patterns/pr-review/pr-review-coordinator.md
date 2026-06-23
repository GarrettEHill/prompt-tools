# PR Review Coordinator

One PR per run. Fetch PR diff via `gh pr diff` / `gh pr view`.

## Loop

1. Live refresh
2. Select reviewers (default: security, test-adequacy, design if DESIGN exists)
3. Spawn disposable reviewer per persona OR blend 2–3 personas in one pass for small PRs
4. Aggregate [`review-result-schema`](../../primitives/review-result-schema/review-result-schema.md)
5. Output verdict + findings (PR comment draft optional)

Read-only on repo — review only, no push unless user asks to apply suggestions.
