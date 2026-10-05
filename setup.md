# ⚙️ Guia de Setup: Event Horizon

Siga este guia para instalar o ambiente otimizado de agentes no seu ecosistema Google Antigravity / Gemini.

## 1. Instalação das Ferramentas CLI (Wrappers)

Os wrappers na pasta `bin/` interceptam comandos pesados e ajudam o modelo a não ler lixo.

1. Copie o conteúdo de `bin/` para o seu diretório binário local:
   ```bash
   cp bin/* ~/.local/bin/
   chmod +x ~/.local/bin/*
   ```
2. Certifique-se de que `~/.local/bin` está no seu `PATH` (ex: no seu `~/.zshrc` ou `~/.bashrc`):
   ```bash
   export PATH="$HOME/.local/bin:$PATH"
   ```

## 2. Configurando Modelos Locais (Zero Custo)

A skill `local-deepseek-router` espera que você tenha um servidor Ollama rodando localmente.

1. Instale o Ollama (se não tiver): `brew install ollama`
2. Baixe o modelo recomendado para tarefas de código:
   ```bash
   ollama run deepseek-coder:6.7b
   ```
3. Mantenha o serviço do Ollama rodando na porta padrão (`http://localhost:11434`). Os agentes passarão a rotear micro-tarefas de formatação silenciosamente para ele via o comando `local-deepseek`.

## 3. Integrando Jules AI via MCP

Para usar a skill `jules-batch-delegator`, você precisa ter o MCP configurado no Antigravity.

1. Edite o arquivo `~/.gemini/config/mcp_config.json`:
   ```json
   {
     "mcpServers": {
       "google-jules": {
         "serverUrl": "http://127.0.0.1:3323/mcp"
       }
     }
   }
   ```
2. Inicie o servidor Jules-MCP localmente. A partir desse momento, pedir "Refatore 50 arquivos" não travará seu terminal. O agente criará uma sessão remota.

## 4. Instalando Regras e Skills (Antigravity Global)

O Antigravity lê nativamente o diretório `~/.gemini/config/` para aplicar as suas restrições e habilidades.

1. Copie as regras e a diretriz Caveman para a configuração global:
   ```bash
   cp AGENTS.md ~/.gemini/config/
   cp -r .agents/rules/* ~/.gemini/config/.agents/rules/
   ```
2. Copie as habilidades cognitivas (Skills):
   ```bash
   cp -r .agents/skills/* ~/.gemini/config/.agents/skills/
   ```
3. **Reinicie seu Antigravity IDE ou CLI.** Todas as proteções (Ponytail, TDD Enforcer, Log Tailer, SDD) estarão armadas e operantes.
