# P4 — Caderno de Notas de Pesquisa

**Paper:** Critical Slowing Down Near Stellar Activity Minima
**Aberto em:** 2026-07-28 (início da fase de auditoria) · **Última entrada:** 2026-11-14 (inspeção, resolução e primeiras decisões; D55–D86)

---

## Como usar este caderno

Este é o registro permanente de **o que foi decidido, quando, com que base, e o que foi
descartado**. Ele existe por três razões:

1. **Auditabilidade.** Qualquer valor ou parâmetro do manuscrito deve poder ser rastreado até
   uma decisão registrada aqui, e daí até uma seção de um artigo-fonte.
2. **Prevenção de loops.** Questões fechadas estão na §8 com a razão do fechamento. Uma questão
   listada lá **não é reaberta** sem evidência nova — e "evidência nova" significa uma fonte não
   auditada, não um novo raciocínio sobre as mesmas fontes.
3. **Continuidade entre conversas.** O fluxo do programa usa conversas separadas com handoff via
   `paper_state.md`. Este caderno é a memória longa; o `paper_state` é o estado corrente.

**Convenções.** Decisões são `D##`, imutáveis: uma decisão revogada recebe `status: revogada` e
uma nova entrada explicando por quê — nunca se edita a original. Achados de auditoria são
citados como `A#-F#` (ex.: `A1-F3`). Graus de evidência seguem o protocolo:
**A** = duas fontes independentes ou checksum · **B** = leitura limpa, uma localização ·
**C** = derivado de figura ou divergência não resolvida · **X** = não obtido.
**Valores grau C não entram no manuscrito.**

---

## 1 · Decisões de escopo e método de trabalho

### D01 — O catálogo é reconstruído das fontes, não corrigido incrementalmente
**Data:** 2026-07-28 · **Base:** A1-F3, A1-F2 · **Status:** ativa
Quatro das doze estrelas do catálogo de `paper_state_v2` estavam classificadas erradamente e uma
(HD 4915) não existe na fonte. Remendar preservaria o problema de proveniência que a auditoria
existe para eliminar.
**Descartado:** emendar `paper_state_v2` in loco.

### D02 — Nenhum valor astronômico vem de memória de treinamento
**Data:** 2026-07-28 · **Base:** protocolo §1; A1-F3 · **Status:** ativa
Todo parâmetro estelar é extraído do PDF da fonte, com dupla verificação. A auditoria encontrou
erros sistemáticos em valores previamente aceitos como corretos.

### D03 — Contradições são registradas, não resolvidas silenciosamente
**Data:** 2026-07-28 · **Base:** protocolo regra 4 · **Status:** ativa
Quando duas fontes discordam e ambas são grau A na própria origem, as duas entram no registro e
a escolha é escalada para decisão humana explícita.

### D04 — A amostra é selecionada do catálogo congelado, antes de qualquer dado real
**Data:** 2026-07-28 · **Base:** protocolo §1 · **Status:** ativa
Nenhuma unidade de auditoria seleciona a amostra. A seleção é feita na consolidação, com o
catálogo fechado e sem ter visto resultados.

### D05 — Verificação por dois métodos independentes
**Data:** 2026-07-28 · **Base:** protocolo §4 · **Status:** ativa
Aceita-se: dois motores/configurações de OCR; camada de texto nativa + render/OCR; checksum
aritmético; ou segunda localização no mesmo artigo. Um PDF com texto nativo **não** dispensa
verificação — em A4 o glifo de menos era extraído como o caractere `2`, o que teria invertido
células inteiras da Tabela 3.

### D06 — Adotado um caderno de notas de pesquisa
**Data:** 2026-08-01 · **Base:** decisão de arquitetura · **Status:** ativa
Este documento. Incorporado à arquitetura de escrita (§7).

---

## 2 · Decisões sobre dados estelares

### D07 — HD 4915 é removida permanentemente
**Data:** 2026-07-28 · **Base:** A1-F2 · **Status:** ativa · **Grau:** A
Busca de texto completo nas 19 páginas de Baliunas+1995: nenhuma ocorrência. A Tabela 2 vai de
HD 4628 direto para HD 6920.

### D08 — ⟨S⟩ é a média anual sobre todos os anos, da Tabela 2 de Baliunas
**Data:** 2026-07-28 · **Base:** A1 nota de rodapé m · **Status:** ativa · **Grau:** A
Consequência: N ≈ 25–26 pontos por estrela (1966–1991).

### D09 — Membership de grupo segue a classificação primária da Tabela 2
**Data:** 2026-07-28 · **Base:** A1 §2.1 · **Status:** ativa · **Grau:** A
Checksum §4.3 de Baliunas (52 ciclos / 31 planas ou com tendência linear / 29 variáveis = 112)
reproduzido exatamente pela extração. `Long` é agrupada com plana/tendência na contagem do
próprio Baliunas, mas rotulada distintamente para que P4 possa decidir se mantém a distinção.

### D10 — Quando há dois períodos, coluna 7 = primário, coluna 9 = secundário
**Data:** 2026-07-28 · **Base:** A1 nota de rodapé o; Apêndice A sobre HD 190406 · **Status:** ativa
Corrige a inversão em `paper_state_v2`, que listava 16.9 yr como P_cyc de HD 190406 quando o
primário é 2.60 ± 0.02 yr.

### D11 — Nenhum σ_S/S por estrela é usado para a amostra P4
**Data:** 2026-07-28 (A1) · **Reafirmada:** 2026-07-30 (A6) · **Base:** A1-F1, A6-F5 · **Status:** ativa
A Tabela 2 de Baliunas não tem coluna σ_S. A Tabela 1 tem — mas é a tabela de **estrelas-padrão**,
17 estrelas apenas, e é precisamente o conjunto que não pode ser usado (D14).

### D12 — Usar apenas Baliunas+1995; N uniforme
**Data:** 2026-07-29 · **Base:** A2-F1, A2 §5 · **Status:** ativa
Lockwood+2007 não publica série numérica de Ca II para estrela alguma; existe só como Figura 3.
Digitalizar seria grau C e violaria a proibição do programa de derivar fotometria própria.
**Consequência favorável:** como nenhuma estrela ganha pontos, **N é uniforme por construção** e
o confundimento comprimento-de-série×grupo não pode surgir. Deve ser dito em Methods.
**Descartado:** (b) séries estendidas para o subconjunto com N como covariável; (c) restringir a
amostra a estrelas de N comparável — ambas pressupõem uma extensão que não existe.

### D13 — Estrelas-padrão de calibração são excluídas da amostra
**Data:** 2026-07-30 · **Base:** A6-F6, A6-F7 · **Status:** ativa
Sete das onze estrelas `Flat` são padrões fotométricos, selecionados por constância e usados para
definir o ponto zero. Incluí-las torna o grupo `Flat` circular.
**Nota obrigatória:** qualquer grupo `Flat` deve registrar, membro a membro, se é padrão (A6 D6).

### D14 — σ_S/S da Tabela 1 de Baliunas admitido em grau A, para as 17 padrões apenas
**Data:** 2026-07-30 · **Base:** A6 §3 · **Status:** ativa · **Grau:** A por checksum
Dois checksums aritméticos exatos: média de 17 estrelas = 1.4%; média de 13 (excluindo as quatro
com marcador de rodapé) = 1.2%. O segundo confirma simultaneamente *quais* quatro carregam o
marcador. Não se aplica a estrelas fora da tabela.

### D15 — Períodos de Saar são registrados ao lado dos de Baliunas, não fundidos
**Data:** 2026-07-30 · **Base:** A6 D4, protocolo regra 4 · **Status:** ativa
Cinco divergências de classificação e várias de período. Registradas em
`saar_baliunas_crossmatch.csv`. Notável: HD 3651 = 13.8 ± 0.4 (Baliunas) vs 14.6 (Saar), com
Saar anotando "sem alterações" — divergência de ~2σ não explicada, na estrela que A1-F5 aponta
como a candidata mais clara a transição.

---

## 3 · Decisões sobre calibração solar

### D16 — S_SUN_MEAN = 0.1694 ± 0.0005
**Data:** 2026-07-29 · **Base:** A3-F1 · **Status:** ativa · **Grau:** A
Média das médias de ciclo, ciclos 15–24 (Egeland+2017). Confirmado no resumo, na Tabela 2, e por
checksum aritmético (minhas dez linhas extraídas dão 0.16936).

### D17 — O ⟨S⟩ solar de Baliunas (0.179) não é usado em lugar nenhum
**Data:** 2026-07-29 · **Base:** A3-F2, A3-F3 · **Status:** ativa
Não é medida: veio de uma transformação-proxy S(K) não publicada, ajustada para reproduzir razões
de amplitude de F10.7 e manchas. Alto 5% na média e **inflado ~76% na amplitude de ciclo**
(ΔS = 0.0251 vs 0.0143 medido). Como CSD compara variância, uma série solar calibrada assim
carregaria ~3× a σ² verdadeira em relação à amostra estelar.
Onde a linha solar da Tabela 2 de Baliunas for reproduzida (é parte legítima do catálogo), deve
levar nota de rodapé dizendo que é estimativa-proxy superada por Egeland.

### D18 — A série solar é posta na escala HKP-2 via Egeland, não por transformação K→S própria
**Data:** 2026-07-29 · **Base:** A3-F3, A3-F5 · **Status:** ativa
A Tabela 4 de Egeland (série S solar calibrada, ciclos 15–24, homogeneizada sobre cinco
instrumentos, machine-readable) é a fonte preferida. **Bloqueada no sandbox** — ver §6.

### D19 — Estabilidade da média de ciclo e declínio da amplitude são reportados separadamente
**Data:** 2026-07-29 · **Base:** A3-F4, A3-F6 · **Status:** ativa
A média de ciclo é estável a ~1.2% (σ_scatter = 0.002) enquanto a amplitude caiu 50% do ciclo 22
(0.0178) ao 24 (0.0089), sendo o ciclo 24 o mais fraco dos dez medidos. São quantidades
diferentes e não devem ser confundidas.

---

## 4 · Decisões de método

### D20 — Janela deslizante = 50% do comprimento; sensibilidade sobre 25–75%
**Data:** 2026-07-29 · **Base:** A4 §1.1 (Dakos Passo 3, Passo 4) · **Status:** ativa
Janelas sobrepostas. Corrige a faixa de sensibilidade de `paper_state_v2` (40/50/60%), estreita
demais frente à publicada.

### D21 — Suavização gaussiana só nas trilhas AR(1) e variância; nunca antes de DFA
**Data:** 2026-07-29 · **Base:** A4 §1.2, Dakos Tabela 3 nota 5 · **Status:** ativa
DFA usa **detrending polinomial dentro de cada janela**. A distinção é explícita na fonte.

### D22 — Significância por 1000 surrogates ARMA(p,q), ajustados por AIC aos resíduos
**Data:** 2026-07-29 · **Base:** A4-F1, A4 §1.3 (Dakos Passo 5) · **Status:** ativa
p = P(τ\* ≤ τ), avaliado sobre toda a grade largura-de-banda × tamanho-de-janela.
**Substitui todos os p-valores de Kendall do `scipy` no pipeline**, que são anticonservativos
porque janelas sucessivas compartilham a maior parte dos dados.
**Expectativa registrada:** o sinal CSD solar deve enfraquecer substancialmente frente ao
"p < 0.0001" atualmente reportado. Registrar isso *antes* de rodar é deliberado.

