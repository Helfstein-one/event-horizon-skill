---
name: hypothesis-loop-engineer
description: Domain-agnostic CoALA reasoning loop (Hypothesis → Evidence → Confirmation) for any task with high uncertainty — debugging, investigation, research, architecture decisions, performance, incidents, unfamiliar codebases or systems. Orchestrates the other Event Horizon skills as evidence tools, evaluators and memory.
---

# Hypothesis Loop Engineer

Motor de incerteza do Event Horizon. Baseado em **CoALA** (*Cognitive Architectures for Language Agents*): memória modular + ciclo de decisão explícito.

**Princípio:** nenhuma ação relevante é tomada sobre suposição. Toda suposição vira hipótese falsificável, é testada com a evidência mais barata possível e só vira fato após confirmação.

## Quando ativar

Ativado pela regra `uncertainty-router` ou explicitamente. Use quando **qualquer** for verdade:
- A causa, a resposta ou o caminho certo é desconhecido.
- Há ≥2 explicações plausíveis concorrentes.
- `react-protocol` falhou em confirmar uma hipótese 2 vezes seguidas.
- O custo de errar (retrabalho, quebra, decisão irreversível) é alto.

**Não** use para tarefas determinísticas e claras — isso é desperdício.

## Memória (CoALA)

| Memória | Arquivo | Regra |
| :--- | :--- | :--- |
| Working | `.agents/loops/<slug>/board.md` | Hipóteses ativas, status, confiança |
| Episodic | `.agents/loops/<slug>/log.md` | 1 linha por iteração |
| Semantic | `.agents/loops/<slug>/knowledge.md` | Só fatos confirmados, com fonte |
| Procedural | skills + `bin/*` | Ferramentas de evidência (tabela abaixo) |

No início de cada iteração, ler **apenas** `knowledge.md` + `board.md` (não o histórico do chat). Isso implementa `stateless-relay`.

## Ciclo

```text
FRAME → OBSERVE → HYPOTHESIZE → PLAN → POOL → EVALUATE → COMMIT → (loop | EXIT → HANDOFF)
```

1. **FRAME** — Escrever a pergunta central em uma frase e o critério de "resolvido". Ex: *"Por que a latência p95 subiu? Resolvido = causa confirmada + correção validada."*
2. **OBSERVE** — Sinais baratos primeiro (estrutura, assinaturas, últimas linhas de log, métricas agregadas).
3. **HYPOTHESIZE** — 3–7 hipóteses falsificáveis e mutuamente distinguíveis:
   `H<n>: <afirmação> | se V, espero <sinal A> | se F, espero <sinal B> | custo de teste: baixo/médio/alto`
4. **PLAN** — Ordenar por `impacto × incerteza ÷ custo`. Escolher o **teste discriminante**: a evidência que separa o maior número de hipóteses de uma vez.
5. **POOL** — Coleta paralela via `parallel-swarm-orchestrator`: um `Evidence Collector` (persona via `persona-forge`, somente leitura, `flash_lite`/`flash`) por hipótese, num único `invoke_subagent`.
   Contrato: `| H | evidência | tipo | fonte | suporta (S/N/P) |`
6. **EVALUATE** — `Skeptic` (via `adversarial-sparring`; para decisões críticas, `reviewer-council`) tenta refutar.
   - ✅ Confirmada: ≥2 evidências independentes de tipos diferentes, nenhuma contrária, confiança ≥ 0.8
   - ❌ Refutada: contra-evidência direta
   - ⚠️ Inconclusiva: refinar hipótese ou buscar evidência mais discriminante
7. **COMMIT** — Confirmadas → `knowledge.md`. Atualizar `board.md`. 1 linha em `log.md`. Gerar hipóteses derivadas.
8. **EXIT** quando: critério do FRAME atingido | 5 iterações | 2 iterações sem fato novo (→ `ask_question` ao usuário com o board atual).
9. **HANDOFF** — Ver seção de integração.

## Tipos de evidência (agnóstico)

| Tipo | Exemplos | Ferramentas Event Horizon |
| :--- | :--- | :--- |
| Estática | Código, configs, schemas, contratos | `ast-search`, `dependency-compiler`, `scout-librarian`, `schema-dumper` |
| Dinâmica | Executar, reproduzir, teste que falha/passa | `tdd-enforcer`, `run_command` + `rtk` |
| Observacional | Logs, métricas, traces | `log-tailer`, `rtk` |
| Documental | Docs, issues, changelog, web | `living-memory` (docs do projeto), `search_web` |
| Humana | Confirmação do usuário/time | `ask_question` |

Preferir evidência **dinâmica** quando possível: um teste reproduzível vale mais que leitura de código.

## Integração com o pacote

| Skill / Regra | Papel no loop |
| :--- | :--- |
| `uncertainty-router` | Decide quando entrar no loop |
| `react-protocol` | Micro-ciclo de 1 hipótese; escala para este loop após 2 falhas |
| `persona-forge` | Define Evidence Collector, Skeptic, Synthesizer |
| `parallel-swarm-orchestrator` | Executa o POOL |
| `scout-librarian`, `ast-search`, `dependency-compiler`, `schema-dumper`, `log-tailer`, `rtk` | Coleta de evidência barata |
| `tdd-enforcer` | Evidência dinâmica: teste que reproduz = hipótese confirmada |
| `adversarial-sparring`, `reviewer-council` | EVALUATE |
| `stateless-relay` | Memória em arquivo substitui histórico |
| `flash-lite-sandwich`, `local-deepseek-router` | Coletores e classificações baratas |
| `jules-batch-delegator` | Coleta massiva (ex: varrer centenas de arquivos) vai para o Jules |
| `spec-driven-enforcer` | HANDOFF: `knowledge.md` vira base da spec |
| `living-memory` | HANDOFF: fatos duráveis promovidos para `ARCHITECTURE.md`/docs |

## Handoff

Ao sair, gerar `.agents/loops/<slug>/conclusion.md`:
```markdown
## Pergunta
## Resposta (fatos confirmados + confiança)
## Hipóteses refutadas (para não reinvestigar)
## Lacunas abertas
## Próxima ação → [spec-driven-enforcer | tdd-enforcer + ponytail | ask_question]
```

## Economia
- Coletores: somente leitura, ≤10 tool calls, fonte curta (`arquivo:linha`, `métrica@timestamp`), nunca blocos inteiros.
- Fato confirmado nunca é reinvestigado. Hipótese refutada fica registrada.
- Teste discriminante primeiro: elimina várias hipóteses por iteração.
