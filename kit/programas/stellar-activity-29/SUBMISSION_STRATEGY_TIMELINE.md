# Estratégia de Submissões e Linha do Tempo
## Programa "Stellar Activity × Critical Phenomena" — 29 Papers

> **Documento de referência estratégica.** Carregar no Projeto Master
> (não nos projetos individuais de cada paper). Atualizar o campo
> "Status atual" mensalmente.

---

## Princípios Estratégicos

### 1. Escrever enquanto espera
O tempo de revisão editorial é 4–8 semanas. Nunca esperar passivamente.
Regra: no dia da submissão de um paper, iniciar imediatamente o próximo.

### 2. Trilhas paralelas
Alguns papers usam dados e conceitos completamente independentes
entre si. Estes podem ser escritos em paralelo — um por semana cada,
com sessões alternadas no Claude Projects.

Critério de paralelismo: dois papers podem ser escritos em paralelo
se não compartilham dados brutos nem dependem dos resultados numéricos
um do outro. Dependência de *conceitos* (P2 usa vocabulário de P1) é
aceitável — dependência de *números* (P11 usa β medido em P2) exige sequência.

### 3. RNAAS como ferramenta de prioridade
Para qualquer resultado piloto pronto antes do paper completo — por exemplo,
o expoente α para uma única amostra de estrelas M antes de ter toda a análise
cruzada — publicar uma nota de 1 página no RNAAS (IOP, sem revisão formal,
sem custo). Estabelece prioridade na data, cria citação futura no paper completo.

### 4. Desk rejection é neutro
Se a revista primária enviar desk rejection (sem revisão, em < 2 semanas),
tratar como sinal de re-direcionamento, não de falha. Redirecionar para
backup imediatamente sem nenhuma alteração no manuscrito.

### 5. arXiv é obrigatório
Postar em astro-ph.SR no mesmo dia de cada submissão.
Benefícios: estabelece prioridade independente do processo editorial,
gera citações enquanto o paper está em revisão, aumenta visibilidade.

---

## Mapa de Dependências

### Dependências fortes (requerem resultado numérico do paper anterior)
```
P1 → P9      (α de flares é input de P9)
P2 → P11     (β de P2 é input de P11)
P2 → F3      (β e γ são inputs para Hyperscaling em F3)
P4 → F16     (H de DFA é base para MFDFA)
P5 → F8      (vocabulário RG e metodologia ODR)
P11 → F3     (expoentes β, γ necessários para verificação Hyperscaling)
F7 → F10     (crossover exponent de F7 referenciado em F10)
F8 → F10     (parâmetro de ordem φ definido formalmente em F8)
```

### Dependências fracas (conceito/vocabulário, podem sobrepor 50%)
```
P2 usa vocabulário estabelecido em P1
P5 se beneficia de P2 estar submetido (terminologia de β, ponto fixo)
P8 se beneficia de P2+P5 (Landau + RG = linguagem compartilhada)
F1 se beneficia de P5 (ponto fixo RG → bifurcação de Parker)
F2 se beneficia de F1 (saturação de Ṁ é análoga à de P2)
F4 se beneficia de P4+P8 (mínimos de Maunder + ciclos de Landau)
F5 se beneficia de P2 (parâmetro de ordem φ já definido)
F6 se beneficia de P11 (expoentes críticos como referência)
```

### Papers completamente independentes entre si (paralelos ideais)
```
P3  ∥  P6    (ambos analíticos, diferentes indicadores)
P1  ∥  P4    (Kepler vs Mount Wilson — dados distintos)
P7  ∥  P8    (Kepler vs Mount Wilson — dados distintos)
F1  ∥  F4    (teoria de Parker vs gap VP — sem sobreposição)
F8  ∥  F9    (Güdel-Benz expoente vs flares rádio — diferentes)
F14 ∥  F12   (ROSAT vs GALEX — surveys distintos)
F15 ∥  F17   (terremotos vs percolação — sem sobreposição)
```

---

## Linha do Tempo — 29 Meses

### Meses 1–4 : Fundação analítica
*Objetivo: estabelecer os dois papers mais rápidos e o pipeline base.*

