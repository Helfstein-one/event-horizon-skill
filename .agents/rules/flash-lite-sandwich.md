# Flash-Lite Sandwich (Micro-Routing)

**Trigger:** `always_on`

**Directives:**
- NEVER use the `pro` model for trivial formatting, simple parsing, regex generation, or basic text extraction.
- ALWAYS delegate micro-tasks to a subagent using `Model: 'flash_lite'`.
- Use `Model: 'flash'` for reading large contexts or summarizing.
- Reserve your own context (`pro`) strictly for complex logical reasoning and architecture decisions.
