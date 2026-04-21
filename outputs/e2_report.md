# E2 Deontic Extraction Report

## Resumo

- **Chunks no corpus:** 27957
- **Chunks processados:** 6059
- **DeonticAtoms extraídos:** 5136
- **Cache hits:** 5223
- **LLM calls:** 836
- **Chunks com 0 atoms:** 2352
- **Atoms com confidence < 0.5:** 0

## DeonticAtoms por Regime

| Regime | Atoms |
|--------|-------|
| brasil | 3206 |
| eu | 1101 |
| usa | 829 |

## DeonticAtoms por chunk_type

| chunk_type | Atoms |
|------------|-------|
| obligation | 3965 |
| principle | 538 |
| procedure | 501 |
| definition | 75 |
| sanction | 57 |

## Distribuição de Modality

| Modality | Quantidade | % |
|----------|-----------|---|
| obligation | 4325 | 84.2% |
| permission | 482 | 9.4% |
| prohibition | 245 | 4.8% |
| faculty | 84 | 1.6% |

## Métricas de Confidence

- **Média:** 0.930
- **Mediana:** 0.950
- **Abaixo de 0.7:** 0 (0.0%)

## Amostras de DeonticAtoms (3 por regime)

### BRASIL

**Chunk:** CF/88 Art. 1p — Parágrafo único. Todo o poder emana do povo, que o exerce po...

```json
{
  "id": "30b6ff2b64d195a9",
  "source_chunk_id": "88e1e79473c20ab4",
  "modality": "obligation",
  "agent": "state",
  "patient": "None",
  "action": "exercise_power_through_elected_or_direct_means",
  "conditions": [],
  "threshold": null,
  "consequence": null,
  "temporality": "unconditional",
  "strength": "constitutional",
  "confidence": 0.95
}
```

**Chunk:** CF/88 Art. 3i i — II - garantir o desenvolvimento nacional;

```json
{
  "id": "6d933d8a33ba3766",
  "source_chunk_id": "bd6aa6df3102b898",
  "modality": "obligation",
  "agent": "state",
  "patient": "None",
  "action": "guarantee_national_development",
  "conditions": [],
  "threshold": null,
  "consequence": null,
  "temporality": "unconditional",
  "strength": "constitutional",
  "confidence": 0.95
}
```

**Chunk:** CF/88 Art. 3i ii — III - erradicar a pobreza e a marginalização e reduzir as de...

```json
{
  "id": "b658570e98674eb8",
  "source_chunk_id": "7ff3ca4783c5d2dd",
  "modality": "obligation",
  "agent": "state",
  "patient": "None",
  "action": "erradicate_poverty_and_marginalization_reduce_social_and Regional_inequalities",
  "conditions": [],
  "threshold": null,
  "consequence": null,
  "temporality": "unconditional",
  "strength": "constitutional",
  "confidence": 0.9
}
```

### EU

**Chunk:** Carta de Direitos Fundamentais UE Art. 15 — Freedom to choose an occupation and right to engage in work...

```json
{
  "id": "a5cdf17ee2c960f0",
  "source_chunk_id": "1846623c43c6e608",
  "modality": "permission",
  "agent": "everyone",
  "patient": "None",
  "action": "engage_in_work",
  "conditions": [],
  "threshold": null,
  "consequence": null,
  "temporality": "unconditional",
  "strength": "constitutional",
  "confidence": 0.95
}
```

**Chunk:** Carta de Direitos Fundamentais UE Art. 24 — The rights of the child 1. Children shall have the right to...

```json
{
  "id": "c9e3bb98de5757e0",
  "source_chunk_id": "1d04ae462082f73e",
  "modality": "obligation",
  "agent": "public_authorities_private_institutions",
  "patient": "child",
  "action": "provide_protection_and_care",
  "conditions": [],
  "threshold": null,
  "consequence": null,
  "temporality": "unconditional",
  "strength": "constitutional",
  "confidence": 0.95
}
```

**Chunk:** Carta de Direitos Fundamentais UE Art. 41 c — the obligation of the administration to give reasons for its...

```json
{
  "id": "ec10181a23ad7b0d",
  "source_chunk_id": "334f4bc93d1cc9f8",
  "modality": "obligation",
  "agent": "administration",
  "patient": "person",
  "action": "give_reasons_for_decisions",
  "conditions": [],
  "threshold": null,
  "consequence": null,
  "temporality": "unconditional",
  "strength": "constitutional",
  "confidence": 0.95
}
```

### USA

**Chunk:** 14th Amendment Section 2. — Representatives shall be apportioned among the several state...

```json
{
  "id": "5ee234c5be4cc461",
  "source_chunk_id": "ace65ec70e3452c2",
  "modality": "obligation",
  "agent": "state",
  "patient": "representatives_apportionment",
  "action": "be_apportioned",
  "conditions": [
    {
      "variable": "persons_count",
      "operator": "=",
      "value": "whole_number_of_persons"
    },
    {
      "variable": "indians_exclusion",
      "operator": "=",
      "value": "not_taxed_indians"
    }
  ],
  "threshold": null,
  "consequence": "federal_compliance_violation",
  "temporality": "unconditional",
  "strength": "constitutional",
  "confidence": 0.95
}
```

**Chunk:** 14th Amendment Section 3. — No person shall be a Senator or Representative in Congress,...

