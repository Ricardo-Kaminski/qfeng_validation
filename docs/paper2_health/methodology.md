# Paper 2 — Methodology (Health Digital)

**Target venues:** Lancet Digital Health | npj Digital Medicine | JAMIA | J Med Internet Res
**Working title:** *Quantum-Cybernetic Governance of AI in Public Health Systems:
A Comparative Normative Analysis across Brazil (SUS), EU, and USA (Medicaid)*

---

## Case 1 — SUS (Sistema Único de Saúde)

### Corpus normativo utilizado

| Documento | Chunks | Papel no case |
|-----------|--------|---------------|
| CF/88 | 389 | Axiomas soberanos (Art. 196-200) |
| Lei 8.080/1990 | 383 | Estrutura organizacional do SUS |
| Lei 8.142/1990 | 27 | Controle social e financiamento |
| Lei 13.979/2020 | 226 | Resposta emergencial (COVID/Manaus) |
| Portarias 2021 (Manaus) | 57 | Regulação operacional de crise |
| PNS 2024-2027 | 19 | Metas operacionais |
| PPA 2024-2027 | 24 | Programas de saúde |

**A incluir quando disponível:**
- [ ] LGPD (Lei 13.709/2018) — dados de saúde sensíveis
- [ ] EBIA 2021 — IA no setor público de saúde
- [ ] Resultados E2-E5 para Case 1

## Case 2 — USA / Medicaid — Viés Algorítmico (Obermeyer et al., 2019)

**Tipo de falha:** CONSTITUTIONAL_FAILURE
**Argumento:** O predicado soberano de equidade racial nunca foi especificado na
arquitetura do algoritmo — o sinal algédônico é estruturalmente impossível de gerar.

### Corpus normativo utilizado

| Documento | Chunks | Papel no case |
|-----------|--------|---------------|
| 14th_amendment.htm | 5 | Axioma soberano — Equal Protection |
| civil_rights_act_title_vi.htm | ~120 | Não-discriminação em programas federais |
| ssa_title_xix_sec_1902.htm | 831 | Medicaid §1902 — obrigações centrais do plano estadual |
| 42_cfr_part_435.htm | 1.823 | Elegibilidade Medicaid — acesso condicional |
| 42_cfr_part_438.htm | ~640 | Managed care — padrões de qualidade e acesso |

### Evidência empírica

**Referência:** Obermeyer, Z. et al. (2019). Dissecting racial bias in an algorithm
used to manage the health of populations. *Science*, 366(6464), 447-453.
DOI: 10.1126/science.aax2342.

| Achado | Valor |
|--------|-------|
| Amostra | n ≈ 48.784 pacientes |
| Fator de viés | 1,87× — pacientes negros têm ~87% mais comorbidades para o mesmo score |
| Mecanismo | Proxy de custo histórico ≠ necessidade clínica real |
| Impacto da correção | +26,7 pontos percentuais de elegibilidade para pacientes negros |

**Arquivo:** `corpora/usa/empirical/obermeyer_2019_summary.md`

### Mecanismo de CONSTITUTIONAL_FAILURE

```
Menor acesso histórico → menor custo registrado → menor score algorítmico
→ menor elegibilidade para care management → perpetuação da subatenção
```

O algoritmo não "sabia" que deveria alertar para disparidades raciais porque o
predicado normativo `racial_equity_verified` **nunca foi especificado** como requisito.
Sem o predicado soberano, o constraint de equidade é logicamente impossível de violar
— e portanto impossível de detectar.

### Distinção tipológica (argumento central do paper)

| Dimensão | Case 1 (Brasil/SUS) | Case 2 (USA/Medicaid) |
|----------|--------------------|-----------------------|
| Sinal algédônico | Gerado, não escalado | Impossível de gerar |
| Tipo de falha | EXECUTION_FAILURE | CONSTITUTIONAL_FAILURE |
| Diagnóstico | Processo de escalamento | Especificação normativa |
| Detectável por NIST/ISO? | Parcialmente | Não |
| Detectável pelo Q-FENG? | Sim (E5) | Sim (E5) |

### A incluir quando disponível
- [ ] Resultados E2 para USA (atoms de §1902 + 14th Amendment)
- [ ] Resultados E3 (predicados Clingo incluindo racial_equity_verified ausente)
- [ ] Resultados E5 (cenário CONSTITUTIONAL_FAILURE executado)
- [ ] Análise comparativa Case 1 × Case 2 via ângulo θ

---

## Referências metodológicas em saúde digital

- Obermeyer, Z. et al. (2019). Dissecting racial bias in an algorithm used
  to manage the health of populations. *Science*, 366(6464).
- Topol, E.J. (2019). High-performance medicine: the convergence of human
  and artificial intelligence. *Nature Medicine*, 25(1).
- Char, D.S. et al. (2018). Implementing machine learning in health care —
  addressing ethical challenges. *NEJM*, 378(11).
