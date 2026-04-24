# Audit Phase 0 Log — Verificações Externas Bloqueantes

Preencher ANTES de iniciar Fase 1 (edições em `.lp` e código Python).
Ambos os itens devem ter desfecho registrado para desbloquear a implementação.

---

## F0-1 — TST-RR-000200-50.2019.5.02.0020

**O que verificar:** acórdão do TST que serve de âncora para T-CLT-04 (STAC positive control).
O paper linha 624 cita o arquivo `corpora/brasil/trabalhista/tst_decisoes/tst_rr_000200_50_2019.lp`
que **não existe no repositório**. Se o acórdão também não existir no TST, o controle positivo se desfaz.

**Como verificar:**
1. Acessar https://jurisprudencia.tst.jus.br
2. Pesquisa por número: `RR-000200-50.2019.5.02.0020`
3. Alternativamente: pesquisa textual por "banco de horas" + "turno de revezamento" + "metalúrgico" + 2019 (TRT-2 São Paulo)

**Desfecho (preencher):**

- [ ] **A — Confirmado:** acórdão existe → URL: ___________________________________
  - Ação: criar `corpora_clingo/brasil/trabalhista/tst_decisoes/tst_rr_000200_50_2019.lp`
    com ementa e dispositivo reais; paper linha 624 permanece como está.

- [ ] **B — Não encontrado:** acórdão não existe ou número errado
  - Alternativa escolhida:
    - [ ] Substituir por decisão TST verificada: ___________________________________
    - [ ] Remover T-CLT-04 do paper (STAC positive control perde âncora real)
    - [ ] Reformular T-CLT-04 como contrafactual sintético explícito (adicionar
          "synthetic scenario" na tabela de cenários e retirar o path do paper)

**Registro final F0-1:**
```
Data verificação : ____/____/____
Desfecho         : A / B
Observações      : 
```

---

## F0-2 — Portaria GM/MS 268/2021

**O que verificar:** a Portaria 268/2021 é usada em `emergencia_sanitaria.lp:12,95-98` como
âncora de `obligation_additional_response_measures` para Manaus.
A auditoria sugere que ela trata do **Plano de Operacionalização da Vacinação contra COVID-19**
(não de medidas emergenciais de resposta hospitalar em Manaus).

**Como verificar:**
1. Acessar https://www.in.gov.br ou https://bvsms.saude.gov.br
2. Buscar: "Portaria GM/MS nº 268, de 28 de janeiro de 2021"
3. Confirmar se o objeto é: (a) vacinação / SI-PNI, ou (b) medidas emergenciais Manaus.

**Desfecho (preencher):**

- [ ] **A — Vacinação (suspeita confirmada):** âncora errada, precisa ser trocada.
  - Nova âncora recomendada (escolher uma):
    - [ ] Lei 13.979/2020 Art. 3º VII + Art. 10 (requisição de bens + ativação COE)
    - [ ] Decretos AM 43.303/2021 (23/jan) + 43.360/2021 (4/fev) — calamidade pública estadual
    - [ ] Portaria GM/MS 30/2020 (institui COE-COVID-19) — se a obrigação é de resposta coordenada
    - [ ] Outra: ___________________________________

- [ ] **B — Medidas Manaus (suspeita errada):** âncora está correta, nenhuma ação necessária.

**Registro final F0-2:**
```
Data verificação : ____/____/____
Desfecho         : A / B
Nova âncora      : (se A)
Observações      : 
```

---

## Status geral Phase 0

| Item | Status | Data |
|------|--------|------|
| F0-1 TST case | ⏳ pendente | — |
| F0-2 Portaria 268 | ⏳ pendente | — |

**→ Fase 1 pode iniciar quando ambos os status estiverem ✅.**
