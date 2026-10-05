---
name: pre-linter
description: Enforces the use of local CPU formatters instead of LLM formatting to save tokens.
---

# Pre-Linter Optimization

**Directives:**
1. Do NOT manually format code (e.g., fixing indentation, quotes, or spacing) using file edits.
2. If code formatting is requested, run the project's native formatter via the terminal (e.g., `npm run format`, `prettier --write`, `black`, `gofmt`).
3. Only use LLM tokens for logic changes, letting the CPU handle the syntax styling.
