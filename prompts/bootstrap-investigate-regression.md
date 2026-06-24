# Remote investigate bootstrap — regression hunt

**Fetched from GarrettEHill/prompt-tools `main`.** Execute on the current workspace.

## Config (from user prompt)

```yaml
repo: <owner/repo>
symptom: <description>
last_good_ref: <tag or sha>  # optional
failing_ref: HEAD  # optional
```

## Remote base

```text
PROMPT_TOOLS_BASE=https://raw.githubusercontent.com/GarrettEHill/prompt-tools/main/
```

## Load

Fetch `{PROMPT_TOOLS_BASE}prompts/manifests/investigate-regression-manifest.md` and all bootstrap files listed.

## Run

Execute per listed pattern files. Pairs with failing-ci-remediation adapter.

**Begin:** load manifest, refresh live state, then run coordinator.
