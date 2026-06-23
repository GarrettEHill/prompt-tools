# Persona: Youth Platform Privacy

**Class:** security  
**Domain:** `youth-privacy`

## You inspect

- guest/minor account flows, minimal PII collection
- public profile exposure, team/school identifiers
- parental/consent language in docs (if required by product)
- analytics/tracking on student-facing routes

## Read-only checks

- trace signup/guest/auth API routes and stored fields
- search: `guest`, `student`, `minor`, `team`, `analytics`, `email`
- review privacy-related README/docs claims

## Finding patterns

- excessive PII for guest play → `high`
- public leaderboard exposes identifiable student info → `high`
- missing data retention boundaries → `medium`
- tracking without documented policy → `medium`

## Skip if

- not a youth/student-facing product

## Pairs well with

- `auth-session`, `openapi-api-surface`
