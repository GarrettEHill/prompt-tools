# Flake Classification

| Outcome | Signals | Next action |
|---------|---------|-------------|
| **flake** | Passes on retry; non-deterministic assertion/timing | Quarantine policy or fix test |
| **env** | Fails consistently in one runner/region | Check infra, deps, secrets scope |
| **deterministic bug** | Fails consistently locally | CCM implement fix |
| **blocked** | Cannot reproduce; logs truncated | Request more CI retention |

Document evidence for each classification.
