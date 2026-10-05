---
name: react-protocol
description: Forces Reason+Act loop for complex logical problems to prevent impulsive code generation.
---

# ReAct Protocol Enforcer

**Trigger:** `always_on`

**Directives:**
1. When facing a complex debugging session or architecture decision, you MUST output a `Thought:` block before taking any action.
2. In the `Thought:` block, explicitly state your hypothesis, what you need to verify, and what tool you will use next.
3. NEVER generate implementation code impulsively without verifying your hypothesis first.

## Integração Event Horizon
- Micro-ciclo de 1 hipótese. Se a hipótese falhar 2 vezes, escalar para `hypothesis-loop-engineer` (ver regra `uncertainty-router`).
