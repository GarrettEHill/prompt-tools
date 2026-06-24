# Flake Hunter

Focused workflow for intermittent CI failures.

## Loop

1. Refresh live state; pull CI logs for failed job(s)
2. Reproduce locally if possible (repeat run N times)
3. Classify per [`flake-classification.md`](flake-classification.md)
4. Route:
   - **flake** → quarantine recommendation + evidence
   - **env** → infra/config issue
   - **deterministic bug** → hand off to CCM
   - **blocked** → insufficient logs

## Output

[`investigation-result-schema`](../../primitives/investigation-result-schema/investigation-result-schema.md) with `type: flake`.

## Evidence for quarantine

Require ≥3 failed runs with inconsistent failure point OR pass on retry without code change.
