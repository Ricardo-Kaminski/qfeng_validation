# Q-FENG Corpus Normativo — Manifesto

## Escopo
Três regimes normativos, hierarquia completa (constitucional → legislação → regulamentação → operacional).
Cada documento gera predicados dPASP concretos (soberanos, obrigações, causais, elásticos, thresholds).

---

## Caso A — Brasil (SUS / Saúde Pública)

### constitucional/
| Arquivo | Fonte | URL | Predicados esperados |
|---------|-------|-----|---------------------|
| `CF88_titulo_viii_cap_ii_sec_ii.htm` | CF/88 Arts. 196-200 (Saúde) | planalto.gov.br | Soberanos: right_to_health, universal_access, equity_principle |
| `CF88_art_3_5.htm` | CF/88 Art. 3° (objetivos), Art. 5° (dir. fundamentais) | planalto.gov.br | Soberanos: equity_principle, right_to_life |

### legislacao/
| Arquivo | Fonte | URL | Predicados esperados |
|---------|-------|-----|---------------------|
| `lei_8080_1990.htm` | Lei Orgânica da Saúde | planalto.gov.br/ccivil_03/leis/l8080.htm | Obrigações: universalidade, integralidade, descentralização |
| `lei_8142_1990.htm` | Participação e transferências SUS | planalto.gov.br/ccivil_03/leis/l8142.htm | Obrigações: participação comunitária, conselhos de saúde |
| `lei_8689_1993.htm` | Extinção do INAMPS | planalto.gov.br/ccivil_03/leis/L8689.htm | Contexto: municipalização (Institutional Drift) |

### regulamentacao/
| Arquivo | Fonte | URL | Predicados esperados |
|---------|-------|-----|---------------------|
| `portaria_consolidacao_2_2017.htm` | Portaria de Consolidação nº 2 (Políticas Nacionais) | bvsms.saude.gov.br | Obrigações: PNAB, PNAU, atenção hospitalar |
| `portaria_consolidacao_5_2017.htm` | Portaria de Consolidação nº 5 (Ações e Serviços) | bvsms.saude.gov.br | Obrigações: vigilância, regulação, programação |
| `portaria_1631_2015.htm` | Critérios e Parâmetros Assistenciais | saude.gov.br | Thresholds: cobertura, produção por serviço (elásticos) |
| `portarias_manaus_2021/` | Portarias de emergência COVID Manaus | saude.gov.br + DOU | Obrigações emergenciais, COES (caso empírico) |

### operacional/
| Arquivo | Fonte | URL | Predicados esperados |
|---------|-------|-----|---------------------|
| `ppa_2024_2027_saude.pdf` | PPA 2024-2027 — Programa Saúde | planejar.gov.br | Indicadores: metas PPA (elásticos), objetivos |
| `pns_2024_2027.pdf` | Plano Nacional de Saúde | saude.gov.br | Indicadores: metas de M&A, diretrizes setoriais |

---

## Caso B — EUA (Medicaid / Obermeyer)

### constitutional/
| Arquivo | Fonte | URL | Predicados esperados |
|---------|-------|-----|---------------------|
| `14th_amendment.htm` | 14th Amendment — Equal Protection | constitution.congress.gov | Soberanos: equal_protection, non_discrimination |
| `civil_rights_act_title_vi.htm` | Civil Rights Act Title VI | uscode.house.gov | Soberanos: no_discrimination_federal_programs |

### statutory/
| Arquivo | Fonte | URL | Predicados esperados |
|---------|-------|-----|---------------------|
| `ssa_title_xix_sec_1902.htm` | SSA Title XIX §1902 (State Plan requirements) | ssa.gov/OP_Home/ssact/title19/1902.htm | Obrigações: mandatory populations, eligibility, single state agency |
| `ssa_title_xix_sec_1396a.htm` | 42 USC §1396a (State plans for medical assistance) | uscode.house.gov | Obrigações: elegibilidade, cobertura, participação financeira |
| `aca_sec_2001_2002.htm` | ACA §2001-2002 (Medicaid expansion) | uscode.house.gov | Thresholds: 138% FPL, newly eligible adults |

