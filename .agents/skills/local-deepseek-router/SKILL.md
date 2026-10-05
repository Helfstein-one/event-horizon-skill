---
name: local-deepseek-router
description: Routes simple code formatting and generation tasks to a local DeepSeek model via Ollama to save cloud tokens.
---

# Hybrid Local Router (DeepSeek)

**Trigger:** `always_on`

**Directives:**
1. When asked to perform trivial text formatting, regex writing, simple function generation, or basic JSON parsing, DO NOT process it using your cloud context.
2. Use the `run_command` tool to execute `local-deepseek "YOUR PROMPT HERE"`.
3. Read the output from the local model and use it directly.
4. Reserve your own reasoning (Gemini Pro) strictly for complex architecture, multi-file refactors, and strategic planning.
