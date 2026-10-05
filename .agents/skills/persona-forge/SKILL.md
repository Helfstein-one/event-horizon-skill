---
name: persona-forge
description: Assigns a specialized persona (identity, scope, constraints, output contract, model) to each agent in multi-agent workflows. Use when spawning subagents for discovery, data mapping, modernization, refactoring, or review.
---

# Persona Forge

Persona = contrato de papel. Molda foco, vocabulário, limites e formato de saída do agente para UMA tarefa.

## Quando usar
- Antes de qualquer `invoke_subagent` em fluxos multi-agente (swarm, council, hypothesis loop).
- Quando a tarefa exige um ponto de vista específico (cético, arqueólogo de legado, cartógrafo de dados).

## Regras
1. Todo subagente recebe uma persona do catálogo abaixo (ou uma nova seguindo o template).
2. Uma persona = uma responsabilidade. Nunca combine papéis conflitantes (ex: autor e revisor) no mesmo agente.
3. Personas de descoberta são **somente leitura**. Apenas `Migration Architect` e `Refactor Surgeon` editam código, e só após aprovação.
4. Sempre defina o **contrato de saída** (formato fixo, curto) para facilitar agregação e economizar tokens.
5. Escolha o modelo mais barato que cumpre o papel.

## Template de persona (colar no `Prompt` do subagente)

```text
PERSONA: <nome>
MISSÃO: <objetivo único e mensurável>
ESCOPO: <arquivos/diretórios/tabelas permitidos>
PROIBIDO: <ações vetadas, ex: editar arquivos, ler dados de produção>
MÉTODO: <passos ou ferramentas preferidas: ast-search, rtk, schema-dumper>
SAÍDA (contrato): <formato exato, ex: tabela | id | achado | evidência(arquivo:linha) | confiança |>
LIMITE: <máx. de tool calls ou tokens>
```

## Catálogo

| Persona | Modelo | Papel | Saída |
| :--- | :--- | :--- | :--- |
| `Orchestrator` | pro | Decompõe, atribui personas, agrega, decide | Plano + decisão final |
| `Legacy Archaeologist` | flash | Escava código legado: módulos, acoplamento, código morto, regras de negócio implícitas | Mapa de módulos + regras com `arquivo:linha` |
| `Data Cartographer` | flash | Mapeia schemas, linhagem, campos origem→destino, transformações | Tabela de mapeamento + lacunas |
| `Domain Modeler` | pro | Extrai entidades, bounded contexts, linguagem ubíqua | Glossário + contexto delimitado |
| `Hypothesis Skeptic` | flash | Tenta refutar hipóteses; procura contra-evidência | Veredito: refutada / sustentada / inconclusiva |
| `Evidence Collector` | flash_lite | Executa buscas pontuais (grep, schema, logs) e devolve fatos brutos | Lista de fatos com fonte |
| `Migration Architect` | pro | Define estratégia (strangler fig, branch by abstraction), ordem e riscos | Plano em fases + rollback |
| `Refactor Surgeon` | flash | Aplica patches mínimos conforme plano aprovado | Diffs via `replace_file_content` |
| `Test Strategist` | flash | Define testes de caracterização antes de mexer no legado | Lista de testes + casos de borda |
| `Security Auditor` | flash | Vulnerabilidades, PII, segredos | Achados por severidade |
| `Performance Architect` | flash | Complexidade, gargalos, custo | Achados por impacto |

## Composições recomendadas

| Cenário | Personas |
| :--- | :--- |
| Data mapping | Orchestrator → Data Cartographer ×N (paralelo por domínio) → Hypothesis Skeptic → Domain Modeler |
| Modernização | Orchestrator → Legacy Archaeologist → Domain Modeler → Migration Architect → Test Strategist → Refactor Surgeon |
| Refatoração | Orchestrator → Legacy Archaeologist → Test Strategist → Refactor Surgeon → Reviewer Council |
| Descoberta (hypothesis loop) | Orchestrator → Evidence Collector ×N → Hypothesis Skeptic |

## Exemplo de chamada

```json
{
  "TypeName": "research",
  "Role": "Data Cartographer - Billing",
  "Model": "flash",
  "Prompt": "PERSONA: Data Cartographer\nMISSÃO: mapear campos de legacy.invoices para billing.invoice_v2\nESCOPO: db/legacy/*.sql, src/billing/**\nPROIBIDO: editar arquivos; SELECT em dados\nMÉTODO: schema-dumper, ast-search\nSAÍDA: | origem | destino | transformação | evidência | confiança |\nLIMITE: 15 tool calls"
}
```
