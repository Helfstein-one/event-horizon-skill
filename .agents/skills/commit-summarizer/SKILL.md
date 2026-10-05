---
name: commit-summarizer
description: Generates a lightweight git commit message using flash-lite.
---

# Commit Summarizer (Flash-only)

**Directives:**
1. To write a commit message, DO NOT process it yourself if you are operating on a Pro model.
2. Run `git diff` and capture the output.
3. Call `invoke_subagent` with `Model: 'flash_lite'` and pass the diff.
4. Instruct the subagent to reply ONLY with a formatted conventional commit message (e.g., `feat: added X`).
5. Execute the `git commit -m "..."` using the subagent's response.
