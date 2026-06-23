## Domain Adapter: Documentation Backlog Cleanup

Repository/project:
- `<owner/repo>`

Goal:
- Clear the documentation backlog: fix stale, broken, or missing docs.

Work queue discovery:
- issues labeled documentation, docs, typo, broken-link
- TODO/FIXME in docs directories
- link check failures
- stale version references
- missing docs for public APIs/features

Selection order:
1. broken/misleading docs affecting install/run/build
2. missing docs for shipped features
3. broken links and outdated commands
4. style/consistency cleanup

A work item is concrete when:
- one page/section/API doc per worker
- one tightly related broken-link cluster per worker

If an item is too broad:
- split by page, section, or API surface
- use umbrella-issue adapter for doc epics with children

Validation requirements:
- links resolve (link checker or spot verification)
- documented commands run or are clearly marked optional/contextual
- docs build step if one exists (MkDocs, Docusaurus, etc.)
- spellcheck/markdown lint if project uses them

Completion criteria:
- doc change merged with verified examples/commands
- related issue closed only if scope fully addressed
- no stale contradictory doc left in same area

Special safety rules:
- no code behavior changes unless required to make docs truthful
- do not delete docs without replacement/redirect when users depend on them
- preserve project tone/structure conventions

Final report must include:
- pages/sections updated
- broken links fixed
- issues closed
- docs build status
