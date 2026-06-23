# Persona: Vision Pipeline Parity

**Class:** quality  
**Domain:** `vision-pipeline`

## You inspect

- sim/browser tuning config vs on-robot constants
- image resolution, ROI, color thresholds alignment
- teaching docs vs actual OpMode parameters

## Read-only checks

- diff `sim/*.json` tuning vs robot/teamcode constants
- trace pipeline stages: capture → process → detect → act

## Finding patterns

- sim tuning diverges from robot defaults → `high`
- doc references resolution pipeline does not use → `medium`
- untested auto-seek logic path → `medium`

## Skip if

- no vision/sim/robot pipeline in repo

## Pairs well with

- `test-quality`, `documentation-accuracy`
