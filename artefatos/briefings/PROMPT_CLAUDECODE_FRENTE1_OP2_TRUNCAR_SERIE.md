# Prompt Claude Code — Frente 1 retroativa: Opção 2 (truncar série em SE 14/2020)

**Workspace:** `C:\Workspace\academico\qfeng_validacao` (conda env `qfeng`)
**Branch ativa:** `caminho2`
**Data de despacho:** 27/abr/2026
**Modus operandi:** 24/7, cada etapa gera artefato md/docx para alimentar reescrita do paper depois

---

## Contexto da decisão editorial

A auditoria de fechamento da Frente 1 (relatório metodológico) identificou que as quatro primeiras semanas epidemiológicas da série (SE 10/2020 a SE 13/2020) registram `hospital_occupancy_pct = 0` por consolidação tardia do registro DEMAS-VEPI. O DEMAS-VEPI só passa a registrar consistentemente ocupação UTI COVID em Manaus a partir de SE 14/2020 (TOH = 48%), o que é cronologicamente coerente com o início efetivo da pandemia em Manaus (primeiro caso 13/03/2020) e com o tempo institucional de padronização do registro pelos hospitais.

Três opções de redação foram consideradas para tratar esta limitação:

- **Opção 1 (não adotada):** manter n=74 e adicionar nota metodológica explicando que SE 10-13/2020 têm TOH zerado.
- **Opção 2 (ADOTADA — esta operação):** truncar a série em SE 14/2020 (primeira SE com TOH primário não-zero) e reportar n=70 SEs em vez de 74. ΔSE_HITL passa a ser computada apenas a partir de dados consolidados.
- **Opção 3 (não adotada):** manter n=74 mas reportar ΔSE_HITL ajustada como métrica complementar.

A decisão editorial é a **Opção 2** — desconsiderar as quatro SEs com TOH=0 da série Frente 1, em vez de mantê-las com nota explicativa. Esta operação retroativa ajusta os artefatos da Frente 1 (parquets, JSON, MD, figuras) e os três relatórios produzidos em chat (`RELATORIO_METODOLOGICO_FRENTE1.md`, `RESULTADOS_FRENTE1_PARA_CANONICO.md`, `INSERCOES_NOVAS_SECOES_CANONICO.md`) para refletir a Opção 2.

**A Frente 2 (Adversarial CLT) que está em execução pelo Code paralelamente NÃO é afetada** por esta operação. Esta é uma operação retroativa exclusiva da Frente 1.

---

## Objetivo

Aplicar a Opção 2 retroativamente na Frente 1, preservando integridade da árvore Git e reprodutibilidade Zenodo:

1. Re-rodar o pipeline Q-FENG sobre 70 SEs (SE 14/2020 a SE 30/2021), com SE 10/2020 a SE 13/2020 excluídas explicitamente como filtro de início da série.
2. Regenerar os artefatos derivados (`frente1_delta_se_antecipacao.json`, `frente1_analise_descritiva.md`, figuras).
3. Atualizar o relatório executivo `outputs/RELATORIO_FRENTE1_FINAL.md` para refletir n=70 SEs.
4. Atualizar os três relatórios produzidos em chat para refletir n=70 SEs e métricas ajustadas.
5. Documentar a decisão editorial e a operação retroativa em adendo metodológico.

**Não** propor matemática nova — toda a formalização Q-FENG já está implementada.
**Não** modificar a Frente 2 — operação retroativa exclusiva da Frente 1.
**Não** apagar o backup `outputs/e5_results/_archive_pre_frente1/` — preservar integralmente.

---

## Estado atual da Frente 1 (auditado 27/abr/2026)

| Artefato | Conteúdo atual (Opção 1 implícita) | Conteúdo desejado (Opção 2) |
|---|---|---|
| `outputs/e5_results/theta_efetivo_manaus.parquet` | 74 linhas (SE 10/2020 a SE 30/2021) | 70 linhas (SE 14/2020 a SE 30/2021) |
| `outputs/e5_results/manaus_bootstrap_ci.parquet` | 74 linhas | 70 linhas |
| `outputs/frente1_delta_se_antecipacao.json` | `delta_se_hitl=46`, `first_hitl_competencia=202010` | `delta_se_hitl=42`, `first_hitl_competencia=202014` |
| `outputs/frente1_analise_descritiva.md` | 153 linhas, n=74 SEs | atualizado para n=70 SEs |
| `outputs/figures/frente1_theta_t_serie_semanal.png` | série de 74 SEs | série de 70 SEs |
| `outputs/figures/frente1_sensibilidade_thresholds.png` | sensibilidade sobre 74 SEs | recomputada sobre 70 SEs |
| `outputs/RELATORIO_FRENTE1_FINAL.md` | 271 linhas, n=74 | atualizado para n=70 |

