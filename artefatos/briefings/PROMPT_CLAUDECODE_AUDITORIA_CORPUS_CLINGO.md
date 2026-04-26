# Prompt operacional Claude Code — Auditoria e correção do corpus Clingo

**Data:** 26/abr/2026
**Workspace:** `C:\Workspace\academico\qfeng_validacao` (conda env `qfeng`)
**Origem do plano:** Sessão de chat Opus 4.7 (26/abr/2026) — auditoria semântica completa dos arquivos do `corpora_clingo/`.
**Objetivo:** Aplicar correções resultantes da auditoria + gerar tripla documentação derivada para incorporação posterior ao Paper 1 Q-FENG.

---

## Contexto

A auditoria semântica do corpus Clingo (todos os arquivos sob `corpora_clingo/`) foi conduzida no chat. Diagnóstico produziu pendências organizadas em quatro classes (A — lacunas estruturais, B — anti-padrões de engenharia, C — cobertura tipológica incompleta, D — refinamentos de constraint) e duas decisões de escopo:

1. **C1 CEAF descartado** do conjunto canônico de cenários de validação Q-FENG. Arquivo `c1_ceaf_facts.lp` deve ser movido para `_deprecated/` com header explicativo. Cobertura normativa permanece (Lei 8080 Art. 6° I d, Art. 7° I/IV) porque os fundamentos são genéricos e relevantes para C2 e C3.

2. **Conjunto canônico de cenários ativos:** C2 Manaus, C3 Concentração regional, C7 Obermeyer, T-CLT-01 Mata v. Avianca, T-CLT-02 Súmula TST 85 distorcida, T-CLT-03 Banco de horas com CCT (controle), T-CLT-04 Citação fundamentada (controle positivo).

A documentação deve ser triplamente derivada:
- **Artefato 1:** Relatório de auditoria operacional (`artefatos/auditorias/`).
- **Artefato 2:** Apêndice candidato acadêmico (`docs/papers/paper1/_apendices/`).
- **Artefato 3:** Notas metodológicas para incorporação ao corpo do canônico (`artefatos/notas_metodologicas/`).

---

## Pré-requisitos operacionais

- Conda env `qfeng` deve estar ativável.
- `clingo --syntax-check` deve estar disponível no PATH (Potassco 5.8).
- Shell padrão do Desktop Commander Windows: `cmd.exe`.
- Para qualquer Python inline: criar arquivo `_tmp_*.py` e executar via `python arquivo.py` (NUNCA `python -c "..."` no Windows cmd.exe).
- Para PowerShell longo: criar `.ps1` e `powershell -ExecutionPolicy Bypass -File arquivo.ps1`.

---

## ETAPA 1 — Limpeza de escopo C1 CEAF

### 1.1. Mover `c1_ceaf_facts.lp` para `_deprecated/`

**Objetivo:** preservar arquivo como rastro histórico fora do pipeline ativo.

**Operações:**

1. Criar diretório (se não existe): `corpora_clingo/_deprecated/`
2. Criar arquivo `corpora_clingo/_deprecated/c1_ceaf_facts.lp` com o conteúdo abaixo (header de deprecation + conteúdo original integral).
3. Deletar `corpora_clingo/scenarios/c1_ceaf_facts.lp` original.

**Conteúdo do novo arquivo `_deprecated/c1_ceaf_facts.lp`:**

```prolog
% ============================================================
% DEPRECATED — CENÁRIO NÃO COMPÕE PIPELINE E5 ATIVO
%
% Este arquivo foi movido para corpora_clingo/_deprecated/ em 26/abr/2026.
% O cenário C1 (CEAF Medicamentos via predictor LightGBM) foi descartado
% como caso de validação simbólica do Q-FENG durante a consolidação do
% conjunto canônico de cenários ativos.
%
% Razão da deprecation:
%   - O preditor LightGBM CEAF foi explorado como possibilidade de cenário
%     em fases anteriores da PoC, mas não foi adotado como caso de
%     validação simbólica na arquitetura final do Q-FENG.
%   - O preditor permanece como artefato de engenharia (pipeline de ML
%     funcional), mas não alimenta o motor simbólico Clingo.
%
% Conjunto canônico de cenários ativos (após decisão de 26/abr/2026):
%   - C2: Manaus 2021 (colapso hospitalar, theta > 120°)
%   - C3: Concentração regional SUS (theta ~ pi)
%   - C7: Obermeyer 2019 / bias algorítmico Medicaid (theta ~ pi)
%   - T-CLT-01: Mata v. Avianca / citação fantasma (theta ~ pi)
%   - T-CLT-02: Súmula TST 85 distorcida (theta > 120°)
%   - T-CLT-03: Banco de horas com CCT (controle, theta < 30°)
%   - T-CLT-04: Citação fundamentada (controle positivo)
%
% Cobertura normativa preservada:
%   Os predicados Lei 8080 Art. 6° I d (assistência farmacêutica integral),
%   Art. 7° I (universalidade) e Art. 7° IV (igualdade) permanecem em
%   sus_direito_saude.lp como cobertura normativa do SUS — eles não
%   dependem de C1 e continuam relevantes para C2 e C3.
%
% Arquivo preservado para rastro histórico e eventual menção como
% caminho não-adotado em notas metodológicas do paper.
% ============================================================

% Cenário C1 — CEAF Medicamentos / Falha de execução (theta ~ 0 -> ruptura)
constitutional_basis("CF88_Art196").
statutory_basis("Lei8080_Art6_I_d").
statutory_basis("Lei8080_Art7_I").
statutory_basis("Lei8080_Art7_IV").

% Estado operacional do predictor LightGBM CEAF
% (valores serão substituídos pelos dados reais do forecast)
medication_shortage_risk(high).
uf_affected("AM").
produto_id("EXEMPLO_PRODUTO").
forecast_ruptura_prob(82).   % probabilidade de ruptura em %

% Ausência do predicado de continuidade — demonstra a lacuna (theta ~ 0)
% sovereign(obligation_continuous_medication_supply) NÃO está ativo
% porque o sistema operacional não reconhece a obrigação

operational_mode(autonomous).
decision_output(patient_collective, continue_distribution).
```

