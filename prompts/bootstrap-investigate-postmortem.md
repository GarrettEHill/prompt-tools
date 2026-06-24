# Remote investigate bootstrap — postmortem generator

**Fetched from GarrettEHill/prompt-tools `main`.** Execute on the current workspace.

## Config (from user prompt)

```yaml
repo: <owner/repo>
input: <path to investigation result or timeline>
```

## Remote base

```text
PROMPT_TOOLS_BASE=https://raw.githubusercontent.com/GarrettEHill/prompt-tools/main/
```

## Load

Fetch `{PROMPT_TOOLS_BASE}prompts/manifests/investigate-postmortem-manifest.md` and all bootstrap files listed.

## Run

Execute per listed pattern files. Blameless postmortem output.

**Begin:** load manifest, refresh live state, then run coordinator.