### D23 — τ é reportado tanto na série original quanto nos resíduos
**Data:** 2026-07-29 · **Base:** A4-F6 · **Status:** ativa
Dakos reporta ambos (AR(1): 0.911 original, 0.944 resíduo). A estrutura de duas trilhas do P4 é
prática padrão — **desde que ambos sejam reportados**, incluindo o τ negativo da série completa.
Reportar só a trilha de resíduos seria deturpar a prática da fonte.

### D24 — DFA não é aplicada às séries estelares do Mount Wilson
**Data:** 2026-07-29 (A4) · **Confirmada:** 2026-07-30 (A5) · **Base:** A4-F4, A5-F5 · **Status:** ativa
Piso de >100 pontos contra N ≈ 26 — fator ~4. Fechado por três direções independentes: dados
(A1), impossibilidade de extensão (A2), algoritmo (A4/A5).

### D25 — α é reportado na convenção crua de Peng, com a convenção explicitada em Methods
**Data:** 2026-07-30 · **Base:** A5-F4, A5 D6 · **Status:** ativa
O indicador DFA de Dakos é *reescalado* (1 = transição, de 1.5 cru). `nolds.dfa` devolve α cru.
O H = 1.235 de `paper_state_v2` é α cru e **não** pode ser comparado numericamente a valores de
Dakos.

### D26 — n_max é reduzido de N/4; checagem de crossover obrigatória antes de reportar α
**Data:** 2026-07-30 · **Base:** A5-F1, A5-F2, A5 D3/D4 · **Status:** ativa
N/4 é 3× a 32× mais agressivo que qualquer faixa de ajuste usada por Peng. O pipeline ajustava
uma única inclinação sobre 3.1 décadas sem checar crossover. α deve ser ajustado dentro de um
único regime de escala.

### D27 — A frase de justificação da Trilha A em `paper_state_v2` é riscada
**Data:** 2026-07-30 · **Base:** A5-F3 · **Status:** ativa
Factualmente incorreta.

### D28 — H = (β+1)/2 é abandonada, salvo nova fonte
**Data:** 2026-07-30 · **Base:** A4-F8, A5 D1 · **Status:** ativa
Não está em Dakos+2012 (a Figura S3, onde vive o tratamento espectral, não está no PDF do
repositório) nem em Peng+1994. Sem fonte auditada, a relação não entra.

### D29 — `nolds` sai da lista de referências
**Data:** 2026-07-30 · **Base:** A5 D8 · **Status:** ativa
O pipeline não o usa após D26.

### D30 — A componente solar de 44 anos entra nas obrigações de Methods
**Data:** 2026-07-30 · **Base:** A6-F12, A6 D7 · **Status:** ativa
Saar atribui ao Sol P_cyc(L) = 44 yr. O registro do P4 tem 55 yr. Uma componente de 44 anos é
quase degenerada com uma tendência monótona numa estatística de janela deslizante, e nem o filtro
gaussiano de σ = 1 yr nem um detrend linear a removem. **Pendente:** decidir se pode ser tratada
num registro de 55 anos, e dizer isso de um jeito ou de outro (§5, Q4).

---

## 4b · Decisões da conversa de consolidação (2026-08-01)

### D31 — O caderno é atualizado apenas no fecho de cada conversa
**Data:** 2026-08-01 · **Base:** instrução do pesquisador · **Status:** ativa
Evita edições parciais e mantém o registro coerente por sessão. Decisões tomadas no meio de uma
conversa são acumuladas e gravadas de uma vez no encerramento.

### D32 — A seleção da amostra (Q1) fica suspensa até A9
**Data:** 2026-08-01 · **Base:** descoberta de Baum+2022 · **Status:** ativa
Baliunas+1995 tem 31 anos. Séries estendidas e homogeneizadas já existem publicadas, e mudam
materialmente a composição possível dos grupos. Decidir a amostra sem elas seria decidir com
informação incompleta — e, sob protocolo §1, a amostra só se congela uma vez.
**Descartado:** decidir Q1 com o catálogo de 1995 apenas.

### D33 — Séries estendidas vêm de compilações homogêneas publicadas, nunca de garimpo por estrela
**Data:** 2026-08-01 · **Base:** Baum+2022; Isaacson+2024 · **Status:** ativa
Montar séries estrela a estrela a partir de fontes heterogêneas reintroduz exatamente o problema
de calibração que A3-F3 documentou no lado solar (transformação-proxy com amplitude inflada 76%),
além de ser inviável em esforço. Adota-se a compilação de terceiros, com os offsets entre
instrumentos auditados como parte da unidade.

### D34 — HD 166620 é caso de classificação época-dependente, não de contradição
**Data:** 2026-08-01 · **Base:** A1 §1.2; Baum+2022; Luhn+2022 · **Status:** ativa · **Grau:** A
Baliunas classifica como ciclo de 15,8 ± 0,3 yr, FAP Excellent, e está correto para 1966–1991.
Baum+2022 e Luhn+2022 mostram transição para estado plano após 2004. **As duas afirmações são
verdadeiras em épocas diferentes.** O catálogo A1 permanece congelado como está; a informação de
transição entra como camada separada, não como correção.
**Divergência registrada, não resolvida:** período pré-transição — Baliunas 15,8 ± 0,3
(FAP Excellent) vs Baum/Luhn 17 yr.

### D35 — A proveniência de HD 4915 fica registrada
**Data:** 2026-08-01 · **Base:** A1-F2; Shah+2018 · **Status:** ativa
A estrela existe e é candidata documentada a mínimo de Maunder (Shah+2018), mas **não está em
Baliunas+1995**. A1-F2 permanece correto e D07 permanece ativa. O que se esclarece é que o
catálogo antigo misturava fontes sem registrar — que é precisamente a falha que a auditoria
existe para eliminar.

### D36 — Catálogos estendidos ficam ao lado do catálogo congelado, nunca fundidos
**Data:** 2026-08-01 · **Base:** D15 (mesmo tratamento dado a Saar) · **Status:** ativa
`baliunas_table2_full.csv` permanece a referência congelada de A1. Séries e classificações de
Baum, Luhn e Isaacson entram como tabelas separadas com cross-match explícito.

### D37 — Quatro unidades de auditoria novas: A9, A10, A11, A12
**Data:** 2026-08-01 · **Status:** ativa
A9 Baum+2022 (séries estendidas; destrava Q1) · A10 Luhn+2022 (a transição em detalhe) ·
A11 A&A 2025 + Isaacson+2024 + CLS VI (raridade, amostras modernas, explicação concorrente) ·
A12 Noyes+1984 (receita de R′_HK). Prompt em `COWORK_PROMPT_A9_A12.md`.

### D38 — Organização de arquivos: `bib/` para PDFs, raiz para tabelas
**Data:** 2026-08-01 · **Base:** instrução do pesquisador · **Status:** ativa
Também é o contorno de rede que já funcionou: PDFs depositados em `bib/` no repositório GitHub
são acessíveis do sandbox, enquanto arXiv, IOP e A&A não são.

### D39 — Nenhuma conversão para R′_HK antes de A12
**Data:** 2026-08-01 · **Status:** ativa
A12 estabelece a receita, os coeficientes de C_cf(B−V) e sobretudo a **faixa de validade em cor**.
Converter antes de conhecer os limites arriscaria aplicar a calibração fora do domínio para as
estrelas vermelhas da amostra (HD 23249 B−V = 0,92; HD 160346 = 0,96; HD 32147 = 1,06).

### D40 — Registrada a propriedade de invariância do τ de Kendall sob mudança de índice
**Data:** 2026-08-01 · **Base:** τ é estatística de postos · **Status:** ativa
Para uma estrela de B−V fixo, S → R′_HK é transformação monotônica. Logo **τ é exatamente
invariante**; φ₁ muda pouco; a variância muda de escala. Consequência prática: uma eventual
migração para R′_HK ataca o confundimento de cor no eixo **comparativo** sem invalidar nada do
eixo **temporal**. Registrado para não ser redescoberto.

---

## 4c · Decisões da segunda rodada de auditoria (A9–A12), 2026-08-01

---

### D41 — Os `.tsv` VizieR da raiz são identificados e passam a ser a fonte numérica primária das séries estendidas
**Data:** 2026-08-01 · **Base:** A9 §0; quatro checksums exatos contra o texto nativo · **Status:** ativa · **Grau:** A

| Arquivo | Catálogo | Artigo | Conteúdo | Linhas |
|---|---|---|---|---|
| `J:AJ:163:183:table1.tsv` | J/AJ/163/183/table1 | Baum+2022 | séries de S-value | 62 135 |
| `J:163:183:table2.tsv` | J/AJ/163/183/table2 | Baum+2022 | parâmetros e classificações | 59 |
| `J:ApJ:936:L23:table2.tsv` | J/ApJ/936/L23/table2 | Luhn+2022 | S_HK de HD 166620 | 1 885 |
| `J:ApJ:936:L23:table3.tsv` | J/ApJ/936/L23/table3 | Luhn+2022 | fotometria APT T4 | 1 278 |
| `J:ApJS:274:35:table2.tsv` | J/ApJS/274/35/table2 | Isaacson+2024 | 710 estrelas, S e σ_S | 710 |
| `J:ApJS:274:35:table3.tsv` | J/ApJS/274/35/table3 | Isaacson+2024 | séries S do Keck | 52 380 |
| `J:ApJS:274:35:table4.tsv` | J/ApJS/274/35/table4 | Isaacson+2024 | 138 ciclos | 138 |

Validação: `Nobs` da Tabela 2 = contagem na Tabela 1, estrela a estrela, 59/59, soma 62 135; `Cadence` = `Nobs`/baseline exato (máx. |Δ| = 0.005); contagens por instrumento de HD 166620 reproduzem exatamente Luhn+2022 §2.1 (107 / 1 547 / 9 / 103).
**Consequência:** o lado **estelar** deixa de depender de rede. O item de ação da Tabela 4 de Egeland (trilha solar) continua bloqueado.

---

### D42 — Os períodos de Baum ficam ao lado dos de Baliunas e de Saar, nunca fundidos, e com o método explícito
**Data:** 2026-08-01 · **Base:** D15, D36, A9-F3, A9-F7 · **Status:** ativa
`baum2022_cycle_periods.csv` tem 14 linhas com a coluna `metodo_baum` distinguindo **10 por periodograma** de **4 estimados a olho** (marcados `?` pelo próprio Baum). Baum **não publica FAP nem qualquer medida de significância**; o período é simplesmente o pico de maior potência. Os períodos de Baum são grau **B** e **não são equiparáveis** a `CYCLE` + FAP Excellent de B95.
**Descartado:** tratar os dois conjuntos de períodos como comensuráveis.

---

### D43 — As classificações de Baum entram como camada época-dependente para todas as 26 estrelas em comum, não só para HD 166620
**Data:** 2026-08-01 · **Base:** D34 generalizada; A9 §2 · **Status:** ativa · **Grau:** A
Das 26 estrelas em comum, **14 receberam nova classificação** (checksum §4.2 de Baum reproduzido). O catálogo `baliunas_table2_full.csv` **permanece congelado**. As classificações de Baum vivem em `baum2022_59stars.csv`, coluna `class_Baum`, ao lado de `class_A1`.
**Descartado:** corrigir A1 com as classificações de 2022.

---

