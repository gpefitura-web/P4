# Recomendações para os itens pendentes

**Pedido do pesquisador (2026-11-24):** "Recomendações para todos." São **recomendações de Claude, não decisões** (D101). Cada uma traz base quantitativa e qualitativa, o risco e a alternativa mais forte. O pesquisador aceita, muda ou rejeita item a item. Ids de `inspecao/checks.csv`; resultados novos em `inspecao/saidas/17_recommendation_support.txt` (`3.19-01` a `3.19-05`; script `17_recommendation_support.py`, sintético sem valores de S onde indicado). Decisões já tomadas (D68–D100) não são repetidas.

## Resumo
| # | Item | Recomendação em uma linha |
|---|---|---|
| R1 | Q1: regra de binaridade das cinco `Flat` (I-06) | D13 mais exclusão dos 12 de B95 Apêndice B, que dá exatamente as cinco |
| R2 | Q1: D04/D11 (I-13) | manter D04/D11 e registrar a exceção declarada; lista de seleção datada antes de qualquer indicador |
| R3 | Hipótese de D90 | duas camadas: comparação de estados (confirmatória) e CSD temporal (exploratório, n = 1) |
| R4 | σ_S (D70) | conta A como principal, conta B como sensibilidade |
| R5 | Junção (D72) | descontinuidade declarada; indicador dentro da era Mount Wilson |
| R6 | D46 (D73) | aceitar com a ressalva de grau C |
| R7 | Layout (D77) | manter até a consolidação assinada |
| R8 | Q2 | classe de B95 como principal, Baum como camada de época |
| R9 | Q3 | varredura pré-registrada de remoção de tendência; σ = 1 ano como padrão |
| R10 | Q4 | declarar como confundidor, sem controlar |
| R11 | Q5 | excluir HD 81809 e HD 219834A dos controles |
| R12 | Q6 | apresentar o limiar `Flat` com o piso e a precisão de B95 lado a lado |
| R13 | Q7 | manter subgigantes como subgrupo declarado, com análise com e sem |
| R14 | Q9 | manter o DFA fora |
| R15 | Q10 | tratar como parte da hipótese, sem estimar tempo de decaimento |
| R16 | Q11 | declarar o confundidor de HD 10700, sem excluir nem estimar |

---

## R1 — Regra de binaridade das cinco `Flat` (Q1, I-06)
**Recomendação:** regra = D13 (exclui as estrelas-padrão) **mais** exclusão das estrelas listadas no Apêndice B de B95 como binárias (12 estrelas). Registrar a regra.
**Quantitativa:** as sete `Flat`/`Flat?` fora das padrões (HD 10700, 23249, 43587, 158614, 178428, 182572, 190360) menos as 12 do Apêndice B (HD 3443, 39587, 76572, 81809, 88355, 114378, 124570, 137107, 141004, 156026, 158614, 178428; A1 §2.5) dão **exatamente** HD 10700, 23249, 43587, 182572, 190360 (`3.19-01`, PASS). A regra reconstrói as cinco sem ajuste.
**Qualitativa:** é uma regra de fonte primária (B95), anterior aos dados do P4, e coincide com o que v4/v6 já usavam; HD 158614 e 178428 têm binaridade declarada na fonte.
**Risco/alternativa:** o Apêndice B não resolve binárias não listadas. Alternativa: sete, só com D13 (N maior, mais contaminação por binárias).

## R2 — D04/D11 contra medidas já feitas (Q1, I-13)
**Recomendação:** **manter D04 e D11** e registrar, em nova D##, uma **exceção declarada**: a seleção foi informada por medidas descritivas prévias (σ_S/S das quatro `Flat` na CLS V e o degrau por estrela). Fixar a **lista final de estrelas por escrito e datada antes de calcular qualquer indicador temporal**.
**Quantitativa:** as medidas vistas são descritivas (σ_S/S de 0.72 a 1.49 %; degrau de 4.47 % entre estrelas, `3.5-02`); **nenhum indicador temporal (AR(1), variância em janela, τ) foi calculado em qualquer estrela real** até aqui; a pertinência à `Flat` vem da classe de B95 e de Baum, não de σ_S/S.
**Qualitativa:** refazer a seleção "como se" não tivesse visto as medidas é impossível e fingiria o contrário; declarar é a prática que o protocolo (D04, §1) pede quando a ordem foi violada.
**Risco/alternativa:** um revisor pode apontar o uso prévio; a defesa é a lista datada antes do indicador e o critério de pertinência independente das medidas.

