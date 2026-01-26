# Flask-Ask

[![CI](https://github.com/animeshkundu/yt-flask/actions/workflows/ci.yml/badge.svg)](https://github.com/animeshkundu/yt-flask/actions/workflows/ci.yml)

Rapid Alexa Skills Kit Development for Amazon Echo Devices in Python.

## Overview

Flask-Ask is a Flask extension that simplifies building Alexa Skills. It provides:

- **Decorator-based intent handling** - Map intents to Python functions
- **Response builders** - Create statements, questions, and audio responses
- **Session management** - Built-in session attribute handling
- **Request verification** - Validate Alexa requests for security

## Installation

```bash
pip install Flask-Ask
```

## Quick Start

```python
from flask import Flask
from flask_ask import Ask, statement, question

app = Flask(__name__)
ask = Ask(app, '/')

@ask.launch
def launch():
    return question("Welcome! What would you like to do?")

@ask.intent('HelloIntent')
def hello():
    return statement("Hello from Flask-Ask!")

if __name__ == '__main__':
    app.run(debug=True)
```

## Documentation

- [Architecture Overview](docs/architecture/README.md)
- [Technical Specifications](docs/specs/README.md)
- [Architecture Decision Records](docs/adrs/README.md)
- [Agent Instructions](docs/agent-instructions/README.md)

## Development

### Setup

```bash
# Clone the repository
git clone https://github.com/animeshkundu/yt-flask.git
cd yt-flask

# Install dependencies
pip install -r requirements.txt
pip install pytest pytest-cov flake8
```

### Validation

Run all validation checks:

```bash
./scripts/validate.sh
```

### Testing

```bash
pytest --cov=flask_ask --cov-report=term-missing
```

## Contributing

Before contributing, please read:

1. [Core Philosophy](docs/agent-instructions/00-core-philosophy.md)
2. [Testing Requirements](docs/agent-instructions/02-testing-and-validation.md)

### Requirements

- Create/update specs before coding
- Maintain 90%+ test coverage
- Pass all CI checks

## License

MIT License