A métrica ΔSE_CB_estável = 19 SEs **não muda** — a primeira ativação CB ocorre em SE 37/2020, instante em que a série já operava com TOH primário consolidado. Apenas a métrica HITL (ΔSE_HITL) é afetada pelo truncamento.

---

## Contrato de execução

1. **Não fazer git push** sem confirmação explícita do autor.
2. **Commits frequentes** ao final de cada Tarefa.
3. **Backup imediato** antes de regenerar parquets: criar `outputs/e5_results/_archive_pre_opcao2/` com cópia das versões atuais (74 SEs).
4. **Não** apagar `_archive_pre_frente1/` (que contém o pipeline mensal pré-Frente 1).
5. Cada Tarefa gera artefato em `artefatos/notas_metodologicas/` ou `outputs/` para alimentar reescrita do paper.

---

## Tarefa OP2.1 — Backup pré-Opção 2 e auditoria de impacto

### Sub-tarefa OP2.1.a — Backup
Criar `outputs/e5_results/_archive_pre_opcao2/` e copiar (cp -p) os 6 parquets atuais (n=74):

- `validation_results.parquet`
- `theta_efetivo_manaus.parquet`
- `manaus_bootstrap_ci.parquet`
- `psi_sensitivity.parquet`
- `threshold_robustness.parquet`
- `llm_comparison.parquet`

Também copiar os outputs analíticos atuais:

- `outputs/frente1_delta_se_antecipacao.json`
- `outputs/frente1_analise_descritiva.md`
- `outputs/figures/frente1_theta_t_serie_semanal.png`
- `outputs/figures/frente1_sensibilidade_thresholds.png`

Gerar `outputs/e5_results/_archive_pre_opcao2/README.md` documentando contexto: "Snapshot dos artefatos Frente 1 antes da operação retroativa Opção 2 (truncar série em SE 14/2020). Versão atual: n=74 SEs (SE 10/2020 a SE 30/2021). Versão pós-Opção 2: n=70 SEs (SE 14/2020 a SE 30/2021)."

### Sub-tarefa OP2.1.b — Auditoria de impacto
Computar antes da regeneração:

- N SEs com `hospital_occupancy_pct == 0` no parquet atual (esperado: 4)
- Lista de competências afetadas (esperado: [202010, 202011, 202012, 202013])
- θ_efetivo destas SEs (esperado: ~115,27° para todas)
- Distribuição de regimes nas 4 SEs (esperado: todas em HITL)
- Confirmar que primeira SE em CB (SE 37/2020) **não está** nas 4 SEs a serem removidas

Gerar `artefatos/notas_metodologicas/OP2_1_auditoria_impacto.md` (max 30 linhas) reportando os achados.

### Output esperado
- Commit: `frente1-op2: backup pre-opcao2 + auditoria de impacto`

---

## Tarefa OP2.2 — Implementação do filtro de início no pipeline

### Sub-tarefa OP2.2.a — Definir constante canônica
Em `src/qfeng/e5_symbolic/manaus_bi_loader.py`, adicionar constante canônica no topo do módulo:

```python
# Opcao 2 (decisao editorial 27/abr/2026): SEs 10-13/2020 excluidas da
# serie Frente 1 por consolidacao tardia do registro DEMAS-VEPI (TOH=0
# nao reflete operacao real, e sim ausencia de registro padronizado).
# Primeira SE com TOH primario consolidado: SE 14/2020.
SE_INICIO_SERIE_FRENTE1 = 202014  # YYYYWW formato
```

### Sub-tarefa OP2.2.b — Aplicar filtro no loader
Em `load_manaus_bi_series()`, antes do retorno final, aplicar filtro:

