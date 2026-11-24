# Subsídios para decidir Q1 (composição da amostra) e validação de D92

**Pedido do pesquisador (2026-11-24):** "Subsídios para decidir Q1. Mas valide o pedido anterior também." Este arquivo **não escolhe** e não recomenda. A recomendação já registrada (v6 §3.4, DECISOES §E item 2) é só repetida na §3. Fatos com id de `inspecao/checks.csv` ou decisão; os números dos grupos vêm de `inspecao/saidas/13_*.txt`.

---

## Parte 1 — Validação do pedido anterior ("A e C", D92)

| Conferência | Resultado |
|---|---|
| **A e C são compatíveis?** | **Sim, com uma diferença só.** A e C concordam em tudo (anual para o CSD temporal; bruta para σ por estado e períodos) exceto no DFA: A o deixa fora (D24), C o admite pela série bruta com Q9 à parte. D92 reúne os dois mantendo o DFA fora até Q9 ser decidida a favor |
| Números de D91 que sustentam D92 | **Reproduzem** (`3.16-01` a `3.16-04`): 22 de 59 estrelas com ≥ 1 000 observações brutas; 0 de 59 com ≥ 100 estações anuais; 4 de 5 `Flat` e 6 de 13 controles presentes |
| Conflito com decisões ativas | **Nenhum.** D24 (DFA fora) mantida; D20–D23 valem para a série anual; D08 (média anual) coerente; D12 (N uniforme) é do catálogo Baliunas (v6 §3.1), não do subconjunto de Baum |
| **Achado novo: a série anual não é uma sequência contínua de anos** | Em 2 das 10 estrelas dos grupos do P4 a **maior sequência de anos consecutivos é menor que a metade das estações** (`3.16-05`): HD 182572 (38 estações, sequência máxima 14, janela de 50 % = 19) e HD 190360 (47 estações, sequência 19, janela 23). Para as outras, a sequência máxima é 29 a 47. Lacunas de anos em HD 166620: 1, 6, 2 e 1 (sequência 30); HD 101501: 13 anos de lacuna (sequência 28) |
| **Consequência para D92** | O CSD temporal em janelas sobre a série anual **precisa de uma regra para anos faltantes** (interpolar, ou não permitir janelas que atravessem lacuna). A4 (Dakos, Tabela 3, nota 1) diz que os métodos servem a séries irregulares e que a interpolação é necessária "only when there are too many missing values". Essa regra **não está decidida** |
| **Ambiguidade a confirmar em D92** | "Períodos" (bruta) pode significar (a) **periodogramas próprios** sobre as observações brutas, ou (b) **os períodos publicados** (Baliunas, Saar, Baum, Oláh), que D15 e D42 mandam registrar ao lado e não fundir. A tabela de subsídios falava de periodogramas, mas D15 e D42 tratam de valores publicados. D92 usa a palavra "períodos" sem resolver isso |

Resultado da validação: **D92 é consistente com as decisões e com os dados**, com duas lacunas que não alteram a escolha (regra para anos faltantes; períodos próprios ou publicados). Estão registradas em D93 para você confirmar ou corrigir.

---

## Parte 2 — Q1: o que a decisão tem de escolher