### 1.2. Ajustar comentário em `sus_direito_saude.lp`

**Localização:** linhas que contêm `(CRÍTICO C1 CEAF)` e o predicado `obligation_continuous_medication_supply`.

**Ação:** substituir o comentário identificador. Encontrar o bloco:

```prolog
% --- Lei 8080/1990 Art. 6°, I, d — Assistência farmacêutica (CRÍTICO C1 CEAF) ---
% Âncora direta do fornecimento contínuo de medicamentos no SUS
% Sem este predicado o cenário C1 não tem base normativa no corpus
sovereign(right_to_integral_pharmaceutical_assistance) :-
    statutory_basis("Lei8080_Art6_I_d").

sovereign(obligation_continuous_medication_supply) :-
    statutory_basis("Lei8080_Art6_I_d"),
    sovereign(right_to_integral_pharmaceutical_assistance).
```

E substituir por:

```prolog
% --- Lei 8080/1990 Art. 6°, I, d — Assistência farmacêutica integral ---
% Âncora normativa do fornecimento contínuo de medicamentos no SUS.
% Cobertura normativa relevante para qualquer cenário de assistência
% farmacêutica no SUS — embora o cenário C1 CEAF tenha sido descartado
% do conjunto canônico de validação Q-FENG (ver _deprecated/c1_ceaf_facts.lp),
% o predicado permanece como base dogmática SOVEREIGN aplicável a
% futuros cenários de saúde envolvendo continuidade de medicação.
sovereign(right_to_integral_pharmaceutical_assistance) :-
    statutory_basis("Lei8080_Art6_I_d").

sovereign(obligation_continuous_medication_supply) :-
    statutory_basis("Lei8080_Art6_I_d"),
    sovereign(right_to_integral_pharmaceutical_assistance).
```

### 1.3. Validação Etapa 1

```cmd
cd C:\Workspace\academico\qfeng_validacao
dir corpora_clingo\_deprecated\c1_ceaf_facts.lp
dir corpora_clingo\scenarios\c1_ceaf_facts.lp 2>nul && echo ERRO: arquivo ainda existe || echo OK: arquivo removido do scenarios/
clingo --syntax-check corpora_clingo\_deprecated\c1_ceaf_facts.lp
clingo --syntax-check corpora_clingo\brasil\saude\sus_direito_saude.lp
```

---

## ETAPA 2 — Bloco 1: Lacunas constitucionais

**Princípio dogmático:** estas correções adicionam predicados constitucionais que sustentam pétreoramente os cenários C2 e os trabalhistas. Não removem nada — apenas adicionam âncoras explícitas.

### 2.1. Adicionar Art. 200 II CF/88 em `sus_direito_saude.lp`

**Localização:** após o bloco `% --- CF/88 Art. 198 — SUS ---`, antes de `% --- Lei 8080/1990 Art. 6°, I, d ---`.

**Adicionar bloco novo:**

```prolog
% --- CF/88 Art. 200 — Competências do SUS ---
% Art. 200, II: vigilância epidemiológica
% Base constitucional para a cadeia: SIVEP-Gripe (vigilância) -> ESPIN (resposta)
% -> Decreto AM 43.303/2021 (calamidade) -> obrigação de insumos.
% CRÍTICO para C2 — funda constitucionalmente o cenário Manaus.
sovereign(obligation_epidemiological_surveillance) :-
    constitutional_basis("CF88_Art200_II").

% Art. 200, II: vigilância sanitária (mesmo inciso, dimensão sanitária)
sovereign(obligation_sanitary_surveillance) :-
    constitutional_basis("CF88_Art200_II").
```

**Atualizar cabeçalho do arquivo** — adicionar na lista de âncoras normativas a linha:

```
%   CF/88 Art. 200, II — Vigilância epidemiológica e sanitária
```

E adicionar à lista de relevância para cenários:

```
%   - C2: vigilância epidemiológica como gatilho da cadeia normativa
```

### 2.2. Adicionar Art. 23 II CF/88 em `cf88_principios_fundamentais.lp`

**Localização:** após o bloco `% --- Art. 60 §4° — Cláusulas pétreas (metanorma) ---`, antes de `% --- Regras de aplicabilidade universal ---`.

**Justificativa dogmática:** Art. 23 II é norma constitucional (não pétrea formal, mas estruturante do federalismo sanitário) que sustenta a articulação tripartite União-Estados-Municípios. Após ADI 6341/STF (2020), foi consolidada como base da competência concorrente para medidas sanitárias durante a pandemia.

**Adicionar bloco novo:**

```prolog
% --- Art. 23, II — Competência comum em saúde (federalismo sanitário) ---
% Competência comum União-Estados-Municípios para cuidar da saúde e
% assistência pública. Após ADI 6341/STF (2020), consolidada como
% base da competência concorrente para medidas sanitárias durante
% emergências de saúde pública.
% CRÍTICO para C2 — funda constitucionalmente a articulação federativa
% entre Decreto AM 43.303/2021 (estadual) e Portaria GM/MS 79/2021 (federal).
%
% NOTE: Art. 23 não é cláusula pétrea formal (Art. 60 §4° não o lista),
%   mas é norma constitucional estruturante da federação sanitária.
%   sovereign() aqui tem sentido de "constitucional-aplicável", não pétreo
%   stricto sensu — distinção análoga à dos Arts. 1° e 3°.
sovereign(common_competence_health_federal_state_municipal) :-
    constitutional_basis("CF88_Art23_II").
```

