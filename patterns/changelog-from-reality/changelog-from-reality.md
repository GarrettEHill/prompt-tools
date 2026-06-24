# Changelog From Reality

Build changelog from merged PRs, commits, and labels since last tag.

## Config

```yaml
since_tag: vX.Y.Z
```

## Steps

1. `git log` / `gh pr list --state merged` since tag
2. Classify: breaking, feat, fix, deps
3. Link PRs/issues
4. Fill [`changelog-template.md`](changelog-template.md)

Used by release-coordinator.