### 2.1 As opções (v6 §3.4, atualizadas com D55–D92)
| Opção | Conteúdo | Ganho | Custo |
|---|---|---|---|
| **(i)** Catálogo Baliunas congelado | 112 estrelas; séries anuais N ≈ 26 (D08, D12); sem séries estendidas | D12 intacta; N uniforme por construção | sem transição amostrada; janela de 50 % de 26 pontos = 13; DFA fora |
| **(ii)** Subconjunto Baum (59 estrelas) | séries até 2020, HKP-1/2 e HIRES-1/2 | cinco décadas (24–54 anos); HD 166620 e HD 101501 | A9-F5 (presença 4/5 contra 6/13); degrau instrumental (D44, D72); 99.73 % de HD 101501 é de Mount Wilson, com lacuna de 13.82 anos (D59) |
| **(iii)** CLS V (285 estrelas, ≥ 45 obs) | um só detector, cerca de 19 anos (2005–2023; v6 §3.4) | homogeneidade instrumental; dispersão publicada | só 19 anos: janela de 50 % de cerca de 9 pontos anuais; exclui o HIRES anterior a 2005; sem transição |
| **(iv)** Estudo de caso HD 166620 + HD 101501 | n = 2 | os dois casos de transição documentados | n = 2; D46; D58/D86 (119 linhas grau C); HD 101501 com lacuna de 13.8 anos |
| **(v) nova** (D85) | (ii) mais o `HK_Project_v2001_NSO` como camada ao lado, para as estrelas que Baum não tem | 4 dos 6 controles ausentes de Baum (HD 160346, 201091, 81809, 103095) com 34–36 anos de Mount Wilson até 2001 e **séries anuais sem lacuna** (sequências de 36, 35, 23 e 34 anos; `11_dataverse_v2001_runs.txt`); presença de controles 6/13 → 10/13 | só até 2001, um instrumento, sem HIRES; não estende HD 166620 nem HD 101501; as `Flat` limpas não ganham nada (só HD 182572, que Baum já tem) |

### 2.2 O que os dados dizem por grupo (subconjunto de Baum; `13_series_roles.txt`, `13_annual_runs.txt`)
| Grupo | Estrelas em Baum | Estações anuais (mediana) | Sequência máxima de anos consecutivos |
|---|---|---|---|
| `Flat` limpas | 4 de 5 (HD 10700, 23249, 182572, 190360) | 48 | 29, 29, 14, 19 |
| `CYCLE` + Excellent | 6 de 13 (inclui HD 166620 e 219834B) | 46 | 47, 36, 30, 29, 30 (HD 219834B sem linhas sob esse id na Tabela 1) |
| HD 166620 | 1 | 45 | 30 |
| HD 101501 | 1 | 32 | 28 |

Fatos: o grupo `CYCLE`+Excellent que a Baum cobre **inclui o próprio HD 166620**, o caso de transição; as `Flat` de Baum são `flat` por B95 e por Baum, de modo que nenhuma delas tem **transição observada**; a presença das `Flat` em Baum é maior (4/5) que a dos controles (6/13) (A9-F5).

### 2.3 Perguntas que Q1 carrega
1. **Regra de exclusão por binaridade (I-06):** as "cinco `Flat` limpas" não saem de D13 sozinha, que dá sete (`3.9-01`); a regra que tira HD 158614 e HD 178428 estava num arquivo ausente. Que regra entra: a que dá cinco, ou outra?
2. **D04 e D11 contra subsídios já calculados nas candidatas (I-13):** D04 manda selecionar "antes de qualquer dado real" e D11 diz que nenhum σ_S/S por estrela é usado para a amostra, mas σ_S/S das quatro `Flat` (CLS V) e o degrau de cada estrela já foram medidos. Opções registráveis: manter D04/D11 como estão e declarar que a seleção foi informada; ou registrar a exceção.
3. **O que a amostra tem de entregar à hipótese de D90.** D90 trata a biestabilidade como hipótese testável de CSD na perda de um ciclo limite. Fatos: só HD 166620 e HD 101501 têm transição ciclo → plano documentada (D49, D50, A10); HD 4915 é contestada (A11b-F3, D47). As `Flat` limpas e os controles dão comparação de nível de variabilidade, não de transição. Qual pergunta a amostra responde (comparar estados entre estrelas, ou acompanhar a transição em poucas) é do pesquisador.
4. **Regra para anos faltantes (Parte 1).** Afeta quais estrelas têm janelas anuais utilizáveis: HD 182572 e HD 190360 as têm curtas.
5. **Heterogeneidade instrumental e de calibração:** o v2001 e o HKP de Baum coincidem em 14 233 de 14 295 linhas; diferenças de calibração entre compilações são de 1 a 2 % pelo README (D85).

