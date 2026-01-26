# 00: Core Philosophy

This document establishes the foundational principles for AI agents working on Flask-Ask.

---

## 🎯 Docs = Code

> **Documentation is not an afterthought—it IS the code specification.**

### The Rule

No implementation code shall be written without first creating or updating the corresponding documentation:

1. **Before coding**: Write or update a spec in `docs/specs/`
2. **During coding**: Keep the spec synchronized with implementation changes
3. **After coding**: Verify the spec matches the final implementation

### Why This Matters

- **Clarity**: Forces clear thinking before implementation
- **Review**: Allows async review of approach before time is invested
- **Context**: Future agents/developers understand WHY decisions were made
- **Quality**: Reduces rework from misunderstood requirements

### Enforcement

AI agents must include spec references in all code-related commits:

```
feat(models): add support for APL directives

Spec: docs/specs/0005-apl-directive-support.md
```

---

## 🔄 Sync: History Updates

> **Every completed piece of work must be recorded.**

After completing any significant work:

1. Create a handoff document in `docs/history/`
2. Document what was done, why, and any follow-up items
3. Reference related PRs, issues, and specs

This ensures knowledge is never lost, even when agents or contributors change.

---

## 👔 The CEO Model

> **The initiating agent is the CEO. Sub-agents are specialist workers.**

### Hierarchy

```
┌─────────────────────────────────────────┐
│           CEO Agent (You)               │
│   - Understands full context            │
│   - Makes strategic decisions           │
│   - Delegates specific tasks            │
└─────────────────┬───────────────────────┘
                  │
    ┌─────────────┼─────────────┐
    │             │             │
┌───▼───┐   ┌─────▼────┐   ┌────▼────┐
│Research│   │  Code    │   │  Test   │
│ Agent  │   │  Agent   │   │  Agent  │
└────────┘   └──────────┘   └─────────┘
```

### Responsibilities

**CEO Agent:**
- Break down large tasks into sub-tasks
- Provide clear context and requirements to sub-agents
- Integrate results from sub-agents
- Make final decisions on conflicts

**Sub-Agents:**
- Execute specific, well-defined tasks
- Report results back to CEO agent
- Ask for clarification when requirements are unclear

---

## 🧠 First Principles Thinking

> **Reason from the ground up. Don't copy-paste solutions blindly.**

### The Process

1. **Understand the Problem**
   - What exactly needs to be solved?
   - What are the constraints?
   - What are the inputs and expected outputs?

2. **Research**
   - What patterns exist for this problem?
   - What are the tradeoffs of each approach?
   - What does the existing codebase already do?

3. **Plan**
   - Write out the approach step-by-step
   - Identify potential issues before coding
   - Consider edge cases

4. **Implement**
   - Follow the plan
   - Deviate only with documented reasoning

5. **Verify**
   - Does the solution solve the original problem?
   - Are there unintended side effects?
   - Do all tests pass?

### Anti-Patterns to Avoid

❌ **Don't**: Copy code from Stack Overflow without understanding it
❌ **Don't**: Implement the first solution that comes to mind
❌ **Don't**: Skip the planning phase for "simple" changes
❌ **Don't**: Make assumptions about APIs without verification

✅ **Do**: Research current best practices
✅ **Do**: Understand why a pattern is used
✅ **Do**: Write down the plan before coding
✅ **Do**: Verify APIs and library behavior

---

## 📋 Decision Checklist

Before starting any work, verify:

- [ ] I have read all files in `docs/agent-instructions/`
- [ ] I have checked `docs/adrs/` for relevant past decisions
- [ ] I have read existing specs related to my work
- [ ] I understand the problem I'm solving
- [ ] I have a plan for implementation
- [ ] I know how I will test and verify my changes

---

*These principles are non-negotiable. Following them ensures quality and maintainability.*
