# Technical Specifications

This directory contains technical specifications for features and changes to the Flask-Ask library.

## Purpose

Technical specifications serve as the **source of truth** for implementation work. They:

- **Drive Development**: All code changes must have a corresponding spec
- **Enable Review**: Allow async review of proposals before implementation
- **Document Intent**: Capture the "why" behind implementations
- **Support AI Agents**: Provide context for autonomous coding agents

## ⚠️ Critical Rule

> **NO CODE WITHOUT A SPEC**
>
> AI agents and contributors MUST write or update a specification in this directory BEFORE writing implementation code.

## Spec Structure

Each specification should include:

```markdown
# Spec: [Feature/Change Name]

## Summary
One-paragraph description of what this spec covers.

## Motivation
Why is this change needed? What problem does it solve?

## Detailed Design
Technical details of the implementation approach.

## API Changes
Any public API additions, modifications, or removals.

## Testing Strategy
How will this change be tested?

## Migration/Compatibility
Any breaking changes or migration requirements.

## Open Questions
Unresolved decisions or areas needing input.
```

## File Naming Convention

Specs should be named using the format: `NNNN-feature-name.md`

- `NNNN`: A four-digit sequence number
- `feature-name`: A lowercase, hyphenated description

## Workflow

1. **Propose**: Create a spec file with `Status: Draft`
2. **Review**: Get feedback from maintainers or team
3. **Approve**: Update status to `Status: Approved`
4. **Implement**: Write code that matches the spec
5. **Complete**: Update status to `Status: Implemented`

---

*Note: AI agents must create or update specs before implementation.*
