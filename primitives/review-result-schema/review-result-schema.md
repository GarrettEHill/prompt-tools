# Review Result Schema

PR/change-scoped review output.

```yaml
review:
  pr: number | null
  branch: string | null
  reviewers: [string]
verdict: approve | request-changes | block
summary: string
findings:
  - reviewer: string
    severity: critical | high | medium | low | nit
    location: string
    evidence: string
    suggestion: string
checks_run: [{cmd, status}]
```

Markdown form for PR comment optional.