```json
{
  "id": "17b6f8da36478e47",
  "source_chunk_id": "62111f4bf7937977",
  "modality": "obligation",
  "agent": "congress",
  "patient": "None",
  "action": "remove_disability",
  "conditions": [
    {
      "variable": "person",
      "operator": "is",
      "value": "engaged_in_insurrection_or_rebellion"
    },
    {
      "variable": "person",
      "operator": "has_given_aid_or_comfort_to_enemies",
      "value": ""
    }
  ],
  "threshold": null,
  "consequence": "two_thirds_vote_of_congress",
  "temporality": "unconditional",
  "strength": "constitutional",
  "confidence": 0.95
}
```

**Chunk:** 42 CFR Part 430 § 430.25 Waivers of State plan requirements. (iv) — (iv) Limit beneficiaries' choice of providers (except in eme...

```json
{
  "id": "e3def3887bae70e2",
  "source_chunk_id": "c3fad262f9329672",
  "modality": "obligation",
  "agent": "state",
  "patient": "beneficiaries",
  "action": "limit_choice_of_providers",
  "conditions": [
    {
      "variable": "situation",
      "operator": "!=",
      "value": "emergency"
    },
    {
      "variable": "service_type",
      "operator": "==",
      "value": "family_planning_services"
    }
  ],
  "threshold": null,
  "consequence": null,
  "temporality": "unconditional",
  "strength": "regulatory",
  "confidence": 0.95
}
```

## Chunks com 0 DeonticAtoms

- CF/88 Art. 1º — Art. 1º A República Federativa do Brasil, formada pela união...
- CF/88 Art. 1i — I - a soberania;
- CF/88 Art. 1i i — II - a cidadania;
- CF/88 Art. 1i ii — III - a dignidade da pessoa humana;
- CF/88 Art. 1i v — IV - os valores sociais do trabalho e da livre iniciativa;
- CF/88 Art. 1v — V - o pluralismo político.
- CF/88 Art. 2º — Art. 2º São Poderes da União, independentes e harmônicos ent...
- CF/88 Art. 3º — Art. 3º Constituem objetivos fundamentais da República Feder...
- CF/88 Art. 3i — I - construir uma sociedade livre, justa e solidária;
- CF/88 Art. 4º — Art. 4º A República Federativa do Brasil rege-se nas suas re...
- CF/88 Art. 4i — I - independência nacional;
- CF/88 Art. 4i i — II - prevalência dos direitos humanos;
- CF/88 Art. 4i ii — III - autodeterminação dos povos;
- CF/88 Art. 4i v — IV - não-intervenção;
- CF/88 Art. 4v — V - igualdade entre os Estados;
- CF/88 Art. 4v i — VI - defesa da paz;
- CF/88 Art. 4v ii — VII - solução pacífica dos conflitos;
- CF/88 Art. 4v — VIII - repúdio ao terrorismo e ao racismo;
- CF/88 Art. 4i x — IX - cooperação entre os povos para o progresso da humanidad...
- CF/88 Art. 4p — Parágrafo único. A República Federativa do Brasil buscará a...
- CF/88 Art. 5l xx — LXX - o mandado de segurança coletivo pode ser impetrado por...
- CF/88 Art. 5 § 2 — § 2º Os direitos e garantias expressos nesta Constituição nã...
- CF/88 Art. 7º — Art. 7º São direitos dos trabalhadores urbanos e rurais, alé...
- CF/88 Art. 7i ii — III - fundo de garantia do tempo de serviço;
- CF/88 Art. 7v — V - piso salarial proporcional à extensão e à complexidade d...
- CF/88 Art. 7v — VIII - décimo terceiro salário com base na remuneração integ...
- CF/88 Art. 8º — Art. 8º É livre a associação profissional ou sindical, obser...
- CF/88 Art. 12 — Art. 12. São brasileiros:
- CF/88 I — I - natos:
- CF/88 Art. 12i — c) os nascidos no estrangeiro de pai brasileiro ou de mãe br...
- CF/88 II — II - naturalizados:
- CF/88 Art. 12 § 3 — § 3º São privativos de brasileiro nato os cargos:
- CF/88 I — I - de Presidente e Vice-Presidente da República;
- CF/88 II — II - de Presidente da Câmara dos Deputados;
- CF/88 III — III - de Presidente do Senado Federal;
- CF/88 IV — IV - de Ministro do Supremo Tribunal Federal;
- CF/88 V — V - da carreira diplomática;
- CF/88 VI — VI - de oficial das Forças Armadas.
- CF/88 Art. 12 § 3 — VII - de Ministro de Estado da Defesa.
- CF/88 Art. 12 § 4 — § 4º - Será declarada a perda da nacionalidade do brasileiro...
- CF/88 Art. 12 § 4 — I - tiver cancelada sua naturalização, por sentença judicial...
- CF/88 Art. 12 § 4 — II - fizer pedido expresso de perda da nacionalidade brasile...
- CF/88 Art. 13 — Art. 13. A língua portuguesa é o idioma oficial da República...
- CF/88 Art. 13 § 2 — § 1º São símbolos da República Federativa do Brasil a bandei...
- CF/88 I — I - plebiscito;
- CF/88 II — II - referendo;
- CF/88 III — III - iniciativa popular.
- CF/88 § 1 — § 1º O alistamento eleitoral e o voto são:
- CF/88 I — I - obrigatórios para os maiores de dezoito anos;
- CF/88 II — II - facultativos para:

*... e mais 2302 chunks.*