# Repo Archaeology

Operate as a map coordinator with disposable mappers. **Read-only.** Do not audit for defects or fix code.

## Loop

1. Refresh live state ([`live-state-refresh`](../live-state-refresh/))
2. Discover map scope ([`map-scope-discovery.md`](map-scope-discovery.md))
3. Plan map runs ([`mappers/mapper-composition.md`](../../mappers/mapper-composition.md))
4. For each run: spawn mapper with 1–2 mappers from [`mappers/`](../../mappers/)
5. Keep compact mapper results only
6. Aggregate into map artifact ([`map-result-schema`](../../primitives/map-result-schema/map-result-schema.md))
7. Produce reading order + open questions

## Deliverables

- module map
- data flow summary
- deploy topology summary
- recommended reading order for new contributors/agents

## Safety

Read-only. No commits, issues, or PRs.