**Atualizar cabeçalho do arquivo** — adicionar na lista de âncoras:

```
%   CF/88 Art. 23, II — Competência comum União-Estados-Municípios em saúde
```

### 2.3. Adicionar Art. 7° XXII CF/88 + reforçar `prohibition_negotiation_reducing_health_safety` em `clt_direitos_trabalhistas.lp`

**Localização:** dentro do arquivo `clt_direitos_trabalhistas.lp`, encontrar o bloco:

```prolog
% --- CLT Art. 611-B — limites do negociado (SOVEREIGN) ---
% Negociação NÃO PODE reduzir: normas de saúde e segurança do trabalho
sovereign(prohibition_negotiation_reducing_health_safety) :-
    statutory_basis("CLT_Art611B_XVII").
```

E substituir por:

```prolog
% --- CLT Art. 611-B — limites do negociado (SOVEREIGN) ---
% Negociação NÃO PODE reduzir: normas de saúde e segurança do trabalho
% Ancorado tanto em Art. 611-B XVII (estatutário) quanto em Art. 7° XXII
% CF/88 (constitucional — redução dos riscos inerentes ao trabalho).
% A dupla ancoragem garante que o predicado é pétreo no sentido forte:
% norma infraconstitucional sustentada por garantia constitucional explícita.
sovereign(prohibition_negotiation_reducing_health_safety) :-
    statutory_basis("CLT_Art611B_XVII"),
    constitutional_basis("CF88_Art7_XXII").

% --- CF/88 Art. 7° XXII — redução de riscos do trabalho (SOVEREIGN) ---
% Base constitucional das normas regulamentadoras (NRs) e do princípio
% da redução de riscos inerentes ao trabalho por meio de normas de
% saúde, higiene e segurança.
sovereign(constitutional_obligation_to_reduce_labor_risks) :-
    constitutional_basis("CF88_Art7_XXII").
```

**Atualizar cabeçalho** — adicionar:

```
%   CF/88 Art. 7° XXII — redução de riscos inerentes ao trabalho (NRs)
```

**Atualizar facts T-CLT** se algum cenário invocar segurança do trabalho — verificar se algum dos `t_clt_*.lp` referencia `CF88_Art7_XXII` e se faz sentido adicionar. **Não adicionar automaticamente** se nenhum cenário atual invoca (preservar minimalismo dos facts files).

### 2.4. Desdobrar Art. 196 CF/88 em três núcleos em `sus_direito_saude.lp`

**Localização:** encontrar o bloco:

```prolog
% --- CF/88 Art. 196 — Direito à saúde ---
% Saúde é direito de todos e dever do Estado
% garantido mediante políticas sociais e econômicas
sovereign(right_to_health_as_duty_of_state) :-
    constitutional_basis("CF88_Art196").

% Acesso universal e igualitário às ações e serviços de saúde
sovereign(universal_equal_access_to_health_services) :-
    constitutional_basis("CF88_Art196").
```

E substituir por:

```prolog
% --- CF/88 Art. 196 — Direito à saúde (três núcleos normativos) ---
%
% Texto pleno: "A saúde é direito de todos e dever do Estado, garantido
% mediante políticas sociais e econômicas que visem à redução do risco
% de doença e de outros agravos e ao acesso universal e igualitário às
% ações e serviços para sua promoção, proteção e recuperação."
%
% O Art. 196 condensa três núcleos normativos distintos. Para fins
% Q-FENG, desdobramos em três predicados independentes para permitir
% invocação seletiva nos cenários:

% Núcleo 1: direito-dever (estrutura subjetiva-objetiva)
sovereign(right_to_health_as_duty_of_state) :-
    constitutional_basis("CF88_Art196").

% Núcleo 2: redução de risco de doença e outros agravos via políticas
% sociais e econômicas. Funda epistemologicamente o argumento do
% predictor BI multi-fonte (Caminho 2): TOH + SRAG + O₂ como série
% temporal que mede precisamente "risco de doença e agravos" no sentido
% constitucional.
sovereign(obligation_reduce_disease_risk_via_social_economic_policies) :-
    constitutional_basis("CF88_Art196").

% Núcleo 3: acesso universal e igualitário às ações e serviços de saúde
% para promoção, proteção e recuperação.
sovereign(universal_equal_access_to_health_services) :-
    constitutional_basis("CF88_Art196").
```

### 2.5. Validação Etapa 2

```cmd
cd C:\Workspace\academico\qfeng_validacao
clingo --syntax-check corpora_clingo\brasil\saude\sus_direito_saude.lp
clingo --syntax-check corpora_clingo\brasil\constitucional\cf88_principios_fundamentais.lp
clingo --syntax-check corpora_clingo\brasil\trabalhista\clt_direitos_trabalhistas.lp
```

**CHECKPOINT — RETORNO AO CHAT:** após Etapa 2 concluída com syntax-check OK, reportar para validação Opus antes de prosseguir para Bloco 2. A validação dogmática das adições constitucionais é cognitivamente densa.

---

## ETAPA 3 — Bloco 2: Integridade do corpus

### 3.1. Implementar Lei 8080 Art. 15 I em `sus_direito_saude.lp`

**Justificativa:** o predicado `obligation_immediate_supply_critical_inputs_oxygen` em `emergencia_sanitaria.lp` invoca `statutory_basis("Lei8080_1990_Art15_I")`, mas o predicado correspondente não existe no corpus. Link quebrado.