### D44 — A incerteza residual dos offsets instrumentais de Baum é grau X; a junção 2001→2004 é tratada como descontinuidade declarada
**Data:** 2026-08-01 · **Base:** A9 §1.5, A9-F6 · **Status:** ativa · **Grau:** X
Baum corrige offsets por **deslocamento aditivo constante que alinha medianas** (§2.1.1–2.1.3). **Não publica** os valores dos offsets, a sua incerteza, nem a identidade das catorze estrelas de §2.1.3. As séries da Tabela 1 contêm apenas valores já corrigidos.
Medição própria do resíduo (`audit/a9_instrument_step.csv`, 51 estrelas): degrau relativo HKP-2 → HIRES-2 com **σ = ±4.47 %** entre estrelas; **25/51 excedem 1.2 %** (precisão de longo prazo, D14); 10/51 excedem 5 %; HD 166620 dá −8.8 % e HD 4628 — que Baum classifica como **ainda cíclica** — dá −16.3 %.
**Regra operacional:** nenhuma janela deslizante atravessa a junção sem decisão explícita registrada.
**Exceção, por D45b:** para **HD 166620** a calibração é robusta, estabelecida por Luhn+2022 §3.1/§4 via sobreposição temporal com os dados de Oláh+2016 e via fotometria APT independente. **A exceção não se estende às outras 58 estrelas.**

---

### D45 — A definição operacional de variabilidade intra-sazonal de Luhn+2022 §3.1 é adotada como receita e como precedente citável
**Data:** 2026-08-01 · **Base:** A10 §1.4, reproduzida exatamente · **Status:** ativa · **Grau:** A
Receita: (1) σ_S calculado **dentro de cada estação**; (2) subtração **em quadratura** de uma estimativa do ruído instrumental — Luhn adota 1.2 % para Mount Wilson (Baliunas+1995, "least variable stars") e **0.3 %** como limite superior do ruído sazonal do Keck; (3) comparação por **F-test**.
Reprodução independente sobre `J:ApJ:936:L23:table2.tsv`: σ_S(mín 1) = **0.0027**, σ_S(mín 2) = **0.0054**, σ_S(grande mínimo) = **0.0019** — os três valores publicados, exatos.
**Consequência:** resolve parcialmente **Q6**, ao dar um tratamento publicado para separar variabilidade astrofísica de ruído instrumental. É a citação mais forte disponível para a escolha de indicador do P4.

---

### D45b — A robustez de calibração estabelecida por Luhn é restrita a HD 166620
**Data:** 2026-08-01 · **Base:** A10-F4 · **Status:** ativa · **Grau:** A
Luhn §4: "the mutual calibration there is robust"; §3.1: "dispelling any doubts about potential offset errors". A conclusão apoia-se em (a) dados de Mount Wilson **contemporâneos** dos dados HIRES pré-2004, e (b) fotometria APT que **atravessa os três conjuntos**. Nenhuma das outras 58 estrelas de Baum tem qualquer dos dois. **D44 permanece em vigor para elas.**

---

### D46 — O teste temporal de CSD no formato de Dakos não é executável em HD 166620; a unidade de análise é a comparação de variabilidade entre estados
**Data:** 2026-08-01 · **Base:** A10-F2 · **Status:** ativa · **Grau:** A
Com os dados de Oláh+2016 a lacuna caiu de 6.91 para **2.82 anos** e a aproximação **está amostrada** — mas com **8 médias anuais de S_HK** (1995–2002) e **12 estações fotométricas APT** (1993–2004). Sob D20 (janela = 50 % do comprimento), 8 pontos dão 5 janelas de 4 pontos: φ₁ sobre 4 pontos não tem sentido estatístico e uma tendência de Kendall sobre 5 valores sobrepostos não é testável pelo procedimento de surrogates de D22.
**Isto entra no manuscrito como limitação declarada, não é contornado.**
**Descartado:** aplicar a maquinaria de janela deslizante do P4 à série anual de HD 166620.

---

### D47 — HD 4915 não é apresentada como candidata a mínimo de Maunder sem citar Isaacson+2024
**Data:** 2026-08-01 · **Base:** A10-F3, A11b-F3 · **Status:** ativa · **Grau:** A
Cadeia cronológica obrigatória: **Shah+2018** propõe a candidatura → **Luhn+2022 nota 8** especula que "may soon be entering its own grand magnetic minimum" → **Isaacson+2024 §5.6**, com linha de base estendida: "our extended time baseline shows **two cycles**. One periodicity is at 4.9 yr, and the second is more than 40 yr, and **the longer-period cycle is now turning higher**." A Tabela 4 da CLS V registra P = 4.86 yr.
**D07 permanece ativa** (HD 4915 removida do catálogo por não estar em Baliunas+1995) e **D35 permanece correta**; o que se acrescenta é que **a candidatura está desmentida na literatura de 2024**.

---

### D48 — A raridade publicada entra na Discussion como taxa-base, com a ressalva de que mede nível instantâneo
**Data:** 2026-08-01 · **Base:** Järvinen & Strassmeier 2025 §6; A11a-F1, A11a-F2 · **Status:** ativa · **Grau:** A
Número a citar: **13 candidatas em 13 326 alvos F8–G8 de sequência principal (0.1 %)**, das quais **11 são estrelas evoluídas** por paralaxe Gaia DR3 → **2 candidatas, 0.015 %**. Sentença: "Contrary to the initial suggestion from the Mount-Wilson H&K Survey, we conclude that such stars are very rare."
**Ressalva obrigatória e sustentada por duas fontes grau A:** o critério de Järvinen & Strassmeier é de **nível instantâneo**, e Luhn+2022 demonstrou que o nível **não cai** num grande mínimo (⟨S_HK⟩ = 0.171 no grande mínimo vs 0.172 no mínimo de ciclo). **HD 166620 não seria selecionada por aquele critério.** Logo o 0.1 % mede a frequência de estrelas *anomalamente fracas*, não de estrelas *em grande mínimo* — quantidades identificadas na literatura antiga e desidentificadas por Luhn+2022.

---

### D49 — A hipótese *aged out* entra na Discussion como nula concorrente; HD 101501 é o discriminante empírico
**Data:** 2026-08-01 · **Base:** CLS VI §3.3, §4; Baum §4.1; A11 §c.1 · **Status:** ativa · **Grau:** A
CLS VI: "noncycling stars that **may have aged out** of their cycles". Explica as mesmas observações sem bifurcação: perda monotônica e irreversível do ciclo por evolução. **Difere do quadro do P4 na reversibilidade e na existência de precursor.**
**Discriminante:** o retorno ao ciclo. **HD 101501** — dez anos de estado plano (≈1980–1990) seguidos de retorno à atividade cíclica **defasado em 180°** (Baum §4.1), 2 239 observações, baseline de 49 anos, presente em `baum2022_59stars.csv` — é o único caso conhecido e **falsifica *aged out* para aquele objeto**. A própria CLS VI §4 declara a lacuna: "Whether or not stars reach a noncycling level that is inescapable or if they can begin cycling again will require additional observations."

---

### D50 — A afirmação de estocasticidade e de transição rápida é citada textualmente e respondida, não omitida
**Data:** 2026-08-01 · **Base:** CLS VI §3.3.1, §3.3; A11 §c.2 · **Status:** ativa · **Grau:** A
Sentenças a citar na íntegra: "**The mechanisms that cause a star to enter and exit a magnetic minimum requires a stochastic process that is poorly understood**" e "suggestive of a **rapid (on stellar timescales) transition** … these transitions can occur **quickly, on order of years**".
**Por que é a objeção mais séria:** CSD exige aproximação lenta em relação à amostragem; transição "na ordem de anos" com amostragem anual não deixa janela — e A10-F2 chegou à mesma conclusão empiricamente no único caso amostrado.
**Resposta registrada, e é teórica:** a CLS VI descreve uma **distribuição bimodal de S-STD**, assinatura de sistema **biestável**. Biestabilidade forçada por ruído produz transições de aparência estocástica que **ainda exibem CSD**, porque a barreira de potencial encolhe antes do salto. **Este argumento exige base auditada em A7 (Scheffer 2009; Held & Kleinen 2004), que ainda não foi executada.** Registrado como dependência.

---

### D51 — A inclinação estelar entra como confundidor declarado do grupo `Flat`
**Data:** 2026-08-01 · **Base:** CLS VI §3.2; A11 §c.3 · **Status:** ativa · **Grau:** A (para τ Cet) / X (para as demais)
CLS VI, literal: "τ Ceti … is known to have a **pole-on inclination** (Korolik et al. 2023) that **precludes us from identifying its chromospheric activity cycle or rotational modulation** via S-STD."
**τ Cet (HD 10700) é uma das cinco `Flat` limpas do P4 e a estrela-padrão de dispersão.** Uma estrela vista de polo tem variabilidade suprimida **por geometria**, sem relação com o dínamo. Nenhuma unidade de auditoria anterior registrou este confundidor.
**Consequência:** afeta Q1, Q2 e Q6. A inclinação das demais `Flat` do P4 **não foi medida em nenhuma fonte auditada** — grau X, item de ação.

---

### D52 — A receita S → R′_HK fica estabelecida em grau A, com faixa de validade
**Data:** 2026-08-01 · **Base:** A12 §2, três passes de verificação · **Status:** ativa · **Grau:** A

```
R_HK      = 1.340 × 10⁻⁴ · C_cf(B−V) · S
log C_cf  = 1.13(B−V)³ − 3.91(B−V)² + 2.84(B−V) − 0.47
log C′_cf = log C_cf + Δ log C ;  Δ log C = 0                                    se B−V > 0.63
                                  Δ log C = 0.135x − 0.814x² + 6.03x³,  x ≡ 0.63 − (B−V) > 0
log R_phot = −4.898 + 1.918(B−V)² − 2.893(B−V)³
R′_HK     = R_HK − R_phot
```

Verificação: o PDF é scan com OCR de origem defeituoso (`10⁻⁴` lido como `Kr4`, `B−V` como `B—F`). Três passes: texto nativo, Tesseract a 400 DPI em `--psm 6/4/11`, e **inspeção visual direta das imagens de página ampliadas** — o passe que fixou expoentes e sinais.
Forma alternativa de Duncan, "fits the one used in this paper to within observational errors": **log R_phot = −4.02 − 1.40(B−V)** (grau B).
A constante 1.340 × 10⁻⁴ absorve a constante de Stefan-Boltzmann e um fator de normalização de 10¹⁴.

---

### D53 — A faixa de validade é 0.44 < B−V < 0.82 para R_phot, com extrapolação declarada acima e até 20 % de incerteza acima de 1.0
**Data:** 2026-08-01 · **Base:** A12 §3, Apêndice *b* e §II de Noyes+1984 · **Status:** ativa · **Grau:** A

| Faixa | Estatuto declarado pela fonte |
|---|---|
| B−V < 0.44 | fora do ajuste de R_phot |
| B−V < 0.63 | requer Δ log C (máximo não-físico de C_cf em 0.43) |
| **0.44 – 0.82** | **faixa em que R_phot foi ajustada** |
| 0.82 – 1.0 | extrapolação declarada; C_cf ainda "quite consistent" com espectrofotometria independente |
| **> 1.0** | "**the calibration may be uncertain by as much as 20 %**"; R_phot "becomes negligible" e "less certain for the coolest stars" |
| ≳ 1.2 | "**the worst discrepancy** in the various attempts at calibration" |

