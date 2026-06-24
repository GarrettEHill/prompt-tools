# Postmortem Generator

Blameless postmortem from compact investigation or incident results.

## Input

- [`investigation-result-schema`](../../primitives/investigation-result-schema/investigation-result-schema.md)
- Incident timeline (optional)
- CCM final-report (optional)

## Steps

1. Load inputs (paths or pasted YAML)
2. Fill [`postmortem-template.md`](postmortem-template.md)
3. Extract action items with owners
4. Optional: create follow-up issues via divide-and-conquer issue-generation

## Output

Markdown postmortem + action item list linkable to GitHub issues.
