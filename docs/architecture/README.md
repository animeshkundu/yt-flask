# Architecture Documentation

This directory contains high-level architectural diagrams and system design documentation for Flask-Ask.

## Purpose

Architecture documentation provides:

- **Visual Understanding**: Mermaid.js diagrams for system components
- **Component Overview**: How different parts of the system interact
- **Design Patterns**: Patterns and conventions used throughout the codebase
- **Integration Points**: How Flask-Ask integrates with Flask and Alexa APIs

## Flask-Ask System Overview

```mermaid
graph TB
    subgraph "Alexa Cloud"
        A[Amazon Alexa Service]
    end
    
    subgraph "Your Server"
        B[Flask Application]
        C[Flask-Ask Extension]
        D[Request Handlers]
        E[Response Models]
        F[Session Cache]
    end
    
    A -->|HTTPS POST| B
    B --> C
    C --> D
    D --> E
    E --> C
    C -->|JSON Response| A
    D <--> F
```

## Core Components

### Request Flow

```mermaid
sequenceDiagram
    participant Alexa
    participant Flask
    participant FlaskAsk
    participant Handler
    
    Alexa->>Flask: POST /alexa (JSON Request)
    Flask->>FlaskAsk: Route to Ask handler
    FlaskAsk->>FlaskAsk: Validate Request
    FlaskAsk->>Handler: Dispatch to intent handler
    Handler->>Handler: Process business logic
    Handler-->>FlaskAsk: Return Response object
    FlaskAsk-->>Flask: Render JSON response
    Flask-->>Alexa: HTTP 200 + JSON
```

### Component Structure

| Component | File | Purpose |
|-----------|------|---------|
| Core | `flask_ask/core.py` | Main Ask class and request handling |
| Models | `flask_ask/models.py` | Response builders (statement, question, audio) |
| Cache | `flask_ask/cache.py` | Session and stream caching |
| Verifier | `flask_ask/verifier.py` | Alexa request verification |
| Convert | `flask_ask/convert.py` | Type conversion utilities |

## Design Patterns

1. **Decorator-based Routing**: Intent handlers are registered via decorators
2. **Builder Pattern**: Response objects use fluent interface for chaining
3. **Context Locals**: Request/session data via Flask-style context locals

## Diagrams

Additional architectural diagrams should be placed in this directory with descriptive filenames:

- `request-lifecycle.md` - Detailed request processing
- `audio-player.md` - AudioPlayer directive handling
- `dialog-management.md` - Dialog delegation flow

---

*Note: Keep diagrams updated when architectural changes are made.*
