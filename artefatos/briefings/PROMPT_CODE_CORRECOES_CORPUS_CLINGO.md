# PROMPT PARA CLAUDE CODE — Correções Corpus Clingo
# ===================================================
# Origem: revisão jurídica Claude Opus 4 — 20 abr 2026
# Prioridade: BLOQUEANTE para cenários C1 e T-CLT-01
# Contexto: C:\Workspace\academico\qfeng_validacao

---

## INSTRUÇÕES GERAIS

Aplicar todas as correções abaixo nos arquivos em corpora_clingo/.
NAO inventar predicados. NAO alterar âncoras normativas sem instrução explícita.
Para cada arquivo: ler, aplicar correções, syntax-check Clingo, reportar.

---

## ARQUIVO 1 — cf88_principios_fundamentais.lp
## Status Opus: APROVADO COM RESSALVA — 1 correção

### Adicionar predicado ausente (Art. 5° XXXV — necessário para T-CLT-01)

Adicionar após o bloco do Art. 5° LV (linha ~55):

% CF/88 Art. 5°, XXXV: inafastabilidade da jurisdição / acesso à justiça
% CRÍTICO para T-CLT-01 — Mata v. Avianca (acesso à fundamentação judicial)
sovereign(right_of_access_to_justice_and_judicial_review) :-
    constitutional_basis("CF88_Art5_XXXV").

### Adicionar nota doutrinária sobre Arts. 1° e 3°

No cabeçalho do arquivo, adicionar após a linha de "Revisão jurídica":

% NOTE sobre Arts. 1° e 3°:
%   Tecnicamente são normas programáticas, não cláusulas pétreas formais.
%   A extensão de sovereign() a estes artigos é doutrinariamente defensável
%   (princípios estruturantes — Gilmar Mendes) mas não pacífica
%   (José Afonso da Silva diverge). Para fins Q-FENG: utilizável com ressalva.

---

## ARQUIVO 2 — sus_direito_saude.lp
## Status Opus: REPROVADO — 3 correções (2 críticas bloqueiam C1)

### CORREÇÃO CRÍTICA 1 — Adicionar Lei 8080 Art. 6°, I, d (BLOQUEIO C1)

Adicionar após o bloco "Lei 8080/1990 Art. 2°":

% Lei 8080/1990 Art. 6°, I, d — assistência farmacêutica (CRÍTICO C1 CEAF)
% Âncora direta do fornecimento contínuo de medicamentos no SUS
% Sem este predicado o cenário C1 não tem base normativa no corpus
sovereign(right_to_integral_pharmaceutical_assistance) :-
    statutory_basis("Lei8080_Art6_I_d").

sovereign(obligation_continuous_medication_supply) :-
    statutory_basis("Lei8080_Art6_I_d"),
    sovereign(right_to_integral_pharmaceutical_assistance).

### CORREÇÃO CRÍTICA 2 — regulatory_basis → statutory_basis (Lei 8080 é lei ordinária)

Localizar e substituir nas linhas do bloco ELASTIC:

ANTES:
    elastic(organization_by_complexity_level) :-
        regulatory_basis("Lei8080_Art7_XI").

    elastic(resource_conjugation_for_health) :-
        regulatory_basis("Lei8080_Art7_XII").

DEPOIS:
    elastic(organization_by_complexity_level) :-
        statutory_basis("Lei8080_Art7_XI").

    elastic(resource_conjugation_for_health) :-
        statutory_basis("Lei8080_Art7_XII").

### CORREÇÃO MODERADA 3 — nota sobre equity vs igualdade

No predicado equity_in_health_assistance, adicionar comentário:

% NOTE: "equity" here encompasses Art. 7° IV (igualdade formal) PLUS
% Art. 3° III (redução de desigualdades regionais — sovereign na camada constitucional)
% Distinção doutrinária: igualdade (Art. 7° IV) ≠ equidade (tratar desigualmente
% os desiguais). Para fins Q-FENG: predicado cobre ambos os sentidos.
sovereign(equity_in_health_assistance) :-
    statutory_basis("Lei8080_Art7_IV").

---

## ARQUIVO 3 — emergencia_sanitaria.lp
## Status Opus: APROVADO COM RESSALVAS — 2 correções moderadas

### CORREÇÃO MODERADA 1 — Art. 3° IX → Art. 3° VIII (importação de insumos)

