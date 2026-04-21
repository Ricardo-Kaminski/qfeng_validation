# Q-FENG — Arquitetura Resumo para Claude Code
## Referência teórica operacional (não modificar sem aprovação do usuário)

---

## Arquitetura em três níveis recursivos

O Q-FENG opera como um Sistema Viável (VSM de Beer) em três níveis recursivos.
Cada nível tem sua própria instância S1–S5.

### Macro (jurisdição nacional)
- S5: pilhas jurisdicionais → CF/88, LGPD, PL 2338/2023
- S1: ecossistema nacional de IA
- Escopo no PoC: regime brasil (CF/88, Lei 8.080/90, Lei 8.142/90)

### Meso (setor institucional)
- S5: normas ministeriais setoriais → Lei 8.080/90, LOSAN, normas MDA
- S1: aplicações de IA da instituição
- Escopo no PoC: portarias SUS, PNS 2024-2027, PPA 2024-2027

### Micro (inferência individual)
- S5: predicados Clingo + requisitos do modelo
- S1: inferências individuais; θ operando em tempo real
- Escopo no PoC: predicados gerados pelo E3, testados no E5

### Transição Meso→Micro (CRÍTICO)
NÃO é mudança de escala — é mudança de natureza operativa:
- Em Meso: S5 é texto normativo que requer interpretação humana
- Em Micro: a interpretação já ocorreu via pipeline C1
  Princípios (ex: `equidade_regional` da Lei 8.080/90) → predicados Clingo executáveis
- Isso é o que o pipeline C1 faz: é a operacionalização da interpretação normativa

---

## Cinco canais inter-nível

| Canal | Direção | Cor nos diagramas | Função |
|-------|---------|-------------------|--------|
| Cascata Normativa | ↓ | âmbar | Propagação de normas Macro → Meso → Micro |
| Sinal Algédônico | ↑ | coral | Alertas de violação Micro → Meso → Macro |
| Feedback de Aprendizado | ↓ | verde | Atualização de pesos e predicados |
| HITL | ↕ | azul tracejado | Intervenção humana em qualquer nível |
| Sincronização Ontológica | ↔ | roxo pontilhado | Consistência entre bases de conhecimento |

---

## Motor simbólico: Clingo ASP

**Engine escolhido: Clingo 5.7+ (University of Potsdam)**

Razão da escolha (DOCUMENTAR no código):
- Clingo preserva a primazia simbólica do Q-FENG
- dPASP foi REJEITADO porque inverte a relação de controle:
  dPASP superpõe uma camada neural sobre a arquitetura Q-FENG,
  subordinando o simbólico ao neural — o oposto da intenção arquitetural
- No Q-FENG: neural detecta padrões → simbólico decide e corrige

Uso no pipeline:
- E3: gerar predicados .lp via Clingo Python API (validação sintática)
- E5: resolver cenários de teste via clingo.Control().solve()
- Clingo Python API: `import clingo; ctl = clingo.Control()`

---

## Ângulo de fase θ (métrica central do Q-FENG)

θ mede a coerência entre predições neurais e normas institucionais.

| Regime θ | Interpretação | Ação |
|----------|---------------|------|
| θ ≈ 0° | Interferência construtiva | Decisão aprovada |
| 45° < θ < 135° | Zona ambígua | Escalamento HITL |
| θ ≈ 180° | Interferência destrutiva | Bloqueio / Circuit Breaker |

No pipeline C1:
- θ não é calculado diretamente (isso é o C2, fase futura)
- O E5 simula cenários onde θ seria destrutivo → falha constitucional
  ou onde θ seria construtivo → aprovação correta

---

## Citação canônica (usar em docstrings e comentários de código)

KAMINSKI, Ricardo S. Quantum-Fractal Neurosymbolic Governance (Q-FENG):
A Cybernetic Architecture for Ontological Friction Mitigation in Sociotechnical
Systems of Critical Infrastructure. SSRN, 17 mar 2026.
DOI: 10.2139/ssrn.6433122
