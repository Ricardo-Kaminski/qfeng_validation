# BRIEFING DIAGNÓSTICO — Desalinhamento de figuras no Paper 1 Q-FENG

**Data:** 23 abr 2026
**Sessão:** Claude Opus 4.7 no Claude Desktop, projeto "Validação Q-FENG"
**Propósito:** Diagnóstico completo do desalinhamento entre legendas no `.md`, arquivos `.png` em disco e placeholders no DOCX. Ponte para a próxima sessão (Claude Code ou Opus 4.7 no chat) executar a reconciliação.
**Arquivo canônico do paper:** `docs/papers/PAPER1_QFENG_VALIDATION.md`

---

## 1. Problema identificado

O Paper 1 do Q-FENG tem **três gerações sobrepostas de figuras** que nunca foram reconciliadas:

1. **Geração 1** (antes de 19/04) — paper tinha 4 figuras planejadas; paths em `docs/figuras/fig1_theta_by_scenario.png` até `fig7_obermeyer_calibration.png` (algumas nunca criadas).
2. **Geração 2** (21/04) — sessão gerou F2-F7 em `outputs/figures/` com nova numeração e nova narrativa.
3. **Geração 3** (22/04 03:43) — Opus 4.7 regerou APENAS `F1_interference_overview.png` (diagrama polar unificado).

**Os paths nas legendas atuais do `.md` apontam para a Geração 1.** Nenhum desses paths existe no disco. O texto das legendas também descreve a narrativa antiga.

---

## 2. Prova irrefutável — os 7 paths do .md estão quebrados

```
[MISSING] docs/figuras/fig1_theta_by_scenario.png
[MISSING] docs/figuras/fig2_born_vs_classical.png
[MISSING] docs/figuras/fig3_manaus_dual_axis.png
[MISSING] docs/figuras/fig4_governance_suppression.png
[MISSING] docs/figuras/fig5_deontic_modality.png
[MISSING] docs/figuras/fig6_alhedonic_heatmap.png
[MISSING] docs/figuras/fig7_obermeyer_calibration.png
```

Linhas do `.md` com as legendas quebradas: 454, 544, 573, 595, 599, 621, 623.

Verificação para qualquer sessão futura:

```powershell
foreach ($p in Get-Content "$dir\docs\papers\PAPER1_QFENG_VALIDATION.md" |
                Select-String -Pattern 'docs/figuras/fig\d+_[^)]+\.png' -AllMatches) {
    # extract and Test-Path each
}
```

---

## 3. Inventário dos arquivos reais em `outputs/figures/`

Sete figuras, numeração F1-F7, todas geradas entre 21 e 22 de abril:

| Arquivo | Tamanho | Timestamp | Título/conteúdo real |
|---|---|---|---|
| `F1_interference_overview.png` | 293 KB | 22/04 03:43 | *"Interference angle θ across seven scenarios — overview of governance regime classification"* (diagrama polar unificado + tabela) |
| `F2_manaus_theta_efetivo.png` | 408 KB | 21/04 01:51 | *"Markovian θ_eff Trajectory — Manaus COVID-19 Health Crisis (Jul 2020 – Jun 2021)"* (série temporal dual-axis com 95% bootstrap CI) |
| `F2_manaus_timeseries.png` | 292 KB | 21/04 00:55 | Versão anterior da F2 (2 meses → 3 meses, sem CI, sem α(t)). **Candidato a renomear como `_ANTIGO_`** |
| `F3_hilbert_decision_space.png` | 530 KB | 21/04 01:39 | *"Q-FENG Interference Geometry in the Decision Hilbert Space"* (7 subplots polares com ângulos θ e GSP) |
| `F4_governance_suppression.png` | 345 KB | 21/04 02:13 | *"Governance Suppression Percentage — Born-rule Quantum vs. Classical Bayesian"* (bar chart GSP por cenário) |
| `F5_threshold_robustness.png` | 304 KB | 21/04 02:21 | *"Threshold Robustness — STAC/CB Classification Stability Across Parameter Grid"* (grid 5×7, 97.96% estabilidade) |
| `F6_psi_sensitivity.png` | 391 KB | 21/04 02:30 | *"ψ-Weight Sensitivity Analysis — Monte Carlo Robustness Under ±20% Perturbation"* (500 samples × 7 cenários) |
| `F7_deontic_regime_modality.png` | 252 KB | 21/04 03:47 | DeonticAtoms per track and modality distribution (2 painéis: atoms por trilha × distribuição modal) |

Também em `docs/figuras/` (pipelines estruturais, não entram no paper):
- `pipeline_corpus_saude.svg` (0.6 KB)
- `qfeng_pipeline_saude_v3.svg` (57.6 KB)
- `qfeng_pipeline_trabalhista_v2.svg` (51.4 KB)

---

## 4. Matriz de reconciliação proposta

### 4.1. Correspondência legenda-atual-no-md ↔ arquivo-real-em-disco

