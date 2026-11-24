# Memorando de decisões humanas — P4 (REG-04)

**Data:** 2026-11-14 · **Para:** Prof. Airton M. S. Borin Junior · **De:** Claude (sessão de inspeção e resolução)
**Regra:** nenhuma Q# foi decidida por Claude. Cada item traz a pergunta, os subsídios com id de checagem (`inspecao/checks.csv`) ou D## do caderno, as alternativas e, **só quando já está registrada**, a recomendação anterior. Cada resposta vira uma entrada nova `D##` (autor: pesquisador) no caderno §4d, e a etapa para (REG-01) até a aprovação escrita.
**Ordem:** de dependência (DECISOES §E). O item 1 governa vários dos seguintes.

---

## 1. A série anual ou a série bruta é o objeto do P4? (decisão-raiz)
**Governa:** Q9 e D24 (DFA), D20–D23 (janela, suavização, significância), o cálculo de φ₁ e σ², o item 5.
**Subsídios:** D24 fechou o DFA com N ≈ 26 médias anuais contra piso de > 100 pontos; no subconjunto Baum a mediana é **27 estações anuais** contra **698 observações brutas** (v6 §6; Q9 do caderno); a Luhn+2022 calcula σ_S por estado sobre as observações (D57), e a série solar de Egeland tem 6 349 linhas com mediana de 152 por ano (D65, `3.12-09`); em D46 o caso HD 166620 tem **8 médias anuais** na aproximação.
**Alternativas:** (a) anual (estações); (b) bruta; (c) as duas, com papéis distintos declarados (por exemplo, σ por estado em bruta; tendências em anual).
**Recomendação registrada:** nenhuma.

## 2. Q1 — composição da amostra
**Subsídios:** quatro opções com custos em `paper_state_v6.md` §3.4: (i) catálogo Baliunas congelado, N ≈ 26; (ii) subconjunto Baum, 59 estrelas; (iii) CLS V, 285 estrelas, cerca de 19 anos; (iv) estudo de caso HD 166620 + HD 101501. Novos desta rodada: a não-uniformidade do subconjunto Baum está na **presença** (4/5 `Flat`, 6/13 controles) e não no N das presentes (I-12; `3.3-55`, `3.3-56`); a regra que define as "cinco `Flat`" não sai de D13 sozinha, dá sete (I-06; `3.9-01`); HD 101501 tem 99.73 % das observações em Mount Wilson e lacuna de 13.82 anos (D59; `3.3-50`, `3.3-52`); D04 e D11 contra subsídios que já usaram dados das candidatas (I-13, abaixo).
**Recomendação registrada** (v6 §3.4, DECISOES §E item 2): as opções (ii) e (iv) não são exclusivas; HD 101501 é o objeto que melhor sobrevive às objeções publicadas.
**Perguntas embutidas:** (a) a regra de exclusão por binaridade que dá as "cinco `Flat`" (HD 158614 e HD 178428 saem por regra de um arquivo ausente); (b) como reconciliar D04 ("antes de qualquer dado real") e D11 com as medidas de σ_S/S das quatro `Flat` na CLS V já usadas em Q2 e v6 §3.3 (I-13): manter, ou registrar que a seleção foi informada.

## 3. Q8 — migrar a análise para log R′_HK?
**Subsídios:** D52, D53, D54; D60 (a CLS VI analisa 91 estrelas por faixa de massa, e o teste não é de CSD); D61 (Noyes trata o nível médio; Linsky 0.3 dex abaixo em B−V = 1.25); D62 (B−V da CLS V é derivado; 78 estrelas dentro pela leitura aberta, 82 pela fechada).
**Alternativas:** migrar; não migrar; índice híbrido (S com massa).
**Recomendação registrada** (D54): **não migrar**. Esta rodada não a alterou.

## 4. A junção instrumental 2001→2004
**Subsídios:** D44 (offset constante aditivo por alinhamento de medianas; incerteza residual grau X); σ do degrau 4.47 % entre estrelas (`audit/a9_instrument_step.csv`); 17 das 51 estrelas têm degrau < 0.2 % e cinco exatamente zero, e as 34 restantes têm σ = 5.48 %, enquanto a dispersão robusta das 51 é 1.23 % (I-09, grau C; `3.5-19` a `3.5-22`). D45b: para HD 166620 a calibração é robusta (fotometria APT).
**Pergunta:** se a opção (ii) do item 2 for escolhida, a junção é (a) uma descontinuidade declarada e nenhuma janela a atravessa (regra operacional de D44), (b) corrigida por um degrau estimado, (c) evitada ao usar só um instrumento por estrela.

