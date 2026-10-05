---
name: reviewer-council
description: Spawns a council of specialized subagents to review critical code concurrently.
---

# Reviewer Council (Multi-Agent Consensus)

**Directives:**
1. When a highly critical piece of architecture or security logic is implemented, a single reviewer is not enough.
2. Spawn at least two specialized concurrent subagents:
   - Subagent A (`Role: 'Security Auditor'`): Focuses strictly on vulnerabilities and edge cases.
   - Subagent B (`Role: 'Performance/Logic Architect'`): Focuses strictly on Big O complexity, token-efficiency, and clean code.
3. Wait for both agents to report back. Resolve any conflicting feedback before finalizing the implementation.

## Integração Event Horizon
- Usado no EVALUATE do `hypothesis-loop-engineer` para conclusões críticas/irreversíveis.
- Cada revisor recebe persona `Reviewer` com uma lente distinta (`persona-forge`).
