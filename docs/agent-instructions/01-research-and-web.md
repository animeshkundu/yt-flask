# 01: Research and Web Access

This document establishes protocols for using web research in development work.

---

## 🌐 Internet is First-Class

> **Web research is not optional—it is a required part of the development process.**

### Why Research Matters

- **Libraries evolve**: APIs change, features are deprecated, best practices shift
- **Security updates**: New vulnerabilities are discovered constantly
- **Better patterns**: The community continuously improves approaches
- **Avoid mistakes**: Learn from others' documented failures

### When to Research

1. **Before implementing a new feature**
2. **Before adding a new dependency**
3. **When encountering an unfamiliar API**
4. **When the existing approach seems outdated**
5. **When debugging a complex issue**

---

## ✅ Validation Protocol

> **Verify before you implement.**

### Library Version Verification

Before using any library:

```
1. Search: "[library name] latest version [year]"
2. Check: Official documentation for current API
3. Verify: Security advisories for known vulnerabilities
4. Confirm: Compatibility with Python 3.x and Flask 2.x
```

### API Verification

Before using any external API:

```
1. Search: "[API name] official documentation"
2. Verify: Endpoint URLs and authentication methods
3. Check: Rate limits and usage restrictions
4. Confirm: Response format matches expectations
```

### Pattern Verification

Before implementing a pattern:

```
1. Search: "[pattern name] best practices [year]"
2. Check: Is this still the recommended approach?
3. Verify: Are there known issues or gotchas?
4. Consider: Does a better alternative exist?
```

---

## 🎯 Information Saturation

> **Research until you stop learning new information.**

### The Saturation Point

Continue researching until:

- Multiple sources agree on the approach
- You understand the tradeoffs of different options
- You can explain WHY the chosen approach is best
- You have not found new information in the last 2-3 searches

### Research Quality Checklist

- [ ] Consulted official documentation
- [ ] Checked multiple independent sources
- [ ] Verified information is current (within last 1-2 years)
- [ ] Understood tradeoffs and alternatives
- [ ] Can explain the reasoning to another developer

---

## 🔍 Research Workflow

### Step 1: Define the Question

Be specific about what you need to know:

❌ Bad: "How to do caching?"
✅ Good: "Best practices for session caching in Flask applications 2024"

### Step 2: Search Strategically

Use targeted search queries:

```
# For library usage
"flask session caching best practices 2024"
"flask-caching vs cachelib comparison"

# For security
"[library] security vulnerabilities CVE"
"flask session security recommendations"

# For patterns
"python alexa skill best practices"
"flask extension architecture patterns"
```

### Step 3: Evaluate Sources

Prioritize sources in this order:

1. **Official documentation** (highest trust)
2. **GitHub issues/discussions** (real-world problems)
3. **Reputable blogs** (thoughtful analysis)
4. **Stack Overflow** (verify answers are current)

### Step 4: Document Findings

Record research results in your spec or PR:

```markdown
## Research Notes

- Flask-Caching is recommended over manual caching (Source: Flask docs)
- cachelib 0.12+ supports async operations (Source: GitHub release notes)
- Session tokens should use secrets.token_urlsafe() (Source: OWASP)
```

---

## ⚠️ Anti-Hallucination Protocol

> **Never invent APIs. When in doubt, search.**

### The Problem

AI models can confidently generate incorrect API calls, library methods, or configuration options that don't exist.

### The Solution

1. **Verify every API call** against official documentation
2. **Don't assume** library methods exist—check first
3. **Test imports** before using them in code
4. **Validate configuration** options are real

### Red Flags

Watch for these signs that research is needed:

- "I think this API might work..."
- "This should be the method name..."
- "The configuration probably looks like..."
- "This library probably supports..."

When you catch yourself using uncertain language, **STOP AND SEARCH**.

---

## 📚 Flask-Ask Specific Research

For this project, always verify:

| Topic | Verify With |
|-------|-------------|
| Alexa request/response format | Amazon Alexa Skills Kit documentation |
| Flask patterns | Flask official documentation |
| Audio Player directives | Alexa AudioPlayer interface docs |
| Request verification | Alexa request verification spec |
| Python async patterns | Python official documentation |

---

*Research is not a shortcut—it is the foundation of quality work.*
