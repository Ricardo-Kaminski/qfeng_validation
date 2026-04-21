# E2 Deontic Extraction Report

## Resumo

- **Chunks no corpus:** 4488
- **Chunks processados:** 4488
- **DeonticAtoms extraídos:** 5006
- **Cache hits:** 55
- **LLM calls:** 4433
- **Chunks com 0 atoms:** 1304
- **Atoms com confidence < 0.5:** 0

## DeonticAtoms por Regime

| Regime | Atoms |
|--------|-------|
| brasil | 5006 |

## DeonticAtoms por chunk_type

| chunk_type | Atoms |
|------------|-------|
| obligation | 4488 |
| principle | 381 |
| sanction | 100 |
| definition | 37 |

## Distribuição de Modality

| Modality | Quantidade | % |
|----------|-----------|---|
| obligation | 3536 | 70.6% |
| prohibition | 814 | 16.3% |
| permission | 461 | 9.2% |
| faculty | 195 | 3.9% |

## Métricas de Confidence

- **Média:** 0.942
- **Mediana:** 0.950
- **Abaixo de 0.7:** 5 (0.1%)

## Amostras de DeonticAtoms (3 por regime)

### BRASIL

**Chunk:** CF/88 Art. 2 — Art. 2� S�o Poderes da Uni�o, independentes e harm�nicos ent...

```json
{
  "id": "0b9e691c6ebc93b5",
  "source_chunk_id": "5b923dbde688d216",
  "modality": "obligation",
  "agent": "union",
  "patient": "None",
  "action": "maintain_independent_powers",
  "conditions": [],
  "threshold": null,
  "consequence": null,
  "temporality": "unconditional",
  "strength": "constitutional",
  "confidence": 0.95
}
```

**Chunk:** CF/88 I — I - construir uma sociedade livre, justa e solid�ria;

```json
{
  "id": "37463507ccca5cff",
  "source_chunk_id": "f14d7d78320d8082",
  "modality": "obligation",
  "agent": "collective",
  "patient": "society",
  "action": "build_free_just_and_solidary_society",
  "conditions": [],
  "threshold": null,
  "consequence": null,
  "temporality": "unconditional",
  "strength": "constitutional",
  "confidence": 0.95
}
```

**Chunk:** CF/88 II — II - garantir o desenvolvimento nacional;

```json
{
  "id": "34cb08806f4420f4",
  "source_chunk_id": "22e5f50f6692fd63",
  "modality": "obligation",
  "agent": "state",
  "patient": "public",
  "action": "guarantee_national_development",
  "conditions": [],
  "threshold": null,
  "consequence": "mandado_seguranca",
  "temporality": "unconditional",
  "strength": "constitutional",
  "confidence": 0.95
}
```

## Chunks com 0 DeonticAtoms

- CF/88 Art. 1 — Art. 1� A Rep�blica Federativa do Brasil, formada pela uni�o...
- CF/88 IV — IV - os valores sociais do trabalho e da livre iniciativa;
- CF/88 Art. 3 — Art. 3� Constituem objetivos fundamentais da Rep�blica Feder...
- CF/88 Art. 4 — Art. 4� A Rep�blica Federativa do Brasil rege-se nas suas re...
- CF/88 XXVIII — XXVIII - s�o assegurados, nos termos da lei:
- CF/88 XLVI — XLVI - a lei regular� a individualiza��o da pena e adotar�,...
- CF/88 LXX — LXX - o mandado de seguran�a coletivo pode ser impetrado por...
- CF/88 Art. 7 — Art. 7� S�o direitos dos trabalhadores urbanos e rurais, al�...
- CF/88 III — III - fundo de garantia do tempo de servi�o;
- CF/88 I — I - de Presidente e Vice-Presidente da Rep�blica;
- CF/88 II — II - de Presidente da C�mara dos Deputados;
- CF/88 IV — IV - de Ministro do Supremo Tribunal Federal;
- CF/88 II — II - o pleno exerc�cio dos direitos pol�ticos;
- CF/88 IV — IV - o domic�lio eleitoral na circunscri��o;
- CF/88 Art. 18 — Art. 18. A organiza��o pol�tico-administrativa da Rep�blica...
- CF/88 I — I - os que atualmente lhe pertencem e os que lhe vierem a se...
- CF/88 V — V - os recursos naturais da plataforma continental e da zona...
- CF/88 VII — VII - os terrenos de marinha e seus acrescidos;
- CF/88 VIII — VIII - os potenciais de energia hidr�ulica;
- CF/88 IX — IX - os recursos minerais, inclusive os do subsolo;
- CF/88 X — X - as cavidades naturais subterr�neas e os s�tios arqueol�g...
- CF/88 XVI — XVI - exercer a classifica��o, para efeito indicativo, de di...
- CF/88 XXI — XXI - estabelecer princ�pios e diretrizes para o sistema nac...
- CF/88 Art. 22 — Art. 22. Compete privativamente � Uni�o legislar sobre:
- CF/88 I — I - direito civil, comercial, penal, processual, eleitoral,...
- CF/88 IV — IV - �guas, energia, inform�tica, telecomunica��es e radiodi...
- CF/88 VI — VI - sistema monet�rio e de medidas, t�tulos e garantias dos...
- CF/88 VII — VII - pol�tica de cr�dito, c�mbio, seguros e transfer�ncia d...
- CF/88 VIII — VIII - com�rcio exterior e interestadual;
- CF/88 IX — IX - diretrizes da pol�tica nacional de transportes;
- CF/88 X — X - regime dos portos, navega��o lacustre, fluvial, mar�tima...
- CF/88 XII — XII - jazidas, minas, outros recursos minerais e metalurgia;
- CF/88 XIII — XIII - nacionalidade, cidadania e naturaliza��o;
- CF/88 XVIII — XVIII - sistema estat�stico, sistema cartogr�fico e de geolo...
- CF/88 XIX — XIX - sistemas de poupan�a, capta��o e garantia da poupan�a...
- CF/88 XXI — XXI - normas gerais de organiza��o, efetivos, material b�lic...
- CF/88 XXII — XXII - compet�ncia da pol�cia federal e das pol�cias rodovi�...
- CF/88 XXIV — XXIV - diretrizes e bases da educa��o nacional;
- CF/88 XXVI — XXVI - atividades nucleares de qualquer natureza;
- CF/88 XXX — XXX - prote��o e tratamento de dados pessoais. (Inclu�do pel...
- CF/88 Art. 23 — Art. 23. � compet�ncia comum da Uni�o, dos Estados, do Distr...
- CF/88 Art. 24 — Art. 24. Compete � Uni�o, aos Estados e ao Distrito Federal...
- CF/88 I — I - direito tribut�rio, financeiro, penitenci�rio, econ�mico...
- CF/88 IX — IX - educa��o, cultura, ensino, desporto, ci�ncia, tecnologi...
- CF/88 Art. 26 — Art. 26. Incluem-se entre os bens dos Estados:
- CF/88 II — II - as �reas, nas ilhas oce�nicas e costeiras, que estivere...
- CF/88 III — III - as ilhas fluviais e lacustres n�o pertencentes � Uni�o...
- CF/88 IV — IV - as terras devolutas n�o compreendidas entre as da Uni�o...
- CF/88 IV — IV - para a composi��o das C�maras Municipais, ser� observad...
- CF/88 X — X - julgamento do Prefeito perante o Tribunal de Justi�a; (R...

*... e mais 1254 chunks.*