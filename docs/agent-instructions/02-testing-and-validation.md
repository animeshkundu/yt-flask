# 02: Testing and Validation

This document establishes testing standards and validation requirements.

---

## 📊 The 90% Rule

> **Minimum 90% code coverage is mandatory for all contributions.**

### Coverage Requirements

| Metric | Minimum |
|--------|---------|
| Line Coverage | 90% |
| Branch Coverage | 85% |
| Function Coverage | 95% |

### Why 90%?

- **Confidence**: High coverage ensures changes don't break existing functionality
- **Documentation**: Tests serve as living documentation of expected behavior
- **Refactoring**: Safe to improve code when tests catch regressions
- **Quality**: Forces consideration of edge cases

### Measuring Coverage

```bash
# Run tests with coverage
pytest --cov=flask_ask --cov-report=term-missing --cov-fail-under=90

# Generate HTML report
pytest --cov=flask_ask --cov-report=html
```

---

## 🧪 Test-Driven Development

> **Write the test BEFORE or WITH the implementation—never after.**

### The TDD Cycle

```
┌─────────────────────────────────────────────────┐
│                                                 │
│    ┌───────┐    ┌───────┐    ┌──────────┐      │
│    │ RED   │───▶│ GREEN │───▶│ REFACTOR │──┐   │
│    │(write │    │(make  │    │(improve  │  │   │
│    │ test) │    │ pass) │    │  code)   │  │   │
│    └───────┘    └───────┘    └──────────┘  │   │
│         ▲                                   │   │
│         └───────────────────────────────────┘   │
│                                                 │
└─────────────────────────────────────────────────┘
```

1. **RED**: Write a failing test that defines expected behavior
2. **GREEN**: Write minimal code to make the test pass
3. **REFACTOR**: Improve the code while keeping tests green
4. **REPEAT**: Continue until feature is complete

### Test First Benefits

- Forces clear understanding of requirements
- Prevents over-engineering (only write what's needed)
- Ensures all code is testable
- Creates immediate feedback loop

---

## 🔬 Test Categories

### Unit Tests

Test individual functions/methods in isolation.

```python
# tests/test_models.py
def test_statement_ends_session():
    """statement() should set shouldEndSession to True."""
    response = statement("Hello")
    rendered = json.loads(response.render_response())
    assert rendered['response']['shouldEndSession'] is True

def test_question_keeps_session():
    """question() should set shouldEndSession to False."""
    response = question("What's next?")
    rendered = json.loads(response.render_response())
    assert rendered['response']['shouldEndSession'] is False
```

### Integration Tests

Test component interactions.

```python
# tests/test_integration.py
def test_full_request_response_cycle():
    """Test complete flow from Alexa request to response."""
    with app.test_client() as client:
        response = client.post('/alexa', json=launch_request)
        assert response.status_code == 200
        data = response.get_json()
        assert 'response' in data
```

### Edge Case Tests

Test boundary conditions and error cases.

```python
# tests/test_edge_cases.py
def test_empty_speech_audio():
    """audio() with empty speech should not include outputSpeech."""
    response = audio('')
    rendered = json.loads(response.render_response())
    assert 'outputSpeech' not in rendered['response']

def test_malformed_ssml_falls_back_to_plaintext():
    """Invalid SSML should be treated as plain text."""
    response = statement("<speak>unclosed tag")
    rendered = json.loads(response.render_response())
    assert rendered['response']['outputSpeech']['type'] == 'PlainText'
```

---

## ✅ Self-Correction Protocol

> **Verify your own work before committing.**

### Pre-Commit Checklist

Before committing any code changes:

```bash
# 1. Run the validation script
./scripts/validate.sh

# 2. Check for linting errors
flake8 flask_ask/

# 3. Run tests with coverage
pytest --cov=flask_ask --cov-fail-under=90

# 4. Check for type errors (if using type hints)
mypy flask_ask/
```

### Self-Review Questions

Ask yourself:

- [ ] Do all tests pass?
- [ ] Is coverage at 90% or above?
- [ ] Did I test the happy path?
- [ ] Did I test edge cases?
- [ ] Did I test error conditions?
- [ ] Are there any untested code paths?

### When Tests Fail

1. **Read the error message carefully**
2. **Understand WHY the test failed**
3. **Fix the root cause, not symptoms**
4. **Run tests again to verify the fix**
5. **Check that no other tests broke**

---

## 📁 Test Organization

### Directory Structure

```
tests/
├── __init__.py
├── conftest.py          # Shared fixtures
├── test_core.py         # Core functionality tests
├── test_models.py       # Response model tests
├── test_cache.py        # Cache functionality tests
├── test_verifier.py     # Request verification tests
├── test_convert.py      # Type conversion tests
└── test_integration.py  # End-to-end tests
```

### Naming Conventions

```python
# Test files: test_<module>.py
test_models.py

# Test functions: test_<what>_<condition>_<expected>
def test_statement_with_card_returns_card_in_response():
    pass

# Test classes: Test<ClassName>
class TestAudioResponse:
    pass
```

### Fixtures

Use pytest fixtures for common setup:

```python
# conftest.py
import pytest

@pytest.fixture
def mock_session():
    """Provide a mock session for tests."""
    return {'attributes': {}, 'sessionId': 'test-session'}

@pytest.fixture
def sample_intent_request():
    """Provide a sample Alexa intent request."""
    return {
        'request': {
            'type': 'IntentRequest',
            'intent': {'name': 'TestIntent'}
        }
    }
```

---

## 🚫 Test Anti-Patterns

Avoid these common mistakes:

### ❌ Testing Implementation Details

```python
# Bad: Tests internal implementation
def test_response_has_internal_flag():
    response = statement("Hello")
    assert response._json_default is None  # Don't test private attrs
```

### ❌ Overly Broad Assertions

```python
# Bad: Too vague
def test_response_works():
    response = statement("Hello")
    assert response  # What are we actually verifying?
```

### ❌ Tests Without Assertions

```python
# Bad: No assertion
def test_does_something():
    result = do_something()
    # Where's the assert?
```

### ✅ Good Test Example

```python
def test_simple_card_includes_title_and_content():
    """simple_card() should add a Simple card with given title and content."""
    response = statement("Hello").simple_card(title="Title", content="Content")
    rendered = json.loads(response.render_response())
    
    card = rendered['response']['card']
    assert card['type'] == 'Simple'
    assert card['title'] == 'Title'
    assert card['content'] == 'Content'
```

---

*Quality tests are as important as quality code. Treat them with the same rigor.*
