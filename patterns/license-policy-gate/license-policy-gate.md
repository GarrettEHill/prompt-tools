# License Policy Gate

Merge/release gate on dependency licenses against project policy.

Uses [`license-policy-template`](../../primitives/license-policy-template/license-policy-template.md).

## Output

```yaml
verdict: pass | fail | review-required
violations: [{dep, license, action}]
```

Integrates with ship-checklist and release-coordinator.
