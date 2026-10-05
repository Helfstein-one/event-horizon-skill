---
name: living-memory
description: Auto-updates project documentation after major changes to preserve agent context.
---

# Living Memory (Auto-Doc)

**Directives:**
1. After successfully completing a refactor, feature implementation, or bug fix, DO NOT consider the task done.
2. Automatically invoke a subagent (Model: `flash_lite` or `flash`) to summarize the changes.
3. Have the subagent append the summary to a `CHANGELOG.md` or update the relevant sections of `ARCHITECTURE.md`.
4. This ensures that future agent sessions have access to up-to-date context without needing to re-read the entire codebase.

## Integração Event Horizon
- Ao fim de um `hypothesis-loop-engineer`, promover fatos duráveis de `knowledge.md` para `ARCHITECTURE.md`/docs.