### 2.4 Pontos que valem para qualquer opção
- O catálogo `baliunas_table2_full.csv` fica congelado; qualquer extensão fica ao lado (D36).
- As 119 linhas `new_MW` não entram como valor (D58, D86).
- O B−V que rege a faixa de Noyes tem de ser declarado (D62); a análise em R′_HK vale na faixa 0.44 < B−V < 0.82 (D53, D69); HD 160346 (B−V 0.96), 201091 (1.18) e 103095 (0.75) estão fora ou perto do limite para R′_HK.
- A recomendação já registrada (v6 §3.4): (ii) e (iv) não são exclusivas; HD 101501 é o objeto que melhor sobrevive às objeções publicadas. **Nova cautela de fato (D59):** a série de HD 101501 tem lacuna de 13.82 anos antes do retorno e só 6 pontos do HIRES; a janela densa pós-retorno tem cerca de 5.5 anos.

Estado: **subsídios entregues; Q1 aberta (D94).**

---

## Adendo de 2026-11-24: interpolar anos faltantes? (como e para quê)
**Pergunta do pesquisador:** "interpolar anos faltantes? (como e para quê?)". Explicação e subsídios, sem decidir. O que vem de fonte está marcado; o que é raciocínio meu está marcado como tal (grau C).

**Para quê.** O CSD em janela mede o AR(1) (correlação entre pontos vizinhos), a variância e o τ de Kendall ao longo de janelas deslizantes (D20–D23). *Raciocínio (C):* com uma média por ano, "vizinho" significa "ano seguinte". Onde falta um ano, o par que cruza a lacuna liga anos separados por 2 ou mais, o que mistura escalas de tempo no AR(1) e faz o tamanho da janela, em pontos, deixar de ser o tamanho em anos. Fonte: Dakos et al. dizem que os métodos servem a séries irregulares e que a interpolação é necessária "only when there are too many missing values" (A4, Tabela 3, nota 1). Held & Kleinen e Livina & Lenton aplicam o AR(1) a séries Δt-agregadas, regulares (A7b item 3; `3.11-55`).

**Quantas lacunas.** Nas 10 estrelas dos grupos do P4 há 39 lacunas de anos (`3.16-06`): **32 de 1 a 2 anos** e **7 de 3 a 13 anos** (HD 10700: 4; HD 182572: 3; HD 152391: 8; HD 166620: 6; HD 26965: 5; HD 4628: 10; HD 101501: 13). As 32 curtas se concentram em HD 182572 (9), HD 23249 (6) e HD 190360 (5). A tabela por estrela está em `inspecao/saidas/13_annual_runs.txt`.

**Como, nas alternativas existentes** (nenhuma recomendada):
| Alternativa | O que faz | Custo |
|---|---|---|
| **1. Não interpolar; janelas só dentro de sequências contínuas de anos** | cada janela cabe numa sequência de anos consecutivos | a maior sequência é 14 em HD 182572 e 19 em HD 190360, menor que a janela de 50 % (19 e 23): essas duas não têm janela de 50 % sem lacuna (`3.16-05`); com 25–75 % (D20) parte delas cabe |
| **2. Interpolar só as lacunas curtas (1–2 anos) e marcar os pontos interpolados; não atravessar as longas (≥ 3 anos)** | recupera as 32 lacunas curtas; as 7 longas dividem a série | *Raciocínio (C):* o valor interpolado entre dois vizinhos é mais parecido com eles que um ano observado, o que tende a **aumentar** a autocorrelação: o artefato vai na mesma direção do sinal de CSD, e o teste de significância (D22, surrogates) deveria passar pela mesma interpolação para ser justo |
| **3. Calcular o AR(1) só com pares de anos consecutivos, sem criar valores** | nenhuma interpolação; as janelas contêm lacunas, e os pares que as cruzam são descartados | menos pares por janela; a variância usa todos os pontos |
| **4. Evitar o problema usando a série bruta em janelas de tempo** (papel de D92 só para σ e períodos; não é o decidido) | sem anos faltantes | tripletos noturnos e lacunas (D91); fora de D92 |

**O que independe da escolha:** HD 166620 e HD 101501 têm lacunas longas (6 e 13 anos) que nenhuma das alternativas fecha; para essas, D46 já limita o teste temporal. A regra deve ser fixada **antes** de olhar o resultado do indicador em qualquer estrela (D04), e a mesma regra vale para os surrogates (D22).

Estado: **explicação entregue; regra para anos faltantes pendente (D95).**
