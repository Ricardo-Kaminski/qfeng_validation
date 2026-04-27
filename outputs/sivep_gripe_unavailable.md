# SIVEP-Gripe — Indisponibilidade de fonte (Fase 2, Tarefa 2.1)

**Data de diagnóstico:** 2026-04-26  
**Branch:** caminho2  
**Status:** Tarefa 2.1 ABORTADA — fontes primária e fallback inacessíveis

---

## Diagnóstico de rede

### Tentativa 1 — OpenDataSUS (primário)

**URL testada:** `https://s3.sa-east-1.amazonaws.com/ckan.saude.gov.br/SRAG/2020/INFLUD20-04-04-2024.csv`  
**Resultado:** `HTTP 403 Forbidden`  
**Timestamp:** 2026-04-26T23:XX UTC-3

**URL testada:** `https://s3.sa-east-1.amazonaws.com/ckan.saude.gov.br/SRAG/2021/INFLUD21-04-04-2024.csv`  
**Resultado:** `HTTP 403 Forbidden`

**Parsing de página HTML:** `https://opendatasus.saude.gov.br/dataset/srag-2020` e  
`https://opendatasus.saude.gov.br/dataset/srag-2021-a-2024`  
**Resultado:** 0 links CSV encontrados (página pode requerer JavaScript ou autenticação)

### Tentativa 2 — FTP DATASUS (fallback)

**Host:** `ftp.datasus.gov.br`  
**Conexão:** OK (autenticação anônima bem-sucedida)  
**Path testado:** `/dissemin/publicos/SIVEP_Gripe/Dados/` → `550 The system cannot find the path specified.`  
**Path testado:** `/dissemin/publicos/SIVEP_Gripe/` → `550 The system cannot find the file specified.`  
**Path disponível:** `/dissemin/publicos/` com 25 itens — nenhum relacionado a SRAG/SIVEP_Gripe

### Tentativa 3 — TabNet (validação cruzada)

Não executada (TabNet é fonte de validação, não de extração completa).

---

## Estado resultante

- `srag_manaus.parquet` permanece STUB (`is_stub=True`, `n_covid=0` em 12 meses)
- Tarefas 2.1 e 2.3 (revalidação cruzada) **ABORTADAS**
- Tarefas 2.2 (refactor loader) e 2.4 (correção diagnóstico) executadas por serem independentes do SRAG

---

## Cenários de continuação (aguardando decisão do autor)

| Cenário | Ação | Implicação |
|---------|------|------------|
| A — Reagendar | Re-executar Tarefa 2.1 em outra sessão/rede | Fase 2 permanece incompleta até SRAG real |
| B — TabNet (amostra) | Extrair contagens mensais via TabNet manualmente | Disponível apenas como arquivo TXT/CSV de totais, sem microdados |
| C — Proxy SIH | Usar `n_obitos` SIH como proxy SRAG COVID (subnotificado) | Degrada qualidade do BI; aceitar como paliativo com nota metodológica |
| D — Desacoplamento | Publicar Paper 1 sem validação cruzada SRAG (Caminho C definitivo) | Justificar indisponibilidade de dados como limitação metodológica |

---

## Próximos passos quando SRAG ficar disponível

1. Executar `scripts/download_sivep_gripe.py` com a URL correta (verificar página OpenDataSUS atualizada)
2. Re-executar `scripts/extract_srag_manaus.py` para substituir o stub
3. Re-executar `scripts/validate_bi_consistency.py` para completar a Tarefa 2.3
4. Atualizar `outputs/bi_dimensional_decision.json` com `decision_method: "pca_validated"`

---

*Gerado automaticamente ao término do diagnóstico de rede — Fase 2 Tarefa 2.1.*
