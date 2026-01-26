# History & Handoffs

This directory records significant changes, handoffs, and deprecated logic in the Flask-Ask project.

## Purpose

The history directory serves as a **knowledge transfer mechanism**:

- **Handoff Documentation**: Record context when work is passed between contributors
- **Deprecation Records**: Document what was removed and why
- **Migration Guides**: Help users upgrade between versions
- **Decision Context**: Preserve reasoning that might not fit in ADRs

## When to Write History

Create a history document when:

1. **Completing a major feature**: Document what was done and any follow-up work
2. **Deprecating functionality**: Explain what was removed and why
3. **Handing off work**: Provide context for the next contributor
4. **Making breaking changes**: Document migration steps

## Document Structure

```markdown
# [Title]: [Brief Description]

## Date
YYYY-MM-DD

## Author
@github-username or AI Agent identifier

## Summary
What was changed/completed/deprecated.

## Context
Why this change was made. What led to this decision.

## Details
Technical details of what was done.

## Follow-up Items
Any remaining work or known issues.

## References
- Links to PRs, issues, or external docs
```

## File Naming Convention

Files should be named using the format: `YYYY-MM-DD-description.md`

Example: `2024-01-15-session-cache-refactor.md`

## Index

| Date | Title | Type |
|------|-------|------|
| - | - | - |

---

*Note: AI agents MUST update this directory after completing significant work.*