**Localização:** após o bloco do Art. 7° (princípios do SUS), antes dos `% --- Predicados ELASTIC ---`.

**Adicionar bloco novo:**

```prolog
% --- Lei 8080/1990 Art. 15 — Atribuições comuns de União/Estados/Municípios ---
% Art. 15, I: definição das instâncias e mecanismos de controle, avaliação
% e fiscalização das ações e serviços de saúde.
% Base estatutária para competência emergencial nos três níveis federativos.
% Invocado por emergencia_sanitaria.lp como suporte ao predicado
% obligation_immediate_supply_critical_inputs_oxygen.
sovereign(common_competence_health_control_evaluation_oversight) :-
    statutory_basis("Lei8080_1990_Art15_I").
```

**Atualizar cabeçalho** — adicionar:

```
%   Lei 8080/1990 Art. 15, I — Atribuições comuns de controle/avaliação/fiscalização
```

### 3.2. Deduplicação CPC entre `cpc_fundamentacao.lp` e `clt_direitos_trabalhistas.lp`

**Princípio:** centralizar todos os predicados CPC em `cpc_fundamentacao.lp`. Em `clt_direitos_trabalhistas.lp`, manter apenas referência via comentário.

**Em `clt_direitos_trabalhistas.lp`,** localizar o bloco:

```prolog
% --- CPC Art. 489 §1° — Fundamentação das decisões judiciais ---
% CRÍTICO para T-CLT-01 — Mata v. Avianca (citação fantasma)
% CPC Art. 489, §1°, V: decisão não fundamentada quando cita precedente
%   sem identificar fundamento determinante (ratio decidendi)
sovereign(obligation_to_ground_decision_in_identified_ratio_decidendi) :-
    statutory_basis("CPC_Art489_par1_V").

% CPC Art. 489, §1°, VI: decisão não fundamentada quando não enfrenta
%   todos os argumentos da parte
sovereign(obligation_to_address_all_legal_arguments) :-
    statutory_basis("CPC_Art489_par1_VI").

% CPC Art. 489, §1°, V-VI: proibição de enunciados genéricos e citação sem ratio
sovereign(prohibition_of_generic_precedent_citation) :-
    statutory_basis("CPC_Art489_par1_V"),
    statutory_basis("CPC_Art489_par1_VI").

% LINDB Art. 20 (Lei 13.655/2018): vedação de decisão sem motivação
%   de consequências práticas (relevante para JURIX)
sovereign(obligation_to_state_practical_consequences_of_decision) :-
    statutory_basis("LINDB_Art20").
```

E substituir por:

```prolog
% --- Predicados de fundamentação processual (CPC + LINDB) ---
% Os predicados sobre fundamentação de decisões judiciais (CPC Art. 489 §1°
% e LINDB Art. 20) estão centralizados em corpora_clingo/brasil/processual/
% cpc_fundamentacao.lp para evitar duplicação. Os cenários T-CLT-* invocam
% esses predicados via inclusão do arquivo de fundamentação processual.
%
% Predicados disponibilizados pelo cpc_fundamentacao.lp:
%   - obligation_to_ground_decision_in_identified_ratio_decidendi
%     (CPC Art. 489 §1° V)
%   - obligation_to_address_all_legal_arguments (CPC Art. 489 §1° VI)
%   - prohibition_of_generic_precedent_citation (V + VI combinados)
%   - obligation_to_state_practical_consequences_of_decision (LINDB Art. 20)
```

**Em `cpc_fundamentacao.lp`,** o conteúdo já está adequado — não modificar (apenas validar que os predicados estão lá após Etapa 4 que os expande).

### 3.3. Documentar âncoras dos limiares operacionais em `emergencia_sanitaria.lp`

**Localização:** encontrar o bloco:

```prolog
% --- Predicados de estado operacional para C2 ---
% Estados do sistema hospitalar Manaus (alimentados pelo predictor TimeSeries)
% NOTE: Clingo usa inteiros — R em percentual (0-100), limiar 85%
hospital_capacity_critical :-
    hospital_occupancy_rate_pct(R), R > 85.

oxygen_supply_critical :-
    oxygen_days_remaining(D), D < 3.
```

E substituir por:

```prolog
% --- Predicados de estado operacional para C2 ---
% Estados do sistema hospitalar Manaus (alimentados pelo predictor TimeSeries).
% NOTE: Clingo usa inteiros — R em percentual (0-100).
%
% Limiar de TOH > 85%: âncora institucional na Ficha Técnica de Indicadores
% da Atenção Hospitalar do MS (Taxa de Ocupação Hospitalar de UTI), elaborada
% pela Coordenação-Geral de Atenção Hospitalar/DAHU/SAES/MS, com base na
% literatura crítica brasileira (AMIB — Associação de Medicina Intensiva
% Brasileira) que classifica TOH > 85% como "saturação operacional" — estado
% em que o tempo de espera por leito UTI cresce não-linearmente e a
% mortalidade por priorização inadequada aumenta significativamente.
%
% Limiar de oxigênio: ver oxygen_critical_threshold_days/1 abaixo (configurável).
%
hospital_capacity_critical :-
    hospital_occupancy_rate_pct(R), R > 85.

% Limiar de cobertura de oxigênio crítico: 3 dias.
% Critério operacional baseado no precedente Manaus 2021: White Martins
% comunicou ao MS em 14/jan/2021 que não conseguiria repor estoque em
% até 24-48h, configurando ponto de não-retorno operacional. O limiar
% de 3 dias é uma janela de antecedência mínima para acionamento de
% requisição emergencial (Lei 13.979/2020 Art. 3° VII) ou reorganização
% logística (transporte aéreo, redirecionamento de pacientes).
oxygen_critical_threshold_days(3).

oxygen_supply_critical :-
    oxygen_days_remaining(D),
    oxygen_critical_threshold_days(T),
    D < T.
```

