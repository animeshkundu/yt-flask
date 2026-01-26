# Claude Instructions for Flask-Ask

> **CRITICAL**: Before answering ANY request, you MUST read `docs/agent-instructions/`

This document provides context and instructions for Claude and other AI coding assistants working on the Flask-Ask repository.

---

## 🎯 Project Overview

**Flask-Ask** is a Python library that simplifies building Alexa Skills with Flask. It provides decorators for intent handling and helper classes for building Alexa-compliant responses.

### Tech Stack

- **Language**: Python 3.8+
- **Framework**: Flask 2.x
- **Purpose**: Alexa Skills Kit integration

### Key Files

| Path | Purpose |
|------|---------|
| `flask_ask/core.py` | Main Ask class, request handling, decorators |
| `flask_ask/models.py` | Response builders (statement, question, audio) |
| `flask_ask/cache.py` | Session and stream caching |
| `flask_ask/verifier.py` | Alexa request signature verification |
| `flask_ask/convert.py` | Slot value type conversion |

---

## 📚 Required Reading

Before making any changes, you **MUST** read:

1. **`docs/agent-instructions/`** - Operating principles and protocols
2. **`docs/adrs/`** - Past architectural decisions (check for relevant context)
3. **`docs/specs/`** - Technical specifications for features

### Quick Links

- [Core Philosophy](docs/agent-instructions/00-core-philosophy.md)
- [Research & Web](docs/agent-instructions/01-research-and-web.md)
- [Testing & Validation](docs/agent-instructions/02-testing-and-validation.md)
- [Tooling & Pipelines](docs/agent-instructions/03-tooling-and-pipelines.md)

---

## 🛠️ Workflow Requirements

### Before Writing Code

1. **Check existing documentation**
   - Read relevant specs in `docs/specs/`
   - Check ADRs in `docs/adrs/` for past decisions
   - Review architecture docs in `docs/architecture/`

2. **Create or update specification**
   - NO CODE without a corresponding spec
   - Document the approach in `docs/specs/` first

3. **Research if needed**
   - Use web search to verify APIs and best practices
   - Don't hallucinate—verify everything

### While Writing Code

1. **Follow existing patterns**
   - Match the code style of surrounding code
   - Use existing utilities and helpers

2. **Write tests alongside code**
   - Minimum 90% coverage required
   - Test edge cases and error conditions

3. **Keep changes minimal**
   - Only modify what's necessary
   - Don't refactor unrelated code

### After Writing Code

1. **Validate your changes**
   ```bash
   ./scripts/validate.sh
   ```

2. **Update documentation**
   - Update specs to match final implementation
   - Update architecture docs if relevant

3. **Document the handoff**
   - Add entry to `docs/history/` for significant changes

---

## 🚫 Rules and Constraints

### DO

- ✅ Read `docs/agent-instructions/` before starting
- ✅ Check `docs/adrs/` for past decisions
- ✅ Create/update specs before coding
- ✅ Write tests with 90%+ coverage
- ✅ Verify APIs with web search when unsure
- ✅ Run `./scripts/validate.sh` before committing

### DON'T

- ❌ Write code without a spec
- ❌ Skip reading existing documentation
- ❌ Hallucinate APIs or library methods
- ❌ Ignore test coverage requirements
- ❌ Make large, sweeping changes
- ❌ Remove existing tests

---

## 🔍 Common Tasks

### Adding a New Response Type

1. Read `docs/specs/` for existing patterns
2. Create spec document for new response type
3. Add class to `flask_ask/models.py`
4. Add export to `flask_ask/__init__.py`
5. Add tests to `tests/test_models.py`
6. Update architecture docs

### Fixing a Bug

1. Check `docs/adrs/` for relevant context
2. Write a failing test that reproduces the bug
3. Fix the bug with minimal changes
4. Verify test passes
5. Run full validation suite

### Updating Dependencies

1. Research the update (security, compatibility)
2. Update version in `requirements.txt`
3. Run full test suite
4. Document in commit message

---

## 📊 Quality Gates

All contributions must pass:

| Check | Requirement |
|-------|-------------|
| Lint | No flake8 errors |
| Tests | All pass |
| Coverage | ≥90% |
| Docs | Spec exists and matches code |

---

## 🔗 External References

- [Alexa Skills Kit Documentation](https://developer.amazon.com/docs/alexa/custom-skills/request-and-response-json-reference.html)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Flask-Ask Original (archived)](https://github.com/johnwheeler/flask-ask)

---

*Remember: Documentation drives code. If unsure, research. Never hallucinate.*