```python
# Aplicar truncamento Opcao 2 (decisao editorial)
df = df[df['competencia'] >= SE_INICIO_SERIE_FRENTE1].reset_index(drop=True)
```

Atualizar docstring da função para refletir que retorna 70 SEs (SE 14/2020 a SE 30/2021), não 74.

### Sub-tarefa OP2.2.c — Validação imediata
Adicionar teste de regressão em `tests/test_manaus_bi_loader.py` (criar arquivo se não existir):

```python
def test_opcao2_filtro_serie_inicio():
    """Frente 1 Opcao 2: serie comeca em SE 14/2020, n=70 SEs."""
    df = load_manaus_bi_series()
    assert len(df) == 70, f"Esperado 70 SEs, obtido {len(df)}"
    assert df['competencia'].min() == 202014
    assert df['competencia'].max() == 202130
    assert (df['hospital_occupancy_pct'] > 0).all(), "Toda SE pos-OP2 deve ter TOH > 0"
```

Rodar `pytest tests/test_manaus_bi_loader.py -v` e confirmar passing.

### Output esperado
- Commit: `frente1-op2: filtro SE_INICIO_SERIE_FRENTE1 no manaus_bi_loader`

---

## Tarefa OP2.3 — Re-execução pipeline E5 com filtro Opção 2

Re-executar pipeline E5 inteiro:

```cmd
conda run -n qfeng python -m qfeng.e5_symbolic.runner
```

### Outputs esperados em `outputs/e5_results/`
- `theta_efetivo_manaus.parquet` — **70 linhas** (era 74)
- `manaus_bootstrap_ci.parquet` — 70 linhas
- `validation_results.parquet`, `psi_sensitivity.parquet`, `threshold_robustness.parquet`, `llm_comparison.parquet` — regenerados

### Validação OP2.3
- 70 linhas em `theta_efetivo_manaus.parquet`
- Primeira competência: 202014; última: 202130
- TOH min > 0 em todas as 70 SEs
- TOH max permanece 212 em SE 03/2021
- ΔSE_CB_estável permanece 19 SEs (não afetado)
- Distribuição de regimes esperada: STAC=0, HITL≈44, CB=26 (4 SEs HITL pré-OP2 removidas)

### Output esperado
- Commit: `frente1-op2: regenerate E5 outputs with truncated series (n=70)`
- Artefato: log JSON em `outputs/e5_results/run_log_op2.txt` com novo n, nova distribuição de regimes, e diff frente ao log_frente1.txt

---

## Tarefa OP2.4 — Regeneração da análise descritiva F1.3

Re-executar `scripts/analise_frente1.py` com input filtrado:

```cmd
conda run -n qfeng python scripts/analise_frente1.py
```

### Validação OP2.4
- `outputs/frente1_delta_se_antecipacao.json` atualizado:
  - `n_ses: 70` (era 74)
  - `se_range: "SE14/2020-SE30/2021"`
  - `delta_se_hitl: 42` (era 46)
  - `first_hitl_competencia: "202014"` (era "202010")
  - `delta_se_cb: 19` (preservado)
  - `delta_se_cb_estavel: 19` (preservado)
  - `gate_passed: true` (preservado)
- `outputs/frente1_analise_descritiva.md` atualizado para n=70 SEs com texto coerente
- `outputs/figures/frente1_theta_t_serie_semanal.png` regenerada (eixo X agora SE 14/2020 a SE 30/2021)
- `outputs/figures/frente1_sensibilidade_thresholds.png` regenerada

### Output esperado
- Commit: `frente1-op2: regenerate F1.3 analise descritiva e figuras`

---

## Tarefa OP2.5 — Atualização do relatório executivo Frente 1

Atualizar `outputs/RELATORIO_FRENTE1_FINAL.md` para refletir n=70 SEs.

### Sub-tarefa OP2.5.a — Substituições textuais

Aplicar localizar/substituir nas seguintes ocorrências:

