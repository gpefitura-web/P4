# P4 — Caderno de Notas de Pesquisa

**Paper:** Critical Slowing Down Near Stellar Activity Minima
**Aberto em:** 2026-07-28 (início da fase de auditoria) · **Última entrada:** 2026-08-01 (fecho da conversa de consolidação)

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

## 5 · Questões abertas — exigem decisão humana

Numeradas `Q#`. Cada uma tem subsídios já levantados; nenhuma tem resposta óbvia.

| # | Questão | Subsídios | Status |
|---|---|---|---|
| **Q1** | **Composição da amostra — SUSPENSA até A9** (D32). Os dois grupos que sustentam a hipótese desapareceram: o grupo do meio era 0/3 (todas cíclicas) e o pós-transição 0/4. | `P4_DECISION_SUPPORT_6.1.md` §8 — cinco opções com poder, confundimento e objeção teórica quantificados | **aberta** |
| **Q2** | **O que conta como "flat".** ρ CrB: Tabela 2 = `Long`; Tabela 1 σ_S/S = 1.0% (dentro da definição `Flat`); Saar lista como flat/Maunder. As três afirmações são grau A. | A6 §6.2; A1 §1.3 | **aberta** |
| **Q3** | **Largura de banda gaussiana.** σ = 1 yr é ~1.8% do registro; o padrão de Dakos é 10%. Mas σ = 1 yr remove um **ciclo determinístico de 11 anos**, que não é o detrending monótono para o qual o passo de Dakos foi desenhado; 5.5 yr deixaria a maior parte do ciclo nos resíduos. Tensão genuína, não erro. | A4-F2 | **aberta** |
| **Q4** | **A componente de 44 anos** pode ser tratada num registro de 55 anos? | D30; A6-F12 | **aberta** |
| **Q5** | **Binárias.** HD 81809 (registro composto; a atividade pode vir da componente de menor massa) e HD 219834A/B (par resolvido; Saar rejeita o ciclo de A, mantém o de B). | A1-F7, A1 §2.5, A6 §2.3 | **aberta** |
| **Q6** | **O grupo `Flat` tem um problema de medida.** O limiar (<1–1.5%) está dentro da precisão de longo prazo declarada por Baliunas (1.4%, ou 1.2% excluindo quatro padrões variáveis), e acima do piso instrumental de 0.8% (A2-F6). Nenhuma estrela `Flat` tem segunda medida na literatura auditada. | A6-F6/F7/F13; A2-F6 | **aberta — decidir apresentação** |
| **Q7** | **Subgigantes no grupo `Flat`.** Três das cinco elegíveis são IV/Vp. Baixa atividade pode ser evolutiva, não Maunder. | `P4_DECISION_SUPPORT_6.1.md` §2 | **aberta** |
| **Q8** | **Migrar a análise para log R′_HK?** O índice S é instrumental e sensível à temperatura fotosférica; os grupos diferem sistematicamente em B−V (0,49 a 0,88 nas medianas), o que confunde a comparação. R′_HK normaliza e torna Sol e estrelas comparáveis; Egeland+2017 Tabela 3 já dá o lado solar. Custo: C_cf(B−V) tem faixa de validade limitada. | `paper_state_v5.md` §4; D40 | **nova — depende de A12** |
| **Q9** | **DFA volta a ser admissível para o subconjunto Baum?** D24 fechou a questão com N ≈ 26 contra piso de >100 pontos. Baum+2022 é fonte nova com cinco décadas de cadência. | A9 | **nova — reaberta legitimamente** |

---

## 6 · Itens de ação — bloqueados no sandbox

| Item | Necessário para | Domínio bloqueado |
|---|---|---|
| **Tabela 4 de Egeland+2017** — série S solar calibrada, ciclos 15–24, machine-readable | D18; substitui a calibração K→S própria e estende a série solar muito além de 1966–2021 | IOP |
| Depósito Harvard Dataverse (Pevtsov 2016, doi:10.7910/DVN/VF5BMO) — índice Ca II K composto subjacente | contexto para D18 | Dataverse |
| Série S solar NSO | trilha solar, caso Egeland T4 não seja obtida | NOAA |

Domínios permitidos: `github.com`, `raw.githubusercontent.com`, `api.github.com`, PyPI, npm.

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