### 3.4. Validação Etapa 3

```cmd
cd C:\Workspace\academico\qfeng_validacao
clingo --syntax-check corpora_clingo\brasil\saude\sus_direito_saude.lp
clingo --syntax-check corpora_clingo\brasil\trabalhista\clt_direitos_trabalhistas.lp
clingo --syntax-check corpora_clingo\brasil\emergencia_manaus\emergencia_sanitaria.lp
```

---

## ETAPA 4 — Bloco 3: Extensões e refinamentos

### 4.1. Expandir CPC Art. 489 §1° I-IV em `cpc_fundamentacao.lp`

**Localização:** após o bloco existente do Art. 489 §1° V e antes do bloco do Art. 489 §1° VI.

**Adicionar bloco novo:**

```prolog
% --- CPC Art. 489 §1° I-IV — outros critérios de decisão não fundamentada ---
%
% §1°, I: decisão não fundamentada quando se limita à indicação,
%   à reprodução ou à paráfrase de ato normativo, sem explicar sua
%   relação com a causa ou a questão decidida.
sovereign(prohibition_of_normative_act_paraphrase_without_explanation) :-
    statutory_basis("CPC_Art489_par1_I").

% §1°, II: decisão não fundamentada quando emprega conceitos jurídicos
%   indeterminados, sem explicar o motivo concreto de sua incidência.
sovereign(prohibition_of_indeterminate_legal_concepts_without_grounding) :-
    statutory_basis("CPC_Art489_par1_II").

% §1°, III: decisão não fundamentada quando invoca motivos que se
%   prestariam a justificar qualquer outra decisão (motivação genérica
%   / boilerplate). CRÍTICO para auditoria de decisões algorítmicas
%   geradas por LLM, que tendem precisamente a esse tipo de motivação.
sovereign(prohibition_of_generic_template_motivation) :-
    statutory_basis("CPC_Art489_par1_III").

% §1°, IV: decisão não fundamentada quando não enfrenta os argumentos
%   deduzidos no processo capazes de, em tese, infirmar a conclusão
%   adotada pelo julgador.
% NOTE: §1° IV e VI são frequentemente confundidos. IV trata de
%   "argumentos deduzidos no processo"; VI trata da regra geral de
%   enfrentamento. A jurisprudência os trata em conjunto, mas
%   desdobramos para fidelidade textual.
sovereign(prohibition_of_ignoring_deduced_arguments) :-
    statutory_basis("CPC_Art489_par1_IV").
```

### 4.2. Refinar constraint T-CLT-01 em `cpc_fundamentacao.lp`

**Localização:** após a constraint existente sobre citação inexistente.

**Adicionar nova constraint:**

```prolog
% Citação de precedente real, mas sem identificação de ratio decidendi,
% também viola CPC Art. 489 §1° V (precedent-mining sem fundamentação).
% Esta constraint complementa a anterior (citação fantasma stricto sensu)
% para cobrir a tipologia completa de violação do inciso V.
%
% NOTE: ratio_decidendi_identified/1 não é definida em facts-files atuais.
% Esta constraint só dispara se algum cenário futuro definir explicitamente
% a ausência de identificação de ratio. Em closed-world (default Clingo),
% a ausência de definição faz a constraint não disparar — isto é o
% comportamento desejado: a constraint é "armada" mas só ativa quando
% um cenário fornece o fato negativo.
:- legal_citation_used(Citation),
   legal_citation_exists(Citation),
   not ratio_decidendi_identified(Citation),
   ratio_decidendi_required(Citation),
   sovereign(obligation_to_ground_decision_in_identified_ratio_decidendi).
```

**NOTE para Claude Code:** verificar se essa constraint introduz UNSAT em algum dos cenários T-CLT-* atuais. Se introduzir, ajustar o predicado de guard `ratio_decidendi_required(Citation)` para que precise ser explicitamente declarado nos facts (e não inferido por default). Reportar ao chat se houver problema.

### 4.3. Generalizar constraint regional_allocation em `sus_direito_saude.lp`

**Localização:** encontrar o bloco final:

```prolog
% Nenhum sistema pode produzir desigualdade regional sistêmica
:- decision_output(_, regional_allocation),
   increases_regional_inequality(regional_allocation),
   sovereign(equity_in_health_assistance).
```

E substituir por:

```prolog
% Nenhuma decisão algorítmica pode produzir desigualdade regional sistêmica.
% Generalizado para qualquer Action (não apenas regional_allocation literal),
% análogo ao constraint correspondente em cf88_principios_fundamentais.lp.
:- decision_output(_, Action),
   increases_regional_inequality(Action),
   sovereign(equity_in_health_assistance).
```

### 4.4. Adicionar Art. 7° XV CF/88 em `clt_direitos_trabalhistas.lp` (completude pétrea)

**Localização:** após o bloco do Art. 7° XVI.

**Adicionar:**

```prolog
% --- CF/88 Art. 7° XV — repouso semanal remunerado (SOVEREIGN) ---
% Repouso semanal remunerado, preferencialmente aos domingos.
% Piso constitucional trabalhista universal — incluído por completude
% pétrea, mesmo não sendo invocado pelos cenários T-CLT-* atuais.
sovereign(weekly_paid_rest) :-
    constitutional_basis("CF88_Art7_XV").
```

### 4.5. Adicionar CLT Art. 818 em `clt_direitos_trabalhistas.lp` (ônus da prova)