- `74 semanas epidemiológicas` → `70 semanas epidemiológicas`
- `74 SEs` → `70 SEs` (todas as ocorrências)
- `(SE 10/2020 – SE 30/2021)` → `(SE 14/2020 – SE 30/2021)`
- `(SE 10/2020 – SE 30/2021, incl. SE 53/2020)` → `(SE 14/2020 – SE 30/2021, incl. SE 53/2020)`
- `ΔSE_HITL | 46 SEs` → `ΔSE_HITL | 42 SEs`
- `SE 10/2020 (início da série)` → `SE 14/2020 (início da série, primeira SE com TOH primário consolidado)`
- `**ΔSE_HITL = 46**` → `**ΔSE_HITL = 42**`
- `ΔSE_HITL = 46` → `ΔSE_HITL = 42`
- Tabela B.1: ajustar contagens para refletir HITL=44, CB=26, total=70

### Sub-tarefa OP2.5.b — Inserção de nota Opção 2

Adicionar parágrafo em §2.1 (Dados e Pipeline) ou §M (Limitações) explicitando a operação retroativa:

```markdown
**Nota sobre o início da série (Opção 2 — decisão editorial 27/abr/2026):** A série Frente 1 começa em SE 14/2020 (não SE 10/2020) por decisão editorial registrada após auditoria de fechamento. As quatro semanas epidemiológicas anteriores (SE 10-13/2020) registravam `hospital_occupancy_pct = 0` por consolidação tardia do registro DEMAS-VEPI no Ministério da Saúde — o sistema só passa a registrar consistentemente ocupação UTI COVID em Manaus a partir de SE 14/2020 (TOH = 48%), cronologicamente coerente com o início efetivo da pandemia em Manaus (primeiro caso 13/03/2020) e com o tempo institucional de padronização do registro pelos hospitais. As quatro SEs descartadas estão arquivadas em `outputs/e5_results/_archive_pre_opcao2/` para reprodutibilidade Zenodo, mas não compõem a série canônica Frente 1.
```

### Sub-tarefa OP2.5.c — Atualização da seção 3.5 (Correlações)

Recomputar correlações Spearman sobre n=70 e atualizar Tabela 3.5. As correlações esperadas devem permanecer aproximadamente iguais (ρ TOH×θ_efetivo ≈ 0,37–0,42; ρ score_pressao×θ_efetivo ≈ 0,89–0,93) — flutuação dentro de erro de ±0,05.

### Output esperado
- Commit: `frente1-op2: atualizar RELATORIO_FRENTE1_FINAL para n=70`

---

## Tarefa OP2.6 — Atualização dos três relatórios produzidos em chat

Os seguintes três artefatos foram produzidos em sessão de chat e estão em `artefatos/notas_metodologicas/`:

- `RELATORIO_METODOLOGICO_FRENTE1.md` (~19.700 bytes, ~188 linhas)
- `RESULTADOS_FRENTE1_PARA_CANONICO.md` (~26.400 bytes, ~239 linhas)
- `INSERCOES_NOVAS_SECOES_CANONICO.md` (~28.800 bytes, ~184 linhas)

Aplicar as mesmas substituições da OP2.5.a nestes três arquivos:

- `74 SEs` → `70 SEs`
- `n=74` → `n=70`
- `(SE 10/2020` → `(SE 14/2020`
- `ΔSE_HITL = 46` → `ΔSE_HITL = 42`
- `ΔSE_HITL | 46 SEs` → `ΔSE_HITL | 42 SEs`
- `SE 10/2020 (início da série)` → `SE 14/2020 (início da série)`
- `74 linhas (anteriormente 12)` → `70 linhas (anteriormente 12)`
- `74 SEs primárias` → `70 SEs primárias`

Adicionalmente:

### Em `RELATORIO_METODOLOGICO_FRENTE1.md`:
Substituir integralmente §6 (atual *Limitação metodológica documentada: TOH zero nas SEs 10-13/2020*) pelo seguinte texto:

