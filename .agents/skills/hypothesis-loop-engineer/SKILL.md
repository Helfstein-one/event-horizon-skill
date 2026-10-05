---
name: hypothesis-loop-engineer
description: CoALA-based discovery loop (Hypothesis → Evidence → Confirmation) with pooled parallel evidence collectors. Use for discovery, data mapping, legacy modernization, and refactoring where the system is not yet understood.
---

# Hypothesis Loop Engineer (CoALA Discovery Loop)

Ciclo de descoberta baseado em **CoALA** (Cognitive Architectures for Language Agents): memória modular + ciclo de decisão explícito. Substitui "ler tudo e adivinhar" por **hipóteses testáveis confirmadas por evidência**.

## Quando usar
- Discovery de sistema legado desconhecido.
- Data mapping (origem → destino, linhagem, regras de transformação).
- Modernização / refatoração (fronteiras de módulos, acoplamento, código morto).
- Qualquer tarefa onde a resposta certa depende de fatos ainda não verificados.

## Memória (CoALA)

| Memória | Onde | Conteúdo |
| :--- | :--- | :--- |
| Working | `.agents/discovery/<tema>/board.md` | Hipóteses ativas, status, confiança |
| Episodic | `.agents/discovery/<tema>/loop-log.md` | Uma linha por iteração: o que foi testado e o resultado |
| Semantic | `.agents/discovery/<tema>/knowledge.md` | Fatos **confirmados** (com fonte). Só entra aqui o que passou na confirmação |
| Procedural | `.agents/skills/*`, `bin/*` | Como coletar evidência: `ast-search`, `rtk`, `schema-dumper`, `log-tailer` |

> Ler `knowledge.md` + `board.md` no início de cada iteração. **Não** reler o histórico do chat (compatível com `stateless-relay`).

## Ciclo de decisão

```text
OBSERVE → HYPOTHESIZE → PLAN → POOL (coleta paralela) → EVALUATE → COMMIT MEMORY → (loop | exit)
```

1. **OBSERVE** — Ler memória semântica e board. Coletar sinais iniciais baratos (estrutura de diretórios, `ast-search`, schema).
2. **HYPOTHESIZE** — Gerar 3–7 hipóteses **falsificáveis**. Formato: `H<n>: <afirmação> | se verdadeira, espero ver <evidência X> | se falsa, espero ver <Y>`.
3. **PLAN** — Para cada hipótese, definir a evidência mínima e a ferramenta. Priorizar por `impacto × incerteza`.
4. **POOL** — Disparar em **um único** `invoke_subagent` um pool de `Evidence Collector` (`flash_lite`/`flash`, somente leitura), uma hipótese por worker. Persona via `persona-forge`. Contrato de saída:
   `| H | evidência | fonte(arquivo:linha / tabela.coluna / log) | suporta? (sim/não/parcial) |`
5. **EVALUATE** — Enviar evidências ao `Hypothesis Skeptic`, que tenta refutar. Classificar:
   - ✅ **Confirmada** — ≥2 evidências independentes, nenhuma contra, confiança ≥ 0.8
   - ❌ **Refutada** — evidência contrária direta
   - ⚠️ **Inconclusiva** — refinar hipótese ou pedir evidência mais específica
6. **COMMIT MEMORY** — Confirmadas → `knowledge.md`. Atualizar `board.md`. Anexar 1 linha em `loop-log.md`. Gerar novas hipóteses derivadas.
7. **EXIT** quando qualquer um:
   - Todas as hipóteses críticas confirmadas/refutadas;
   - Máximo de **5 iterações**;
   - Duas iterações seguidas sem novo fato confirmado (estagnação) → perguntar ao usuário.

## Formato do board

```markdown
| ID | Hipótese | Evidência esperada | Status | Conf. | Fontes |
| :- | :------- | :----------------- | :----- | :---: | :----- |
| H1 | `customer.status` legado mapeia para `account.state` | CASE em proc `sp_sync` | ✅ | 0.9 | sp_sync.sql:42, etl/map.py:17 |
| H2 | Módulo `billing` não depende de `crm` | sem imports cruzados | ❌ | — | billing/api.ts:8 importa crm |
```

## Modos de aplicação

### Data mapping
- Hipóteses típicas: correspondência de campos, regras de transformação, chaves de junção, cardinalidade, campos órfãos, PII.
- Evidência: `schema-dumper`, SQL de procedures/ETL, código de serialização, contagens agregadas (nunca linhas brutas).
- Entregável: `mapping.md` com `| origem | destino | transformação | regra | evidência | confiança |` + lista de lacunas.

### Modernização
- Hipóteses típicas: fronteiras de bounded context, módulos isoláveis (candidatos a strangler fig), código morto, regras de negócio escondidas.
- Evidência: grafo de imports (`ast-search`), rotas/entrypoints, logs de uso (`log-tailer`), testes existentes.
- Entregável: mapa de módulos + ordem de extração + riscos → entrada para `Migration Architect`.

### Refatoração
- Hipóteses típicas: "função X tem efeitos colaterais em Y", "dá para extrair interface Z sem quebrar chamadores".
- Evidência: `scout-librarian` (impact map), testes de caracterização (`tdd-enforcer`).
- Entregável: plano de patches confirmado → `Refactor Surgeon`.

## Regras de economia
- Coletores são **somente leitura** e com limite de tool calls (≤10).
- Evidência sempre com fonte curta (`arquivo:linha`), nunca blocos de código inteiros.
- Hipótese confirmada nunca é re-investigada; vive em `knowledge.md`.
- Use `json-optimizer` / tabelas compactas entre agentes.
