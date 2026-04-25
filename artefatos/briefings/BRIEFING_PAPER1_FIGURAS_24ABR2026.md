# Briefing-ponte — Sessão Q-FENG Paper 1 figuras (24/abr/2026)

**De:** Sessão atual (24/abr/2026, claude.ai)
**Para:** Próxima sessão (continuação ou nova)
**Tema:** Diagramas conceituais para inserção no Paper 1 Q-FENG (validação empírica), em revisão pós-auditoria, em vias de submissão a Zenodo + SSRN + arXiv (cs.AI cross-list cs.CY) + Internet Policy Review como primeira tentativa de revista diamond OA.

---

## 1. Estado consolidado dos artefatos

**Diretório-base:** `C:\Workspace\academico\qfeng_validacao\artefatos\figuras_paper1\`

### 1.1 Arquivos prontos para inserção no .docx

| Sufixo | Quantidade | Estado | Ação pendente |
|--------|------------|--------|---------------|
| `Diagram*.svg` (originais) | 11 + 2 PNG | preservados, NÃO modificar | — |
| `*_clean.svg` | 16 | dPASP→Clingo (ASP), títulos/captions removidos | converter para PNG 300dpi |
| `Diagram2_QFENG_Engineering_v2.svg` | 1 | versão estendida com OFS+L_Global+Markovian horizon, S1 generalizado, S3* label centralizado | já pronto + PNG validado |
| `auxiliares_govern_ai_paper/*.svg` | 7 | em português, redundância com Diagram*.svg em ~5 casos | só FiguraA8 candidata se Via C++ (re-rotulagem PT→EN) |
| `auxiliares_livro/*.svg` | 6 | em português, redundância com Diagram*.svg | não usar no Paper 1 |

### 1.2 Decisão Via C++ (8 diagramas) — confirmada

| # | Status | Arquivo a usar | Local exato no paper |
|---|--------|----------------|---------------------|
| D1 | ★★★ | `Diagram2_QFENG_Engineering_v2.svg` (PRONTO) | §1 Introduction, antes da enumeração das 3 contribuições originais |
| D2 | ★★★ | `Diagram4_Fractal_VSM_clean.svg` | §2.7 VSM, após parágrafo "Mapping the full Q-FENG C1 architecture..." |
| D3 | ★★★ | `Diagram1_Interference_Regimes_clean.svg` | §3.1, antes da Tabela 1 |
| D4 | ★★★ | `Diagram3_Loss_Landscape_clean.svg` | §3.4, após Eq. (11) |
| D5 | ★★★ | `Diagram8_Manaus_Timeline_clean.svg` | §5.3, após Figure 3 (θ_eff trajectory) |
| D6 | ★★ | `auxiliares_govern_ai_paper/FiguraA8_Theta_Instantaneo_vs_Efetivo.svg` | §3.2, após Eq. (5) — REQUER re-rotulagem PT→EN |
| D7 | ★★ | `Diagram6_Neurosymbolic_Thermo_clean.svg` | §4.4 E4 HITL, após parágrafo SOVEREIGN/ELASTIC |
| D8 | ★★ | `Diagram9_Equity_Map_clean.svg` | §5.2 C3 Regional SUS Concentration |

### 1.3 Diagramas NÃO usar no Paper 1

- `Diagram5_MLOps_Pipeline.svg` → reservar para Paper 2 (JURIX 2026) ou paper de deployment
- `Diagram7_Triadic_Tension.svg` → pertence ao livro Kaminski 2026a
- `Diagram10_Comparative_Table.svg` → conteúdo melhor expresso como Tabela 9 em prosa
- `Diagram11_Sidecar_Deploy.svg` → engenharia de deployment, escopo de outro paper

---

## 2. Prosa de conexão e captions já produzidas

A sessão anterior produziu, para cada inserção D1–D5 + Bn-1/Bn-2 (= D7/D8 atuais), o pacote completo de:

1. **Frase-âncora exata** (literal) para localizar o ponto de inserção no .docx
2. **Texto NOVO a inserir ANTES** da imagem (parágrafo de conexão)
3. **Caption** (texto da legenda)
4. **Texto NOVO a inserir DEPOIS** da imagem (payoff, quando aplicável)

Esse material está disperso na conversa anterior, mas o resumo operacional é a tabela na seção 1.2 acima. **Para a próxima sessão**, recomenda-se que o Claude Code receba como anexo um arquivo `DIAGRAM_INSERTION_PROSE.md` consolidado com os 5 blocos completos. Se ainda não foi gerado, gerar antes de invocar o Code.

---

## 3. Scripts utilitários neste diretório (todos validados)

| Script | Função | Como rodar |
|--------|--------|------------|
| `_clean_diagrams.py` | Remove dPASP, títulos "Figure N.", captions de rodapé. Preserva originais, gera `_clean.svg`. | `python _clean_diagrams.py` |
| `_gen_v2.py` | Gera o `Diagram2_QFENG_Engineering_v2.svg` (versão custom estendida) | `python _gen_v2.py` |
| `_render_v2.py` | Renderiza SVG v2 → PNG 1400px wide via cairosvg | `python _render_v2.py` |
| `_fix_s3_label.py` | Patch posicional do label S3* (centralizado, sem sobreposição) | já aplicado |
| `_diag.py` | Diagnóstico de bytes/encoding do SVG (debug) | `python _diag.py` |

---

## 4. Bug crítico do Desktop Commander (PERSISTENTE)

**Sintoma:** Chamadas a `write_file` com `content` longo (>~5KB) ou contendo aspas/ângulos pesados resultam em arquivos corrompidos no disco — o tool reporta "X linhas escritas" mas o arquivo fica com 1-7 bytes inválidos. Já registrado em memória persistente.

**Contorno validado:**
1. Escrever um SCRIPT PYTHON via `write_file` (texto simples, poucas linhas)
2. O script Python contém o conteúdo real em uma triple-quoted string
3. O script faz `Path(...).write_text(CONTENT, encoding="utf-8")`
4. Executar o script via `start_process` com `python <caminho.py>`

**Aplica-se a:** SVG longos, .docx XML interno, JSON grande, qualquer texto >5KB.
**NÃO aplica-se a:** scripts Python curtos com texto simples (funcionam normalmente).

**Outras armadilhas conhecidas (já registradas em memória):**
- REPL `python -i` interativo quebra em comandos multi-linha (try/except, for, def)
  → usar scripts no disco, não REPL interativo
- PowerShell com aspas duplas internas é embrulhado pelo wrapper MCP e quebra
  → usar Python script no disco
- `findstr` (Windows) substitui `grep` para buscas rápidas
- `fileWriteLineLimit` foi elevado para 500 (default era 50)

---

## 5. Próximos passos (em ordem)

### 5.1 Imediato (próxima sessão chat)

1. **Gerar `DIAGRAM_INSERTION_PROSE.md`** consolidando os 5 blocos completos (âncora + prosa antes + caption + prosa depois) para D1–D5, e os 2 blocos para D7/D8.
2. **Re-rotulagem da FiguraA8 PT→EN** (caso D6 entre na inserção): traduzir os textos internos "Tempo (τ)", "Zona HITL", "Circuit Breaker (120°)" para "Time (τ)", "HITL zone", "Circuit Breaker (120°)" — cuidadosamente preservando posicionamento.
3. **Conversão SVG → PNG 300dpi** dos 8 SVGs selecionados, padronizada via cairosvg.

### 5.2 Para o Claude Code (sessão local de execução)

Prompt sugerido a passar ao Code:

```
TAREFA: Inserir 8 diagramas conceituais (Diagrams 1–8) no .docx do Paper 1 Q-FENG,
preservando integralmente a numeração de Figures 1–7, Tables 1–8, Equações (1)–(11)
e bibliografia.

ARQUIVO-FONTE:
  C:\Workspace\academico\qfeng_validacao\docs\papers\
      PAPER1_QFENG_FINAL_prob_dados_clingo_auditfixed - Copia.docx

ARQUIVO-SAÍDA:
  C:\Workspace\academico\qfeng_validacao\docs\papers\
      PAPER1_QFENG_FINAL_withDiagrams.docx

PASTA DE FIGURAS:
  C:\Workspace\academico\qfeng_validacao\artefatos\figuras_paper1\

INSTRUÇÕES DETALHADAS:
  C:\Workspace\academico\qfeng_validacao\artefatos\briefings\
      DIAGRAM_INSERTION_PROSE.md  (a ser criado na próxima sessão)

PASSOS:
1. Pré-processar SVGs:
   - Para os 7 _clean.svg: converter para PNG 300dpi via cairosvg
   - Para o Diagram2_v2.svg: já tem PNG pronto, usar
   - Para FiguraA8: aplicar tradução PT→EN antes de converter

2. Inserir no .docx via python-docx:
   - Localizar parágrafo-âncora (frase exata em DIAGRAM_INSERTION_PROSE.md)
   - Inserir parágrafo de prosa de conexão (texto NOVO ANTES)
   - Inserir imagem PNG (largura ~6.5 polegadas)
   - Inserir caption em estilo Caption do Word
   - Inserir parágrafo de payoff (texto NOVO DEPOIS), quando especificado

3. Validar:
   - 7 Figures originais permanecem com numeração intacta
   - 8 Diagrams aparecem na ordem correta
   - Tables 1–8 intactas
   - Equações (1)–(11) intactas
   - Bibliografia intacta
   - Documento abre sem erros no Word
   - Tamanho final < 8MB (reduzir DPI se necessário)
```

### 5.3 Submissão (após inserção)

1. **Zenodo:** depósito imediato (DOI em segundos), licença CC BY 4.0 para o texto, comunidade EU Open Research Repository
2. **SSRN:** depósito com DOI Zenodo no rodapé do PDF (1-3 semanas de fila)
3. **arXiv:** registrar conta com email institucional `@pucpr.br`, iniciar submissão para obter código de endosso, enviar email a Lamb (rascunho pronto da sessão atual, em português, formato salvo na conversa)
4. **Internet Policy Review:** primeira submissão a revista indexada com IF 4.35, Q1, ZERO APC (diamond OA), Humboldt Institute Berlin

---

## 6. Verificações externas concluídas (Phase 0 audit)

- **F0-1 TST-RR-000200-50.2019.5.02.0020:** NÃO EXISTE. Numeração inconsistente com padrão CNJ pós-2008. Substituir por `TST-Ag-RR-868-65.2021.5.13.0030` (DEJT 06/12/2023, 2ª Turma, validade CCT à luz do Tema 1046/STF), ou reformular T-CLT-04 como controle sintético explícito.
- **F0-2 Portaria GM/MS 268/2021:** ERRO. A única Portaria nº 268/2021 do MS é a SE nº 268, de 29/06/2021, sobre metas institucionais — sem relação com Manaus. Substituir por: Lei 13.979/2020 Art. 3º VII + Art. 10 + Decreto AM 43.303/2021 + Portaria GM/MS 79/2021 (ampliação Mais Médicos para Manaus em 18/jan/2021).

Resultado registrado em `AUDIT_PHASE0_LOG.md` (sessão anterior).

---

## 7. Lições registradas em memória persistente (para evitar reincidência)

- Autorização padrão para operações de filesystem nos projetos acadêmicos (sem confirmação repetida)
- Bug write_file Desktop Commander para conteúdo longo + contorno validado
- Desktop Commander é ferramenta padrão de PRIMEIRA escolha para acesso a arquivos locais
- Acesso completo ao filesystem local via MCP no Claude.ai desktop app

---

## 8. Estado emocional/operacional

- Paper em revisão pós-auditoria, ainda sendo editado pelo Claude Code (mudanças nos dados, não nos diagramas conceituais)
- Deadline DSSGx Munich 2026 (24/abr) já passou — paper não foi finalizado a tempo dessa janela
- Próximas janelas: JURIX 2026 (Toulouse, ~setembro/2026) para Paper 2 (labour-law); IEEE CAI 2026 (Granada, 8-10/maio) como ponto de networking UGR/DaSCI
- Estratégia de outreach: Lamb (UFRGS) → d'Avila Garcez (City StG, UK) → Belle (Edinburgh) — emails redigidos na sessão atual, prontos para envio assim que código de endosso arXiv estiver em mãos

---

**Fim do briefing.** Ao iniciar a próxima sessão, abrir este arquivo e o README.md de figuras_paper1/.


---

## 9. CORREÇÃO IMPORTANTE — `DIAGRAM_INSERTION_PROSE.md` parcialmente pronto

Verificado em 24/abr/2026 às 20:58: o arquivo
`artefatos/briefings/DIAGRAM_INSERTION_PROSE.md` (4891 bytes, criado às 09:51 do
mesmo dia) JÁ CONTÉM os 5 blocos de prosa de conexão para D1–D5 (INS-1 a INS-5).

O que ESTÁ pronto:
- INS-1 a INS-5: parágrafo de prosa de conexão (texto que vai DEPOIS do parágrafo-
  âncora e ANTES do Diagram correspondente)
- Cada bloco identifica a frase-âncora pelo seu início (ex.: "This paper presents
  the Q-FENG C1 pipeline")

O que FALTA acrescentar antes da inserção via Claude Code:
- Frase-âncora COMPLETA e LITERAL (não só os primeiros termos) para uso com
  python-docx find/replace
- Caption (texto da legenda) para cada um dos 5+2 diagramas
- Texto de payoff (parágrafo a inserir DEPOIS do diagrama, quando aplicável —
  pelo menos para D2, D4 e D5)
- Blocos completos para D7 (Bn-1, Diagram6_Neurosymbolic_Thermo) e
  D8 (Bn-2, Diagram9_Equity_Map) — atualmente ausentes

Recomendação para a próxima sessão:
1. Abrir DIAGRAM_INSERTION_PROSE.md
2. Para cada bloco D1–D5: adicionar a frase-âncora literal (extraível de
  paper_dump.md no mesmo diretório), a caption, e o payoff
3. Adicionar blocos novos para D7 e D8
4. Validar contra o paper_dump.md que cada frase-âncora aparece UMA SÓ VEZ no
  paper (requisito do find/replace via python-docx)

Antes de iniciar, confirmar com Ricardo se a Via C++ (8 diagramas) ainda é a
escolhida ou se ele opta pela Via C+ (7) ou Via Mínima (5).
