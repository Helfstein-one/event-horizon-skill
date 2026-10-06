---
name: eval-harness
description: Framework to benchmark and audit agent trajectories, token consumption, and regression testing on real tasks.
---

# Eval Harness (Benchmark & Regression Testing)

Framework para validação empírica de performance e consumo de tokens do agente.

## Como Executar
1. Execute a suíte de avaliação com:
   ```bash
   python3 evals/run_evals.py
   ```
2. Audite a trajetória gravada no transcript:
   - Verifique se chamadas a `view_file` foram evitadas em arquivos brutos.
   - Verifique se patches via `replace_file_content` foram usados em vez de reescrita.
   - Meça a proporção de tokens de entrada/saída gastos por tarefa resolvida.
