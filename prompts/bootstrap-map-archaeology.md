# Remote map bootstrap — repo archaeology

```yaml
repo: <owner/repo>
prompt_tools_base: https://raw.githubusercontent.com/GarrettEHill/prompt-tools/main/
output: chat-only | docs/map/<YYYY-MM-DD>/
```

1. Fetch `{base}prompts/manifests/map-archaeology-manifest.md` and bootstrap files listed
2. Execute [`patterns/repo-archaeology/repo-archaeology.md`]({base}patterns/repo-archaeology/repo-archaeology.md) on this workspace
3. Read-only. Deliver map artifact + reading order

**Begin:** Phase 0 live refresh, then map scope discovery.