## R3 — Enunciado da hipótese de D90
**Recomendação:** duas camadas, declaradas antes de rodar.
- **H1 (confirmatória, dado grau A):** a variabilidade (σ_S, receita R4) de HD 166620 no grande mínimo é menor que nos mínimos de ciclo (reprodução de Luhn+2022 §3.1, três valores publicados). Não é CSD; é o diagnóstico de estado.
- **H2 (exploratória, grau do teste: poder baixo):** no segmento anterior à transição, os indicadores anuais (AR(1) e variância do resíduo) têm tendência **positiva** (τ de Kendall unilateral, p < 0.05 por surrogates com as lacunas e a interpolação de D98). **Critério de não suporte:** τ ≤ 0 ou p ≥ 0.05 nos dois indicadores. Um resultado de não suporte é reportado como "não suportado com poder baixo", **não** como refutação.
**Quantitativa:** só **HD 166620** tem segmento ≥ 24 anos antes da transição (segmento de Mount Wilson de 30 anos, `17_recommendation_support.txt` §2); a aproximação em 1995–2002 tem 8 pontos (D46) e é grau C (D58, D86): é o trecho que preenche a lacuna de 6.9 anos de Baum. HD 101501 tem cerca de 12 anos antes do estado plano (1968–1980, Baum §4.1), abaixo do piso de 24 anos (D100). O poder do τ é AUC 0.57–0.67 (`3.18-05`; D100). Logo H2 tem n = 1 e poder baixo.
**Qualitativa:** é o que D90 pede (hipótese testável com precedente ausente) e o que Scheffer e Held & Kleinen exigem (falso negativo declarado; séries longas). As demais estrelas dão a distribuição de referência dos indicadores onde não há transição (taxa de falso positivo sob surrogates).
**Risco/alternativa:** reduzir a hipótese à comparação de estados (H1 só) é mais honesto sobre o que os dados permitem, ao custo de abandonar o CSD como teste; manter só H2 não é recomendável.

## R4 — Receita de σ_S (D70)
**Recomendação:** adotar a **conta A** (σ do intervalo inteiro, menos o ruído em quadratura) como principal; reportar a **conta B** (por estação) como sensibilidade; registrar por nova D## que o passo 1 de D45 não descreve a conta A; citar o p de Luhn (8.78 × 10⁻⁶) como de **variâncias brutas** e o recalculado com σ corrigidos (8.7 × 10⁻³) lado a lado.
**Quantitativa:** a conta A reproduz os três valores publicados (0.0027, 0.0054, 0.0019; `3.4-25`, `3.4-32`, `3.4-39`); a B dá 0.0028, 0.0048, 0.0015 (razões B/A 1.04, 0.89, 0.79) e usa só 4, 4 e 9 estações (`3.4-56`); a conta A não usa as 119 linhas grau C (A13-F3).
**Qualitativa:** a conta A é a que o artigo de fato executa, de modo que citar Luhn como precedente fica coerente; a B é a leitura literal de D45 e serve de teste de robustez.
**Risco/alternativa:** a conta A mistura variância intra-sazonal com modulação lenta do intervalo (leitura própria); a B é mais próxima do objeto físico, mas não reproduz a publicação.

## R5 — Junção instrumental (D72)
**Recomendação:** **descontinuidade declarada** (D44): nenhuma janela atravessa a junção HKP-2 → HIRES-2; o indicador temporal roda **dentro da era Mount Wilson**; segmentos da era Keck são só descritivos; **sem correção de degrau**. Para HD 166620, a comparação de estados cruza a junção sob a exceção D45b (fotometria APT independente).
**Quantitativa:** a era Mount Wilson tem segmento ≥ 24 anos nas **10 de 10** estrelas (28–36 anos), a era Keck em **3 de 10** (HD 23249, 190360, 10476; `3.19-02`); o degrau tem σ = 4.47 %, 25 de 51 estrelas passam de 1.2 % e 10 passam de 5 % (`3.5-02`, `3.5-06`, `3.5-07`); 17 de 51 têm degrau < 0.2 % por alinhamento de medianas (Baum §2.1.3).
**Qualitativa:** Baum não publica offsets nem incerteza (A9 §1.5, grau X); instrumento e astrofísica são inseparáveis com os dados publicados (A9-F6), logo corrigir um degrau inventaria um valor.
**Risco/alternativa:** perde-se o trecho Keck para o CSD temporal em 7 de 10 estrelas (curto demais pelo piso de D100); corrigir por degrau estimado daria séries contínuas ao custo de incerteza X.

## R6 — Aceitar D46 (D73)
**Recomendação:** **aceitar D46** e declarar a limitação, com a ressalva de grau C (D58, D86).
**Quantitativa:** 8 médias anuais na aproximação (`3.4-13`) contra o piso de 24 anos (D100): o segmento de aproximação de HD 166620 (1995–2002) é três vezes menor que o piso; a janela de 50 % teria 4 pontos.
**Qualitativa:** D46 é a conclusão de A10-F2 e é coerente com Scheffer, Boulton e Held & Kleinen (falsos negativos, séries curtas). Aceitá-la não impede o H1 de R3.
**Risco/alternativa:** não aceitar exigiria os dados reais de Oláh (D86 decidiu seguir sem eles).

