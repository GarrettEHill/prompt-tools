# Config Drift Fix

Align env templates, compose profiles, CI matrices — detect drift and queue fixes.

## Drift checklist

- `.env.example` vs documented vars vs CI secrets names
- `docker-compose*.yml` service/env parity
- CI matrix vs supported runtimes
- Feature flags default consistency

Execute fixes via CCM. Adapter: [`env-compose-ci-drift`](../../adapters/env-compose-ci-drift/domain-adapter.md).