## 5. Aceitar D46?
**O que D46 diz:** o teste temporal no formato de Dakos não é executável em HD 166620; a unidade de análise é a comparação de variabilidade entre estados.
**Subsídios:** A10-F2 (8 médias anuais na aproximação); **D58: essas 8 médias dependem das 119 linhas digitalizadas, grau C**; lacuna real de 6.91 anos (1997.73–2004.64) (A13-F3); Scheffer e Boulton exigem séries longas e escolha de janela (A7-F5).
**Alternativas:** aceitar e declarar no manuscrito; aceitar com a ressalva de grau C de D58; pedir os dados reais a K. Oláh e W. Soon antes de decidir.

## 6. A resposta teórica a D50 é sustentável?
**O que D50 diz:** a objeção de estocasticidade e de transição rápida é citada e respondida pela biestabilidade.
**Subsídios (A7, A8, D66):** Scheffer descreve a Hopf como estável → oscilante; o P4 é o sentido oposto, e **nenhuma fonte lida dá sinal precursor para a perda de um ciclo limite** (A7-F2); "flickering" e bimodalidade de Scheffer são do mesmo sistema ao longo do tempo, a bimodalidade da CLS VI é entre estrelas (A7-F4); Usoskin: "hardly able to predict" e precursores só qualitativos, sem tipo CSD (A8-F1, A8-F2); Boulton: sem equilíbrio o sinal "should not work as well" (A7-F3); Held & Kleinen não foi lido (A7-F1).
**Alternativas:** manter a resposta como extensão por analogia declarada; reformular como hipótese e não como resposta; esperar Held & Kleinen.

## 7. A receita de D45 e o que o p de Luhn mede (I-01, BLOQUEANTE)
**Subsídios (D57):** três contas diferentes. (i) σ do intervalo inteiro menos ruído em quadratura: 0.00269 / 0.00542 / 0.00195, os valores publicados; (ii) leitura literal do passo 1 de D45 (por estação): 0.0028 | 0.0025, 0.0048 | 0.0049, 0.0015 | 0.0014; (iii) o F-test publicado, 8.78 × 10⁻⁶, reproduz-se com variâncias brutas (8.80 × 10⁻⁶); com σ_S corrigidos, 8.68 × 10⁻³ (`3.4-25` a `3.4-54`).
**Pergunta:** qual conta é "a receita" que o P4 adota (a); e o P4 cita o p de Luhn como valor das variâncias brutas (b), ou recalcula (c).

## 8. Piso instrumental e a apresentação de Q6
**Subsídios (D67):** pela tabela da CLS V (Nobs ≥ 45): HD 187923 0.372 %, HD 144579 0.397 %, HD 55575 0.448 %; o "0.45 %" é o texto do artigo. "Três vezes abaixo do limiar `Flat`" depende do número. D45 oferece a subtração em quadratura; D57 diz qual conta o artigo reproduz.
**Pergunta:** que número citar como piso (0.372 %, 0.448 % ou ambos) e se o limiar `Flat` (< 1–1.5 %) é declarado dentro da precisão de longo prazo de Baliunas (1.4 %).

## 9. Q2–Q7 e Q11
| Q | Pergunta | Subsídios novos |
|---|---|---|
| Q2 | O que conta como `Flat` (ρ CrB: `Long` na Tabela 2, 1.0 % na Tabela 1, "flat" em Saar) | D51; σ_S/S das quatro `Flat`: 0.72 / 0.86 / 0.95 / 1.49 %; HD 3651 tem ciclo de 10.01 anos (D67) |
| Q3 | Largura de banda gaussiana | inalterada |
| Q4 | Componente de 44 anos | A11b-F5: componentes longas junto do ciclo são o caso típico; Oláh+2016 Tabela 1 marca tendências `lt` em várias estrelas (A13) |
| Q5 | Binárias (HD 81809, HD 219834A/B) | HD 81809 ausente de Baum |
| Q6 | Medida do grupo `Flat` | item 8 |
| Q7 | Subgigantes no `Flat` | três fontes (Wright 2004; Baum §5.5; Järvinen & Strassmeier §1 e §6) |
| Q11 | Inclinação estelar | Korolik+2023 em `bib/` (τ Ceti), ainda não auditado; D51 |
**Pergunta:** responder agora, deixar abertas, ou pedir auditoria prévia (Korolik para Q11).

## 10. Layout do repositório e migração ao Kit (I-27)
**Subsídios:** o repositório mistura o pacote do P4 (subpasta `P4/`) e PDFs na raiz; o Kit espera `p4_star_catalog.csv` e `P4_SOURCE_VALUES.md` gerados na consolidação assinada; D38 fixa `bib/` para PDFs e a raiz para tabelas.
**Alternativas:** manter o layout atual e só acrescentar; migrar ao layout do Kit numa rodada própria, com a consolidação.