## R7 — Layout do repositório (D77)
**Recomendação:** **manter o layout atual** até a consolidação assinada; na migração, criar `DECISIONS.md` que **remete** às D## sem renumerá-las.
**Quantitativa:** 24 arquivos do pacote têm cópia idêntica na raiz e nenhuma diverge (`1-02`, `1-03`); 23 nomes de arquivo citados e ausentes (`1-07`) mostram o custo de mover sem atualizar; nada na pesquisa em curso depende do layout.
**Qualitativa:** D31, D38 e a imutabilidade das D## (regra 4) tornam a migração parcial um risco de inconsistência; a consolidação já cria `p4_star_catalog.csv` e `P4_SOURCE_VALUES.md`, o momento natural para migrar.
**Risco/alternativa:** adiar mantém a divergência com o Kit; migrar já custa uma rodada.

## R8 — Q2: o que conta como `Flat`
**Recomendação:** classe de **B95** (catálogo congelado, D36) como principal; a de **Baum** como camada de época (D43); manter `Flat` e `Flat?` distintos; sinalizar ρ CrB (HD 143761, `Long` na Tabela 2 de B95 e 1.0 % na Tabela 1).
**Quantitativa:** o catálogo tem 112 estrelas; Baum tem 4 das 5 `Flat` limpas; Baum **não tem limiar numérico** para `flat` (A9), enquanto B95 usa σ_S/S < 1–1.5 %.
**Qualitativa:** só a definição de B95 é numérica e auditável; D15/D42/D43 já mandam registrar as de outras fontes ao lado.
**Risco/alternativa:** a interseção das duas é mais conservadora, com N menor.

## R9 — Q3: remoção de tendência e largura gaussiana
**Recomendação:** **varredura pré-registrada** de σ ∈ {1, 3, 5} anos mais "sem remoção"; **σ = 1 ano como padrão** de D21; o ciclo ajustado só como sensibilidade; o p do τ sempre por surrogates passando pelo **mesmo** filtro; resultado só é destacado se concordar em pelo menos 3 das 4 configurações.
**Quantitativa** (sintético, ciclo de 10 anos de amplitude 3 SD mais ruído AR(1), L = 54; `3.19-03` a `3.19-05`): AC1 do resíduo, com valor de referência 0.44: sem remoção +0.73; σ = 1: **+0.05** (a gaussiana de 1 ano remove o ciclo **e a memória**); σ = 3: +0.69; σ = 5: +0.73; ciclo ajustado com período certo: +0.38; **com período 20 % errado: +0.73** (não remove). O τ nulo fica em torno de zero em todos (−0.02 a +0.05), então **a validade do teste não depende do filtro**; o poder também quase não (AUC 0.59–0.63).
**Qualitativa:** nenhum filtro separa um ciclo de 10 anos da memória AR(1); o ciclo ajustado exigiria período conhecido a ~10 %, e os períodos publicados divergem por mais de 2 dP em 23 de 25 estrelas (A13-F1). Dakos pede varredura de sensibilidade, não um valor único (A4-F2).
**Risco/alternativa:** σ = 1 ano torna o AR(1) pouco informativo (nível 0.05); a variância do resíduo continua informativa e é a quantidade próxima de σ_S.

## R10 — Q4: componente de 44 anos
**Recomendação:** **declarar como confundidor e não controlar**; marcar a série solar como exploratória.
**Quantitativa:** uma componente de 44 anos é maior que a metade do registro solar (50 anos em Egeland, D65) e que o piso de segmento (24 anos, D100); só 4 estrelas têm segmento ≥ 40 anos (HD 23249, 190360, 10476, 182572; lista de segmentos em `16_min_segment.txt` §3).
**Qualitativa:** A6-F12 diz que controlá-la "is doubtful"; A11b-F5 mostra que componentes longas são típicas; D30 já a coloca em Methods.
**Risco/alternativa:** ajustá-la e removê-la num registro de 50 anos é circular.

## R11 — Q5: binárias
**Recomendação:** **excluir HD 81809 e HD 219834A** dos controles; manter HD 219834B só se houver série utilizável (não há linhas na Tabela 1 sob esse id).
**Quantitativa:** com v2001 (D95) há 9 controles com série utilizável (5 de Baum com linhas na Tabela 1 e 4 do v2001; HD 219834B consta em Baum mas não tem linhas); sem HD 81809 ficam **8 de 12 controles estelares** mais o Sol.
**Qualitativa:** HD 81809 é composto e o ciclo pode ser de uma companheira de menor massa (A1-F7); Saar rejeita o ciclo de HD 219834A e mantém o de B (A6 §2.3).
**Risco/alternativa:** mantê-las com sinalização preserva N e contamina o grupo `CYCLE`.

