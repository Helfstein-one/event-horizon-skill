# JSON Structure Optimizer (Schema Minimalism)

**Trigger:** `always_on`

**Directives:**
- When outputting structured data or generating JSON, NEVER use long, verbose keys.
- Use simple flat Arrays or ultra-short keys (e.g., `{"id": 1, "st": "ok"}`) instead of `{"transactionIdentifier": 1, "currentProcessingStatus": "ok"}`.
- Minimize structural overhead (braces, spaces, indentation) when passing data between subagents.
