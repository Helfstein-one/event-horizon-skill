# Flash Subagent Routing (Token Optimization)

**Trigger:** `always_on`

**Directives:**
- When tasked with extensive file searching, codebase research, or reading documentation, DO NOT do it yourself.
- Use `invoke_subagent` to spawn a `research` subagent with `Model: 'flash'`.
- Tell the subagent to summarize the exact details you need and report back.
- Reserve your own context (`pro` model) strictly for execution and planning.