### regulatory/
| Arquivo | Fonte | URL | Predicados esperados |
|---------|-------|-----|---------------------|
| `42_cfr_430_456.htm` | 42 CFR Parts 430-456 (Medicaid CoPs) | ecfr.gov | Obrigações: prestadores, acesso, qualidade |
| `cms_managed_care_2024.pdf` | CMS Managed Care Final Rule (2024) | cms.gov | Obrigações: rede, acesso, managed care |

### empirical/
| Arquivo | Fonte | URL | Predicados esperados |
|---------|-------|-----|---------------------|
| `obermeyer_2019_science.pdf` | Obermeyer et al. (2019) — artigo referência | science.org | Evidência: viés racial em algoritmo de saúde |
| `README_synthpop.md` | Instruções para dataset synthpop | gitlab.com | Dados sintéticos para replicação |

---

## Caso C — UE (EU AI Act / Regulação de IA)

### treaties/
| Arquivo | Fonte | URL | Predicados esperados |
|---------|-------|-----|---------------------|
| `carta_direitos_fundamentais_ue.htm` | Carta dos Direitos Fundamentais da UE | eur-lex.europa.eu | Soberanos: dignity, non_discrimination, health |

### regulation/
| Arquivo | Fonte | URL | Predicados esperados |
|---------|-------|-----|---------------------|
| `eu_ai_act_2024_1689.htm` | Regulation (EU) 2024/1689 (EU AI Act — texto integral) | eur-lex.europa.eu | Obrigações: Art.6 (risco), Art.9 (gestão), Art.14 (human oversight), Art.15 (accuracy), Annexes I-VIII |
| `gdpr_art_22_35.htm` | GDPR Arts. 22, 35 (automated decisions, DPIA) | eur-lex.europa.eu | Obrigações: explicabilidade, avaliação de impacto |

### standards/
| Arquivo | Fonte | URL | Predicados esperados |
|---------|-------|-----|---------------------|
| `iso_iec_42001_summary.md` | ISO/IEC 42001 (AI Management System) — resumo | iso.org | Referência comparativa (não gera predicados diretos) |
| `README_cen_cenelec.md` | Status dos Harmonised Standards CEN/CENELEC | cen.eu / cenelec.eu | Em elaboração — monitorar |

### comparative/
| Arquivo | Fonte | URL | Predicados esperados |
|---------|-------|-----|---------------------|
| `pl_2338_2023.htm` | PL 2338/2023 (Marco Legal da IA brasileira) | camara.leg.br | Comparação bilateral: Normative Correspondence Matrix |

---

## Totais

| Regime | Constitucional | Legislação | Regulamentação | Operacional | Total |
|--------|---------------|------------|----------------|-------------|-------|
| Brasil | 2 | 3 | 4+ | 2 | 11+ |
| EUA    | 2 | 3 | 2 | 2 | 9 |
| UE     | 1 | 2 | 2 | 1 | 6 |
| **Total** | **5** | **8** | **8+** | **5** | **26+** |

---

## Notas de escopo

1. Cada documento deve ser salvo em formato texto legível (HTML ou TXT). PDFs são aceitos mas preferimos HTML/TXT para parsing pelo E1.
2. Documentos marcados como "caso empírico" (Obermeyer, portarias Manaus) não passam pelo pipeline E1 de extração deôntica — alimentam diretamente a validação empírica dos predicados.
3. A Normative Correspondence Matrix (EU AI Act ↔ PL 2338) é artefato de pesquisa do WP §7.4.1, não input do pipeline.
4. Portarias de Manaus 2021: precisam de levantamento específico no DOU — será feito em etapa posterior.
