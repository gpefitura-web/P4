# paper_state_v5.md — P4
# Critical Slowing Down Near Stellar Activity Minima
# Versão 5.0 · Fecho da conversa de consolidação · 2026-08-01

---

## 1 · O que mudou nesta conversa

Três coisas, em ordem de consequência.

**(a) A auditoria A1–A6 está completa e o catálogo está congelado.** 112 linhas, nada em grau
C ou X. `baliunas_table2_full.csv` verificado íntegro (8 kB) após upload.

**(b) Os subsídios para a seleção da amostra foram levantados — e revelaram um confundimento
que o desenho original não controlava.** Os grupos candidatos diferem sistematicamente em cor e
nível de atividade, não só em classe de variabilidade. Detalhe em `P4_DECISION_SUPPORT_6.1.md`.

**(c) A decisão de amostra foi suspensa por descoberta de fonte nova.** Baliunas+1995 tem 31
anos; várias dessas estrelas foram seguidas por mais três décadas, e isso já está publicado de
forma homogênea. **HD 166620 — que a auditoria "derrubou" do grupo Maunder — é hoje o primeiro
análogo verdadeiro de mínimo de Maunder confirmado na literatura.** Ver §3.

---

## 2 · Estado da auditoria

| Unidade | Fonte | Estado | Achados |
|---|---|---|---|
| A1 | Baliunas+1995 | fechada | F1–F9 |
| A2 | Lockwood+2007 | fechada | F1–F7 |
| A3 | Egeland+2017 | fechada | F1–F6 |
| A4 | Dakos+2012 | fechada | F1–F8 |
| A5 | Peng+1994 | fechada | F1–F6 |
| A6 | Saar & Brandenburg 1999 | fechada | F1–F14 |
| **A9** | **Baum+2022** | **aberta — destrava Q1** | — |
| **A10** | **Luhn+2022** | **aberta** | — |
| **A11** | **A&A 2025 + Isaacson+2024 + CLS VI** | **aberta** | — |
| **A12** | **Noyes+1984** | **aberta — receita de R′_HK** | — |
| A7 | Scheffer+2009, Held & Kleinen 2004 | pendente (Introduction) | — |
| A8 | Usoskin+2017 | pendente (Discussion) | — |

30 decisões registradas (D01–D30) em `P4_RESEARCH_NOTEBOOK.md`.

---

## 3 · A descoberta que suspende a decisão de amostra

Baum+2022 (AJ 163, 183) publica **cinco décadas de atividade cromosférica em 59 estrelas tipo
solar**, unindo Mount Wilson (1966–2001) e California Planet Search/Keck HIRES (1996–). É o
conjunto do P4, estendido, homogeneizado e publicado — sem necessidade de garimpo estrela a
estrela.

**HD 166620** cicla a ~17 anos durante o Mount Wilson e fica plana depois de 2004. Luhn+2022
(ApJL 936, L23) preenche a lacuna com dados MWO adicionais (Oláh+2016) e fotometria APT de
~30 anos, e apresenta o caso como **o primeiro análogo verdadeiro de mínimo de Maunder**.

Isto reconcilia um aparente conflito da auditoria em vez de contradizê-lo: A1 mostrou que
Baliunas classifica HD 166620 como ciclo de 15,8 anos, FAP Excellent — e está correto para
1966–1991. A transição é posterior. **As duas afirmações são verdadeiras em épocas diferentes.**

**HD 4915** existe e é candidata documentada (Shah+2018); apenas não está em Baliunas+1995.
A1-F2 permanece correto; o que se esclarece é a proveniência do valor no catálogo antigo.

**Por que isso muda o desenho.** O P4 precisava de um objeto apanhado *atravessando* a transição
— CSD é uma afirmação sobre a aproximação à bifurcação, não sobre estados. HD 166620 é esse
objeto, com cobertura de cinco décadas. O teste temporal deixa de existir só para o Sol.

**Ressalvas já identificadas, a auditar em A9/A10:**

1. Luhn+2022 declara que não há garantia de concordância absoluta entre os quatro instrumentos
   (MW HKP-1, MW HKP-2, HIRES-1, HIRES-2). Um degrau instrumental espúrio infla exatamente φ₁ e
   σ² — os indicadores de CSD.
2. A lacuna observacional coincide com a transição. Se a *aproximação* não estiver amostrada, o
   teste temporal não é executável — e isso precisa ser dito de um jeito ou de outro.
3. Literatura de 2025 (A&A) conclui que estrelas de mínimo de Maunder são **muito raras**,
   contra a sugestão inicial do MWO. É a questão Q7 do protocolo e exige engajamento explícito.
4. CLS VI levanta a explicação concorrente de estrelas que "envelheceram para fora" de seus
   ciclos (*aged out*) — alternativa direta à interpretação de bifurcação.

---

## 4 · A questão do índice unificado — análise preliminar

Pergunta levantada: a análise poderia ser unificada em log R′_HK em vez do índice S?

**A favor, e o argumento é forte.** O índice S é instrumental (escala HKP-2 por definição,
A3 §3.1) e sensível à temperatura fotosférica — Baliunas observa que a atividade aparente cresce
com B−V primariamente por isso. A auditoria quantificou que os grupos candidatos diferem
sistematicamente em cor:

| Grupo | B−V mediana |
|---|---|
| `CYCLE` Excellent | 0,88 |
| `Flat`+`Flat?` | 0,73 |
| `Var` | 0,61 |
| `Long` | 0,49 |