ANTES:
    sovereign(authorization_to_import_without_prior_registration) :-
        statutory_basis("Lei13979_Art3_IX"),

DEPOIS:
    sovereign(authorization_to_import_without_prior_registration) :-
        statutory_basis("Lei13979_Art3_VIII"),

Adicionar comentário:
% Art. 3°, VIII: importação e distribuição de produtos sem registro prévio
% (Art. 3°, IX trata de fabricação/distribuição excepcional — distinto)
% Para crise de oxigênio Manaus: Art. 3°, VII (requisição) + Art. 3°, VIII

### CORREÇÃO MODERADA 2 — nota sobre sovereign() para portarias

No cabeçalho do arquivo, adicionar:

% NOTE sobre sovereign() para portarias (Camada 3):
%   Portarias são atos administrativos revogaréis por portaria posterior.
%   A classificação sovereign() aqui tem sentido TEMPORAL E OPERACIONAL:
%   durante a vigência da ESPIN (2020-02-03 a 2022-04-22) as obrigações
%   têm eficácia plena e imediata. O mecanismo period_within/2 já garante
%   que estes predicados só são derivados dentro do período relevante.
%   Fora do período: historicamente corretos, operacionalmente inativos.

---

## ARQUIVO 4 — clt_direitos_trabalhistas.lp
## Status Opus: REPROVADO — 3 correções críticas

### CORREÇÃO CRÍTICA 1 — CLT_Art59B não existe para banco de horas

ANTES:
    elastic(hour_bank_without_cct_max_6_months) :-
        statutory_basis("CLT_Art59B"),
        not collective_bargaining_agreement_active.

    elastic(hour_bank_with_cct_max_1_year) :-
        statutory_basis("CLT_Art59B"),
        collective_bargaining_agreement_active.

DEPOIS:
    % Banco de horas SEM CCT: Art. 59, §5° (Reforma 2017) — máximo 6 meses
    elastic(hour_bank_without_cct_max_6_months) :-
        statutory_basis("CLT_Art59_par5"),
        not collective_bargaining_agreement_active.

    % Banco de horas COM CCT: Art. 59, §2° — máximo 1 ano
    elastic(hour_bank_with_cct_max_1_year) :-
        statutory_basis("CLT_Art59_par2"),
        collective_bargaining_agreement_active.

### CORREÇÃO CRÍTICA 2 — Súmula TST 85, III desatualizada

ANTES:
    sovereign(invalidity_of_clause_suppressing_overtime_payment) :-
        jurisprudential_basis("SumulaTST_85_III").

DEPOIS:
    % CLT Art. 611-B, IX proíbe negociação que reduza adicional mínimo de 50%
    % (Súmula TST 85, III não trata de invalidade de cláusula supressiva)
    sovereign(invalidity_of_clause_suppressing_overtime_payment) :-
        statutory_basis("CLT_Art611B_IX"),
        constitutional_basis("CF88_Art7_XVI").

### CORREÇÃO CRÍTICA 3 — Adicionar predicados CPC Art. 489 (BLOQUEIO T-CLT-01)

Adicionar nova seção antes dos constraints:

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

% CPC Art. 489, §1°, I-III: proibição de enunciados genéricos
sovereign(prohibition_of_generic_precedent_citation) :-
    statutory_basis("CPC_Art489_par1_V"),
    statutory_basis("CPC_Art489_par1_VI").

% LINDB Art. 20 (Lei 13.655/2018): vedação de decisão sem motivação
%   de consequências práticas (relevante para JURIX)
sovereign(obligation_to_state_practical_consequences_of_decision) :-
    statutory_basis("LINDB_Art20").

### CORREÇÃO MODERADA — constraint T-CLT-02 âncora semântica

ANTES:
    :- hour_bank_period(P), P > 6,
       not collective_bargaining_agreement_active,
       sovereign(overtime_daily_limit_2h).

DEPOIS:
    % Âncora: Art. 59 §5° (prazo), não Art. 59 caput (limite diário)
    :- hour_bank_period(P), P > 6,
       not collective_bargaining_agreement_active,
       elastic(hour_bank_without_cct_max_6_months).

---

## ARQUIVO 5 — eu_ai_act_obligations.lp
## Status Opus: APROVADO COM RESSALVAS — 3 correções moderadas

