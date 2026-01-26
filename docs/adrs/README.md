# Architecture Decision Records (ADRs)

This directory contains Architecture Decision Records (ADRs) that document significant architectural decisions made for the Flask-Ask project.

## Purpose

ADRs capture the context, decision, and consequences of architectural choices. They serve as:

- **Historical Record**: Document why decisions were made at a specific point in time
- **Onboarding Tool**: Help new contributors understand the codebase's evolution
- **Regression Prevention**: Ensure AI agents don't undo intentional architectural choices

## How to Use

1. **Before making architectural changes**: Check existing ADRs for relevant context
2. **When proposing new architecture**: Create a new ADR using `0000-template.md`
3. **When revisiting decisions**: Update or supersede existing ADRs

## File Naming Convention

ADRs should be named using the format: `NNNN-short-title.md`

- `NNNN`: A four-digit sequence number (e.g., `0001`, `0002`)
- `short-title`: A lowercase, hyphenated description

## Template

See [0000-template.md](./0000-template.md) for the standard ADR template.

## Index

| ADR | Title | Status | Date |
|-----|-------|--------|------|
| [0000](./0000-template.md) | Template | Template | N/A |

---

*Note: AI agents must consult this directory before making architectural changes.*