| Semana | Trilha A | Trilha B | Ação editorial |
|--------|----------|----------|----------------|
| 1–2 | Escrever P3 | Escrever P6 | — |
| 3 | Revisar P3 | Revisar P6 | — |
| 4 | Submeter P3 → ApJ L | Submeter P6 → ApJ L | arXiv simultâneo |
| 5–7 | Escrever P1 (pipeline Kepler) | — | Aguardar P3/P6 |
| 8 | Submeter P1 → ApJ L | — | — |
| 9–11 | Escrever P2 (Wright+2011) | Escrever P4 (Mount Wilson) | Resp. referee P3/P6 |
| 12 | Submeter P2 → ApJ | Submeter P4 → Solar Phys | arXiv simultâneo |

**RNAAS sugerido:** No mês 2, ao completar o ajuste de α para M dwarfs
em P1, publicar nota RNAAS com resultado piloto (1 pág, 1 figura).

---

### Meses 5–8 : Expansão do núcleo
*Objetivo: completar os papers de método (P5, P7) e teoria (P8).*

| Semana | Trilha A | Trilha B | Ação editorial |
|--------|----------|----------|----------------|
| 17–19 | Escrever P9 (Kepler+McQuillan) | Escrever P5 (RG fixed point) | Resp. referee P1/P2 |
| 20 | Submeter P9 → ApJ L | Submeter P5 → ApJ | arXiv |
| 21–23 | Escrever P7 (finite-size) | Escrever P8 (Landau) | Resp. referee P4 |
| 24 | Submeter P7 → ApJ | Submeter P8 → Solar Phys | arXiv |

**Nota sobre P8:** Deve ser submetido depois que P2 tiver pelo menos
recebido relatório de referees (não precisa estar aceito). P8 cita
P2 como "submetido" (under review), o que é prática editorial normal.

---

### Meses 9–12 : Completar Fase 1
*Objetivo: P10, P11, P12 + iniciar Fase 2 em paralelo.*

| Semana | Trilha A | Trilha B | Ação editorial |
|--------|----------|----------|----------------|
| 33–35 | Escrever P10 (MUSCLES) | Escrever F1 (Parker bifurcação) | Resp. referee P5/P7/P8 |
| 36 | Submeter P10 → AJ | Submeter F1 → Solar Phys | arXiv |
| 37–39 | Escrever P11 (universality class) | Escrever F2 (saturação Ṁ) | Resp. referee P9 |
| 40 | Submeter P11 → ApJ | Submeter F2 → Ap&SS | arXiv |
| 41–43 | Escrever P12 (habitabilidade) | Escrever F4 (VP gap) | Resp. referee P10/P11 |
| 44 | Submeter P12 → ApJ | Submeter F4 → ApJ L | arXiv |

**Marco:** Ao final do mês 12, toda a Fase 1 está submetida.
A essa altura, 4–6 papers da Fase 1 já estarão aceitos ou em revisão final.

---

### Meses 13–16 : Fases 2–3 completas
*Objetivo: Vento estelar (F1–F3) e transições HR (F4–F7).*

| Semana | Trilha A | Trilha B | Ação editorial |
|--------|----------|----------|----------------|
| 49–51 | Escrever F3 (r_A = ξ) | Escrever F5 (dividing line) | Resp. referee P12/F1/F2 |
| 52 | Submeter F3 → ApJ | Submeter F5 → ApJ | arXiv |
| 53–55 | Escrever F6 (0.35 M☉) | Escrever F7 (ultracool GB) | Resp. referee F3/F4/F5 |
| 56 | Submeter F6 → ApJ | Submeter F7 → ApJ L | arXiv |

---

### Meses 17–20 : Fase 4 — Rádio
*Objetivo: F8, F9, F10 + iniciar Fase 5.*

| Semana | Trilha A | Trilha B | Ação editorial |
|--------|----------|----------|----------------|
| 61–63 | Escrever F8 (Güdel-Benz expoente) | Escrever F9 (flares rádio SOC) | Resp. referee F6/F7 |
| 64 | Submeter F8 → ApJ | Submeter F9 → ApJ L | arXiv |
| 65–67 | Escrever F10 (parâmetro de ordem M7) | Escrever F14 (ROSAT revisitado) | Resp. referee F8/F9 |
| 68 | Submeter F10 → ApJ L | Submeter F14 → AJ | arXiv |

---

### Meses 21–25 : Fase 5 — Surveys de larga escala
*Objetivo: F11–F14 (eROSITA, GALEX, XMM, ROSAT).*

