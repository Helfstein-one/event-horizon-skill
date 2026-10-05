---
name: log-tailer
description: Restricts full log viewing, forcing truncated log extraction.
---

# Log Tailer Optimization

**Directives:**
1. NEVER use `view_file` on `.log` files or terminal outputs exceeding 200 lines.
2. ALWAYS use terminal commands like `tail -n 100 file.log` or `grep -C 10 "ERROR" file.log` to fetch only the relevant failing context.
3. If investigating an ongoing issue, use the `rtk` wrapper or standard Unix slicing to prevent blowing up the context window.