| Legenda atual no `.md` (Geração 1) | Arquivo em disco (Geração 2/3) | Match? |
|---|---|---|
| Figure 1 — bar chart STAC/HITL/CB | `F1_interference_overview.png` (polar) | semântico (approx) |
| Figure 2 — Born-rule vs. Bayesian 2-panel | `F2_manaus_theta_efetivo.png` (série Manaus) | **MISMATCH total** |
| Figure 3 — Manaus dual-axis | `F3_hilbert_decision_space.png` (7 polares) | **MISMATCH total** |
| Figure 4 — GSP por cenário | `F4_governance_suppression.png` (bar chart GSP) | MATCH |
| Figure 5 — DeonticAtom modality | `F5_threshold_robustness.png` (grid) | **MISMATCH total** |
| Figure 6 — Alhedonic heatmap | `F6_psi_sensitivity.png` (Monte Carlo) | **MISMATCH total** |
| Figure 7 — Obermeyer histogram | `F7_deontic_regime_modality.png` (atoms) | **MISMATCH total** |

Só 2 de 7 têm correspondência semântica. Os outros 5 são mismatch completo.

### 4.2. Renumeração proposta (ordem narrativa do paper)

Matriz final que a próxima sessão deve aplicar ao `.md`:

| Nº novo | Arquivo real | Título/legenda a escrever | Seção do paper |
|---|---|---|---|
| Figure 1 | `F1_interference_overview.png` | Interference angle θ across seven scenarios — overview of governance regime classification | §5.1 |
| Figure 2 | `F4_governance_suppression.png` | Governance Suppression Percentage — Born-rule Quantum vs. Classical Bayesian | §5.2 (mantém narrativa Born-rule) |
| Figure 3 | `F2_manaus_theta_efetivo.png` | Markovian θ_eff Trajectory — Manaus COVID-19 Health Crisis (Jul 2020 – Jun 2021) | §5.3 |
| Figure 4 | `F3_hilbert_decision_space.png` | Q-FENG Interference Geometry in the Decision Hilbert Space | §5.4 |
| Figure 5 | `F7_deontic_regime_modality.png` | DeonticAtoms per track and modality distribution | §5.5 |
| Figure 6 | `F5_threshold_robustness.png` | Threshold Robustness — STAC/CB Classification Stability | §6.1 |
| Figure 7 | `F6_psi_sensitivity.png` | ψ-Weight Sensitivity Analysis — Monte Carlo ±20% Perturbation | §6.2 |

**Decisões editoriais pendentes do usuário:**
- Confirmar a ordem acima (pode ser invertida se a narrativa do paper pedir outra sequência)
- Decidir se a Figure 2 original (Born-rule 2-panel como scatter com error bars) ainda deve ser gerada OU se basta a F4 como substituta (a F4 atual JÁ MOSTRA P_q vs. P_cl com error bars — parece suficiente)
- Decidir se as "Figure 6 alhedonic heatmap" e "Figure 7 Obermeyer histogram" originais devem ser geradas OU se a renumeração acima encerra o assunto (não gerando novas figuras)

---

## 5. Status dos scripts de reconciliação

**Planejado mas nunca criado:** `scripts/reconcile_figures_numbering.py`

O briefing `BRIEFING_PONTE_F7_DOCX_22abr2026.md` (seção 5) planejou esse script para fazer três edições no `.md`:
1. Renumerar as referências de figura conforme mapeamento
2. Inserir placeholders faltantes em §6.1 e §6.2
3. Ajustar legendas cujo conteúdo não corresponda mais ao `.png` apontado

Verificação: `Test-Path scripts/reconcile_figures_numbering.py` → **False**

Deve seguir o padrão dos outros scripts do projeto:
- Validação prévia de `old_str` único no arquivo
- Backup `.bak3` antes de qualquer alteração (já existem `.bak` e `.bak2`)
- Pós-verificação explícita com `[OK]` / `[!!]`
- Preferir `Desktop Commander:edit_block` sobre `Filesystem:edit_file` para edições no `.md`

---

## 6. Ordem de operações crítica para próxima sessão

A ordem não pode ser invertida sob pena de propagar defeitos:

1. **Dedup** — executar `scripts/fix_duplicate_pipeline_survival.py` (pronto, pendente de execução). Remove a duplicação do parágrafo "Pipeline survival E2 → E3 → E4" nas linhas 430/432.
2. **Reconciliação de figuras** — criar e executar `scripts/reconcile_figures_numbering.py` conforme matriz §4.2 acima. Aplicar em `docs/papers/PAPER1_QFENG_VALIDATION.md` com backup `.bak3`.
3. **Validar `.md`** — confirmar que os 7 paths das legendas agora apontam para arquivos existentes em `outputs/figures/`.
4. **Regerar DOCX** — via Claude Code, substituindo placeholders `[INSERT FIGURE N HERE]` pelas imagens `outputs/figures/F*.png` na nova numeração. Preservar estilo Chicago.
5. **Inspeção visual do DOCX** — abrir `PAPER1_QFENG_VALIDATION_CHICAGO_FINAL.docx` e confirmar que cada Figure N tem a imagem certa abaixo da legenda certa.

