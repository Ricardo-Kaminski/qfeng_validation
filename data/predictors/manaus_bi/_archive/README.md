# Arquivo: _archive — TOH pré-Fase 2.1.5-bis

## Conteúdo

| Arquivo | Versão | Source | Linhas |
|---------|--------|--------|--------|
| `toh_semanal_manaus_FASE215_PRE_BIS.parquet` | Fase 2.1.5 (FVS-AM) | FVS-AM boletins 2020-2021 (interpolado mensalmente) | 73 |

## Por que este backup existe

Durante a Fase 2.1.5 (26/abr/2026), o TOH semanal de Manaus foi calculado via **interpolação de patamares constantes** a partir dos boletins mensais da FVS-AM/SES-AM.
A Fase 2.1.5-bis (27/abr/2026) identificou que o pipeline original usava `sep=";"` para ler os CSVs DEMAS-VEPI, que são separados por vírgula (`sep=","`).
Isso causava descarte falso-negativo dos ~6.945 registros de Manaus, forçando fallback para a fonte estimada FVS-AM.

## Diferença metodológica

| | Fase 2.1.5 (FVS-AM) | Fase 2.1.5-bis (DEMAS-VEPI) |
|---|---|---|
| Fonte | FVS-AM/SES-AM boletins (mensal) | DEMAS-VEPI microdados (diário por CNES) |
| Granularidade original | Mensal → interpolado para SE | Diário → agregado para SE |
| Tipo | Estimado (`is_estimated=True`) | Real (`is_estimated=False` para 71/74 SEs) |
| TOH pico | ~0.85 (85%) | 2.115 (211%) |
| Método denominador | Capacidade declarada FVS-AM | CNES-LT municipal (288→395 leitos) |
| SE coverage | 73 SEs | 74 SEs |

## Decisão arquitetônica

A Fase 2.1.5-bis adotou microdados primários DEMAS-VEPI como fonte canônica do TOH.
O TOH > 1.0 no pico (2021-W03 = 211%) é historicamente correto: a crise hospitalar de Manaus em janeiro/2021
envolveu uso de leitos emergenciais não declarados no CNES-LT, configurando **Fricção Ontológica** entre os sistemas.

O arquivo `toh_semanal_manaus_FASE215_PRE_BIS.parquet` é preservado exclusivamente como evidência forense da
trajetória metodológica, não para uso analítico.

## Referência

- Commit que introduziu a versão FVS-AM: `f4e652c` (feat(bi-fase2): TOH semanal Manaus via interpolacao linear FVS-AM)
- Commit que introduziu a versão DEMAS-VEPI: `d4b4109` (task4: juncao numerador x denominador)
- Commit que arquivou este backup: `e5d9774` (task2) / confirmado em `d4b4109`
