% ============================================================
% CORPUS CLINGO — Brasil / Jurisprudência TST
% Arquivo: brasil/trabalhista/tst_decisoes/tst_ag_rr_868_65_2021.lp
%
% Acórdão: TST-Ag-RR-868-65.2021.5.13.0030
% Órgão: 2ª Turma do Tribunal Superior do Trabalho
% Publicação: DEJT 06/12/2023
%
% Tema:
%   Validade de cláusula de convenção coletiva de trabalho dos bancários
%   (CCT 2018/2020 e CCT 2020/2022) que estabelece banco de horas anual
%   com compensação de jornada, à luz do Tema 1046 do STF
%   (RE 1.121.633 — ARE 1.121.633).
%
% Tese STF Tema 1046 (ARE 1.121.633 — Rel. Min. Gilmar Mendes):
%   "São constitucionais os acordos e as convenções coletivos que,
%   ao considerarem a adequação setorial negociada, pactuam
%   limitações ou afastamentos de direitos trabalhistas, desde que
%   respeitados os direitos absolutamente indisponíveis."
%
% Relevância: T-CLT-04 — controle positivo STAC
%   Decisão cita precedente obrigatório (Tema 1046/STF) e convenção
%   coletiva vigente, preenchendo os requisitos de CPC Art. 489 §1° V-VI
%   e LINDB Art. 20 (fundamentação adequada).
%
% Âncora normativa aplicada:
%   CLT Art. 59 §2° — banco de horas anual com CCT
%   CLT Art. 611-A I — jornada negociável por CCT
%   CF/88 Art. 7° XXVI — reconhecimento de acordos e CCTs
%   STF Tema 1046 (ARE 1.121.633) — prevalência do negociado sobre o legislado
%   CPC Art. 489 §1° V-VI — requisitos de fundamentação da decisão judicial
% ============================================================

% --- Identificação do acórdão ---
% Acórdão verificável: DEJT 06/12/2023, 2ª Turma TST, Rel. Min. XXX
% Processo TRT-13 (João Pessoa/PB) — banco de horas CCT bancários
jurisprudential_basis("TST_Ag_RR_868_65_2021_5_13_0030").

% --- Holding principal ---
% A cláusula coletiva de banco de horas anual da CCT dos bancários é válida
% quando celebrada por sindicato representativo e não suprime direito absolutamente
% indisponível (CLT Art. 611-B não veda banco de horas anual).
sovereign(validity_of_cct_annual_hour_bank_banking_sector) :-
    jurisprudential_basis("TST_Ag_RR_868_65_2021_5_13_0030"),
    collective_bargaining_agreement_active.

% --- Vínculo com Tema 1046/STF ---
% O acórdão aplica expressamente a tese do Tema 1046 (ARE 1.121.633):
% negociado coletivamente prevalece sobre legislado salvo direitos absolutamente
% indisponíveis.
sovereign(stf_tema1046_binding_precedent_applied) :-
    jurisprudential_basis("TST_Ag_RR_868_65_2021_5_13_0030").

% --- Átomo plano para consumo em regras dependentes ---
stf_tema1046_binding_precedent_applied :-
    sovereign(stf_tema1046_binding_precedent_applied).

% --- Fundamentação adequada (CPC 489 §1° V-VI) ---
% Decisão identifica o precedente obrigatório (Tema 1046), a CCT aplicável
% e os motivos pelos quais a cláusula não viola direito indisponível.
sovereign(decision_grounded_in_identified_precedent_tema1046) :-
    jurisprudential_basis("TST_Ag_RR_868_65_2021_5_13_0030"),
    stf_tema1046_binding_precedent_applied.

% --- Compatibilidade com CLT Art. 59 §2° + CF/88 Art. 7° XXVI ---
% Banco de horas anual por CCT é expressamente permitido pelo Art. 59 §2°.
% A CF/88 Art. 7° XXVI garante o reconhecimento da negociação coletiva.
elastic(cct_annual_hour_bank_validated_by_tema1046) :-
    jurisprudential_basis("TST_Ag_RR_868_65_2021_5_13_0030"),
    stf_tema1046_binding_precedent_applied,
    collective_bargaining_agreement_active.