## R12 — Q6: apresentação do grupo `Flat`
**Recomendação:** apresentar o limiar `Flat` (< 1–1.5 %) **com o piso instrumental (0.37–0.45 %, D75) e a precisão de B95 (1.4 %; 1.2 % sem quatro padrões) lado a lado**; definir `Flat` como "variabilidade não distinguível da precisão de longo prazo de B95", sem afirmar "três vezes acima do piso".
**Quantitativa:** σ_S/S medido nas `Flat` de 0.72 a 1.49 %, isto é, 1.6 a 4 vezes o piso e de 0.5 a 1.1 vezes a precisão de B95; limiar acima do piso antigo de 0.8 % (A2-F6).
**Qualitativa:** a CLS V e Luhn dão o piso moderno; B95 dá a precisão do registro antigo; D45 dá a subtração em quadratura.
**Risco/alternativa:** usar só o σ corrigido (R4) é mais fino, mas depende da receita.

## R13 — Q7: subgigantes
**Recomendação:** **manter os subgigantes como subgrupo declarado** e rodar a análise **com e sem** eles; usar log g e [Fe/H] de Baum e da CLS V como covariáveis; citar Wright 2004 e a objeção.
**Quantitativa:** o catálogo marca 4 das 5 `Flat` limpas com "IV" ou "Vp" (`3.9-06`); excluí-los deixa **uma** (HD 43587, ausente de Baum): inviável. Pelo log g de Baum, HD 10700 (4.60) e HD 190360 (4.29) são anãs e HD 23249 (3.75) e HD 182572 (4.15) são mais evoluídas: o tipo do catálogo e o log g **divergem** para HD 10700.
**Qualitativa:** três fontes independentes (Wright 2004, Baum §5.5, Järvinen & Strassmeier §1 e §6; A11a-F3) tornam a objeção publicada; a resposta por construção da amostra é impossível com N tão pequeno, e a análise com e sem mostra a sensibilidade.
**Risco/alternativa:** excluí-los é a resposta "por construção", ao custo de N = 1 na `Flat`.

## R14 — Q9: DFA
**Recomendação:** **manter o DFA fora** (D24, D92).
**Quantitativa:** a série anual (27 na mediana das 59; 46–48 nos grupos) fica abaixo do piso de D24 (> 100); a bruta passa de mil observações em 22 de 59 (`3.16-01`) mas é irregular, com tripletos noturnos, e a calibração de Livina foi ajustada em AR(1) regular de 20 000 pontos.
**Qualitativa:** Livina & Lenton pedem ~mil pontos e dizem que a calibração pode ser inadequada para dados não lineares; Peng+1993 mostra que a incerteza do expoente cai com √N; a hipótese (R3) usa AR(1) e variância, não α.
**Risco/alternativa:** admiti-lo nas 22 estrelas abriria uma segunda frente sem benefício para H2.

## R15 — Q10: a transição é lenta o bastante?
**Recomendação:** tratar como **parte da hipótese** (R3: a falsificação é o resultado) e **não** estimar o tempo de decaimento como etapa preliminar.
**Quantitativa:** o desvio-padrão do AR(1) é 0.25 em 12 pontos e 0.18 em 24 (`3.18-06`), de modo que c = 0.5 ± 0.2 corresponde a tempos de memória de 0.8 a 2.8 anos (−1/ln c); a precisão é insuficiente para decidir "lento ou rápido" frente à amostragem anual.
**Qualitativa:** Held & Kleinen e Scheffer pedem muitos tempos de decaimento; a CLS VI diz "on order of years" a partir de uma lacuna entre estrelas, não de série.
**Risco/alternativa:** estimar o tempo daria um número sem precisão; declarar a limitação é o honesto.

## R16 — Q11: inclinação
**Recomendação:** **declarar o confundidor para HD 10700** (Korolik: 7° ± 7°) e deixar as demais como grau X; **não excluir e não estimar** inclinação própria.
**Quantitativa:** v sin i = 0.1 km/s (piso de Baum) aparece em HD 10700, 23249 e 143761 e **também em estrelas com ciclo**, HD 10476 e HD 166620; só HD 182572 (1.3) e HD 190360 (2.1) estão acima; v sin i baixo não discrimina inclinação de rotação lenta.
**Qualitativa:** a ligação "inclinação → ciclo não identificável" é da CLS VI, não de Korolik (A14-F3); a regra 8 impede medir.
**Risco/alternativa:** excluir HD 10700 reduz a `Flat` limpa para 3 em Baum.

---
Estado: **recomendações entregues; nenhuma é decisão (D101).**
