# Agent Instructions

This directory contains instructions and protocols for AI agents working on the Flask-Ask codebase.

## Purpose

These documents define the operating principles, workflows, and quality standards that AI agents MUST follow when contributing to this repository.

## Instruction Files

| File | Purpose |
|------|---------|
| [00-core-philosophy.md](./00-core-philosophy.md) | Foundational principles: Docs=Code, CEO Model, First Principles |
| [01-research-and-web.md](./01-research-and-web.md) | Web research requirements and validation protocols |
| [02-testing-and-validation.md](./02-testing-and-validation.md) | Testing standards, coverage requirements, self-correction |
| [03-tooling-and-pipelines.md](./03-tooling-and-pipelines.md) | Tool creation, CI/CD, automation guidelines |

## Reading Order

Agents should read these files in numerical order before beginning any work:

1. **00-core-philosophy.md** - Understand the fundamental approach
2. **01-research-and-web.md** - Learn research requirements
3. **02-testing-and-validation.md** - Understand quality gates
4. **03-tooling-and-pipelines.md** - Know the automation standards

## Quick Reference

### Before Writing Code

- [ ] Read relevant specs in `docs/specs/`
- [ ] Check ADRs in `docs/adrs/` for past decisions
- [ ] Research current best practices
- [ ] Create/update spec document

### After Writing Code

- [ ] Run tests with `./scripts/validate.sh`
- [ ] Ensure 90% code coverage
- [ ] Update architecture docs if needed
- [ ] Document handoff in `docs/history/`

---

*These instructions are mandatory for all AI agents working on this repository.*
