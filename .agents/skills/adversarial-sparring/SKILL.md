---
name: adversarial-sparring
description: Forces self-auditing through subagent red-teaming.
---

# Adversarial Sparring (Red-Teaming)

**Directives:**
1. When generating critical logic, algorithms, or complex refactors, DO NOT present the first draft directly to the user.
2. Call `invoke_subagent` with `Role: 'Code Reviewer/Red-Teamer'` and `Model: 'flash'`.
3. Provide the subagent with the code and instruct it to fiercely audit it for bugs, edge cases, and security flaws.
4. Incorporate the subagent's fixes before writing the final output via `replace_file_content`.

## Integração Event Horizon
- Atua como `Skeptic` no passo EVALUATE do `hypothesis-loop-engineer`.