Aplicação ao catálogo congelado de A1 → `noyes1984_validade_cor.csv` (112 linhas). Distribuição: 82 dentro · 17 em 0.82–1.0 · 6 acima de 1.0 · 2 acima de 1.2 · 5 abaixo de 0.44.

---

### D54 — A migração para R′_HK deixa de ser melhoria presumida e passa a trade-off quantificado; a recomendação registrada é **não migrar**
**Data:** 2026-08-01 · **Base:** A12-F1, A12-F2, A12-F5; CLS VI §5 e §3.1 · **Status:** ativa · **Decisão final: humana (Q8 continua aberta)**

Três evidências contrárias novas, todas grau A:

1. **A validade da calibração é correlacionada com o grupo (A12-F1).** Das cinco `Flat` limpas, **quatro estão dentro** de 0.44–0.82; das treze `CYCLE` + FAP Excellent, **apenas cinco estão dentro e oito extrapolam**, duas (HD 32147 B−V = 1.06 e HD 201091 = 1.18) na região de até 20 % de incerteza declarada. Converter trocaria um confundimento de cor **conhecido e declarável** por um **erro sistemático concentrado num só braço da comparação** — que é pior.
2. **A fonte se desautoriza para o regime do P4 (A12-F2).** Noyes+1984, Apêndice *b*: a subtração de R_phot "does not have a large effect for active chromosphere stars, but **it can be a very significant correction for the chromospherically less active stars. For these stars in particular it is important to determine the photospheric correction more rigorously than has been done here.**" A amostra inteira do P4 está nesse regime.
3. **A comparação já foi feita e deu o resultado oposto ao esperado.** CLS VI §5, sobre 710 estrelas com séries de 20 anos: "neither average activity metrics of S-value, **log(R′_HK)-N1984**, nor the revised log(R′_HK) metric from Lorenzo-Oliveira et al. (2018) are able to identify [as não-cíclicas]. **More so than these two types of log(R′_HK), the S-value itself best correlates with S-value variability.**" E §3.1: "**the S-value plus the stellar mass is the best metric**."

**D40 confirmada e delimitada (A12-F5):** para B−V fixo a transformação é monotônica, logo τ é **exatamente** invariante, φ₁ muda pouco e σ² apenas reescala. O eixo **temporal** nada sofre com a migração — e nada ganha. O ganho seria todo no eixo **comparativo**, que é exatamente onde as três evidências acima incidem. Acresce que a receita tem **duas descontinuidades** (B−V = 0.63 e 0.82) **no interior da amostra P4** (A12-F3): um índice com costuras internas não é um índice unificador.

**Recomendação registrada:** manter S; tratar massa ou T_eff como covariável, seguindo a CLS VI; citar A12-F1 e A12-F2 como justificação explícita em Methods. **A decisão continua sendo humana.**

---

## 4d · Decisões da inspeção e da resolução (2026-11-14)