---

## 7. Tarefas laterais descobertas nessa sessão

### 7.1. Renomear F2 antigo

O diretório `outputs/figures/` tem **dois arquivos com prefixo F2**:
- `F2_manaus_theta_efetivo.png` (atual, versão boa, 408 KB)
- `F2_manaus_timeseries.png` (anterior, obsoleto, 292 KB)

Risco: scripts que iteram por `F2*.png` pegam os dois. Sugestão: renomear o antigo para `_ARCHIVE_F2_manaus_timeseries.png` ou mover para `outputs/figures/_archive/`.

### 7.2. Adição de entrada no menu de contexto do Windows (concluído nesta sessão)

Instalado em `HKCU\Software\Classes\`:
- `Directory\shell\ClaudeCode`
- `Directory\Background\shell\ClaudeCode`
- `Drive\shell\ClaudeCode`

Comando: `powershell.exe -NoExit -Command "Set-Location -LiteralPath '%V'; claude --model opusplan"`

Backups dos `.reg` em `C:\Workspace\claude-code-context-menu.reg` (instalar) e `C:\Workspace\claude-code-context-menu-REMOVE.reg` (reverter — mas escreve em HKCR, não em HKCU onde foi aplicado).

Para desinstalar:
```powershell
Remove-Item "HKCU:\Software\Classes\Directory\shell\ClaudeCode" -Recurse -Force
Remove-Item "HKCU:\Software\Classes\Directory\Background\shell\ClaudeCode" -Recurse -Force
Remove-Item "HKCU:\Software\Classes\Drive\shell\ClaudeCode" -Recurse -Force
Stop-Process -Name explorer -Force
```

---

## 8. Arquivos de referência para a próxima sessão

- `docs/papers/PAPER1_QFENG_VALIDATION.md` (canônico, 963 linhas, 135 KB)
- `outputs/figures/F1_interference_overview.png` até `F7_deontic_regime_modality.png`
- `artefatos/briefings/BRIEFING_SESSAO_20-21abr2026.md` (plano original das figuras)
- `artefatos/briefings/DIAGNOSTICO_F7_atom_counts_21abr2026.md` (três fontes de contagem de atoms)
- `artefatos/briefings/BRIEFING_PONTE_F7_DOCX_22abr2026.md` (primeiro diagnóstico do desalinhamento; tabela §3.2 está desatualizada face ao presente briefing)
- **ESTE ARQUIVO** (`BRIEFING_DIAGNOSTICO_FIGURAS_23abr2026.md`)

---

## 9. Contexto da sessão de 23 abril que gerou este briefing

Sessão iniciada pelo usuário no Claude Desktop para resolver três assuntos que acabaram se encadeando:

1. **Configurar modo `opusplan` do Claude Code** (concluído — documentado em seção 7.2 via menu de contexto).
2. **Validar correspondência da "Figure 2" do paper** — usuário trouxe a legenda "Born-rule vs. classical Bayesian probability" e a imagem `F2_manaus_theta_efetivo.png`. Primeiro alerta do desalinhamento.
3. **Comparação entre duas versões de F2** — usuário trouxe `F2_manaus_timeseries.png` (anterior) e `F2_manaus_theta_efetivo.png` (atual). Confirmação de que a v2 é iterativa e correta, v1 é obsoleta.
4. **Validação do diagrama polar** — usuário trouxe a figura atual (o que chamou de "Image 1", gerada pelo Opus 4.7) com a mesma legenda de Born-rule. Terceiro e definitivo alerta: a narrativa dos sete cenários CB/HITL/STAC com eixo θ NÃO corresponde à legenda de Born-rule vs. Bayesian.

Diagnóstico completo feito cruzando:
- Listagem de arquivos em `outputs/figures/` e `docs/figuras/`
- Extração das 7 legendas do `.md` (linhas 454, 544, 573, 595, 599, 621, 623)
- Conteúdo dos briefings `BRIEFING_SESSAO_20-21abr2026.md` e `BRIEFING_PONTE_F7_DOCX_22abr2026.md`
- Validação visual (view) das 7 figuras `.png` em `outputs/figures/`
- Teste individual dos 7 paths declarados no `.md` → todos `MISSING`

---

*Preparado para transferência à próxima sessão (Claude Code ou Opus 4.7 no chat do projeto Validação Q-FENG).*
*Arquivo canônico referenciado: `C:\Workspace\academico\qfeng_validacao\docs\papers\PAPER1_QFENG_VALIDATION.md`.*
*Este briefing SUPERA a tabela §3.2 do briefing de 22 abril, que estava incompleta.*