### CORREÇÃO MODERADA 1 — Adicionar Art. 17° (declarado no cabeçalho, sem predicados)

Adicionar após o bloco do Art. 14°:

% --- Art. 17° — Sistema de gestão de qualidade (QMS) ---
sovereign(obligation_quality_management_system) :-
    regulatory_basis("EUAIA_Art17_I"),
    sovereign(health_ai_classified_as_high_risk).

### CORREÇÃO MODERADA 2 — Nota de escopo sobre sovereign() em Regulamento EU

No cabeçalho, adicionar:

% NOTE: sovereign() aqui = não derrogável pelo deployer/operador individual
% Sentido operacional, não hierárquico-constitucional.
% Regulamento EU pode ser emendado por atos delegados (Art. 97 EU AI Act)
% e por revisão legislativa ordinária — diferente de cláusula pétrea CF/88.

### CORREÇÃO MODERADA 3 — Annex III categoria mais precisa

ANTES:
    sovereign(health_ai_classified_as_high_risk) :-
        regulatory_basis("EUAIA_Art6"),
        annex_iii_category("health_critical_infrastructure").

DEPOIS:
    % Annex III, pt. 5: acesso a serviços públicos essenciais / prestações sociais
    % (mais preciso que "health_critical_infrastructure" para evitar questionamento em peer review)
    sovereign(health_ai_classified_as_high_risk) :-
        regulatory_basis("EUAIA_Art6"),
        annex_iii_category("essential_public_services_health").
    % NOTE: maps to EU AI Act Annex III, point 5 (access to essential services)
    % or point 1 (critical infrastructure) depending on deployment context

---

## CRIAR ARQUIVO NOVO — brasil/processual/cpc_fundamentacao.lp

Criar o arquivo com os predicados CPC já adicionados ao trabalhista,
mais os contextos de fundamentação geral:

Caminho: corpora_clingo/brasil/processual/cpc_fundamentacao.lp

Conteúdo: predicados CPC Art. 489 §1° já listados acima +
o seguinte adicional:

% CF/88 Art. 93, IX — fundamentação obrigatória de decisões judiciais
% (âncora constitucional do dever de fundamentar)
sovereign(constitutional_obligation_to_state_reasons_for_decisions) :-
    constitutional_basis("CF88_Art93_IX").

% Integração com Art. 5° XXXV (inafastabilidade da jurisdição)
:- legal_decision_issued(Decision),
   not decision_grounded_in_identified_precedent(Decision),
   sovereign(obligation_to_ground_decision_in_identified_ratio_decidendi).

---

## APÓS TODAS AS CORREÇÕES

### Syntax-check Clingo em todos os arquivos:
clingo --syntax-check corpora_clingo/brasil/constitucional/cf88_principios_fundamentais.lp
clingo --syntax-check corpora_clingo/brasil/saude/sus_direito_saude.lp
clingo --syntax-check corpora_clingo/brasil/emergencia_manaus/emergencia_sanitaria.lp
clingo --syntax-check corpora_clingo/brasil/trabalhista/clt_direitos_trabalhistas.lp
clingo --syntax-check corpora_clingo/eu/ai_act/eu_ai_act_obligations.lp
clingo --syntax-check corpora_clingo/brasil/processual/cpc_fundamentacao.lp

### Contar predicados sovereign() e elastic() por arquivo:
python -c "
import pathlib, re
base = pathlib.Path('C:/Workspace/academico/qfeng_validacao/corpora_clingo')
for f in sorted(base.rglob('*.lp')):
    txt = f.read_text(encoding='utf-8')
    s = len(re.findall(r'^sovereign\(', txt, re.MULTILINE))
    e = len(re.findall(r'^elastic\(', txt, re.MULTILINE))
    c = len(re.findall(r'^:-', txt, re.MULTILINE))
    print(f'{f.relative_to(base)}: sovereign={s} elastic={e} constraints={c}')
"

### Reportar para cada arquivo:
- Linhas totais antes e depois
- Resultado do syntax-check (OK / ERRO)
- Lista de predicados sovereign() adicionados
- Cenários desbloqueados (C1, T-CLT-01 devem aparecer como desbloqueados)

### NAO prosseguir para criar cenários ou facts.lp sem aprovação de Ricardo.
