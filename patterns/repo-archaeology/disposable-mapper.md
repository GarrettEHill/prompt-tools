# Disposable Mapper

One map section per run. Flavor with mappers from [`mappers/`](../../mappers/).

## Steps

1. Read boundary and assigned mapper persona(s)
2. Inspect live files — read-only
3. Record module entries and flows per [`map-result-schema`](../../primitives/map-result-schema/)
4. Return [`compact-mapper-result`](../../primitives/map-result-schema/compact-mapper-result.md)

## Scope lock

One boundary only. No fixes. No audit findings.
