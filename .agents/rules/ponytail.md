# Ponytail Mode (Patch-Only)

**Trigger:** `always_on`

**Directives:**
- NEVER rewrite entire files for minor changes.
- ALWAYS use `replace_file_content` (or sed/awk patches) for targeted edits.
- Only output the exact lines being changed.
- If a file is large, do not `view_file` the entire content; use slice notation to read only the needed chunk.
