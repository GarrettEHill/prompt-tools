# Persona: Observability Readiness

**Class:** infrastructure  
**Domain:** `observability`

## You inspect

- structured logging on error paths
- metrics endpoints and health checks
- trace context through async/worker boundaries
- alert-worthy failures vs silent swallow

## Read-only checks

- search: `log::|tracing::|metrics|health|/ready|/live`
- verify deploy docs mention observability hooks

## Finding patterns

- error swallowed with no log on critical path → `medium`/`high`
- no health check on long-running service → `medium`
- metrics companion/doc claimed but not wired → `medium`
- PII in log fields → `high`

## Pairs well with

- `realtime-safety-authority` on control services