## 11. Partes da incorporação ao caderno que a instrução de DECISOES não cobre (I-18)
**O que foi feito além da instrução**, por inclusão e para o pesquisador aprovar ou desfazer: cabeçalho "Última entrada"; §6 (bloqueios) reescrita com o estado do ambiente; §7 com as obrigações de Methods de D44–D61; §10 (fatos com página) e §11 (uso de IA); a coluna "Subsídios" da §5 deixou de existir, como manda a instrução.
**Pergunta:** aprova, ou quer a coluna "Subsídios" de volta.

---

## Registro das respostas
**Bloco 1 (2026-11-14):** item 1 → D68 (ambas, papéis por definir); item 3 → D69 (S e R′_HK, ambos); item 7 → D70 ("subsídios para defesa": `SUBSIDIOS_RECEITA_SIGMA_S.md`, escolha adiada); item 11 → D71 (aprovo). 
**Bloco 2 (2026-11-14):** item 4 → D72 e item 5 → D73 ("subsídios para decidir": `SUBSIDIOS_JUNCAO_E_D46.md`, escolha adiada); item 6 → D74 (esperar Held & Kleinen); item 8 → D75 (citar os dois: 0.37–0.45 %). Pendentes: 2, 9, 10 e os papéis das séries.

Cada resposta será registrada como `D68` em diante, com data, autor "pesquisador" e a base (o número do item acima). Nada neste memorando altera uma decisão ou recomendação já registrada.

**Bloco 3 (2026-11-14):** papéis das séries → D76 (subsídios: `SUBSIDIOS_PAPEIS_SERIES.md`, escolha adiada); item 10 → D77 (subsídios: `SUBSIDIOS_LAYOUT_KIT.md`); item 9 → D78 (Q2–Q7 abertas; Q11 com A14); item 2 / Q1 → D79 (espera os papéis).

**Bloco 4 (2026-11-24):** o item 6 (D50) voltou a ser decidível: Held & Kleinen foi lido (D81, `audit/A7b_held_kleinen.md`). Subsídio novo: o artigo trata o decaimento de um ponto fixo e deixa os modos oscilatórios de fora ("could be easily included by a 2D ansatz", p. 2); nenhuma fonte teórica lida dá sinal precursor para a perda de um ciclo limite. Alternativas do item 6: manter como extensão por analogia declarada; reformular como hipótese. **Aguarda a escolha do pesquisador.**

**Bloco 5 (2026-11-24):** dados de Oláh e Soon → D86 (seguir sem eles, grau C; pedido não enviado). O HK_Project_v2001_NSO (D85) é subsídio novo para Q1: quatro dos seis controles ausentes de Baum (HD 160346, 201091, 81809, 103095) têm 35 anos de Mount Wilson até 2001 nele.

**Bloco 6 (2026-11-24):** item 6 (D50) → D87: "subsídios para decidir" (`SUBSIDIOS_D50.md`); escolha adiada.

**Bloco 7 (2026-11-24):** item 6 (D50) → buscada fonte sobre ciclo limite (D88, A7c): três lidas, nenhuma trata o sentido ciclo → equilíbrio. O item continua pendente da sua escolha, agora com a lacuna confirmada em três linhas de fontes.

**Bloco 8 (2026-11-24):** Bury+2020 enviado e lido (D89, adendo de A7c): analisa só a aproximação pelo lado do equilíbrio; a lacuna do lado do ciclo permanece. Item 6 segue pendente da sua escolha.

**Bloco 9 (2026-11-24):** item 6 → D90: a resposta teórica de D50 é reformulada como hipótese testável. Pendente: o enunciado da hipótese (indicador, série, sinal esperado, refutação).

**Bloco 10 (2026-11-24):** papéis das séries → D91 (subsídios completos em `SUBSIDIOS_PAPEIS_SERIES.md`, adendo 2: A, B ou C); escolha pendente.

**Bloco 11 (2026-11-24):** papéis das séries → D92 ("A e C": anual para CSD temporal; bruta para σ por estado e períodos; DFA só se Q9 for decidida a favor). Q1 destravada.

**Bloco 12 (2026-11-24):** D92 validado (D93); Q1 → D94 (subsídios em `SUBSIDIOS_Q1.md`); escolha pendente.

**Bloco 13 (2026-11-24):** Q1 → opção (v) (D95); períodos = publicados; interpolação de anos faltantes explicada, regra pendente; sub-perguntas de Q1 (binaridade, D04/D11) pendentes.