```markdown
## 6. Decisão editorial Opção 2: truncamento da série em SE 14/2020

A auditoria forense de fechamento da Frente 1 identificou que as quatro primeiras semanas epidemiológicas da série (SE 10/2020 a SE 13/2020) registravam `hospital_occupancy_pct = 0`. A causa é a consolidação tardia do registro DEMAS-VEPI no Ministério da Saúde: o sistema só passa a registrar consistentemente ocupação UTI COVID em Manaus a partir de SE 14/2020 (TOH = 48%), cronologicamente coerente com o início efetivo da pandemia em Manaus (primeiro caso 13/03/2020) e com o tempo institucional de padronização do registro pelos hospitais.

A decisão editorial adotada (Opção 2, registrada em 27/abr/2026) é truncar a série em SE 14/2020 e operar exclusivamente sobre n = 70 SEs com TOH primário consolidado. Esta decisão é metodologicamente preferível à manutenção da série completa com nota explicativa porque (i) elimina ambiguidade sobre o significado de θ_efetivo nas SEs com TOH = 0; (ii) alinha a janela temporal com o período de operação consistente do sistema DEMAS-VEPI; (iii) preserva integralmente o resultado primário ΔSE_CB_estável = 19 SEs, que não é afetado pelo truncamento (a primeira ativação CB ocorre em SE 37/2020, instante em que a série já opera com TOH primário consolidado).

A operação retroativa preserva os artefatos pré-Opção 2 em `outputs/e5_results/_archive_pre_opcao2/` para reprodutibilidade Zenodo. A constante `SE_INICIO_SERIE_FRENTE1 = 202014` em `src/qfeng/e5_symbolic/manaus_bi_loader.py` codifica a decisão como filtro de início aplicado no loader, garantindo que toda execução futura do pipeline opere sobre a série canônica de 70 SEs.
```

### Em `RESULTADOS_FRENTE1_PARA_CANONICO.md`:
Substituir integralmente §G (atual *Limitação metodológica: TOH zero nas SEs 10-13/2020*) pelo seguinte texto:

```markdown
## G. Decisão editorial Opção 2: truncamento da série em SE 14/2020

A série Frente 1 reportada nesta seção corresponde a 70 SEs (SE 14/2020 a SE 30/2021), não às 74 SEs originalmente computadas. A redução de quatro SEs decorre de decisão editorial adotada na auditoria de fechamento da Frente 1 (27/abr/2026): as SEs 10-13/2020 foram excluídas da série canônica por registrarem `hospital_occupancy_pct = 0`, consequência da consolidação tardia do registro DEMAS-VEPI no Ministério da Saúde. O sistema só passa a registrar consistentemente ocupação UTI COVID em Manaus a partir de SE 14/2020 (TOH = 48%), o que é cronologicamente coerente com o início efetivo da pandemia em Manaus (primeiro caso 13/03/2020) e com o tempo institucional de padronização do registro pelos hospitais.

A justificativa metodológica para o truncamento é dupla: (i) θ_efetivo nas SEs descartadas era artefatualmente determinado pela inicialização do cache Markoviano e pela dimensão simbólica ψ_S, sem ancoragem operacional real; (ii) a manutenção destas SEs sob nota explicativa expunha o paper a crítica metodológica de tipo *garbage in, garbage out* mais severa do que a documentação transparente do truncamento. A operação retroativa preserva os parquets pré-Opção 2 em `outputs/e5_results/_archive_pre_opcao2/` para reprodutibilidade Zenodo. O resultado primário ΔSE_CB_estável = 19 SEs não é afetado pelo truncamento — a primeira ativação CB em SE 37/2020 ocorre quase 23 SEs após o início da série canônica.
```

### Em `INSERCOES_NOVAS_SECOES_CANONICO.md`:
Verificar com grep por `n=74`, `46 SEs`, `SE 10/2020`. Se houver, aplicar substituições. Se não houver, deixar intocado.

### Output esperado
- Commit: `frente1-op2: atualizar tres relatorios em chat para n=70`

---

## Tarefa OP2.7 — Adendo metodológico Opção 2

Criar `artefatos/notas_metodologicas/_addendum_OPCAO2_truncamento_serie.md` documentando a decisão editorial e a operação retroativa.

### Conteúdo esperado