Origem: `inspecao/RELATORIO_INSPECAO.md` (I-01 a I-46), `audit/ERRATA_2026-11-14.md`, `audit/A7_theory.md`, `A8_usoskin.md`, `A13_olah.md`. **D55–D67 só registram fatos conferidos e corrigem texto de entradas anteriores por inclusão; D68 em diante são respostas do pesquisador ao memorando (autor: pesquisador)** (as D## antigas ficam como estão, regra 4). Nenhuma escolhe entre alternativas de mérito, nenhuma fecha uma Q#, nenhuma altera uma recomendação já registrada. Onde há escolha, a pergunta está em `P4_MEMORANDO_DECISOES_2026-11-14.md`.

---

### D55 — Errata de D41: a Tabela 3 da CLS V tem 52 372 linhas de dados, não 52 380
**Data:** 2026-11-14 · **Base:** I-10, `3.6-05`, `3.6-06` · **Status:** ativa · **Grau:** A · **Corrige:** D41
O arquivo `data/J_ApJS_274_35_table3.tsv` tem 52 413 linhas: 36 de comentário, 2 em branco, 3 de cabeçalho e **52 372 de dados**, igual às 52 372 do texto do artigo. O "Δ = 8" de D41, A9 §0, A11 e v6 §10 não existe. D41 não é editada; este é o valor a usar. Detalhe em `audit/ERRATA_2026-11-14.md` E-I10.

---

### D56 — O checksum de D43 (14 reclassificações de Baum) é grau B
**Data:** 2026-11-14 · **Base:** I-04, `3.8-08` a `3.8-11b` · **Status:** ativa · **Grau:** A (a contagem), B (o checksum) · **Corrige:** D43, A9 §2
A Tabela 2 de Baum dá mudança de tipo de classe em 13 das 26 estrelas comuns; HD 190406 não muda de tipo; contando `flat?` → `flat`, são 15. O 14 vem do texto de Baum §4.2 e a identidade dos 14 não se obtém da tabela. D43 permanece ativa em sua substância (camada época-dependente; catálogo congelado). O que muda: o "checksum §4.2 reproduzido" não sustenta grau A.

---

### D57 — Registro de fato sobre a receita de σ_S de Luhn+2022 e o F-test (I-01)
**Data:** 2026-11-14 · **Base:** I-01, `3.4-25` a `3.4-54`, `3.11-42` a `3.11-47`, A10 §1.4 · **Status:** ativa · **Grau:** A (os números), pergunta de mérito aberta · **Complementa:** D45
Três contas distintas existem e não coincidem: (i) desvio-padrão bruto do intervalo inteiro, com ruído de 1.2 % (Mount Wilson) ou 0.3 % (Keck) de ⟨S_HK⟩ subtraído em quadratura: 0.00269 / 0.00542 / 0.00195, os três valores publicados; (ii) a leitura literal do passo 1 de D45 (σ por estação de ano civil, quadratura por estação, média | mediana): 0.0028 | 0.0025, 0.0048 | 0.0049, 0.0015 | 0.0014; (iii) o F-test: variâncias brutas p = 8.80 × 10⁻⁶ (publicado 8.78 × 10⁻⁶); σ_S corrigidos p = 8.68 × 10⁻³ bilateral e 4.34 × 10⁻³ unilateral; valores arredondados p = 4.1 × 10⁻³. O p publicado de 8.78 × 10⁻⁶ reproduz-se com as variâncias **brutas** (8.80 × 10⁻⁶), e não com os σ_S corrigidos como a frase de v6 §2 sugere. A10-F1 (158 contra 119 observações) está resolvida por D58. **Não se escolhe a receita**: está no memorando (item 7). D45 permanece ativa como registrada.

---

### D58 — As 119 linhas `new_MW` de HD 166620 (1995–2002) são grau C: foram digitalizadas da Figura 2 de Oláh+2016
**Data:** 2026-11-14 · **Base:** A13-F2, I-44, Luhn arXiv:2207.00612 PDF p. 2, `3.4-60` a `3.4-63`, `3.11-42` a `3.11-45` · **Status:** ativa · **Grau:** A (o fato) / C (os dados) · **Complementa:** D46, D45b, A10 §1.2
O manuscrito de Luhn (versão de 5 de julho de 2022) diz que os dados completos de Mount Wilson de 1966–2002 não foram publicados e que usaram "a web application to scrape the data from Figure 2 of Oláh et al. (2016)", "reliable, but not exact", "119 (scraped) observations". A versão publicada troca isso por dados cedidos por K. Oláh e W. Soon e 158 observações. O VizieR tem 119 linhas `new_MW` com S_HK em 8 casas contra 4 nas outras, instantes fora do padrão e 29 linhas com época repetida. Pelo protocolo §4 são **grau C** até que os dados reais sejam obtidos. Não dependem delas: σ_S dos três estados, as médias de S_HK e o F-test de Luhn (A13-F3). Dependem: as oito médias anuais de 1995–2002, a lacuna de 2.82 anos e a afirmação de que a aproximação à transição está amostrada (D46). A lacuna de Baum de 6.91 anos (1997.73 a 2004.64) permanece real. Não decide o que fazer com a série; ver memorando.

---

### D59 — HD 101501: texto completo de Baum §4.1, cobertura e o que D49 deve dizer
**Data:** 2026-11-14 · **Base:** I-08, I-35, Baum PDF p. 7, `3.3-40`, `3.3-50` a `3.3-54`, `3.11-10` · **Status:** ativa · **Grau:** A · **Complementa:** D49, v6 §3.4
Baum §4.1: a estrela "appears to have entered a time period of about 10 yr from 1980 to 1990 where its previously identified periodic behavior dropped to a low S-value with little variation. It then returned to its strong, periodic activity variation." Cobertura: 2 239 observações em 49 anos; HKP-1 193, HKP-2 2 040, HIRES-1 0, HIRES-2 6; última época de Mount Wilson 1995.45; Keck de 2009.27 a 2017.14; maior lacuna 13.82 anos; 99.73 % de Mount Wilson. O estado plano e o retorno estão dentro de um só instrumento. Nenhuma estatística de variabilidade foi calculada (D04). D49 continua ativa; o texto do manuscrito sobre HD 101501 deve reproduzir a frase de Baum inteira e a cobertura acima.

---

### D60 — Errata de D54 item 3: a CLS VI analisa 91 estrelas, dentro de faixas de massa
**Data:** 2026-11-14 · **Base:** I-36, CLS VI PDF p. 1 e p. 4, `3.11-19`, `3.11-20` · **Status:** ativa · **Grau:** A · **Corrige:** D54 item 3, DECISOES §B, v6 §7 e §12
"We analyze the spectra of 91 solar-type G- and K-type main-sequence dwarfs"; log R′_HK < −4.90; massas 0.7–1.1 M☉ em quatro faixas (ciclo/total: 18/24, 20/29, 15/24, 5/13); 58 com ciclo. As 710 estrelas são a CLS V. A comparação de S contra log R′_HK é feita **dentro de cada faixa de massa**, e o artigo diz que a divisão por massa "reduces the need for a spectral-type indifferent metric". O teste compara métricas de atividade média com S-STD e não testa um indicador de CSD. A recomendação registrada em D54 (não migrar) não é alterada por esta entrada; o que muda é o número e o desenho que o manuscrito pode citar.

---

### D61 — Escopo de Noyes+1984 e magnitude da discrepância com Linsky (complementa D52, D53)
**Data:** 2026-11-14 · **Base:** I-43, Noyes PDF pp. 2 e 13–14, `3.11-27` a `3.11-30` · **Status:** ativa · **Grau:** A · **Complementa:** D52, D53
Noyes declara: "We are concerned in this paper with the mean level of activity" (p. 2), não com flutuações; define ⟨S⟩ pelo nível intermediário de uma curva traçada à mão. A calibração de Linsky et al. fica 0.3 dex abaixo da de Noyes em B−V = 1.25 ("disagreement by a factor of 2 seems large", p. 13); D53 registra a pior discrepância como "até 20 %" sem o valor. O uso de R′_HK em estudos de variabilidade é uma extensão do escopo de Noyes e deve ser declarada como tal. A recomendação de D54 permanece.

---

### D62 — B−V do catálogo de Baliunas e B−V da CLS V têm definições diferentes
**Data:** 2026-11-14 · **Base:** I-07, `3.9-21` a `3.9-24`, `3.7-09`, `3.7-10`, CLS V PDF p. 5, `3.11-15` · **Status:** ativa · **Grau:** A · **Complementa:** D53, A12-F1
O B−V da CLS V é derivado de T_eff e [Fe/H] (Ramírez & Meléndez 2005), não fotométrico. Nas 38 estrelas comuns, A1 − CLS V tem mediana +0.030 e 19 estrelas com |Δ| > 0.03. HD 10476 (0.84 → 0.801) entra e HD 32147 (1.06 → 0.993) sai da região de D53 conforme a fonte. D53 imprime a faixa como aberta (0.44 < B−V < 0.82); `noyes1984_validade_cor.csv` a trata como fechada: quatro estrelas em exatamente 0.44 ou 0.82 contam "dentro" (82 contra 78 pela leitura aberta). Sem o Sol: 4 dentro, 8 fora de 12 (A12-F1). A assimetria entre os braços permanece em todas as leituras. Que fonte de B−V rege a faixa é decisão humana, só se Q8 for reaberta.

---

### D63 — Todo PDF é validado na primeira página antes de ser usado
**Data:** 2026-11-14 · **Base:** I-38, A7-F1 · **Status:** ativa · **Grau:** A · **Complementa:** D38
O arquivo `Held & Kleinen 2004, GRL 31, L23207.pdf` é Boulton, Allison & Lenton 2014. Regra: título, autores e DOI conferidos nas páginas 1–2 do PDF e DOI conferido no Crossref (incluindo errata, REG-R11) antes de qualquer fato entrar. Registro em `bib/MANIFEST.json` (sha256, DOI, origem, publicada ou manuscrito) e `bib/DOWNLOAD_LOG.md`. Máximo de duas tentativas por fonte (REG-R8). Versões de arXiv são rotuladas como manuscrito. Não se contornam acessos bloqueados.

---

### D64 — Períodos de Baliunas+1995 que o catálogo congelado perdeu: reparos num arquivo lateral
**Data:** 2026-11-14 · **Base:** I-11, I-41, B95 Tabela 2 pp. 280–281, `3.13-01` a `3.13-04`, `consolidacao/rascunho_reparos_catalogo.csv` · **Status:** ativa · **Grau:** B (leitura visual única) · **Complementa:** D36, D01
B95 imprime período tentativo para seis estrelas `CYCLE` que v4 §2 chama "sem período": HD 10780 "> 7", 88737 "24?", 111456 "7?", 126053 "22?", 176051 "10?", 185144 "7?" (nota s: dados esparsos antes de 1980, fora do periodograma). HD 76572: "7.1 ± 0.2, Poor"; HD 219834A: "21 ± 1, Good". São 10 reparos de valor e 33 normalizações de `secondary`, num arquivo **lateral**; `baliunas_table2_full.csv` permanece congelado (112 × 14, `3.13-04`). Os seis tentativos entram como campo próprio `P_cyc_tentativo`, sem uso como `P_cyc`. A explicação de A9-F2 para o branco de Baum em HD 185144 não se sustenta para o período e A9-F2 segue como contradição aberta. Os dois passes do protocolo (§4) não foram refeitos: grau B.

---

### D65 — A Tabela 4 de Egeland+2017 foi obtida; cobre 1966–2016, ciclos 20–24
**Data:** 2026-11-14 · **Base:** I-45, `3.12-01` a `3.12-13`, `data/Egeland2017_table4_apjaa4e49t4_mrt.txt`, Egeland PDF p. 9 · **Status:** ativa · **Grau:** A · **Complementa:** D18, D16 · **Corrige:** A3-F5 (cobertura)
6 349 linhas, 1966.669–2016.153, cinco instrumentos (MWO/HKP-1 162, MWO/HKP-2 75, NSO/SP 4 112, SSS/CCD-1 1 241, SSS/CCD-2 759), maior lacuna interna 2.67 anos, mediana de 152 observações por ano. Egeland §4.6: a composta cobre os ciclos 20–24; os ciclos 15–19 só na composta mensal KKL. O pipeline (célula 10) assume ~20 440 pontos para 1966–2021, o que não é o tamanho da série (pipeline congelado, não editado). A média das médias anuais é 0.1702 em 1966–2016 contra 0.1694 (ciclos 15–24) de Egeland: janelas diferentes. D18 está desbloqueada para 1966–2016; o resto da escolha (anual ou bruta, janela) é do pesquisador. O IOP respondeu (arquivo servido publicamente); o item da §6 sai.

---

### D66 — Estado das auditorias A7, A8 e A13
**Data:** 2026-11-14 · **Base:** `audit/A7_theory.md`, `A8_usoskin.md`, `A13_olah.md` · **Status:** ativa · **Grau:** A (citações) · **Complementa:** D37
A7 fechada **parcialmente**: Scheffer 2009 auditado por inteiro, Boulton+2014 como fonte complementar; Held & Kleinen 2004 pendente de upload (DOI 10.1029/2004GL020972). A7-F2: a bifurcação de Hopf de Scheffer é do sentido estável → oscilante, e o caso do P4 é o oposto; nenhuma fonte lida dá sinal precursor para perda de ciclo limite (extensão por analogia). A8 fechada com leitura parcial declarada (Usoskin §3 e §5 não lidos): a previsão de grandes mínimos "hardly" possível; o mínimo de 2008–2009 é "unusual for the space era but may be quite typical for the normal activity"; a série solar cobre o fim de um grande máximo. A13: Oláh+2016 é fonte de período independente (23 de 25 períodos diferem de B95 por mais de 2 dP). Nenhuma decide mérito. Protocolo §10 atualizado.

---

### D67 — Errata dos números de A9, A11, A12 e do v6
**Data:** 2026-11-14 · **Base:** I-02, I-03, I-05, I-12, I-15, I-16, I-23, I-24, I-33, I-42 · **Status:** ativa · **Grau:** A · **Complementa:** A9, A11, A12, v5, v6
Lista, com valor correto e checagem, em `audit/ERRATA_2026-11-14.md` (E-I02 a E-I43). Entre as que mudam o uso: HD 3651 tem ciclo de 10.01 anos na CLS V (A11 dizia "não"); as três estrelas de menor SSD/Smed com Nobs ≥ 45 são HD 187923 (0.372 %), HD 144579 (0.397 %) e HD 55575 (0.448 %), de modo que o "piso 0.45 %" é o valor do texto e não da tabela (grau X até o pesquisador escolher qual citar em Q6); a mediana de B−V de `Long` é 0.525, não 0.49, e a faixa "0.49 a 0.88" de Q8 não se reproduz.

---

---

---

### D68 — A série anual e a série bruta entram **ambas**, com papéis distintos
**Data:** 2026-11-14 · **Autor:** pesquisador · **Base:** memorando item 1; Q9, D24, D46, D57, D65 · **Status:** ativa · **Grau:** decisão humana
Resposta do pesquisador à pergunta "a série anual ou a bruta é o objeto do P4?": **"Ambas, com papéis distintos."** Não define ainda qual métrica roda em qual série: essa distribuição de papéis é pergunta de acompanhamento (memorando, rodada 2). Não altera D24, D20–D23 enquanto os papéis não forem definidos; Q9 permanece aberta até lá. Q1 não é respondida por esta entrada.

---

### D69 — S e R′_HK são analisados **ambos**; a migração exclusiva para R′_HK é descartada como decisão
**Data:** 2026-11-14 · **Autor:** pesquisador · **Base:** memorando item 3 (Q8); D52, D53, D54, D60, D61, D62 · **Status:** ativa · **Grau:** decisão humana · **Complementa:** D54
Resposta: **"Ambos, porque R′_HK é fotosférico subtraído, diferente de S-index que tem componente fotosférico e cromosférico."** A análise usa os dois índices. D54 continua registrada com a sua recomendação histórica (não migrar), que passa a ser superada por esta decisão no ponto "migrar ou não"; o que D54 estabelece sobre a receita e a faixa de validade continua valendo. Consequências a observar, não decididas aqui: a parte em R′_HK fica sob a faixa 0.44 < B−V < 0.82 de D53 e o escopo de Noyes (D61: nível médio, não flutuação), com a definição de B−V declarada (D62); a CLS VI testa métricas dentro de faixas de massa (D60). Quais estrelas e quais estatísticas entram em R′_HK fica para a rodada de Q1 e Q2.

---

### D70 — A receita de σ_S de Luhn (D45 / D57): subsídios entregues, escolha adiada
**Data:** 2026-11-14 · **Autor:** pesquisador · **Base:** memorando item 7; I-01 · **Status:** ativa · **Grau:** A (subsídios)
Resposta do pesquisador: **"Subsídios para defesa."** Entregue `SUBSIDIOS_RECEITA_SIGMA_S.md` (para cada conta, o que sustenta e o que enfraquece, com ids). **Nenhuma receita foi escolhida.** I-01 permanece aberto como pergunta de mérito. O texto de Methods sobre σ_S fica bloqueado até a escolha.

---

### D71 — Aprovada a incorporação ao caderno além da instrução de DECISOES
**Data:** 2026-11-14 · **Autor:** pesquisador · **Base:** memorando item 11; I-18 · **Status:** ativa · **Grau:** decisão humana
Resposta: **"Aprovo."** Ficam aprovados o cabeçalho "Última entrada", a §6 reescrita, as obrigações de Methods adicionadas à §7, as novas §10 (fatos com página) e §11 (uso de IA) e a supressão da coluna "Subsídios" da §5.

---

---

### D72 — Junção instrumental 2001→2004 (item 4): subsídios entregues, escolha adiada
**Data:** 2026-11-14 · **Autor:** pesquisador · **Base:** memorando item 4; D44; I-09 · **Status:** ativa · **Grau:** A (subsídios)
Resposta do pesquisador: **"Subsídios para decidir."** Entregue `SUBSIDIOS_JUNCAO_E_D46.md` (parte "Item 4"). Nenhuma alternativa escolhida; vale a regra operacional de D44 (nenhuma janela atravessa a junção sem decisão registrada) até a escolha.

---

### D73 — Aceitar D46 (item 5): subsídios entregues, escolha adiada
**Data:** 2026-11-14 · **Autor:** pesquisador · **Base:** memorando item 5; D46; D58 · **Status:** ativa · **Grau:** A (subsídios)
Resposta: **"Subsídios para decidir."** Entregue `SUBSIDIOS_JUNCAO_E_D46.md` (parte "Item 5"). D46 permanece como registrada, sem ser aceita nem revogada por esta entrada.

---

### D74 — Resposta teórica de D50 (item 6): esperar Held & Kleinen
**Data:** 2026-11-14 · **Autor:** pesquisador · **Base:** memorando item 6; D50; A7-F1, A7-F2 · **Status:** ativa · **Grau:** decisão humana
Resposta: **"Esperar Held & Kleinen."** A decisão sobre a sustentação da resposta teórica de D50 fica adiada até o pesquisador subir o PDF (DOI 10.1029/2004GL020972), que será validado (D63) e lido para completar A7. D50 permanece como registrada.

---

### D75 — Piso instrumental de Q6 (item 8): citar os dois valores
**Data:** 2026-11-14 · **Autor:** pesquisador · **Base:** memorando item 8; I-03; D67 · **Status:** ativa · **Grau:** decisão humana · **Complementa:** Q6 (que permanece aberta quanto à apresentação do grupo `Flat`)
Resposta: **"Citar os dois."** O piso é citado como a faixa **0.37–0.45 %**, com as duas fontes: 0.372 % (HD 187923) é o menor SSD/Smed da Tabela 2 da CLS V com Nobs ≥ 45, e 0.45 % é o valor do texto do artigo (HD 55575, 0.448 % na tabela). A frase "três vezes abaixo do limiar `Flat`" deve ser reescrita com a faixa (`3.6-24` a `3.6-26`). Não decide Q6.

---

---

### D76 — Papéis das séries anual e bruta (D68): subsídios entregues, escolha adiada; A14 (Korolik) executada para Q11
**Data:** 2026-11-14 · **Autor:** pesquisador · **Base:** memorando, desdobramento de D68 e Q11; `audit/A14_korolik.md` · **Status:** ativa · **Grau:** A (subsídios e citações) · **Complementa:** D68, D51
Resposta sobre a distribuição dos papéis: **"Definir depois dos subsídios."** Entregue `SUBSIDIOS_PAPEIS_SERIES.md` (por métrica: DFA, CSD em janelas, σ por estado, ciclo, comparação de estados). Nenhum papel foi atribuído. Sobre Q11 o pesquisador pediu **"Auditar Korolik antes"**; A14 fechada: τ Ceti tem inclinação 7° ± 7° (grau A), P_rot não determinado (46 ± 4 d por girocronologia, 32 ± 9 d no Mount Wilson, 43 ± 7 d no APT, 23 d em RV), e a ligação "inclinação → ciclo não identificável" é da CLS VI, não de Korolik; a inclinação das demais `Flat` segue grau X (A14-F4). Q11 permanece aberta.

---

### D77 — Layout do repositório e migração ao Kit (item 10, I-27): subsídios entregues, escolha adiada
**Data:** 2026-11-14 · **Autor:** pesquisador · **Base:** memorando item 10; I-27 · **Status:** ativa · **Grau:** A (subsídios)
Resposta: **"Subsídios."** Entregue `SUBSIDIOS_LAYOUT_KIT.md` (mapa arquivo a arquivo, conflitos com D31 e D38, três alternativas). O layout atual permanece até a escolha.

---

### D78 — Q2–Q7 permanecem abertas; entram na rodada de Q1
**Data:** 2026-11-14 · **Autor:** pesquisador · **Base:** memorando item 9 · **Status:** ativa · **Grau:** decisão humana
Resposta ao item 9 ("auditar Korolik antes (Q11)", sem pedir mais nada): Q2, Q3, Q4, Q5, Q6 (apresentação do grupo `Flat`; o piso instrumental já está em D75) e Q7 **ficam abertas**, sem subsídios novos pedidos nesta rodada.

---

### D79 — Q1 espera a definição dos papéis das séries
**Data:** 2026-11-14 · **Autor:** pesquisador · **Base:** memorando item 2; D68, D76 · **Status:** ativa · **Grau:** decisão humana
Resposta: **esperar os papéis das séries** (a opção que o memorando indicava). Q1 permanece aberta e não recebe subsídios nesta rodada.

---

### D80 — Errata de D66: o log de auditorias do protocolo (§10) não foi atualizado
**Data:** 2026-11-14 · **Autor:** Claude (registro de fato) · **Base:** `P4_AUDIT_PROTOCOL.md` §10 (A7 e A8 ainda "open"); `git log` do arquivo · **Status:** ativa · **Grau:** A · **Corrige:** D66
D66 diz "Protocolo §10 atualizado". **Isso não é verdade**: o protocolo é arquivo existente e não foi editado nesta rodada (`P4_AUDIT_PROTOCOL.md` só tem o commit de upload original). A7, A8 e A13 constam como "open" ou ausentes no §10 do protocolo; o estado real está em `audit/A7_theory.md`, `A8_usoskin.md`, `A13_olah.md`, `A14_korolik.md` e em D66/D76. Atualizar o log do protocolo, se desejado, é decisão do pesquisador.

---

### D81 — Held & Kleinen 2004, Livina & Lenton 2007 e Peng+1993 validados, lidos e auditados (A7b, A5b)
**Data:** 2026-11-24 · **Base:** `audit/A7b_held_kleinen.md`, `audit/A5b_peng_livina.md`, `3.11-50` a `3.11-62`, `bib/MANIFEST.json` · **Status:** ativa · **Grau:** A (citações) · **Complementa:** D50, D24, D26, D63; **cumpre a condição de D74**
Os três PDFs subidos pelo pesquisador em 2026-11-24 têm título, DOI e volume conferidos na página 1 (Peng também no Crossref). Fatos, com página do PDF:
- **Held & Kleinen** (pp. 1–4): em qualquer bifurcação o menor decaimento κ se anula e a variabilidade do modo diverge (p. 1); o modelo é AR(1) unidimensional, com c = exp(κΔt) obtido da autocorrelação de lag 1 após remover tendência linear (p. 2); **"oscillatory modes do not play a major role … could be easily included by a 2D ansatz" (p. 2)**, sem tratamento; erro δκ ≈ √(2κ/T) (p. 3); três obstáculos em dados reais, entre eles "the system may not be as close to a bifurcation" (p. 4). **Nenhuma das três fontes teóricas lidas (Scheffer, Boulton, Held & Kleinen) dá sinal precursor para a perda de um ciclo limite** (A7b-F1).
- **Livina & Lenton** (pp. 1–4): a calibração DFA → c (α = 1.5 como c → 1) está no §2.4 (p. 3), é empírica, ajustada em AR(1) de 20 000 pontos; "the record should be at least of order a thousand points" (p. 3); janela de ACF de 10 % da série (p. 2); série da Groenlândia, 1586 pontos não equidistantes, janelas de 500 (p. 4). **Fecha o X de A5 §6 sobre o reescalonamento.**
- **Peng+1993** (pp. 1–4): o desvio-padrão do expoente de uma sequência de comprimento finito cai com √N e **não depende da amplitude do ruído**; "inversely proportional to the square root of the number of independent samples" (p. 2); inclinação 1/2 na Fig. 3 (p. 3); o estimador é o da caminhada de DNA, anterior ao DFA. **Fecha o X de A5 §6 sobre o viés de comprimento finito.** Continua X: `H = (β+1)/2`.
Nada disto decide D50, D24 ou Q9. D50 permanece como registrada; o item 6 do memorando volta a ser decidível pelo pesquisador (D74 pedia esperar este artigo). A7 e A5 não são editadas.

---

### D82 — Os dados reais de Mount Wilson de HD 166620 (1995–2002) não estão em catálogo público alcançável
**Data:** 2026-11-24 · **Base:** `bib/DOWNLOAD_LOG.md` (seção de 2026-11-24); pedido do pesquisador "verificar e baixar através de catálogos do VizieR" · **Status:** ativa · **Grau:** A (a ausência vista) / X (a existência dos dados) · **Complementa:** D58
Resultado: os servidores do CDS não respondem deste ambiente; o espelho de Harvard tem `J/ApJ/936/L23` (a tabela de Luhn já em `data/`, com as 119 linhas digitalizadas) e **não tem** `J/A+A/590/A133` (Oláh+2016), nem sua `table1` (duas tentativas, REG-R8), nem `J/ApJ/438/269`; o TAP do espelho não responde. Não se achou nenhuma série de 1995–2002 de HD 166620 em catálogo. As 119 linhas continuam grau C (D58). Caminho que resta: pedir a série de 158 pontos a K. Oláh e W. Soon (rascunho `consolidacao/PEDIDO_DADOS_OLAH_SOON.md`, não enviado). A Figura 2 de Oláh não é digitalizada (regra 8). O Dataverse de Radick & Pevtsov não foi tentado.

---

### D83 — O espelho NAO do VizieR devolve a mesma tabela de Luhn: 119 linhas `new_MW`, sem a série de 158 pontos
**Data:** 2026-11-24 · **Base:** `asu1.tsv` enviado pelo pesquisador (sha256 em `bib/DOWNLOAD_LOG.md`), comparado a `data/J_ApJ_936_L23_table2.tsv` · **Status:** ativa · **Grau:** A · **Complementa:** D58, D82
As tabelas 2 e 3 de `J/ApJ/936/L23` baixadas do espelho NAO são idênticas às já em `data/` (1 885 linhas: 1 654 MW, 112 HIRES, **119 `new_MW`**; 1 278 APT). O VizieR, portanto, só tem o conjunto digitalizado; **os dados cedidos por Oláh e Soon (158 pontos) não estão no catálogo**. As 119 linhas seguem grau C (D58). O caminho que resta é o pedido aos autores (D82).

---

### D84 — Outras fontes públicas esgotadas: a série de HD 166620 em 1995–2002 só existe com Oláh e Soon
**Data:** 2026-11-24 · **Autor:** pesquisador (opção 2: "tentar outras fontes públicas"), execução por Claude · **Base:** `bib/DOWNLOAD_LOG.md` (seção "noite") · **Status:** ativa · **Grau:** A (as ausências vistas) · **Complementa:** D58, D82, D83
O Dataverse de Harvard tem o arquivo do HK Project de 2001 (`HK_Project_v2001_NSO`, 35 estrelas, até o fim de 2001), **sem HD 166620**, e o de 1995, que só chega a 1995. Os pacotes TeX de Luhn e de Oláh não trazem a série (um trecho de 5 linhas e figuras EPS). Digitalizar as figuras é proibido (regra 8). Nenhuma fonte pública alcançável tem os dados; as 119 linhas continuam grau C (D58). O caminho que resta é o pedido aos autores (rascunho `consolidacao/PEDIDO_DADOS_OLAH_SOON.md`, não enviado).

---

### D85 — HK_Project_v2001_NSO: dados públicos de Mount Wilson até 2001 para 29 estrelas que Baum não tem, entre elas quatro dos sete controles ausentes
**Data:** 2026-11-24 · **Base:** `data/HK_Project_v2001_NSO/` (Dataverse `10.7910/DVN/H85QPF`; README: observações "through late 2001"), `3.15-01` a `3.15-06`, `inspecao/saidas/11_dataverse_v2001*.txt` · **Status:** ativa · **Grau:** A (a comparação) · **Complementa:** D41, D33, D36; **informa** Q1 (não a decide)
Fatos:
- O pacote tem 35 estrelas, **sem HD 166620** (`3.15-02`); seis delas estão no subconjunto de Baum (HD 10476, 143761, 146233, 152391, 182572, 185144). Para essas seis as linhas HKP de Baum são as mesmas do v2001: 14 233 de 14 295 coincidem (tempo a 0.002 ano, S a 5 × 10⁻⁴; as 62 restantes são de HD 10476, diferenças de calibração entre compilações, que o README estima em 1–2 %) e **nenhuma linha v2001 passa do último ponto HKP de Baum** (`3.15-04`, `3.15-05`). Ou seja, Baum já tinha o v2001 para elas; **não há extensão**.
- Os outros 29 são estrelas que Baum não tem, com 33–35 anos (1966–2001), 1 459 a 4 819 observações cada e lacuna máxima de cerca de 1 ano (exceções: HD 129333, 4.97 anos; HD 158614, 3.90 anos; HD 203387 só desde 1982). Tabela em `saidas/11_dataverse_v2001_not_in_baum.txt`.
- Dos **seis controles ausentes de Baum** (I-12; A9-F5), **quatro estão no v2001: HD 160346, 201091, 81809, 103095** (`3.15-06`); HD 16160 e 32147 não. Das cinco `Flat` limpas só HD 182572 está no v2001 (já em Baum); as `Flat` que o v2001 acrescenta são não limpas (HD 13421, 124570, 158614, 216385).
Limites: o v2001 é um único instrumento e calibração (HKP-2 após 1977) e termina em 2001, **sem o HIRES**, de modo que não tem os 50 anos de Baum; não substitui nem altera o catálogo congelado nem as séries de Baum (D36, D41). Obrigação de agradecimento do README: citar "The HK_Project_v1995_NSO data derive from the Mount Wilson Observatory HK Project, which was supported by both public and private funds through the Carnegie Observatories, the Mount Wilson Institute, and the Harvard-Smithsonian Center for Astrophysics…" e designar os arquivos como "HK_Project_v2001_NSO". Nenhuma Q# é decidida; o subsídio para Q1 é que o desequilíbrio de presença entre `Flat` (4/5) e controles (6/13) pode cair para 10/13 se o v2001 entrar como camada ao lado, ao custo de um baseline de 35 anos sem HIRES.

---

### D86 — Seguir sem os dados de Oláh e Soon; as 119 linhas `new_MW` ficam grau C
**Data:** 2026-11-24 · **Autor:** pesquisador · **Base:** D58, D82, D83, D84, D85; pergunta "é mesmo necessário pedir os dados à Oláh?" · **Status:** ativa · **Grau:** decisão humana · **Complementa:** D58, D46
Resposta do pesquisador: **"Seguir sem os dados de Oláh, mantendo grau C."** Consequências registradas, sem decisão nova de mérito: (i) o pedido a Oláh e Soon **não será enviado** (o rascunho em `consolidacao/PEDIDO_DADOS_OLAH_SOON.md` fica arquivado); (ii) as 119 linhas `new_MW` de HD 166620 (1995–2002) permanecem **grau C** (D58) e, pela regra 8 do CLAUDE.md e pelo protocolo §4, não chegam ao manuscrito como valor; qualquer uso (por exemplo, as oito médias anuais ou a lacuna de 2.82 anos) é análise de sensibilidade declarada como digitalizada; (iii) o que não depende delas segue válido: σ_S dos três estados, as médias de S_HK e o F-test de Luhn (A13-F3); (iv) a frase "a aproximação à transição está amostrada" (D46) não pode ser afirmada com grau A. D46 e a receita de σ_S (D70) continuam pendentes.

---

## 5 · Questões abertas — exigem decisão humana

Numeradas `Q#`. Cada uma tem subsídios já levantados; nenhuma tem resposta óbvia.

| # | Questão | Estado após A9–A12 |
|---|---|---|
| **Q1** | **Composição da amostra** | **aberta — desbloqueada.** D32 cumprida. Subsídios: `paper_state_v6.md` §3, com quatro opções e os custos de cada uma. Custo novo e decisivo: A9-F5 (N × grupo no subconjunto Baum) |
| **Q2** | O que conta como "flat" | **aberta — subsídio novo.** Quatro das cinco `Flat` têm agora medida moderna: σ_S/S = 0.72 / 0.86 / 0.95 / **1.49 %** (A11 §b.3). HD 182572 falha. **E D51 acrescenta a inclinação como confundidor geométrico completo** |
| **Q3** | Largura de banda gaussiana | **aberta — inalterada** |
| **Q4** | A componente de 44 anos | **aberta — reforçada.** A11b-F5: componentes longas quase degeneradas com tendência são o caso **típico**, não uma idiossincrasia solar. Isso transforma Q4 numa questão genérica do método |
| **Q5** | Binárias | **aberta — inalterada.** Nota: HD 81809 está **ausente** de Baum |
| **Q6** | O grupo `Flat` tem problema de medida | **aberta — grande avanço.** Piso instrumental moderno = **0.45 %**, três vezes abaixo do limiar `Flat`. **D45** dá o tratamento de subtração de ruído em quadratura. Continua a exigir decisão de apresentação |
| **Q7** | Subgigantes no grupo `Flat` | **aberta — agora é objeção publicada.** Três fontes independentes: Wright 2004, Baum §5.5 (A9-F8), Järvinen & Strassmeier §1 e §6 (11 de 13 candidatas eliminadas por serem evoluídas). Tem de ser neutralizada **por construção da amostra**, não por argumento |
| **Q8** | Migrar para log R′_HK? | **aberta — balanço invertido.** D54: três evidências contrárias grau A. Recomendação registrada: **não migrar** |
| **Q9** | DFA volta a ser admissível para o subconjunto Baum? | **aberta — reportada, não decidida.** N mediano = **27 estações anuais** (abaixo do piso) vs **698 observações brutas** (acima). **A pergunta é anterior:** a série anual ou a bruta é o objeto do P4? (`paper_state_v6.md` §6) |
| **Q10** | **NOVA — a transição é lenta o bastante para ter precursor detectável?** | **aberta.** CLS VI: "on order of years". A10-F2: 8 pontos anuais na aproximação do único caso amostrado. **Se a resposta for não, a tese central do P4 não é testável com os dados existentes.** Depende de A7 |
| **Q11** | **NOVA — a inclinação estelar confunde o grupo `Flat`?** | **aberta.** D51. Confirmada para τ Cet; não medida para as demais |

**Atualização de 2026-11-14 (respostas do pesquisador ao memorando):** Q8 → **D69** (S e R′_HK, ambos); decisão-raiz anual × bruta → **D68** (ambas, papéis por definir; Q9 segue aberta); receita de σ_S → **D70** (subsídios entregues, escolha adiada); I-18 → **D71**; junção → **D72** e D46 → **D73** (subsídios entregues, escolha adiada); D50 → **D74** (esperar Held & Kleinen); piso de Q6 → **D75** (0.37–0.45 %); papéis das séries → **D76** (subsídios) e A14 (Korolik); layout → **D77** (subsídios); Q2–Q7 → **D78** (abertas); Q1 → **D79** (espera os papéis). Q1–Q7, Q10 e Q11 seguem abertas.

**Atualização de 2026-11-24:** Held & Kleinen, Livina & Lenton e Peng+1993 lidos → **D81** (D74 cumprida na condição; o item 6 do memorando volta a ser decidível); dados de HD 166620 em 1995–2002 não achados em catálogo → **D82**.

---

## 6 · Itens de ação e bloqueios (atualizado em 2026-11-14)

Ambiente testado em 2026-11-14 (REG-08): respondem Crossref, arXiv, IOP (download público), Semantic Scholar, OpenAlex; **bloqueados** (HTTP 403): Wiley/AGU, site da A&A; Peng+1993 é de acesso fechado; a cópia do PIK de Held & Kleinen é privada (não contornada). `pdftotext` disponível; `tesseract` não (usado RapidOCR e leitura visual).

| Item | Estado | Necessário para |
|---|---|---|
| **Tabela 4 de Egeland+2017** | **resolvida** (D65): `data/Egeland2017_table4_apjaa4e49t4_mrt.txt`, 6 349 linhas, 1966–2016 | D18 |
| **Held & Kleinen 2004** (10.1029/2004GL020972) | **resolvido em 2026-11-24** (D81): `bib/Held_2004_GRL_31_L23207.pdf` (o arquivo da raiz com este nome continua sendo Boulton+2014, D63) | A7, D50, Q10 |
| Livina & Lenton 2007 (10.1029/2006GL028672) | **resolvido em 2026-11-24** (D81): `bib/Livina_2007_GRL_34_L03712.pdf` | A5, Q9 |
| Peng et al. 1993 (10.1103/PhysRevE.47.3730) | **resolvido em 2026-11-24** (D81): `bib/Peng_1993_PRE_47_3730.pdf` | A5, Q9 |
| Järvinen & Strassmeier 2025, versão publicada, DOI 10.1051/0004-6361/202554111 | opcional — há o manuscrito do arXiv | citação final |
| Oláh+2016, versão publicada, DOI 10.1051/0004-6361/201628479 | opcional — há o manuscrito do arXiv | citação final |
| Dados reais de Mount Wilson de HD 166620 em 1995–2002 (Oláh e Soon) | **não estão em fonte pública** (D82–D85); **decidido seguir sem eles, grau C (D86)**; o pedido aos autores não será enviado | D46 |
| Harvard Dataverse: Radick & Pevtsov (10.7910/DVN/ZRJ6NT, 10.7910/DVN/H85QPF); Pevtsov 2016 (10.7910/DVN/VF5BMO) | não testados; opcional | offsets de Baum (D44); contexto de D18 |
| Série S solar NSO | dispensada pela D65 (Tabela 4) | — |

Obtidos e validados nesta rodada, em `bib/` (ver `bib/MANIFEST.json`): Shah+2018 (HD 4915), Brandenburg+1998 (Paper I), Korolik+2023 (τ Ceti), Egeland+2017 (arXiv), Luhn+2022 (arXiv), Baum+2022 (arXiv).

---

## 7 · Arquitetura de escrita do paper

O caderno passa a fazer parte da arquitetura de documentos. Papéis:

| Documento | Papel | Ciclo de vida |
|---|---|---|
| **`P4_RESEARCH_NOTEBOOK.md`** (este) | memória longa: toda decisão, base e alternativa descartada | permanente; só cresce, nunca é reescrito |
| `paper_state_v#.md` | estado corrente: o que está feito, o que vem a seguir | substituído a cada conversa |
| `audit/A#_*.md` | extrações graduadas, achado a achado | congelados após o fechamento da unidade |
| `P4_SOURCE_VALUES.md` | referência única de valores para o manuscrito | gerado na consolidação; **nada em grau C** |
| `p4_star_catalog.csv` | catálogo congelado da amostra | gerado na consolidação |
| `audit/*.csv` | dados brutos extraídos e cross-matches | congelados |

**Regra de rastreabilidade:** todo número do manuscrito → entrada em `P4_SOURCE_VALUES.md` →
decisão `D##` neste caderno → seção de um artigo-fonte. Uma cadeia quebrada é um bloqueio de
submissão, não um detalhe.

**Obrigações de Methods que já estão fixadas** (para não serem redescobertas na redação):
D08 (média anual, N≈26), D12 (N uniforme por construção — dizer explicitamente), D20–D23
(parâmetros e significância), D24–D26 (DFA), D30 (componente de 44 anos), e a ressalva de Q6.

**Obrigações de Methods adicionadas em 2026-11-14** (já fixadas pelas decisões ativas; nenhuma escolha nova): D44 (a junção 2001→2004 é uma descontinuidade declarada; nenhuma janela a atravessa sem decisão registrada; incerteza dos offsets de Baum é grau X), D45 e D57 (a receita de σ_S deve ser descrita exatamente como executada), D46 (8 médias anuais comparam estados e não alimentam janela deslizante), D58 (as 119 linhas `new_MW` são digitalizadas, grau C), D49 e D59 (HD 101501: citar Baum §4.1 inteiro e a cobertura), D50 (estocasticidade e transição rápida citadas e respondidas), D51 (inclinação), D52–D53 e D61 (receita S → R′_HK, faixa de validade, escopo de Noyes), D60 (a CLS VI analisa 91 estrelas por faixa de massa). Limitação de D46 a constar na Discussão.

---

## 8 · Questões **fechadas** — não reabrir sem fonte nova

Esta seção existe para prevenir loops. Cada item foi decidido com base auditada; revisitá-lo por
novo raciocínio sobre as mesmas fontes é retrabalho.

| Questão | Resposta | Fechada por |
|---|---|---|
| DFA serve para as séries estelares? | **Não** para o catálogo Baliunas (N≈26 vs piso >100). **⚠ Reaberta como Q9** para o subconjunto Baum+2022 — fonte nova, conforme a regra desta seção | A1-F9, A2 §5, A4-F4, A5-F5; reabertura D37 |
| Lockwood+2007 estende a série? | **Não.** Nenhuma série numérica publicada | A2-F1 |
| N é confundido com grupo? | **Não.** Uniforme por construção | A2 §5 |
| Estrelas e Sol estão na mesma escala? | **Sim**, desde que se use Egeland para o Sol. S é HKP-2 por definição | A3 §3.1 |
| S_SUN_MEAN está correto? | **Sim**, 0.1694, grau A por checksum | A3-F1 |
| A Tabela 2 de Baliunas tem coluna σ_S? | **Não.** A Tabela 1 tem, mas é de estrelas-padrão | A1-F1, A6 §3 |
| HD 4915 existe? | **Não** | A1-F2 |
| Como se estabelece significância? | 1000 surrogates ARMA sobre resíduos | A4 §1.3 |
| Lockwood+2007 estende a série? (revisitado) | Não — mas **Baum+2022 sim**. A2-F1 continua correto sobre Lockwood; a extensão vem de outra fonte | A2-F1; D33 |
| O ⟨S⟩ solar de Baliunas serve? | **Não.** Proxy, +5% na média, +76% na amplitude | A3-F2/F3 |
| Baliunas e Saar concordam nas classificações? | **Parcialmente.** 5 divergências de classe, 5 de período, registradas | A6 §2.2–2.4 |
| Baum+2022 estende as séries de forma utilizável? | **Sim, numericamente.** 62 135 observações, 59 estrelas, 1966–2020, machine-readable e locais. **Mas a extensão é não-uniforme entre os grupos do P4** e a incerteza dos offsets não é publicada | A9 §1.1–1.3; A9-F5; D41, D44 |
| A média de atividade discrimina um grande mínimo? | **Não.** ⟨S_HK⟩ = 0.171 no grande mínimo vs 0.172 no mínimo de ciclo. O discriminante é a **variabilidade** | A10 §1.3, três checksums exatos |
| A lacuna observacional em HD 166620 foi fechada? | **Sim.** De 6.91 para 2.82 anos, com os dados de Oláh+2016 | A10 §1.2 |
| A aproximação à transição está amostrada? | **Sim — com 8 médias anuais e 12 estações fotométricas.** Suficiente para comparar estados, **insuficiente** para a maquinaria de janela deslizante do P4 | A10-F2; D46 |
| Existe precedente publicado para usar variabilidade como diagnóstico de estado magnético? | **Sim.** Luhn+2022 §3.1, com receita completa, reproduzida exatamente | A10 §1.4; D45 |
| Alguém já afirmou que grandes mínimos são estocásticos/imprevisíveis? | **Sim, em 2025.** CLS VI §3.3.1: "requires a stochastic process that is poorly understood"; transições "on order of years" | A11 §c.2; D50 |
| Qual a taxa-base publicada de estrelas em estado tipo mínimo de Maunder? | **0.1 %** antes do corte evolutivo, **0.015 %** depois — **mas por critério de nível instantâneo**, que Luhn+2022 declara inválido | A11a-F1/F2; D48 |
| HD 4915 é candidata a mínimo de Maunder? | **Não, segundo a fonte mais recente.** Isaacson+2024: dois ciclos, 4.9 yr e > 40 yr, com o longo subindo | A11b-F3; D47 |
| Qual a receita de conversão S → R′_HK e a sua faixa de validade? | **Estabelecida em grau A.** R_phot ajustada em 0.44 < B−V < 0.82; até 20 % de incerteza acima de B−V = 1.0 | A12 §2–3; D52, D53 |
| R′_HK é melhor que S como correlato de variabilidade? | **Não, segundo teste publicado em 710 estrelas.** S + massa estelar é a melhor métrica | CLS VI §5; A12-F1/F2; D54 |

**Registrado como problema conhecido, não como questão aberta:** o resultado de
`paper_state_v2` — φ₁(Variable) > φ₁(Maunder), p = 0.029 — comparou, após a auditoria, três
estrelas cíclicas contra duas estrelas cíclicas e uma `Long`. Não é evidência de CSD. Não deve
reaparecer em nenhuma versão do manuscrito.

---

## 9 · Log de entradas

| Data | Entrada | Decisões |
|---|---|---|
| 2026-07-28 | Abertura; A1 (Baliunas) fechada | D01–D05, D07–D11 |
| 2026-07-29 | A2 (Lockwood), A4 (Dakos), A3 (Egeland) fechadas | D12, D16–D24 |
| 2026-07-30 | A5 (Peng), A6 (Saar) fechadas em Cowork | D13–D15, D25–D30 |
| 2026-08-01 | Subsídios §6.1 levantados; caderno criado | D06 |
| 2026-08-01 | **Fecho da conversa de consolidação.** Descoberta das séries estendidas (Baum+2022, Luhn+2022, Isaacson+2024, CLS VI, A&A 2025); Q1 suspensa; quatro unidades novas; questão do índice unificado levantada | D31–D40 |
| 2026-08-01 | **Segunda rodada de auditoria: A9 (Baum+2022), A10 (Luhn+2022), A11 (Järvinen & Strassmeier 2025 + CLS V + CLS VI), A12 (Noyes+1984) fechadas em Cowork.** Q1 desbloqueada; Q9 reportada e devolvida; Q8 com balanço invertido; duas questões novas (Q10, Q11). Séries estendidas obtidas em forma numérica local. Cinco contradições registradas | D41–D54 |
| 2026-11-14 | **Inspeção completa, só de leitura** (`inspecao/`, 43 achados I-01 a I-43) e **resolução do que não depende de mérito**: PDFs lidos por inteiro e guardados em `bib/` (MANIFEST); A7, A8, A13 executadas; Tabela 4 de Egeland obtida; D41–D54 incorporadas (a proposta de `inspecao/NOTEBOOK_proposta_D41_D54.md`); errata em `audit/ERRATA_2026-11-14.md`; reparos do catálogo em arquivo lateral. Nenhuma Q# decidida | D55–D67 |
| 2026-11-14 | **Respostas do pesquisador ao memorando (bloco 1):** anual e bruta, ambas; S e R′_HK, ambos; subsídios para a receita de σ_S; incorporação aprovada. Q1–Q7, Q10, Q11 e os itens 2, 4, 5, 6, 8, 9, 10 do memorando seguem pendentes | D68–D71 |
| 2026-11-14 | **Respostas do pesquisador (bloco 2):** subsídios para junção e D46; D50 espera Held & Kleinen; piso de Q6 citado como 0.37–0.45 % | D72–D75 |
| 2026-11-14 | **Respostas do pesquisador (bloco 3):** papéis das séries e layout pedem subsídios; Korolik auditada (A14) para Q11; Q2–Q7 abertas; Q1 espera os papéis | D76–D79 |
| 2026-11-24 | **Três PDFs subidos (Held & Kleinen, Livina & Lenton, Peng+1993) validados e lidos; busca dos dados de HD 166620 no VizieR sem resultado.** A7b e A5b; item 6 do memorando de novo decidível | D81, D82 |

---

## 10 · Fatos com fonte e página (REG-03) — lidos em PDF validado, 2026-11-14

Página = página do arquivo PDF (1 = primeira). Id = checagem em `inspecao/checks.csv` e `inspecao/saidas/06_pdf_pages.txt`. Nada daqui foi tomado de memória.

| Fato | Fonte | Pág. | Id | Grau |
|---|---|---|---|---|
| 59 estrelas, 62 135 observações, HKP-1/2 e HIRES-1/2 | Baum+2022 AJ 163, 183 | 1, 3 | 3.11-08, 3.11-09 | A |
| Lacuna e HD 101501: período plano de ~10 anos e retorno | Baum+2022 §4.1 | 7 | 3.11-10 | A |
| σ_S da CLS V; B−V derivado de T_eff e [Fe/H] | Isaacson+2024 ApJS 274, 35 | 5, 14 | 3.11-13 a 3.11-15 | A |
| "256 stars" × 285 (Figura 10); "138/284" | Isaacson+2024 | 10, 14 | 3.11-16, 3.11-17 | A |
| 91 estrelas, faixas de massa, ciclos | Isaacson+2025 AJ 170, 181 (CLS VI) | 1, 4 | 3.11-19, 3.11-20 | A |
| Transições "on order of years" | CLS VI | 6, 7, 11 | 3.11-21 a 3.11-24 | A |
| Estrelas evoluídas e inclinação | Järvinen & Strassmeier 2025 (arXiv) | 1, 7 | 3.11-25, 3.11-26 | A |
| Escopo "mean level of activity"; Linsky 0.3 dex | Noyes+1984 | 2, 13, 14 | 3.11-27 a 3.11-30 | A |
| CSD: lentidão de recuperação, Hopf estável → oscilante, não-local sem trabalho explícito | Scheffer+2009 Nature 461, 53 | 3, 4 | 3.11-31 a 3.11-33 | A |
| Previsão de grandes mínimos, precursor, mínimo de 2008–2009 | Usoskin+2017 LRSP 14, 3 | 4, 23, 58 | 3.11-36 a 3.11-38 | A |
| ⟨S⟩ solar 0.1694 ± 0.0005; ΔS_cyc ± 0.0012 × 0.0014; Tabela 4 cobre ciclos 20–24 | Egeland+2017 ApJ 835, 25 | 1, 9, 11 | 3.11-39, 3.11-40, 3.12-07 | A |
| Janela 25–75 %, 1 000 surrogates ARMA | Dakos+2012 PLoS ONE 7, e41010 | 17 | 3.11-41 | A |
| 119 observações digitalizadas da Figura 2 de Oláh+2016; versão publicada 158 | Luhn+2022 (arXiv 2207.00612; ApJL 936, L23) | 2, 3, 5 | 3.11-42 a 3.11-47 | A |
| Dados de Baum no arXiv × publicada: sem divergência numérica | Baum+2022 (arXiv 2203.13376) | 1, 8 | 3.11-48, 3.11-49 | A |
| Períodos de Oláh (Tabela 1) × B95, Baum, Saar | Oláh+2016 (arXiv) | Tabela 1 | 3.10-01 a 3.10-08 | A |
| Calibração DFA → c; ordem de mil pontos para o DFA; viés de comprimento finito cai com √N; ausência de modos oscilatórios em Held & Kleinen | Livina & Lenton 2007 GRL 34, L03712; Peng+1993 PRE 47, 3730; Held & Kleinen 2004 GRL 31, L23207 | 3, 3, 2 | 3.11-50 a 3.11-62 | A |

---

## 11 · Uso de IA no processo (REG-IA)

Em 2026-11-14 a inspeção, a leitura dos PDFs, os scripts de verificação (`inspecao/scripts/`, Python, `python -I`), as auditorias A7/A8/A13, a errata, o rascunho de reparos do catálogo e as entradas D55–D67 foram produzidos por **Claude (Anthropic), em sessão de Claude Code, sob direção do pesquisador**. Limitações declaradas: o OCR dos oito valores de B95 foi feito com RapidOCR e leitura visual (sem Tesseract), logo grau B; A7 sem Held & Kleinen; A8 sem §3 e §5 de Usoskin; o relatório afirma só o que cada checagem mostra. Toda decisão de mérito (Q#) permanece do pesquisador; cada resposta dele é registrada como D## nova com autor "pesquisador".