| Semana | Trilha A | Trilha B | Ação editorial |
|--------|----------|----------|----------------|
| 77–79 | Escrever F12 (GALEX) | — | Resp. referee F10/F14 |
| 80 | Submeter F12 → ApJ | — | arXiv |
| 81–83 | Escrever F13 (4XMM) | Escrever F15 (SOC unificado) | Resp. referee F12 |
| 84 | Submeter F13 → ApJ | Submeter F15 → Sci.Reports | arXiv |
| 85–87 | Escrever F11 (eROSITA) | Escrever F17 (percolação) | Resp. referee F13/F15 |
| 88 | Submeter F11 → ApJ | Submeter F17 → ApJ | arXiv |

**Nota sobre F11:** Verificar disponibilidade do eROSITA DR1 antes do
mês 21. Se ainda não disponível, inverter com F13 (4XMM) na ordem.

---

### Meses 26–29 : Fase 6 — Interdisciplinar + buffer
*Objetivo: F16 (MFDFA) e buffer para revisões acumuladas.*

| Semana | Trilha A | Trilha B | Ação editorial |
|--------|----------|----------|----------------|
| 97–99 | Escrever F16 (MFDFA) | — | Resp. referee F11/F17 |
| 100 | Submeter F16 → ApJ | — | arXiv |
| 101–104 | Buffer: revisões 2ª rodada | Buffer: revisões 2ª rodada | Todas pendentes |
| 105–116 | Buffer extra + papers bonus | — | Consolidação |

---

## Tabela Mestre de Periódicos

### Fase 1 — Núcleo

| Paper | Título curto | Primário | IF | Backup | IF | Editora |
|-------|-------------|---------|---|--------|---|---------|
| P1 | SOC universalidade | ApJ Letters | 8.9 | Solar Physics | 3.0 | IOP / Springer |
| P2 | Saturação = fase 2ª ordem | ApJ | 5.0 | New Astronomy | 2.0 | IOP / Elsevier |
| P3 | Relações de escala | ApJ Letters | 8.9 | Ap&SS | 2.0 | IOP / Springer |
| P4 | Critical slowing down | Solar Physics | 3.0 | Space Weather | 5.5 | Springer / Wiley |
| P5 | L_X vs Φ: ponto fixo RG | ApJ | 5.0 | New Astronomy | 2.0 | IOP / Elsevier |
| P6 | Fluxo basal: ponto fixo trivial | ApJ Letters | 8.9 | Ap&SS | 2.0 | IOP / Springer |
| P7 | Finite-size scaling | ApJ | 5.0 | New Astronomy | 2.0 | IOP / Elsevier |
| P8 | Landau para ciclos | Solar Physics | 3.0 | ApJ | 5.0 | Springer / IOP |
| P9 | Rossby como parâmetro SOC | ApJ Letters | 8.9 | New Astronomy | 2.0 | IOP / Elsevier |
| P10 | MUSCLES expoentes críticos | AJ | 3.6 | New Astronomy | 2.0 | IOP / Elsevier |
| P11 | Classe de universalidade | ApJ | 5.0 | Ap&SS | 2.0 | IOP / Springer |
| P12 | Habitabilidade: diagrama de fases | ApJ | 5.0 | Adv. Space Res. | 2.6 | IOP / Elsevier |

### Fases 2–4 — Vento, HR, Rádio

| Paper | Título curto | Primário | IF | Backup | IF | Editora |
|-------|-------------|---------|---|--------|---|---------|
| F1 | Parker = bifurcação sela-nó | Solar Physics | 3.0 | Ap&SS | 2.0 | Springer |
| F2 | Saturação Ṁ = fenômeno crítico | Ap&SS | 2.0 | New Astronomy | 2.0 | Springer / Elsevier |
| F3 | Raio de Alfvén = comprimento ξ | ApJ | 5.0 | MNRAS | 4.9 | IOP / Oxford |
| F4 | VP gap = coexistência de fases | ApJ Letters | 8.9 | Solar Physics | 3.0 | IOP / Springer |
| F5 | Dividing line = fronteira de fase | ApJ | 5.0 | New Astronomy | 2.0 | IOP / Elsevier |
| F6 | Transição 0.35 M☉ | ApJ | 5.0 | New Astronomy | 2.0 | IOP / Elsevier |
| F7 | Quebra de universalidade M7 | ApJ Letters | 8.9 | JHEAP | 4.5 | IOP / Elsevier |
| F8 | Güdel-Benz: expoente crítico | ApJ | 5.0 | Solar Physics | 3.0 | IOP / Springer |
| F9 | Flares rádio = SOC | ApJ Letters | 8.9 | JHEAP | 4.5 | IOP / Elsevier |
| F10 | Transição rádio/X em M7 | ApJ Letters | 8.9 | JHEAP | 4.5 | IOP / Elsevier |

