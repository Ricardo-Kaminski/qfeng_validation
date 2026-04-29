# Arquivo Pré-Redesenho — Braços B3a/B4a/B5

**Data:** 29/abr/2026
**Contexto:** Descoberta de falhas arquitetônicas críticas nos braços B3, B4 e B5
do experimento adversarial CLT da Frente 2 do projeto Q-FENG.

## Resumo das falhas

| Braço | Arquivado como | Falha | Validade residual |
|-------|---------------|-------|-------------------|
| B3 | B3a | Scaffolding ingênuo (predicados estáticos, sem solver) | Achado secundário: efeito de prompting estruturado |
| B4 | B4a | Ventriloquismo Q-FENG (LLM imita Q-FENG via prompt) | Achado secundário: teste de imitação de sistema |
| B5 | B5 | Vazamento θ no prompt (violação VSM opacidade hierárquica) | Cautionary tale pedagógico |

## Estrutura

```
_archive_pre_redesenho_29abr2026/
├── README.md          (este arquivo)
├── B3a/               (600 JSONs — scaffolding ingênuo)
│   ├── README.md
│   └── *.json
├── B4a/               (600 JSONs — ventriloquismo Q-FENG)
│   ├── README.md
│   └── *.json
└── B5/                (69 JSONs — vazamento θ)
    ├── README.md
    └── *.json
```

## Documentação completa

- Retrospectiva arquitetônica: `artefatos/notas_metodologicas/B5_RETROSPECTIVA_ARQUITETURA_29abr2026.md`
- Plano de redesenho: `artefatos/briefings/PROMPT_CLAUDECODE_P_FASE1_ARQUIVAMENTO_E_SETUP.md`
- Snapshot forense pré-arquivamento: `artefatos/snapshots/PRE_REDESENHO_29abr2026/`

## Referência

Beer, S. (1979). *The Heart of Enterprise*. Wiley.
Beer, S. (1985). *Diagnosing the System for Organizations*. Wiley.
