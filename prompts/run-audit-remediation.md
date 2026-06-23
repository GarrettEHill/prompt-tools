# Run Audit Remediation

Paste into Cursor on the **same repo**, after audit issues exist.

## Config

```yaml
repo: <owner/repo>
prompt_tools: <local path | GarrettEHill/prompt-tools>
handoff: |
  (paste Phase 8 output from audit run — remediation_queue + CCM handoff block)
```

## Bootstrap

1. Set `PROMPT_TOOLS_BASE` (local path or `https://raw.githubusercontent.com/GarrettEHill/prompt-tools/main/`).
2. **Load** `prompts/manifests/remediation-manifest.md` and all bootstrap files listed there.
3. Parse `handoff` for the prioritized issue queue.

## Run

Act as CCM coordinator. Process one `audit-finding` issue per worker iteration.  
Load per-iteration files from the remediation manifest. Follow `continuous-completion-model.md`.

**Start now:** load manifest, refresh live state, take first queued issue.
