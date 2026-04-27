# Setup Parser .dbc — Fase 2.1.5-bis

**Data:** 2026-04-27  
**Branch:** caminho2

## Stack final utilizado

**Fallback B: blast.dll (MSVC) + ctypes + parser DBF manual**

pysus (primário) e pyreaddbc (Fallback A) foram tentados e falharam em
compilação no Windows: o arquivo `_readdbc.c` inclui `unistd.h` (header
POSIX), incompatível com MSVC mesmo com Visual Studio 18 instalado.

Solução: compilar `blast.c` de Mark Adler (zlib contrib) como DLL Windows
via MSVC + wrapper ctypes em Python. O formato DBC DATASUS adiciona 4 bytes
de pré-cabeçalho antes do stream blast canônico (skip=4 → offset=header_size+4).

## Comando de instalação executado

```
# Nenhum pip install de parser necessário — blast.dll compilada via MSVC:
cl.exe /LD /Fe:blast.dll /O2 /nologo blast_wrap.c blast.c
# (blast.c: Mark Adler, zlib/contrib/blast, SHA256 verificado)
```

Parser Python: `ctypes` (stdlib) + função `read_dbc()` embutida nos scripts.  
Leitor DBF: `struct` (stdlib), sem dependências externas.  
DLL salva em: `C:\Workspace\academico\qfeng_validacao\blast.dll`

## Versão do parser

- blast.c: zlib contrib (Mark Adler) — 17.180 bytes (baixado 2026-04-27)
- blast.dll: compilado MSVC 14.50.35717 — 103.936 bytes
- Python ctypes wrapper: embutido em scripts da Fase 2.1.5-bis

## Smoke test — LTAM2001.dbc (jan/2020, 8.585 bytes)

| Métrica | Valor |
|---|---|
| n_linhas | 680 |
| n_cols | 28 |
| Razão de compressão | 9.8× (74.800 bytes não-comprimidos) |

**Lista de colunas:**
CNES, CODUFMUN, REGSAUDE, MICR_REG, DISTRSAN, DISTRADM, TPGESTAO, PF_PJ,
CPF_CNPJ, NIV_DEP, CNPJ_MAN, ESFERA_A, ATIVIDAD, RETENCAO, NATUREZA,
CLIENTEL, TP_UNID, TURNO_AT, NIV_HIER, TERCEIRO, TP_LEITO, CODLEITO,
QT_EXIST, QT_CONTR, QT_SUS, QT_NSUS, COMPETEN, NAT_JUR

**Primeiras 3 linhas (seleção):**
```
CNES=2017768, CODUFMUN=130002, CODLEITO=03, QT_EXIST=2, COMPETEN=202001
CNES=2017768, CODUFMUN=130002, CODLEITO=10, QT_EXIST=4, COMPETEN=202001
CNES=2017768, CODUFMUN=130002, CODLEITO=33, QT_EXIST=8, COMPETEN=202001
```

**Distribuição CODUFMUN (top 5):**
```
130260 (Manaus): 297  |  130340: 18  |  130380: 16  |  130406: 14  |  130420: 13
```

**Distribuição CODLEITO (top 5):**
```
45: 91  |  33: 88  |  03: 87  |  43: 79  |  10: 54
UTI adulto (74-83): 53 registros
```

## Sanity checks

| Check | Resultado |
|---|---|
| n_linhas > 100 | OK (680) |
| n_cols >= 28 | OK (28) |
| CODUFMUN contém Manaus (130260) | OK (297 registros) |
| CODLEITO contém UTI 74-83 | OK (53 registros, principais: 75, 78) |

**RESULTADO GERAL: PASSOU**
