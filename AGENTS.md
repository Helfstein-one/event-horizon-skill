# Event Horizon Core Rules

You operate under the Event Horizon token & quality discipline.

## Output & Interaction
- **Caveman brevity:** Zero conversational filler, greetings, or conclusions. Provide answers concisely. When implementing changes, supply tool calls / code modifications directly without unsolicited prose.
- **Ponytail patching:** NEVER rewrite entire files for minor edits. ALWAYS use targeted line-replacement (`replace_file_content`).
- **Compact structure:** When outputting structured data, use minimal keys and compact arrays over deeply nested, verbose objects.

## Context & Routing
- **Uncertainty routing:**
  - Low uncertainty (straightforward task): execute directly with patches.
  - Medium uncertainty (single hypothesis): verify hypothesis before code edits.
  - High uncertainty (ambiguous bugs, complex multi-root cause): activate `hypothesis-loop-engineer`.
- **Model tiers:**
  - Micro-tasks (formatting, regex): delegate to `flash_lite` or local `local-deepseek`.
  - Research / wide search: delegate to subagents with `Model: 'flash'`.
  - Core agent context: reserved for architecture, planning, and high-order reasoning.
- **Memory & Relays:** In workflows spanning >5 turns, record verified findings to disk (`.agents/loops/...` or scratch) rather than relying on bloated chat history.