```markdown
# Adendo metodológico — Opção 2: truncamento da série Frente 1 em SE 14/2020

**Branch:** `caminho2`  ·  **Data da decisão:** 27/abr/2026
**Operação retroativa:** Frente 1 do Caminho 2

## Síntese

A série semanal canônica da Frente 1 do Caminho 2 (Manaus 2020-2021) é truncada em SE 14/2020 (primeira SE com TOH primário consolidado no DEMAS-VEPI), totalizando n = 70 SEs (SE 14/2020 a SE 30/2021), em substituição à versão preliminar de n = 74 SEs originalmente computada (SE 10/2020 a SE 30/2021).

## Justificativa

A auditoria forense de fechamento da Frente 1, executada em sessão de chat em 27/abr/2026, identificou que as quatro primeiras SEs da série (SE 10-13/2020) registravam `hospital_occupancy_pct = 0`. A causa é a consolidação tardia do registro DEMAS-VEPI: o Ministério da Saúde só passa a registrar consistentemente ocupação UTI COVID em Manaus a partir de SE 14/2020 (TOH = 48%). Em contexto, o primeiro caso de COVID em Manaus foi notificado em 13/03/2020 (SE 11/2020), mas o sistema operacional dos hospitais levou aproximadamente 4-6 semanas para padronizar o registro do campo "Ocupação UTI COVID" no preenchimento diário do DEMAS-VEPI.

Três opções de redação foram consideradas:

- **Opção 1:** manter n=74 e adicionar nota metodológica explicativa.
- **Opção 2 (adotada):** truncar a série em SE 14/2020 e operar exclusivamente sobre n=70 SEs com TOH primário consolidado.
- **Opção 3:** manter n=74 e reportar ΔSE_HITL ajustada como métrica complementar.

A Opção 2 foi adotada por três motivos:

1. Elimina ambiguidade sobre o significado de θ_efetivo nas SEs com TOH = 0 (que era artefatualmente determinado pela inicialização do cache Markoviano e pela ψ_S simbólica).
2. Alinha a janela temporal com o período de operação consistente do sistema DEMAS-VEPI, evitando heterogeneidade de qualidade de fonte dentro da série.
3. Preserva integralmente o resultado primário ΔSE_CB_estável = 19 SEs, que não é afetado pelo truncamento (a primeira ativação CB ocorre em SE 37/2020, 23 SEs após o início da série canônica).

## Operação retroativa

A operação foi executada como prompt Code dedicado e consistiu em:

1. Backup integral dos artefatos pré-Opção 2 em `outputs/e5_results/_archive_pre_opcao2/`.
2. Inserção de constante canônica `SE_INICIO_SERIE_FRENTE1 = 202014` em `src/qfeng/e5_symbolic/manaus_bi_loader.py`.
3. Re-execução do pipeline E5 inteiro com filtro de início aplicado.
4. Regeneração de `outputs/frente1_delta_se_antecipacao.json` com novas métricas (`delta_se_hitl=42`, `first_hitl_competencia=202014`).
5. Regeneração de `outputs/frente1_analise_descritiva.md` e das duas figuras.
6. Atualização de `outputs/RELATORIO_FRENTE1_FINAL.md` para n=70.
7. Atualização dos três relatórios em chat: `RELATORIO_METODOLOGICO_FRENTE1.md`, `RESULTADOS_FRENTE1_PARA_CANONICO.md`, `INSERCOES_NOVAS_SECOES_CANONICO.md`.

A integridade do backup `outputs/e5_results/_archive_pre_frente1/` (do pipeline mensal pré-Frente 1) foi preservada — não confundir com `_archive_pre_opcao2/`, que é específico desta operação retroativa.

## Métricas comparadas

| Métrica | Pré-Opção 2 (n=74) | Pós-Opção 2 (n=70) |
|---|---|---|
| Range | SE 10/2020–SE 30/2021 | SE 14/2020–SE 30/2021 |
| TOH min | 0 | >0 (todas as SEs) |
| ΔSE_HITL | 46 SEs | 42 SEs |
| ΔSE_CB | 19 SEs | 19 SEs |
| ΔSE_CB_estável | 19 SEs | 19 SEs |
| Gate criterion | ✓ aprovado | ✓ aprovado |
| ρ Spearman score_pressao × θ_efetivo | 0.906 | ~0.90–0.93 |
| ρ Spearman TOH × θ_efetivo | 0.374 | ~0.37–0.42 |

## Impacto sobre a Frente 2 (Adversarial CLT)

**Nenhum.** A Frente 2 opera sobre cenários CLT independentes da série Manaus. Esta operação retroativa é exclusiva da Frente 1.

---

*Fim do adendo metodológico Opção 2.*
*Branch `caminho2` · Q-FENG Caminho 2 Frente 1*
```

### Output esperado
- Commit: `frente1-op2: adendo metodologico Opcao 2`

---

