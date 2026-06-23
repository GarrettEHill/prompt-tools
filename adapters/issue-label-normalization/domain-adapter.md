## Domain Adapter: Issue Label Normalization

Repository/project:
- `<owner/repo>`

Goal:
- Normalize issue labels to match project taxonomy and required label sets.

Work queue discovery:
- open issues missing required labels
- issues with deprecated or conflicting labels
- issues mislabeled by area/priority/type
- label taxonomy from docs or `.github/ISSUE_TEMPLATE`

Selection order:
1. missing required labels on recent/active issues
2. deprecated label replacements
3. conflicting label pairs
4. historical backlog items

A work item is concrete when:
- one issue per worker, or
- one normalization rule across a small explicit set if policy allows safe batching

If an item is too broad:
- split by label rule or issue cohort
- do not rename global labels without a dedicated migration item

Validation requirements:
- compare against documented label policy
- ensure required label sets are satisfied
- no issue body/title edits unless explicitly in scope

Completion criteria:
- issue labels conform to policy
- deprecated labels removed/replaced
- comments added only when policy requires explanation

Special safety rules:
- do not close issues during label normalization unless explicitly in scope
- do not rename global labels without migration plan
- preserve human-applied labels when policy says to

Final report must include:
- issues updated count
- deprecated labels replaced
- policy gaps discovered
