# Uncertainty Router

**Trigger:** `always_on`

Antes de agir, classifique a incerteza da tarefa e escolha o modo:

| Nível | Sinal | Modo |
| :--- | :--- | :--- |
| Baixa | Caminho claro, determinístico | Agir direto (patch via `ponytail`) |
| Média | 1 hipótese principal a verificar | `react-protocol` (Thought → ação → verificação) |
| Alta | Causa/caminho desconhecido, ≥2 explicações, ou erro caro | `hypothesis-loop-engineer` |
| Requisito ambíguo | Não se sabe *o que* construir | `ask_question` → `spec-driven-enforcer` |

Escalada: se `react-protocol` falhar 2 vezes, escalar para `hypothesis-loop-engineer`.
Nunca use o loop para tarefas de baixa incerteza.
