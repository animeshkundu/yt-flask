# Flask-Ask (yt-flask)

Flask-Ask helps you build Amazon Alexa skills with Flask by mapping Alexa requests to Flask view functions.

## Installation

```bash
pip install -e .
```

## Minimal usage

```python
from flask import Flask
from flask_ask import Ask, question

app = Flask(__name__)
ask = Ask(app, "/")

@ask.launch
def launched():
    return question("Welcome to Flask-Ask")

if __name__ == "__main__":
    app.run()
```

## Development: lint and test

Install development tools:

```bash
python -m pip install -e . pytest ruff
```

Run lint and tests:

```bash
ruff check tests
pytest -q
```
