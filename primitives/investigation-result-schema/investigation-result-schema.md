# Investigation Result Schema

Compact output for regression hunt, flake hunter, and incident workflows.

```yaml
investigation:
  type: regression | flake | incident
  repo: string
  symptom: string
  status: root-cause-found | mitigated | blocked | inconclusive
summary: string
timeline:
  - at: string
    event: string
    evidence: string
hypothesis:
  - statement: string
    confidence: high | medium | low
    evidence: string
root_cause: string | null
regression_window:
  good_ref: string | null
  bad_ref: string | null
  suspect_commits: [string]
classification: flake | env | deterministic-bug | null
impact:
  severity: sev1 | sev2 | sev3 | sev4
  scope: string
mitigations:
  - action: string
    type: mitigation | fix
    status: proposed | applied | blocked
blockers: [string]
checks_run: [{cmd, status}]
next_steps: [string]
```