R′_HK remove a contribuição fotosférica e normaliza pelo fluxo bolométrico. É a variável correta
para comparar estrelas de tipos diferentes **e para comparar o Sol com as estrelas** — e
Egeland+2017 já publica a Tabela 3 com medidas solares por ciclo em log R′_HK, de modo que o lado
solar existe pronto na mesma escala.

**Contra, ou pelo menos a ponderar.** A conversão usa o fator de correção de cor C_cf(B−V) de
Noyes+1984, que tem faixa de validade limitada; várias estrelas do P4 estão em B−V ≥ 0,9
(HD 23249 = 0,92; HD 160346 = 0,96; HD 32147 = 1,06) e podem cair fora. A subtração fotosférica
acrescenta sistemática própria.

**O ponto que decide o custo-benefício.** Para uma estrela isolada, com B−V fixo, S → R′_HK é
uma transformação monotônica fixa. Portanto:

- **O τ de Kendall é exatamente invariante** — é estatística de postos. Todos os testes de
  tendência do P4, solares e estelares, dariam numericamente o mesmo resultado.
- **φ₁ muda pouco** (a transformação é suave e as variações são pequenas).
- **A variância muda de escala**, o que importa para comparações entre estrelas.

Ou seja: **R′_HK ajuda a comparação entre grupos e entre Sol e estrelas, e é quase irrelevante
para a análise temporal dentro de cada objeto.** Isso é uma boa notícia — significa que a
migração pode ser feita para o eixo comparativo sem invalidar o eixo temporal, e que ela ataca
precisamente o confundimento de cor que os subsídios identificaram como o problema mais sério do
desenho de três grupos.

**Encaminhamento:** A12 estabelece a receita e seus limites. A decisão é humana e vem depois.

---

## 5 · Questões abertas

| # | Questão | Estado |
|---|---|---|
| **Q1** | Composição da amostra | **suspensa até A9** |
| Q2 | O que conta como "flat" (ρ CrB: `Long` / σ_S/S 1,0% / flat em Saar) | aberta |
| Q3 | Largura de banda gaussiana (σ = 1 ano vs 10% de Dakos) | aberta |
| Q4 | Componente solar de 44 anos num registro de 55 | aberta |
| Q5 | Binárias (HD 81809 composta; HD 219834A/B par resolvido) | aberta |
| Q6 | Problema de medida do grupo `Flat` | aberta |
| Q7 | Subgigantes no grupo `Flat` | aberta |
| **Q8** | **Migrar para log R′_HK?** | **nova — depende de A12** |
| **Q9** | **DFA volta a ser admissível para o subconjunto Baum?** | **nova — reaberta legitimamente por fonte nova; depende de A9** |

---

## 6 · Plano sequenciado

| # | Etapa | Depende de | Produto |
|---|---|---|---|
| 1 | **A9–A12 (Cowork)** | — | `audit/A9..A12`, tabelas na raiz, PDFs em `bib/` |
| 2 | A7 + A8 | — | Introduction e Discussion; fecha Q7 do protocolo |
| 3 | **Consolidação humana** | A1–A12 | `P4_SOURCE_VALUES.md` + `p4_star_catalog.csv`; decide Q1–Q9 |
| 4 | Reconstrução do pipeline | consolidação assinada | surrogates ARMA (D22), n_max + crossover (D26), sweep de largura de banda, troca de catálogo |
| 5 | Aquisição de dados reais | itens de ação §7 | Egeland T4 (solar); séries de Baum (estelares) |
| 6 | Análise | 4 + 5 | esperar enfraquecimento do sinal solar sob surrogates |
| 7 | Figuras | 6 | 4 figuras, estilo Super Mongo |
| 8 | Manuscrito | 6, 7 | — |

---

## 7 · Itens de ação — bloqueados no sandbox

| Item | Para quê | Domínio |
|---|---|---|
| Egeland+2017 Tabela 4 (série S solar calibrada, ciclos 15–24) | D18 — trilha solar | IOP |
| PDFs de A9–A12 | segunda rodada de auditoria | arXiv, IOP, A&A |
| Pevtsov 2016 (Ca II K composto) | contexto de D18 | Harvard Dataverse |
| Série S solar NSO | alternativa à Egeland T4 | NOAA |

**Contorno que já funcionou:** colocar os PDFs em `bib/` no repositório
`github.com/gpefitura-web/P4` e buscá-los de lá.

---

## 8 · Advertências que não devem se perder

1. **O resultado antigo φ₁(Var) > φ₁(Maunder), p = 0,029 não é evidência de CSD.** Após a
   auditoria, comparou três estrelas cíclicas contra duas cíclicas e uma `Long`. Não deve
   reaparecer em nenhuma versão do manuscrito.
2. **Espera-se que o sinal CSD solar enfraqueça** sob os surrogates ARMA (D22). Registrado antes
   de rodar, deliberadamente.
3. **O grupo `Flat` é medido perto do ruído.** Limiar < 1–1,5% contra piso instrumental de 0,8%
   (A2-F6) e precisão de longo prazo de 1,2–1,4% (D14). O contraste que sobrevive à objeção é em
   **φ₁**, não em variância.
4. **N uniforme por construção** enquanto se usar só Baliunas (D12) — dizer explicitamente em
   Methods. Se A9 trouxer as séries de Baum, esta propriedade **se perde** e o confundimento
   comprimento×grupo volta a ser real.
5. Toda cadeia número → `P4_SOURCE_VALUES.md` → `D##` → seção de artigo-fonte deve estar
   íntegra. Cadeia quebrada é bloqueio de submissão.
