---
name: parallel-swarm-orchestrator
description: Detects parallelizable tasks and deploys a swarm of concurrent subagents.
---

# Parallel Swarm Orchestrator

**Trigger:** `always_on`

**Directives:**
1. Upon receiving a batch request (e.g., "Refactor these 5 files", "Write unit tests for these 10 components", "Summarize these 8 logs"), DO NOT process them sequentially.
2. Analyze the task for independence. If the tasks do not strictly depend on the output of one another, they are parallelizable.
3. Act as the **Orchestrator**. Use the `invoke_subagent` tool and pass an array of multiple subagents in a single tool call to launch them concurrently.
4. Assign `Model: 'flash'` to the worker subagents to save cost and speed up execution.
5. Wait for all subagents to report back via messages, aggregate their work, and present the final unified output.

## Integração Event Horizon
- Executa o passo POOL do `hypothesis-loop-engineer` (1 Evidence Collector por hipótese).
- Toda subagente recebe persona via `persona-forge`.
