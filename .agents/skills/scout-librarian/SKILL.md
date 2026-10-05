---
name: scout-librarian
description: Deploys a read-only subagent to map project impact before edits.
---

# The Scout (Librarian Pattern)

**Directives:**
1. Before modifying core files or heavily used utility functions, spawn a `research` subagent (The Scout) using `invoke_subagent`.
2. Give The Scout read-only instructions: Map all dependents of the function/file about to be changed using `grep_search` or AST tools.
3. The Scout must return an "Impact Map" listing all files that will break if the signature changes.
4. Use this map to plan a safe, cascading refactor without blind spots.
