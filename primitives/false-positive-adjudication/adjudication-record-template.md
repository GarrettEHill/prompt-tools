# Adjudication Record Template

```markdown
## Adjudication Record

**Finding:** <id or link>
**Tool/rule:** <sonar rule, clippy lint, eslint rule, etc.>
**Location:** <file:line or issue reference>

### Evidence reviewed
- <log, test, policy doc, runtime behavior>

### Classification
- [ ] true positive
- [ ] false positive
- [ ] policy disagreement — needs human
- [ ] tool/environment bug

### Action taken
- [ ] fix implemented
- [ ] narrow suppression with justification
- [ ] issue closed as false positive
- [ ] left open/blocked

### Justification
<short, specific reason>

### Follow-up
<none | human review | create child issue>
```
