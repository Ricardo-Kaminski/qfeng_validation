# Prompt Phase 0 — Verificações Externas Bloqueantes
# Cole este prompt no claude.ai para executar as verificações F0-1 e F0-2.

---

Contexto: Estou preparando o paper "Q-FENG: Quantum-Fractal Neurosymbolic
Governance Framework — Validation across Healthcare and Labour Law Scenarios"
para submissão ao JURIX 2026, com revisão de Paco Herrera e Natalia Díaz-
Rodríguez (Universidad de Granada). Minha vaga de pós-doc depende da
integridade do artigo. O código será público. Uma auditoria pré-submissão
revelou dois itens que precisam de verificação externa antes que possamos
corrigir o paper. São verificações que exigem busca jurisprudencial e
regulatória — não posso fazer sozinho sem acesso ao sistema do TST e ao
Diário Oficial.

---

## VERIFICAÇÃO F0-1: Acórdão TST-RR-000200-50.2019.5.02.0020

**Por que importa:**
O paper (seção de cenários trabalhistas) usa este acórdão como âncora do
cenário T-CLT-04 — o controle positivo STAC (sistema funcionando
corretamente), onde uma IA cita jurisprudência real e fundamentada do TST
sobre banco de horas com CCT. Se o acórdão não existir, o controle positivo
do experimento Q-FENG não tem âncora factual e o paper não pode ser submetido
sem reformulação.

**O que verificar:**
Por favor, busque na jurisprudência do TST pelo número exato:
RR-000200-50.2019.5.02.0020

Site: https://jurisprudencia.tst.jus.br/

Ou tente variações de formatação aceitas pelo sistema:
- RR-0000200-50.2019.5.02.0020
- AIRR-000200-50.2019.5.02.0020
- RO-000200-50.2019.5.02.0020

O número indica: processo do TRT-2 (São Paulo), ano-base 2019, vara 0020.

**O que registrar:**
- Resultado A (encontrado): título/ementa do acórdão, data de julgamento,
  relator, se trata de banco de horas + CCT conforme CLT Art. 59 §2.
- Resultado B (não encontrado com esse número exato): tentar busca por
  assunto "banco de horas" + "CCT" + "Art. 59" nos anos 2019-2022 para
  encontrar um acórdão real substituto adequado.
- Resultado C (nenhum acórdão adequado): registrar que T-CLT-04 precisará
  ser reformulado como contrafactual sintético explícito.

---

## VERIFICAÇÃO F0-2: Portaria GM/MS 268/2021 — escopo real

**Por que importa:**
O corpus normativo do Q-FENG atribui à Portaria GM/MS 268/2021 a
"obligation_additional_response_measures" para a crise de Manaus (jan/2021).
A auditoria identificou que a Portaria 268/2021 pode ser, na verdade, a que
institui o Plano de Operacionalização da Vacinação contra COVID-19 — o que
seria uma atribuição normativa completamente errada.

**O que verificar:**
Por favor, confirme o escopo da Portaria GM/MS Nº 268, de 28 de janeiro de 2021.

Fontes para busca:
- https://bvsms.saude.gov.br/bvs/saudelegis/gm/2021/
- https://www.in.gov.br/ (Diário Oficial da União, 29/jan/2021)
- Busca: "Portaria 268 2021 Ministério Saúde"

**O que registrar:**
- Se for sobre Plano de Vacinação: a âncora normativa do cenário Manaus
  precisa ser substituída. A correção deverá usar:
  • Lei 13.979/2020 Art. 3º VII (requisição) + Art. 10 (coordenação federativa)
  • Decretos AM 43.303/2021 (calamidade pública estadual, 23/jan) e
    43.360/2021 (medidas adicionais, fev/2021)
  • Portaria GM/MS 30/2020 (COE-COVID-19, que é a correta para medidas de
    resposta coordenada)
- Se for sobre outra coisa (medidas de resposta Manaus, reforço insumos, etc.):
  registrar o ementa exata e manter a atribuição atual.

---

## FORMATO DE RESPOSTA ESPERADO

Para cada verificação, registre no seguinte formato para eu copiar ao arquivo
`artefatos/briefings/AUDIT_PHASE0_LOG.md`:

```
### F0-1 — TST-RR-000200-50.2019.5.02.0020
**Status:** [CONFIRMADO / NÃO ENCONTRADO / SUBSTITUÍDO]
**Data verificação:** [data]
**Resultado:** [descrição]
**Ação no paper:** [manter / substituir por X / reformular T-CLT-04 como sintético]

### F0-2 — Portaria GM/MS 268/2021
**Status:** [CORRETO / ERRO — substituir âncora]
**Ementa real:** [texto]
**Data publicação:** [data no DOU]
**Ação no corpus:** [manter / substituir por: Lei X + Decreto Y]
```

Após as verificações, preciso saber os resultados para desbloquear as Fases
2 e 3 da auditoria pré-submissão (correções de prosa do paper e integridade
estrutural do §5).
