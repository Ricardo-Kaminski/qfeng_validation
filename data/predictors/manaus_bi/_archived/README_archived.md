# Arquivos Arquivados — Fase 1 BI Manaus

Arquivados em Tarefa 2.D (Fase 2.1.5 reorientada, 26/abr/2026).

## Conteúdo

### toh_fvs_am_fase1/

`toh_uti_manaus_mensal.parquet` — TOH UTI adulto COVID Manaus, granularidade mensal (12 meses).

Fonte primária: boletins epidemiológicos FVS-AM/SES-AM 2020-2021.
Construído na Fase 1 Tarefa 1.1 (commit `236a4ea`).

**Por que arquivado:** Granularidade mensal substituída por semanal (SE) em Fase 2.1.5.
Substituto: `derived/toh_semanal_manaus.parquet` (73 SEs, interpolação linear FVS-AM).

### srag_stub_fase1/

`srag_manaus_stub.parquet` — SRAG Manaus STUB (is_stub=True, n_covid=0 em todos os registros).

Construído na Fase 1 Tarefa 1.2 (commit `96b8bb9`) antes do acesso aos INFLUD reais.
OpenDataSUS retornou HTTP 403; FTP DATASUS path ausente na época.

**Por que arquivado:** Substituído por dados reais SIVEP-Gripe em Fase 2.1.5.
Substituto: `derived/srag_semanal_manaus.parquet` (73 SEs, is_stub=False, n_covid=21.212).

## Restrição

NÃO deletar estes arquivos. Mantidos para auditoria forense e reprodutibilidade.
Referenciados em: `outputs/relatorio_fase1_bi_bivariado.md`, `outputs/relatorio_fase2_bi_bivariado.md`.