**Localização:** após o bloco da OJ SDI-1 233.

**Adicionar:**

```prolog
% --- CLT Art. 818 — Ônus da prova trabalhista ---
% Ônus da prova: incumbe ao reclamante quanto ao fato constitutivo
% de seu direito; ao reclamado quanto à existência de fato impeditivo,
% modificativo ou extintivo do direito do reclamante.
% §1°: nos casos de difícil produção de prova ou maior facilidade de
% obtenção pela parte contrária, o juízo poderá atribuir o ônus
% diversamente, decisão fundamentada nos termos do CPC Art. 489.
% Estruturalmente decisivo para T-CLT-01/02 — articula-se com o dever
% de fundamentação: a redistribuição do ônus exige motivação explícita.
sovereign(burden_of_proof_default_distribution) :-
    statutory_basis("CLT_Art818_caput").

elastic(burden_of_proof_redistribution_with_motivation) :-
    statutory_basis("CLT_Art818_par1"),
    statutory_basis("CPC_Art489_par1_V").
```

### 4.6. Adicionar Lei 13.979 Art. 3° §7° em `emergencia_sanitaria.lp` (dispensa de licitação)

**Localização:** após o bloco da Lei 13.979 Art. 3° VIII.

**Adicionar:**

```prolog
% --- Lei 13.979/2020 Art. 3° §7° — Dispensa de licitação emergencial ---
% Autoriza dispensa de licitação para aquisição de bens, serviços e
% insumos relacionados ao enfrentamento da emergência de saúde pública.
% Completa a cadeia jurídica do C2: Estado pode requisitar (Art. 3° VII)
% e adquirir sem licitação (Art. 3° §7°), garantindo base legal completa
% para a obrigação de fornecimento imediato de O₂.
sovereign(authorization_to_dispense_bidding_in_emergency) :-
    statutory_basis("Lei13979_Art3_par7"),
    health_emergency_declared.
```

### 4.7. Adicionar comentários de unidade temporal em `clt_direitos_trabalhistas.lp`

**Localização:** localizar as constraints com `hour_bank_period(P)`.

**Ação:** adicionar comentário inline explicitando a unidade.

```prolog
% T-CLT-02: Banco de horas sem CCT não pode ultrapassar 6 meses
% Âncora: Art. 59 §5° (prazo máximo), não Art. 59 caput (limite diário)
% NOTE: P em meses (unidade canônica de hour_bank_period/1)
:- hour_bank_period(P), P > 6,
   not collective_bargaining_agreement_active,
   elastic(hour_bank_without_cct_max_6_months).

% T-CLT-03: Banco de horas COM CCT válido até 1 ano — STAC (theta < 30°)
% (ausência de constraint = predicado ELASTIC corretamente satisfeito)
% NOTE: P em meses (unidade canônica de hour_bank_period/1)
hour_bank_valid_with_cct :-
    hour_bank_period(P), P <= 12,
    collective_bargaining_agreement_active,
    elastic(annual_hour_bank_negotiable).
```

### 4.8. Validação Etapa 4

```cmd
cd C:\Workspace\academico\qfeng_validacao
clingo --syntax-check corpora_clingo\brasil\saude\sus_direito_saude.lp
clingo --syntax-check corpora_clingo\brasil\trabalhista\clt_direitos_trabalhistas.lp
clingo --syntax-check corpora_clingo\brasil\processual\cpc_fundamentacao.lp
clingo --syntax-check corpora_clingo\brasil\emergencia_manaus\emergencia_sanitaria.lp
clingo --syntax-check corpora_clingo\brasil\constitucional\cf88_principios_fundamentais.lp
```

---

## ETAPA 5 — Validação integrada por cenário

Para cada cenário ativo, executar Clingo com o conjunto de arquivos que ele invoca. O objetivo é detectar UNSAT introduzido pelas correções e validar que cada cenário produz o regime esperado.

### 5.1. Criar script de validação

**Criar arquivo `scripts/validate_clingo_corpus.py`:**

