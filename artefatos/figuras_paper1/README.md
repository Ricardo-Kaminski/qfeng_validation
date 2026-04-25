# figuras_paper1 — Diagramas conceituais para o Paper 1 Q-FENG

**Criado:** 24/abr/2026 **Última atualização:** 24/abr/2026 (sessão 2) **Propósito:** Centralizar os diagramas conceituais para inserção na revisão pós-auditoria do Paper 1 Q-FENG (validação empírica), mantendo procedência clara para depósito Zenodo/SSRN/arXiv.

## Estrutura

### Originais (mantidos para referência)

`Diagram*.svg/png` (origem: Working Paper arXiv abr/2026)

Origem canônica: `D:\OneDrive\Documentos\- Pós-Doc Q-FENG\Artigos\Onda 1 - Working Paper arXiv (abr 2026)\`

### Versões limpas (`*_clean.svg`)

Geradas pelo script `_clean_diagrams.py`. Operações aplicadas:

1. **dPASP → Clingo (ASP)** em 8 arquivos (13 substituições totais)
2. **Remoção de títulos gravados** ("Figure N. ...", "Figura N. ...") em 11 SVGs
3. **Remoção de captions de rodapé** em 14 SVGs (41 captions removidas)

A separação é importante: o paper insere via caption do .docx (`<text class="caption">` no .docx style), portanto NÃO deve haver título/legenda gravados na imagem.

### Versão estendida custom (`Diagram2_QFENG_Engineering_v2.svg`)

Gerada pelo script `_gen_v2.py`. Estende o `Diagram2_QFENG_Engineering.svg` original (ou seu `_clean.svg`) com:

1. **S1 generalizado**: "Neural / ML predictor" com nota técnica indicando exemplos (LSTM Manaus SIH, LightGBM CEAF, GPT, time-series, ensemble)
2. **S5 com Clingo (ASP) solver** (não dPASP)
3. **Ontological Feature Store estendido** com fórmula explícita `L_Global = L_Perf + lambda . max(0, -cos theta)` (Eq. 11) e indicação do gradiente de retreinamento para S1
4. **Markovian horizon of possible worlds** (faixa inferior nova)
   - Sovereign anchor omega\* (w -&gt; +infinity)
   - 2 mundos compliant orbit (P high)
   - 2 mundos HITL zone (P mid)
   - 2 mundos suppressed (P -&gt; 0, dashed)
   - Setas de probabilidade com espessura proporcional
   - Trajectory theta_eff(t) sobre o horizonte (Eq. 5)
5. **SEM títulos, captions ou legendas internas** — todas vão para caption do .docx

PNG associado: `Diagram2_QFENG_Engineering_v2.png` (1400px wide, \~140 KB)

### Auxiliares

`auxiliares_govern_ai_paper/` — origem livro Kaminski 2026a (em português, não inseridas no Paper 1 mas mantidas para consulta) `auxiliares_livro/` — origem pasta livro/ do govern_ai_paper (idem, em português)

## Mapa de inserção no Paper 1 (recomendação Via C++)

#StatusDiagramaLocalStatusD1★★★Diagram2_QFENG_Engineering_v2.svg§1 Introduction**PRONTO** (este arquivo)D2★★★Diagram4_Fractal_VSM_clean.svg§2.7 VSM_clean PRONTOD3★★★Diagram1_Interference_Regimes_clean.svg§3.1 antes Tab 1_clean PRONTOD4★★★Diagram3_Loss_Landscape_clean.svg§3.4 após Eq.11_clean PRONTOD5★★★Diagram8_Manaus_Timeline_clean.svg§5.3 após Fig 3_clean PRONTOD6★★FiguraA8 (auxiliar, requer re-rotular PT-&gt;EN)§3.2 após Eq.5requer pre-processD7★★Diagram6_Neurosymbolic_Thermo_clean.svg§4.4 E4 HITL_clean PRONTOD8★★Diagram9_Equity_Map_clean.svg§5.2 C3 narrative_clean PRONTO

## Operações pendentes para inserção no .docx

1. Conversão SVG -&gt; PNG 300dpi (para embedding no Word)
2. Re-rotulagem PT-&gt;EN da FiguraA8 (caso D6 seja adotado)
3. Inserção no .docx via python-docx no Claude Code com:
   - Ancoragem por frase exata (mapa em DIAGRAM_INSERTION_PROSE.md, sessão anterior)
   - Caption em estilo Caption do Word
   - Prosa de conexão antes/depois conforme tabela final

## Scripts utilitários (este diretório)

- `_clean_diagrams.py` — auditor + cleaner (dPASP, títulos, captions)
- `_gen_v2.py` — gerador do Diagram2 v2 estendido
- `_render_v2.py` — renderizador SVG -&gt; PNG via cairosvg
- `_diag.py` — diagnóstico de bytes/encoding (debug)

## Verificação de integridade

26 arquivos originais copiados em 24/abr/2026 (MD5 verificado contra origem)

- 16 arquivos `_clean.svg` gerados localmente
- 1 arquivo `_v2.svg` gerado localmente (Diagram2 estendido)
- 1 PNG de validação visual

## Notas operacionais

- **MCP** `write_file` **corrompe arquivos longos**: contornar gerando o conteúdo dentro de Python script no disco que faz `Path.write_text()` (método validado)
- **Originais preservados**: NUNCA sobrescrever os Diagram\*.svg originais — sempre operar sobre `_clean.svg` ou criar `_v2.svg`
- **Esta pasta NÃO entra no Zenodo**: workspace interno; versões finais para publicação ficarão em `docs/papers/figuras_paper1_final/` antes do build PDF
