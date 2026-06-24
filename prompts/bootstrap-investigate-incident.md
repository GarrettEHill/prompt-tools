# Remote investigate bootstrap — incident coordinator

**Fetched from GarrettEHill/prompt-tools `main`.** Execute on the current workspace.

## Config (from user prompt)

```yaml
repo: <owner/repo>
incident: <title>
severity: sev2  # optional
```

## Remote base

```text
PROMPT_TOOLS_BASE=https://raw.githubusercontent.com/GarrettEHill/prompt-tools/main/
```

## Load

Fetch `{PROMPT_TOOLS_BASE}prompts/manifests/investigate-incident-manifest.md` and all bootstrap files listed.

## Run

Execute per listed pattern files. Document only — no prod changes without approval.

**Begin:** load manifest, refresh live state, then run coordinator.