```python
"""
Valida o corpus Clingo executando cada cenário ativo.

Cada cenário é executado com os arquivos normativos relevantes carregados
em conjunto. Reporta SAT/UNSAT/UNKNOWN e detecta regressões introduzidas
pelas correções aplicadas em 26/abr/2026.
"""
import subprocess
from pathlib import Path

ROOT = Path(__file__).parent.parent / "corpora_clingo"

# Mapeamento canônico cenário -> conjunto de arquivos
SCENARIOS = {
    "C2_Manaus": [
        "brasil/constitucional/cf88_principios_fundamentais.lp",
        "brasil/saude/sus_direito_saude.lp",
        "brasil/emergencia_manaus/emergencia_sanitaria.lp",
        "scenarios/c2_manaus_facts.lp",
    ],
    "C3_Concentracao": [
        "brasil/constitucional/cf88_principios_fundamentais.lp",
        "brasil/saude/sus_direito_saude.lp",
        "scenarios/c3_concentracao_facts.lp",
    ],
    "C7_Obermeyer": [
        "usa/civil_rights/civil_rights_14th.lp",
        "usa/medicaid/medicaid_access.lp",
        "scenarios/c7_obermeyer_facts.lp",
    ],
    "T_CLT_01_Mata_Avianca": [
        "brasil/constitucional/cf88_principios_fundamentais.lp",
        "brasil/processual/cpc_fundamentacao.lp",
        "brasil/trabalhista/clt_direitos_trabalhistas.lp",
        "scenarios/t_clt_01_facts.lp",
    ],
    "T_CLT_02_Sumula85_Distorcida": [
        "brasil/constitucional/cf88_principios_fundamentais.lp",
        "brasil/processual/cpc_fundamentacao.lp",
        "brasil/trabalhista/clt_direitos_trabalhistas.lp",
        "scenarios/t_clt_02_facts.lp",
    ],
    "T_CLT_03_Banco_Horas_CCT": [
        "brasil/constitucional/cf88_principios_fundamentais.lp",
        "brasil/processual/cpc_fundamentacao.lp",
        "brasil/trabalhista/clt_direitos_trabalhistas.lp",
        "scenarios/t_clt_03_facts.lp",
    ],
    "T_CLT_04_Citacao_Fundamentada": [
        "brasil/constitucional/cf88_principios_fundamentais.lp",
        "brasil/processual/cpc_fundamentacao.lp",
        "brasil/trabalhista/clt_direitos_trabalhistas.lp",
        "scenarios/t_clt_04_facts.lp",
    ],
}

# Resultado esperado por cenário
EXPECTED = {
    "C2_Manaus": "UNSAT",  # Constraint disparada (operação autônoma com capacidade crítica)
    "C3_Concentracao": "UNSAT",  # Constraint disparada (manter alocação que aumenta desigualdade)
    "C7_Obermeyer": "UNSAT",  # Constraint disparada (deny_access com disparate impact)
    "T_CLT_01_Mata_Avianca": "UNSAT",  # Constraint citação fantasma
    "T_CLT_02_Sumula85_Distorcida": "UNSAT",  # Constraint banco horas sem CCT > 6 meses
    "T_CLT_03_Banco_Horas_CCT": "SAT",  # Controle: deve ser SAT (predicado ELASTIC satisfeito)
    "T_CLT_04_Citacao_Fundamentada": "SAT",  # Controle positivo: SAT
}


def run_clingo(files):
    cmd = ["clingo", "--mode=clingo", "0"] + [str(ROOT / f) for f in files]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        out = result.stdout.lower() + result.stderr.lower()
        if "unsatisfiable" in out:
            return "UNSAT"
        if "satisfiable" in out:
            return "SAT"
        if "unknown" in out:
            return "UNKNOWN"
        return f"PARSE_ERROR: {result.stdout[:200]}"
    except subprocess.TimeoutExpired:
        return "TIMEOUT"
    except Exception as e:
        return f"ERROR: {e}"


def main():
    print(f"{'='*72}")
    print(f"VALIDAÇÃO INTEGRADA DO CORPUS CLINGO Q-FENG — 26/abr/2026")
    print(f"{'='*72}\n")
    
    results = {}
    for scenario, files in SCENARIOS.items():
        actual = run_clingo(files)
        expected = EXPECTED[scenario]
        status = "OK" if actual == expected else "FAIL"
        results[scenario] = (actual, expected, status)
        print(f"[{status}] {scenario}: {actual} (esperado: {expected})")
    
    print(f"\n{'='*72}")
    failures = [s for s, (a, e, st) in results.items() if st == "FAIL"]
    if failures:
        print(f"FALHAS DETECTADAS ({len(failures)}/{len(SCENARIOS)}):")
        for f in failures:
            a, e, _ = results[f]
            print(f"  - {f}: obtido {a}, esperado {e}")
        print(f"\nReportar ao chat para análise.")
    else:
        print(f"TODOS OS {len(SCENARIOS)} CENÁRIOS VALIDADOS COM SUCESSO.")
    print(f"{'='*72}")


if __name__ == "__main__":
    main()
```

### 5.2. Executar validação integrada

```cmd
cd C:\Workspace\academico\qfeng_validacao
conda activate qfeng
python scripts\validate_clingo_corpus.py
```

**CHECKPOINT — RETORNO AO CHAT:** após Etapa 5 concluída, reportar resultado integral. Se houver `FAIL` em qualquer cenário, NÃO prosseguir para Etapa 6 — trazer logs e diagnóstico para chat resolver.

---

## ETAPA 6 — Geração da tripla documentação derivada

**Esta etapa exige conteúdo redacional de Opus.** Após validação Clingo OK, retornar ao chat para que Opus gere os três artefatos:

1. **Artefato 1 — Relatório de auditoria operacional** (`artefatos/auditorias/AUDITORIA_CORPUS_CLINGO_26abr2026.md`)
2. **Artefato 2 — Apêndice candidato acadêmico** (`docs/papers/paper1/_apendices/apendice_corpus_clingo.md`)
3. **Artefato 3 — Notas metodológicas** (`artefatos/notas_metodologicas/NOTAS_CORPUS_CLINGO_para_canonico.md`)

A tarefa de Claude Code na Etapa 6 será apenas:

- Criar os diretórios destino se não existirem.
- Receber os três conteúdos do chat (em mensagens subsequentes) e gravar nos respectivos paths.
- Validar que os arquivos foram criados corretamente.

**NÃO gerar prosa autonomamente** — esperar conteúdo gerado por Opus no chat.

---

## ETAPA 7 — Sumário e commit

### 7.1. Atualizar CHANGELOG.md

Adicionar entrada no `docs/papers/paper1/historico_submissoes/CHANGELOG.md` (se existe) ou criar `CHANGELOG_CORPUS_CLINGO.md` na raiz do `corpora_clingo/`:

