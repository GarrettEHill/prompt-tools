# Remote remediation bootstrap

**Fetched from GarrettEHill/prompt-tools `main`.** Execute on the current workspace. Requires prior audit with `audit-finding` issues.

## Config (from user prompt)

```yaml
repo: <owner/repo>
handoff: |
  (remediation_queue + CCM handoff from audit — or omit to discover via gh issue list --label audit-finding)
```

## Remote base

```text
PROMPT_TOOLS_BASE=https://raw.githubusercontent.com/GarrettEHill/prompt-tools/main/
```

## Load

Fetch `{PROMPT_TOOLS_BASE}prompts/manifests/remediation-manifest.md` and all bootstrap files listed.

## Run

CCM coordinator per `continuous-completion-model.md`. One audit-finding issue per worker. Re-fetch manifest files each iteration if needed.

**Begin:** load manifest, refresh live state, process first queued issue.
