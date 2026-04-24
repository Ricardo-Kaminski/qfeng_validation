# PROMPT PARA CLAUDE CODE (modo opusplan) - Correcao de figuras no PAPER1 Q-FENG

## CONTEXTO (leia antes de planejar)

O usuario (Ricardo Kaminski) esta submetendo o Paper 1 do Q-FENG e descobriu que o arquivo canonico **PAPER1_QFENG_FINAL_editando.docx** esta com figuras desalinhadas das legendas. Nao regenerar do .md - o .md esta desatualizado (falta a revisao de literatura de Herrera/Diaz-Rodriguez adicionada manualmente no Word). Toda correcao deve ser feita **diretamente no docx**.

## ARQUIVO CANONICO

- **Documento a editar:** `C:\Workspace\academico\qfeng_validacao\docs\papers\PAPER1_QFENG_FINAL_editando.docx`
- **Espelho .txt para analise textual:** `C:\Workspace\academico\qfeng_validacao\docs\papers\PAPER1_QFENG_FINAL.txt`
- **Pasta das figuras reais:** `C:\Workspace\academico\qfeng_validacao\outputs\figures\`
- **NAO USAR** como fonte: `PAPER1_QFENG_VALIDATION.md` (desatualizado)

## FECHAR WORD ANTES DE COMECAR

Se o Word estiver aberto no docx, o python-docx falha. Antes de qualquer coisa, executar:
```powershell
Get-Process WINWORD -ErrorAction SilentlyContinue | Stop-Process -Force
```

## ESTADO ATUAL DO DOCX (auditoria ja feita no chat)

No `.txt` (espelho do docx), as legendas aparecem nestas linhas:

| Linha | Legenda atual | Imagem embedada no docx |
|---|---|---|
| 457 | Figure 1. Interference angle theta by scenario with governance regime bands. | image1.png 293 KB = F1_interference_overview (polar unificado) |
| 537 | Figure 2. Born-rule vs. classical Bayesian probability... 2-panel... | image2.png 408 KB = F2_manaus_theta_efetivo (MISMATCH: imagem eh Manaus) |
| 664 | Figure 3. Manaus theta-efetivo dual-axis... | image3.png 292 KB = F2_manaus_timeseries (VERSAO ANTIGA v1!) |
| 729 | Figure 4. Governance suppression percentage... | image4.png 345 KB = F4_governance_suppression |
| 733 | [INSERT FIGURE 5 HERE] + legenda Figure 5. DeonticAtom modality distribution... | placeholder textual |
| 783 | [INSERT FIGURE 6 HERE] + legenda Figure 6. Alhedonic heatmap... | placeholder textual |
| 787 | [INSERT FIGURE 7 HERE] + legenda Figure 7. Obermeyer C7 psi_N calibration... | placeholder textual |

## FIGURAS REAIS DISPONIVEIS EM `outputs/figures/`

| Arquivo | KB | Conteudo real |
|---|---|---|
| F1_interference_overview.png | 293 | Diagrama polar unificado (todos os 7 cenarios num circulo) + tabela lateral |
| F2_manaus_theta_efetivo.png | 408 | Serie temporal dual-axis Manaus Jul2020-Jun2021 com 95% bootstrap CI |
| F2_manaus_timeseries.png | 292 | VERSAO ANTIGA da F2 (obsoleta - renomear como _ARCHIVE_) |
| F3_hilbert_decision_space.png | 530 | 7 subplots polares individuais (C2, C3, C7, T-CLT-01/02 = CB; T-CLT-03/04 = STAC) com theta e GSP |
| F4_governance_suppression.png | 345 | Bar chart GSP Born-rule vs Bayesian por cenario |
| F5_threshold_robustness.png | 304 | Grid 5x7 STAC/CB stability 97.96% |
| F6_psi_sensitivity.png | 391 | Monte Carlo +/-20% perturbation, 500 samples x 7 scenarios |
| F7_deontic_regime_modality.png | 252 | DeonticAtoms por trilha (Brazil/EU/USA health + Brazil labour) + modalidade |

## MATRIZ DE RECONCILIACAO DECIDIDA (ROTA 2 - reordenar)

Mapeamento final que DEVE ser aplicado:

| Nova posicao no docx | Arquivo em outputs/figures/ | Legenda nova (reescrever) |
|---|---|---|
| **Figure 1** | F1_interference_overview.png | Interference angle theta across seven scenarios - overview of governance regime classification. Predictor states psi_N (dashed) plotted by their angular separation from the normative reference psi_S (solid). Five CIRCUIT-BREAKER scenarios cluster at 127.8deg-134.7deg (destructive interference); two positive controls fall within the STAC band at 5.7deg-7.1deg (constructive interference). |
| **Figure 2** | F3_hilbert_decision_space.png | Q-FENG Interference Geometry in the Decision Hilbert Space. Angle theta between predictor state psi_N (dashed) and normative state psi_S (solid) across seven scenarios and two normative regimes. Health Governance: C2, C3, C7 (3D projection). Labour Law: T-CLT-01 through T-CLT-04 (2D native). GSP annotation shows governance suppression percentage per scenario. |
| **Figure 3** | F2_manaus_theta_efetivo.png (v2, 408 KB) | Markovian theta_eff Trajectory - Manaus COVID-19 Health Crisis (Jul 2020 - Jun 2021). Circuit-Breaker activated October 2020, three months before the January 2021 ICU collapse declared by Portaria MS 69/2021. Left axis: theta_eff Markovian (SIH/DATASUS) and theta_t instantaneous, with 95% bootstrap CI shading. Right axis: hospital occupancy rate (%). Peak February 2021 at theta_eff = 130.9deg. |
| **Figure 4** | F4_governance_suppression.png | Governance Suppression Percentage by scenario - Born-rule Quantum vs. Classical Bayesian. GSP quantifies the suppression of the norm-violating action probability by the quantum interference formalism, relative to a classical Bayesian mixture model. CB scenarios (theta >= 120deg): destructive interference, GSP in [9.4%, 25.2%]. STAC positive controls (theta < 30deg): constructive interference, GSP in [-0.44%, -0.28%]. |
| **Figure 5** | F7_deontic_regime_modality.png | DeonticAtoms per applied track and modality distribution. Panel (a): atoms extracted per normative track (Brazil health, EU health, USA health, Brazil labour). Panel (b): modality distribution (obligation, permission, prohibition, faculty) by track. Total: 10,142 DeonticAtoms at E2 (5,136 health/governance, 5,006 labour). |
| **Figure 6** | F5_threshold_robustness.png | Threshold Robustness - STAC/CB Classification Stability Across Parameter Grid. Grid search over theta_stac in {20,25,30,35,40}deg and theta_block in {100,105,...,130}deg (5x7=35 combinations per scenario; 245 total evaluations). Overall robustness: 97.96% (240/245 correctly classified). At theta_block <= 125deg: 100% stability. Empirical theta gap: [7.0deg, 127.8deg]. |
| **Figure 7** | F6_psi_sensitivity.png | psi-Weight Sensitivity Analysis - Monte Carlo Robustness Under +/-20% Perturbation. For each scenario, 500 perturbation samples were drawn by adding U(-delta, +delta) noise to each component of psi_N (with delta=20%), re-normalising, and recomputing theta. Correct regime preservation: 100% across all 7 scenarios (3500 total samples). Maximum sigma_theta: 2.01deg (T-CLT-02). |