```markdown
## 26/abr/2026 — Auditoria semântica completa do corpus Clingo

**Escopo:** auditoria das duas frentes ativas (saúde + trabalhista) com correções estruturais, integridade do corpus e extensões tipológicas.

**Mudanças aplicadas:**

### Etapa 1 — Limpeza de escopo
- C1 CEAF descartado do conjunto canônico de cenários ativos.
- `c1_ceaf_facts.lp` movido para `_deprecated/` com header explicativo.
- Comentário em `sus_direito_saude.lp` ajustado: predicados Lei 8080 Art. 6° I d permanecem (cobertura normativa SUS) sem invocação a C1.

### Etapa 2 — Bloco 1: Lacunas constitucionais
- Adicionado Art. 200 II CF/88 (vigilância epidemiológica/sanitária) em `sus_direito_saude.lp`.
- Adicionado Art. 23 II CF/88 (competência comum federalismo sanitário) em `cf88_principios_fundamentais.lp`.
- Adicionado Art. 7° XXII CF/88 (redução de riscos do trabalho) em `clt_direitos_trabalhistas.lp` + reforço da ancoragem dupla do `prohibition_negotiation_reducing_health_safety`.
- Art. 196 CF/88 desdobrado em três núcleos (direito-dever, redução de risco, acesso universal igualitário) em `sus_direito_saude.lp`.

### Etapa 3 — Bloco 2: Integridade do corpus
- Implementado predicado Lei 8080 Art. 15 I (link quebrado consertado).
- Deduplicação CPC: predicados centralizados em `cpc_fundamentacao.lp`, removidos de `clt_direitos_trabalhistas.lp` (substituídos por comentário de referência).
- Documentadas âncoras dos limiares operacionais em `emergencia_sanitaria.lp` (TOH > 85% via Ficha Técnica MS/AMIB; oxygen days < 3 via precedente Manaus 2021).

### Etapa 4 — Bloco 3: Extensões e refinamentos
- CPC Art. 489 §1° I-IV adicionados em `cpc_fundamentacao.lp`.
- Constraint T-CLT-01 refinada com cobertura de citação real sem ratio.
- Generalizada constraint regional_allocation em `sus_direito_saude.lp`.
- Adicionado Art. 7° XV CF/88 (repouso semanal) por completude pétrea.
- Adicionado CLT Art. 818 (ônus da prova) com distinção SOVEREIGN/ELASTIC.
- Adicionado Lei 13.979 Art. 3° §7° (dispensa de licitação emergencial) em `emergencia_sanitaria.lp`.
- Documentada unidade temporal (meses) nas constraints de banco de horas.

### Auditorias acumuladas
- Audit C-1: wrapper sovereign() / átomo plano (já existente).
- Audit C-3: remoção de constraint UNSAT espúrio (já existente).
- Audit C-4: Portaria 69/2021 substituída por Decreto AM 43.303/2021 (já existente).
- Audit C-5 [novo]: desdobramento Art. 196 em três núcleos.
- Audit C-6 [já existente]: TST-RR fabricado substituído por TST-Ag-RR-868.
- Audit F0-1: detecção de citação sintética (já existente).
- Audit H-5: Portaria 268/2021 removida (já existente).
- Audit H-6: scope guard Lei8080_Art7_I (já existente).
- Audit LAW-BR-04: predicado Mais Médicos renomeado (já existente).
- Audit LAW-BR-05 [novo]: ancoragem dupla de Art. 611-B XVII com Art. 7° XXII.
- Audit LAW-BR-06 [novo]: link Lei 8080 Art. 15 I implementado.
- Audit LAW-BR-07 [novo]: deduplicação CPC.
- Audit LAW-BR-08 [novo]: limiares operacionais documentados.
- Audit LAW-BR-09 [novo]: cobertura tipológica CPC §1° I-IV.

### Validação
- Todos os arquivos passam `clingo --syntax-check`.
- Todos os 7 cenários ativos validados via `scripts/validate_clingo_corpus.py`:
  - SAT: T-CLT-03, T-CLT-04
  - UNSAT: C2, C3, C7, T-CLT-01, T-CLT-02

### Documentação derivada gerada
- `artefatos/auditorias/AUDITORIA_CORPUS_CLINGO_26abr2026.md` (relatório operacional)
- `docs/papers/paper1/_apendices/apendice_corpus_clingo.md` (apêndice acadêmico)
- `artefatos/notas_metodologicas/NOTAS_CORPUS_CLINGO_para_canonico.md` (snippets para corpo do paper)
```

### 7.2. Sugestão de commit Git

```cmd
cd C:\Workspace\academico\qfeng_validacao
git add corpora_clingo\ artefatos\auditorias\ docs\papers\paper1\_apendices\ artefatos\notas_metodologicas\ scripts\validate_clingo_corpus.py
git commit -m "Auditoria semântica corpus Clingo 26/abr/2026: lacunas constitucionais + integridade + extensões tipológicas + tripla documentação derivada"
```

**NÃO executar `git push`** sem confirmação explícita do autor.

---

## Resumo executivo da execução

| Etapa | Bloco | Tipo | Modo |
|---|---|---|---|
| 1 | Limpeza C1 CEAF | Mecânica | Direto |
| 2 | Bloco 1 — Lacunas constitucionais | Dogmática | Após checkpoint |
| 3 | Bloco 2 — Integridade do corpus | Mecânica | Direto |
| 4 | Bloco 3 — Extensões | Mecânica | Direto |
| 5 | Validação integrada | Validação | Direto + reportar |
| 6 | Tripla documentação | Redacional | Aguardar conteúdo Opus |
| 7 | CHANGELOG + commit | Mecânica | Direto |

**Tempo estimado total Claude Code:** 30-45 minutos (com Etapa 6 aguardando conteúdo redacional do chat).

**Pontos de retorno ao chat:**
1. Após Etapa 2 (validação dogmática das adições constitucionais).
2. Após Etapa 5 (se houver FAIL na validação integrada).
3. Antes de Etapa 6 (para receber conteúdo dos três artefatos derivados).

---

*Fim do prompt.*
