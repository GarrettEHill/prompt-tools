# OpenAPI Drift Fix

Generate or patch OpenAPI/spec to match handlers (inverse of openapi-api-surface audit).

## Steps

1. Read route handlers / controllers
2. Update OpenAPI spec to match
3. Validate spec against routes
4. PR with spec + optional client regen

Pairs with schema-contract-drift and openapi-api-surface persona.
