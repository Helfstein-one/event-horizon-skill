---
name: jules-batch-delegator
description: Delegates heavy, asynchronous, and batch tasks to Jules AI via the local MCP server.
---

# Jules Batch Delegator (MCP Integration)

**Trigger:** `always_on`

**Directives:**
1. You have access to Jules AI via the Model Context Protocol (MCP) server running locally.
2. When the user requests heavy, asynchronous, or mass-refactoring tasks (e.g., "document all files," "migrate the entire codebase to v2," "audit the whole project for security issues"), DO NOT process this synchronously in the current context.
3. Instead, delegate the workload to Jules AI.
4. Execute the tool `jules_create_session` (provided by the `google-jules` MCP integration) to create an asynchronous working session.
5. Provide a highly detailed prompt/title in the session payload, including references to specific files or directories Jules should focus on.
6. Once the session is spawned, inform the user that Jules is working on the task in the background, effectively saving tokens and synchronous compute time on your end.

## Integração Event Horizon
- Coleta de evidência massiva no `hypothesis-loop-engineer` (ex: varrer centenas de arquivos) pode ser delegada ao Jules.
