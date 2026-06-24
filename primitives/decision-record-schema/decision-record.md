# Decision Record Schema

Output for Decide family workflows. **No merge by default.**

```yaml
decision:
  title: string
  status: proposed | accepted | rejected | deferred
  date: string
context: string
options:
  - name: string
    pros: [string]
    cons: [string]
    risks: [string]
recommendation: string
non_goals: [string]
evidence: [string]
follow_up:
  issues: [string]
  spikes: [string]
no_commit: true
```
