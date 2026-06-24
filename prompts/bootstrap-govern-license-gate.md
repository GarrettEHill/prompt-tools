# Remote govern bootstrap — license policy gate

**Fetched from GarrettEHill/prompt-tools `main`.** Execute on the current workspace.

## Config (from user prompt)

```yaml
repo: <owner/repo>
policy: <path to license-policy-template>
```

## Remote base

```text
PROMPT_TOOLS_BASE=https://raw.githubusercontent.com/GarrettEHill/prompt-tools/main/
```

## Load

Fetch `{PROMPT_TOOLS_BASE}prompts/manifests/govern-license-gate-manifest.md` and all bootstrap files listed.

## Run

Execute per listed pattern files. 

**Begin:** load manifest, refresh live state, then run coordinator.
