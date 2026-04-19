# Corpus Brasil Trabalhista — Q-FENG Paper 2
# ===========================================
# Uso: Cenários T-CLT-01 a T-CLT-04
# Caso âncora: Mata v. Avianca, 678 F.Supp.3d 443 (S.D.N.Y. 2023)
# Scope: advocacia_trabalhista.yaml

## Escopo deliberado

Corpus restrito a jornada de trabalho (Arts. 58-66 CLT) e rescisão
(Arts. 477-484 CLT) + Súmulas TST relevantes. Justificativa:
- Alta densidade de predicados soberanos verificáveis numericamente
- Baixa ambiguidade hermenêutica para demonstração Q-FENG
- Conexão direta com os 3 tipos de alucinação documentados em Mata v. Avianca

## Diferença de classes em relação ao corpus de saúde

| Dimensão       | Saúde (SUS/Medicaid)           | Trabalhista (CLT/TST)            |
|----------------|-------------------------------|----------------------------------|
| Agente         | estado, município, secretaria  | empregador, sindicato, empresa   |
| Paciente       | paciente, população            | empregado, trabalhador           |
| Threshold      | leitos, taxa_mortalidade       | horas, dias, R$ (salário)        |
| Soberano típico| direito_saude, equidade_regional| jornada_maxima_8h, prazo_rescisorio |
| Elástico típico| protocolo_pcdt, limiar_cobertura| banco_horas_com_cct, jornada_12x36 |
| Dado empírico  | SIH/SUS séries temporais       | Mata v. Avianca (caso documentado) |

Predicados agnósticos (valem para AMBOS os domínios):
  sovereign(citacao_verificavel)     — citação existe no ordenamento
  sovereign(fidelidade_normativa)    — holding correto
  sovereign(regime_normativo_correto)— norma aplicada ao regime certo

## Documentos e predicados esperados

### constitucional/CF88_art7_xiii_xvi.htm
Fonte: planalto.gov.br/ccivil_03/constituicao/constituicaocompilado.htm
Seção: Art. 7º, XIII (duração normal 8h/44h) e XVI (hora extra 50%)
Predicados:
  sovereign(jornada_normal_8h_diaria)   — strength: constitutional
  sovereign(jornada_normal_44h_semanal) — strength: constitutional
  sovereign(adicional_hora_extra_50pct) — strength: constitutional, threshold: 0.50

### legislacao/clt_art58_66_jornada.htm
Fonte: planalto.gov.br/ccivil_03/decreto-lei/del5452.htm (Arts. 58-66)
Predicados:
  sovereign(jornada_maxima_8h)         — Art. 58, threshold: 8
  sovereign(limite_horas_extras_2h)    — Art. 59, threshold: 2
  sovereign(intervalo_intrajornada_1h) — Art. 71, threshold: 60min
  sovereign(intervalo_interjornada_11h)— Art. 66, threshold: 11h
  elastic(banco_horas_sem_cct_6m)      — Art. 59 §5 (pós-reforma 13.467)

### legislacao/clt_art477_484_rescisao.htm
Fonte: planalto.gov.br/ccivil_03/decreto-lei/del5452.htm (Arts. 477-484)
Predicados:
  sovereign(prazo_rescisorio_10d)        — Art. 477 §6, threshold: 10 dias
  sovereign(multa_atraso_rescisao)       — Art. 477 §8
  sovereign(fgts_obrigatorio_rescisao)   — Art. 477 + Lei 8.036/90
  sovereign(homologacao_dispensa_coletiva)— Art. 477-A

### legislacao/lei_13467_2017_reforma.htm
Fonte: planalto.gov.br/ccivil_03/_ato2015-2018/2017/lei/l13467.htm
Predicados:
  elastic(banco_horas_individual_6m)   — Art. 59 §5: até 6m sem CCT
  elastic(jornada_12x36_acordo_individual)— Art. 59-A
  elastic(teletrabalho_acordo_individual) — Art. 75-C

### jurisprudencia/sumula_tst_85.htm
Fonte: tst.jus.br/sumulas (Súmula 85)
Predicados:
  elastic(banco_horas_com_cct)                    — válido com CCT
  sovereign(invalidade_banco_horas_desconto_dsr)  — não pode descontar DSR

### jurisprudencia/sumula_tst_291.htm
Fonte: tst.jus.br/sumulas (Súmula 291)
Predicados:
  sovereign(indenizacao_supressao_horas_extras) — 50% das horas suprimidas

### jurisprudencia/sumula_tst_277.htm
Fonte: tst.jus.br/sumulas (Súmula 277)
Predicados:
  elastic(clausula_negociada_cctnorm)
  sovereign(vigencia_cctnorm_2_anos)

## Script de download

Ver: scripts/download_corpus_trabalhista.py

## Status
- [ ] CF88_art7_xiii_xvi.htm
- [ ] clt_art58_66_jornada.htm
- [ ] clt_art477_484_rescisao.htm
- [ ] lei_13467_2017_reforma.htm
- [ ] sumula_tst_85.htm
- [ ] sumula_tst_291.htm
- [ ] sumula_tst_277.htm

---
*Criado: 2026-04-19*
*Responsável download: Claude Code*