### Fases 5–6 — Surveys e Interdisciplinar

| Paper | Título curto | Primário | IF | Backup | IF | Editora |
|-------|-------------|---------|---|--------|---|---------|
| F11 | eROSITA: distribuição de atividade | ApJ | 5.0 | A&A | 6.2 | IOP / EDP |
| F12 | GALEX: expoentes para 50k estrelas | ApJ | 5.0 | AJ | 3.6 | IOP |
| F13 | 4XMM: mecânica estatística coronal | ApJ | 5.0 | JHEAP | 4.5 | IOP / Elsevier |
| F14 | ROSAT revisitado | AJ | 3.6 | New Astronomy | 2.0 | IOP / Elsevier |
| F15 | Flares + sismos + neurônios | Sci. Reports | 4.6 | ApJ | 5.0 | Springer / IOP |
| F16 | Multifractalidade em Ca II | ApJ | 5.0 | Solar Physics | 3.0 | IOP / Springer |
| F17 | Percolação da rede magnética | ApJ | 5.0 | Solar Physics | 3.0 | IOP / Springer |

---

## Distribuição por Editora (projeção)

Considerando que ~80% dos papers serão aceitos nos alvos primários:

| Editora | Papers estimados | Periódicos |
|---------|-----------------|-----------|
| IOP (AAS) | ~19 | ApJ (9), ApJ L (7), AJ (2), RNAAS (1+) |
| Springer | ~6 | Solar Physics (4), Ap&SS (2) |
| Elsevier | ~3 | New Astronomy (2), JHEAP (1) |
| Springer Nature | ~1 | Scientific Reports |
| Oxford (MNRAS) | 0–1 | MNRAS (backup F3) |

Esta distribuição cobre as exigências CAPES de presença em Wiley,
Elsevier e Springer. A dominância IOP é esperada dado o escopo do programa.

---

## Estratégia para Desk Rejections

Se um paper receber desk rejection do alvo primário, o protocolo é:

1. Verificar se o motivo é escopo (mais comum) ou qualidade (raro)
2. Se escopo: submeter ao backup no mesmo dia, sem alterações
3. Se qualidade: abrir conversa no projeto do paper com o relatório
   do editor e revisar seções específicas apontadas

Taxas históricas de desk rejection por revista:
- ApJ Letters: ~30% (escopo muito focado)
- ApJ: ~15%
- Solar Physics: ~10%
- New Astronomy: ~5%

Para papers da Fase 6 (interdisciplinar), o desk rejection no ApJ
é mais provável por escopo amplo. Nesses casos, Scientific Reports
é o alvo natural — política editorial ampla, IF competitivo.

---

## Gestão de Revisões Simultâneas

A partir do mês 6, haverá múltiplos papers em revisão simultaneamente.
Regra de priorização para respostas a referees:

1. Papers mais antigos em revisão têm prioridade absoluta
2. Prazo típico para resposta: 60 dias após recebimento do relatório
3. Usar o prompt padrão "Revisão de Referee" do `UNIVERSAL_PAPER_CONTEXT.md`
4. Atualizar `paper_state.md` com status "Em revisão" imediatamente ao receber

Template de controle de revisões pendentes (manter no Projeto Master):

```
REVISÕES PENDENTES — atualizar semanalmente

Paper | Submetido | Relatório recebido | Prazo resposta | Status
P1    | MM/AAAA   | MM/AAAA            | MM/AAAA        | [status]
P2    | MM/AAAA   | MM/AAAA            | MM/AAAA        | [status]
...
```

---

## Indicadores de Progresso

Métricas a monitorar mensalmente:

| Indicador | Meta mensal | Meta anual |
|-----------|------------|-----------|
| Papers submetidos | 1 | 12 |
| Papers aceitos | 0.6–0.8 | 7–10 |
| Papers no arXiv | 1 | 12 |
| Revisões respondidas | variável | todas dentro do prazo |
| Papers em produção ativa | 1–2 | — |

---

*Estratégia v1.0 — Atualizar status mensalmente no Projeto Master*
