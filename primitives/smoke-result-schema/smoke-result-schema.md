# Smoke Result Schema

```yaml
smoke:
  environment: string
  deploy_ref: string
  verdict: pass | fail | partial | blocked
summary: string
checks:
  - name: string
    type: health | critical-path | integration
    status: pass | fail | skip
    evidence: string
rollback_triggered: false
blockers: [string]
checks_run: [{cmd, status}]
```
