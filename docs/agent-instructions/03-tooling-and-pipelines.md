# 03: Tooling and Pipelines

This document establishes guidelines for automation, tooling, and CI/CD.

---

## 🔧 Tool Creation Principle

> **If you do it twice, automate it.**

### The Rule

When an agent or developer performs a verification task more than once:

1. **Identify** the repetitive task
2. **Create** a script to automate it
3. **Document** how to use the script
4. **Commit** the script to `scripts/` or `tools/`

### Examples

| Manual Task | Automated Solution |
|-------------|-------------------|
| Run linter + tests | `scripts/validate.sh` |
| Check coverage | `scripts/coverage.sh` |
| Format code | `scripts/format.sh` |
| Verify dependencies | `scripts/check-deps.sh` |

### Script Requirements

All automation scripts must:

- Be executable (`chmod +x`)
- Include usage documentation at the top
- Exit with non-zero code on failure
- Work on clean checkout (no assumed state)

---

## 🏗️ CI/CD Priority

> **GitHub Actions is the source of truth for build status.**

### Pipeline Philosophy

1. **Every push triggers validation**
2. **Every PR requires passing checks**
3. **Main branch is always deployable**
4. **Failures block merging**

### Required Checks

All PRs must pass:

| Check | Purpose | Tool |
|-------|---------|------|
| Lint | Code style | flake8 |
| Type Check | Type safety | mypy |
| Test | Correctness | pytest |
| Coverage | Test completeness | pytest-cov |
| Security | Vulnerability scan | pip-audit |

### Workflow Structure

```yaml
# .github/workflows/ci.yml
name: CI

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  lint:
    # Fast feedback on style issues
    
  test:
    # Run test suite with coverage
    
  security:
    # Scan for vulnerabilities
```

---

## 📜 Scripts Directory

### Required Scripts

Every repository should have these scripts:

#### `scripts/validate.sh`

One-command validation for local development:

```bash
#!/bin/bash
# Run all validation checks locally
# Usage: ./scripts/validate.sh

set -e

echo "Running linter..."
flake8 flask_ask/

echo "Running tests..."
pytest --cov=flask_ask --cov-fail-under=90

echo "All validations passed!"
```

#### `scripts/setup.sh`

Bootstrap development environment:

```bash
#!/bin/bash
# Set up development environment
# Usage: ./scripts/setup.sh

set -e

python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install -r requirements-dev.txt

echo "Development environment ready!"
```

### Script Guidelines

1. **Use bash shebang**: `#!/bin/bash`
2. **Fail fast**: `set -e` at the start
3. **Be verbose**: Echo what's happening
4. **Document**: Comment explaining purpose

---

## 🤖 Agent Automation

### For AI Agents

When working on this repository, agents should:

1. **Use existing scripts** before writing custom commands
2. **Create new scripts** for any task done more than once
3. **Document scripts** so future agents can use them
4. **Test scripts** to ensure they work correctly

### Self-Validation Workflow

```bash
# Before committing any changes:

# 1. Run the standard validation
./scripts/validate.sh

# 2. If validation fails, fix issues and re-run

# 3. Only commit when validation passes
```

### Creating New Scripts

When creating a new automation script:

```bash
#!/bin/bash
# SCRIPT_NAME: Brief description
# 
# Purpose: Detailed explanation of what this script does
#
# Usage: 
#   ./scripts/SCRIPT_NAME.sh [options]
#
# Options:
#   -v    Verbose output
#   -h    Show this help
#
# Examples:
#   ./scripts/SCRIPT_NAME.sh
#   ./scripts/SCRIPT_NAME.sh -v

set -e

# Script implementation here
```

---

## 🔍 Dependency Management

### Adding Dependencies

When adding a new dependency:

1. **Research** the library (see 01-research-and-web.md)
2. **Verify** no known security vulnerabilities
3. **Add** to `requirements.txt` with pinned version
4. **Document** why the dependency was added

### Dependency Format

```
# requirements.txt
# Core dependencies
Flask==2.1.3          # Web framework
aniso8601==9.0.1      # ISO 8601 datetime parsing

# Security
cryptography==42.0.5  # For request verification
pyOpenSSL==24.1.0     # TLS support
```

### Updating Dependencies

When updating dependencies:

1. Run `pip-audit` to check for vulnerabilities
2. Update one dependency at a time
3. Run full test suite after each update
4. Document the update in commit message

---

## 📊 Monitoring and Reporting

### Build Status

- Display build status badge in README
- Monitor for flaky tests
- Track coverage trends over time

### Coverage Reports

```yaml
# In CI workflow
- name: Upload coverage
  uses: codecov/codecov-action@v3
  with:
    files: ./coverage.xml
```

### Security Scanning

```yaml
# In CI workflow
- name: Security scan
  run: pip-audit --strict
```

---

## 🚀 Deployment Considerations

### Pre-Deployment Checklist

Before any release:

- [ ] All CI checks pass
- [ ] Coverage meets 90% threshold
- [ ] No security vulnerabilities
- [ ] Changelog updated
- [ ] Version bumped
- [ ] Documentation updated

### Release Process

1. Create release branch
2. Update version in `setup.py`
3. Update CHANGELOG.md
4. Create PR and get approval
5. Merge and tag release
6. CI builds and publishes package

---

*Automation reduces errors and speeds up development. Invest in tooling.*
