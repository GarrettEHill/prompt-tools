# Cost Finding Schema

```yaml
cost_review:
  period: string
  sources: [string]
findings:
  - category: overprovisioned | idle | misconfigured | unknown
    resource: string
    evidence: string
    estimated_savings: string
    risk: low | medium | high
recommendations:
  - action: string
    priority: high | medium | low
    requires_approval: true
```