## Tarefa OP2.8 — Verificação final e relatório de fechamento

### Sub-tarefa OP2.8.a — Auditoria forense pós-Opção 2

Rodar script de verificação que confirma:

1. `theta_efetivo_manaus.parquet` tem 70 linhas
2. Range competência: 202014 a 202130
3. TOH min > 0
4. `delta_se_hitl=42` no JSON
5. `delta_se_cb_estavel=19` no JSON (preservado)
6. Backup `_archive_pre_opcao2/` existe com 6 parquets + 4 outputs analíticos
7. Backup `_archive_pre_frente1/` permanece intacto
8. Os três relatórios em chat foram atualizados (grep por `n=74` ou `46 SEs` deve retornar 0 hits, exceto em contexto de comparação histórica permitida)

Gerar `artefatos/notas_metodologicas/OP2_8_verificacao_final.md` com checklist de verificação.

### Sub-tarefa OP2.8.b — Sumário executivo da operação

Adicionar uma seção final ao `_addendum_OPCAO2_truncamento_serie.md`:

```markdown
## Status final da operação retroativa Opção 2

| Item | Status |
|---|---|
| Backup pré-Opção 2 | ✓ |
| Filtro `SE_INICIO_SERIE_FRENTE1` no loader | ✓ |
| Re-execução pipeline E5 (n=70) | ✓ |
| Regeneração análise F1.3 | ✓ |
| Atualização RELATORIO_FRENTE1_FINAL.md | ✓ |
| Atualização RELATORIO_METODOLOGICO_FRENTE1.md | ✓ |
| Atualização RESULTADOS_FRENTE1_PARA_CANONICO.md | ✓ |
| Verificação INSERCOES_NOVAS_SECOES_CANONICO.md | ✓ |
| Adendo metodológico criado | ✓ |
| Verificação forense pós-operação | ✓ |
| Frente 2 não afetada | ✓ |
```

### Output esperado
- Commit: `frente1-op2: verificacao final e fechamento operacao retroativa`

---

## Critérios de aceitação operação retroativa Opção 2

- [ ] `theta_efetivo_manaus.parquet` tem 70 linhas (não 74).
- [ ] `delta_se_hitl = 42` no JSON (era 46).
- [ ] `delta_se_cb_estavel = 19` preservado.
- [ ] TOH min > 0 em todas as 70 SEs.
- [ ] Backup `_archive_pre_opcao2/` existe e contém 6 parquets + 4 outputs analíticos + README.
- [ ] Backup `_archive_pre_frente1/` permanece intacto (não foi confundido nem sobrescrito).
- [ ] Três relatórios em chat atualizados para n=70 com substituições textuais consistentes.
- [ ] §G de `RESULTADOS_FRENTE1_PARA_CANONICO.md` substituída por texto da Opção 2.
- [ ] §6 de `RELATORIO_METODOLOGICO_FRENTE1.md` substituída por texto da Opção 2.
- [ ] Adendo metodológico `_addendum_OPCAO2_truncamento_serie.md` criado com justificativa, operação, métricas comparadas e status.
- [ ] Frente 2 (em execução paralela pelo Code) não afetada.
- [ ] Cadeia de commits frente1-op2 íntegra: backup → filtro → re-execução → análise → relatórios → adendo → verificação.

---

## Notas operacionais para o Code

1. **Esta operação é completamente independente da Frente 2.** Pode ser executada antes, durante ou depois da execução paralela da Frente 2 (Adversarial CLT). Não há touchpoint entre as duas operações nem em código nem em arquivos.

2. **Nenhum git push.** Apenas commits locais. O autor revisa antes de push.

3. **A constante `SE_INICIO_SERIE_FRENTE1 = 202014`** é a única alteração de código fonte. Todas as demais operações são regeneração de artefatos derivados.

4. **Preservar logs.** Os logs de execução da Frente 1 original (`run_log_frente1.txt`) devem ser preservados; o novo log da Opção 2 vai como `run_log_op2.txt` separado.

5. **Não tocar Frente 2.** Estrutura `experiments/adversarial_clt/`, `corpora_clingo/clt*.lp`, e tudo o que o Code estiver criando para Frente 2 não é tocado por esta operação.

---

**Fim do prompt operação retroativa Opção 2.**
