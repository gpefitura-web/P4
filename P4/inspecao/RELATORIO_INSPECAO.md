# RELATÓRIO DE INSPEÇÃO — Paper P4

Data: 2026-11-14 · Pacote inspecionado: `P4/` (subpasta do repositório `gpefitura-web/p4`) · Todos os números abaixo remetem a `inspecao/checks.csv` (coluna `id`) ou a arquivo e seção do pacote. Adendo com a verificação contra os PDFs de Baum, Luhn e CLS V na seção 6.

## Resumo

**Checagens** (`checks.csv`, 394 linhas): **256 passam, 27 falham, 111 são informativas** (valor registrado sem esperado nos documentos). As 27 falhas se distribuem assim: 21 estão no **texto** de auditorias ou documentos de estado, 2 em **arquivos de dados derivados**, 2 no **pipeline**, 1 é a contradição já conhecida A10-F1 e 1 é diferença de **critério da minha reprodução** (tabela na seção 3). Nenhuma falha está nos TSVs do VizieR.

**O que reproduz exatamente:** as 112 linhas e 52/31/29 do catálogo; 62 135 observações, 59 estrelas, contagens por instrumento e por flag de Baum; Nobs da Tabela 2 = Tabela 1 em 59/59; medianas 698 e 27, 56/59, 0/59, lacuna 7.17 anos, 42/59; `baum2022_59stars.csv` célula a célula; o degrau instrumental (51 estrelas, 4.47 %, 25/51, 10/51, −8.78 %, −16.3 %); 1 885 linhas de Luhn, ⟨S_HK⟩ 0.1810/0.1724/0.1705 e σ_S 0.0027/0.0054/0.0019; 710 estrelas, 138 ciclos e as 48 do filtro de Isaacson; 82/17/6/2/5 de Noyes; 27 contra 26 com HD 185144; os 14 períodos e os Δ/σ de A9-F3; 4/5 e 6/13.

**BLOQUEANTE (1)**

- **I-01 — D45 descreve uma receita e reproduz outra, e o F-test de 8.78 × 10⁻⁶ não sai dos σ_S corrigidos.** Os três σ_S publicados só se reproduzem com o desvio-padrão do intervalo inteiro, não "dentro de cada estação" como diz o passo 1 de D45. O p de 8.78 × 10⁻⁶ sai das variâncias brutas (8.80 × 10⁻⁶, bilateral); com os σ_S corrigidos dá 8.7 × 10⁻³. `paper_state_v6.md` §2 associa esse p aos σ_S corrigidos.

**IMPORTANTES que mexem em subsídios de decisão**

- **I-02** — A11 §b.3 diz que HD 3651 não tem ciclo na CLS V; a Tabela 4 dá 10.01 anos. HD 32147 aparece com traço e tem 9.53 anos.
- **I-03** — o "piso instrumental de 0.45 %" (HD 55575) não é o mínimo da tabela: HD 187923 tem 0.372 % e HD 144579 tem 0.397 %, ambas com mais de 45 observações.
- **I-04** — as "14 reclassificadas" de D43 não fecham por regra única: a lista de A9 §2 tem 15 nomes; regras consistentes dão 13 ou 15.
- **I-05** — medianas de B−V: 0.49 (`Long`) não se reproduz (0.525); 0.73 é das cinco `Flat` limpas e não de `Flat`+`Flat?` (0.56); 0.88 exige excluir o Sol.
- **I-06** — as "cinco `Flat` limpas" não saem de D13 sozinha (dá sete); a regra que tira HD 158614 e HD 178428 está num arquivo ausente.
- **I-07** — o B−V do catálogo A1 é sistematicamente mais vermelho que o da CLS V (mediana +0.03, até +0.085); duas estrelas mudam de faixa de Noyes. **O balanço de D54 (não migrar) não se inverte**, mas as contagens "8 de 13 fora" e "duas acima de 1.0" dependem da fonte de B−V.
- **I-08** — HD 101501: os números de D49 estão certos (2 239 observações, 49 anos), mas 99.7 % das observações são de Mount Wilson e terminam em 1995.45; depois há uma lacuna de 13.8 anos e seis pontos do Keck. **Qualifica a recomendação registrada, não a inverte.**
- **I-09** — no degrau instrumental, 17 das 51 estrelas têm medianas coincidentes a menos de 0.2 % (cinco exatamente iguais), padrão compatível com o alinhamento de medianas que Baum declara para 14 estrelas não nomeadas.

**Bloqueios de verificação:** os PDFs de toda a segunda rodada (Baum, Luhn, Järvinen & Strassmeier, CLS V, CLS VI, Noyes, Oláh) não estão no clone; nenhuma citação literal de D47–D51 e D54 pôde ser conferida (I-25). `P4_DECISION_SUPPORT_6.1.md` falta e é a única definição dos grupos (I-06).

**Documentação:** o caderno ainda não tem D41–D54, Q10, Q11, dez linhas da §8 e a linha do log; a proposta está em `NOTEBOOK_proposta_D41_D54.md` e o que a instrução de incorporação não cobre está em I-18. O pipeline contradiz decisões ativas em 30 pontos (`MAPA_PIPELINE.md`).

---

## 1. Achados

Grau: A, B, C, X como no protocolo §4, aplicado à evidência do achado. "Quem": P = pesquisador (decisão humana); C = consolidação (correção documental, sem decisão de mérito).

### 1.1 Reprodução numérica

**I-01 · BLOQUEANTE · grau A · D45 e o F-test**
- D45, passo 1: "σ_S calculado **dentro de cada estação**". A10 §1.4, tabela de reprodução: "desvio-padrão bruto **do intervalo**".
- Intervalo inteiro, ruído de 1.2 % (MW) ou 0.3 % (Keck) de ⟨S_HK⟩ em quadratura: 0.00269 / 0.00542 / 0.00195, isto é, os três valores publicados (`3.4-25`, `3.4-32`, `3.4-39`; cinco casas em `3.4-26`, `3.4-33`, `3.4-40`).
- Leitura literal do passo 1 (σ por estação de ano civil, quadratura por estação, média | mediana): 0.0028 | 0.0025, 0.0048 | 0.0049, 0.0015 | 0.0014 (`3.4-27`, `3.4-34`, `3.4-41`).
- F-test, mínimo 1 contra grande mínimo: variâncias brutas, bilateral, p = 8.80 × 10⁻⁶ (`3.4-50`, passa contra 8.78 × 10⁻⁶); σ_S corrigidos, p = 8.68 × 10⁻³ bilateral e 4.34 × 10⁻³ unilateral (`3.4-52`, `3.4-53`); valores arredondados publicados, p = 4.1 × 10⁻³ (`3.4-54`).
- `paper_state_v6.md` §2: "σ_S corrigido cai de 0.0027 / 0.0054 para 0.0019, com F-test de 8.78 × 10⁻⁶".
- A reprodução não foi ajustada. A divergência está no texto de D45 e do v6, não nos dados.
- **A decidir (P):** qual das duas contas é "a receita" que D45 adota, e a que grandezas o p publicado se refere. Sem o PDF de Luhn+2022 (ausente, I-25) não é possível dizer qual delas o artigo descreve.

**I-02 · IMPORTANTE · grau A · A11 §b.3, coluna "Ciclo detectado"**
- A11 §b.3: HD 3651 "não"; HD 32147 "—".
- `data/J_ApJS_274_35_table4.tsv`: HD 3651 Per = 10.01; HD 32147 Per = 9.53 (`3.6-27`, `3.6-29`). As outras oito linhas da tabela reproduzem.
- HD 3651 é a candidata a transição de A1-F5 e de D15. **A corrigir (C):** tabela de A11; conferir se algum subsídio de Q1/Q2 usou "sem ciclo" para HD 3651.

**I-03 · IMPORTANTE · grau A · "piso instrumental moderno = 0.45 %"**
- A11 §b.2, `paper_state_v6.md` §3.3, DECISOES §C (Q6): HD 55575 é "a menos ativa com ≥ 45 obs", 0.45 %.
- Tabela 2 da CLS V, Nobs ≥ 45: HD 187923, SSD/Smed = 0.372 % (106 obs); HD 144579, 0.397 % (122 obs); HD 55575, 0.448 % (135 obs) (`3.6-24` a `3.6-26`; as três são as primeiras linhas de `isaacson2024_least_active_50.csv`).
- A frase de A11 é citação do texto do artigo; a tabela do mesmo artigo discorda. Pelo protocolo §4 isso é grau X até resolver. **A decidir (P):** que número citar como piso em Q6; "três vezes abaixo do limiar `Flat`" muda com o valor.

**I-04 · IMPORTANTE · grau A · as 14 reclassificações (D43, A9 §2, checksum 6)**
- A9 §2 lista sob o rótulo "treze": 100180, 101501, 10780, 115617, 126053, 143761, 182572, 188512, 190406, 217014, 22072, 37394, 3795, 9562. São 14 nomes (`3.8-09`). Com HD 10700 somam 15, e o texto fecha "Total 14".
- Tabela 2 de Baum, 26 estrelas com `ClassB95`: mudança de tipo de classe em 13 (`3.8-08`); HD 190406 não muda de tipo, é `fair-2.6+good-16.9` → `17.2?` (`3.8-10`, `3.8-11c`).
- Contando também `flat?` → `flat`, a regra que A9 aplica a HD 10700, entram HD 10700 e HD 23249: total 15 (`3.8-11`, `3.8-11b`).
- O número 14 é de Baum §4.2; quais 14 não é determinável com a tabela. O "checksum reproduzido" de D43 não sustenta grau A. **A corrigir (C):** rebaixar o grau desse checksum e registrar as três leituras.

**I-05 · IMPORTANTE · grau A · medianas de B−V por grupo**

| Grupo | `paper_state_v5.md` §4 | A12 §3.1 | Recalculado do catálogo | Checagem |
|---|---|---|---|---|
| `CYCLE` + FAP Excellent | 0,88 | 0.88 | 0.87 com o Sol (13); 0.875 sem o Sol (12) | `3.9-30`, `3.9-31` |
| `Flat`+`Flat?` | 0,73 | — | 0.56 (15 estrelas) | `3.9-32` |
| `Flat` limpo (5) | — | 0.73 | 0.73 | `3.9-33` |
| sete `Flat`/`Flat?` não-padrão (D13 só) | — | — | 0.72 | `3.9-40` |
| `Var` | 0,61 | 0.610 | 0.61 | `3.9-34` |
| `Long` | 0,49 | 0.525 | 0.525 (16); 0.52 sem padrões (9) | `3.9-35`, `3.9-36`, `3.9-41` |

- A12 §3.1 afirma que "Long 0.49 · Flat 0.73 · CYCLE Excellent 0.88 são reproduzidas para os subconjuntos relevantes"; nenhum subconjunto testado dá 0.49.
- O caderno, Q8, repete "0,49 a 0,88 nas medianas". **A corrigir (C):** rótulos e o valor de `Long`. Sim, as medianas dependem da definição do grupo: o 0.73 só vale para as cinco limpas.

**I-06 · IMPORTANTE · grau X · definição das "cinco `Flat` limpas"**
- A9 §2.1: "Grupo `Flat` limpo (5 estrelas, pós-D13)". D13 exclui estrelas-padrão.
- `Flat` + `Flat?` menos as padrões de A6 §3: sete estrelas, 10700, 23249, 43587, 158614, 178428, 182572, 190360 (`3.9-01`).
- As cinco saem se também se excluem HD 158614 e HD 178428, ambas na lista de binárias do Apêndice B (A1 §2.5) (`3.9-02`, `3.9-03`). Essa regra não está escrita em nenhum arquivo do pacote; o caderno remete a `P4_DECISION_SUPPORT_6.1.md` §2 e §8, ausente.
- Caderno Q7: "Três das cinco elegíveis são IV/Vp". No catálogo: três IV (23249, 182572, 190360) e uma Vp (10700), quatro ao todo (`3.9-06`).
- **A decidir (P):** registrar a regra de exclusão por binaridade como decisão, ou recuperar o arquivo.

**I-07 · IMPORTANTE · grau A · B−V do catálogo contra B−V da CLS V; fronteiras das faixas de Noyes**
- 38 estrelas do catálogo A1 estão na Tabela 2 da CLS V. Diferença A1 − CLS V: mediana +0.030; 19 com |diferença| > 0.03 (`3.9-24`). Nas 14 candidatas do P4 presentes: mínimo +0.005, mediana +0.0405, máximo +0.085 (`3.9-21`).
- Mudam de faixa com o B−V da CLS V: HD 10476, 0.84 → 0.801 (entra em 0.44–0.82); HD 32147, 1.06 → 0.993 (sai da região "> 1.0") (`3.9-22`).
- D53 imprime a faixa como aberta, 0.44 < B−V < 0.82. `noyes1984_validade_cor.csv` trata como fechada: quatro estrelas estão exatamente em 0.44 ou 0.82 (HD 3229, 182101, 26965, 149661) e contam como "DENTRO"; pela leitura aberta são 78 dentro, não 82 (`3.7-09`, `3.7-10`). HD 26965 é uma das "cinco dentro" de A12-F1; pela leitura aberta são quatro (`3.9-16`).
- A12-F1 conta o Sol entre as treze. Sem o Sol: 4 dentro, 8 fora, de 12 (`3.9-18`). Só no subconjunto de Baum: `Flat` 3/4 dentro, controles 2/6 dentro (`3.9-19`).
- **Efeito sobre D54:** a assimetria entre os braços permanece em todas as leituras. O que muda é "duas na região de até 20 %", que vira uma (HD 201091) com o B−V da CLS V. As duas fontes de B−V são grau A na origem; a contradição fica registrada. **A decidir (P):** que B−V rege a faixa de validade, se Q8 for reaberta.

**I-08 · IMPORTANTE · grau A · cobertura de HD 101501 (D49; v6 §3.4)**
- D49: "2 239 observações, baseline de 49 anos". Confere (`3.3-40`).
- Por instrumento: HKP-1 193, HKP-2 2 040, HIRES-1 0, HIRES-2 6. Última época de Mount Wilson 1995.45; Keck de 2009.27 a 2017.14; maior lacuna 13.82 anos, de 1995.45 a 2009.27 (`3.3-50`). 99.73 % das observações são de Mount Wilson (`3.3-52`).
- 1980–1990: 11 anos com dados, 1 455 observações (`3.3-53`). Depois de 1990 a série densa cobre até 1995.45.
- Fora do arquivo de degrau instrumental por ter menos de dez pontos HIRES-2 (`3.3-54`). Na CLS V tem 15 observações (abaixo do corte de 45).
- Consequência factual: o estado plano e o retorno estão dentro de um só instrumento (a junção de D44 não os atravessa), e o trecho pós-retorno com cadência densa tem cerca de 5.5 anos. Nenhuma estatística de variabilidade foi calculada aqui (D04). **A considerar (P)** ao decidir Q1, opção (iv).

**I-09 · IMPORTANTE · grau C · composição da estatística do degrau (D44, A9 §1.7)**
- Os números de D44 reproduzem a partir da Tabela 1 com os pontos `sigma` removidos; essa regra de filtragem não está escrita em A9 (`3.5-11` a `3.5-18`).
- Cinco estrelas têm degrau exatamente zero (10697, 132142, 179957, 217014, 22072) e 17 têm |degrau| < 0.2 % (`3.5-19`, `3.5-19b`). Baum §2.1.3, citado em A9 §1.5, diz que catorze estrelas não nomeadas foram deslocadas para alinhar medianas.
- Sem essas 17, o desvio-padrão das 34 restantes é 5.48 % (`3.5-19c`). A dispersão robusta das 51 (1.4826 × MAD) é 1.23 % (`3.5-22`).
- É inferência (grau C): coincidência de medianas não prova alinhamento. Indica que "mediana 0.00 %" e "σ = 4.47 %" misturam estrelas alinhadas por construção com estrelas não alinhadas. **A considerar (P)** no item 4 da §E.

**I-10 · IMPORTANTE · grau A · contagem de linhas da Tabela 3 da CLS V (D41)**
- D41, A9 §0, A11 verificação 3 e v6 §10: 52 380 linhas, com "Δ = 8" em relação às 52 372 do texto do artigo.
- O arquivo tem 52 413 linhas, das quais 36 de comentário, 2 em branco e 3 de cabeçalho: **52 372 linhas de dados** (`3.6-05`, `3.6-06`). Nobs da Tabela 2 coincide com a contagem da Tabela 3 nas 710 estrelas (`3.6-08`).
- A discrepância de 8 não existe. D41 é imutável (regra 4 do CLAUDE.md). **A decidir (P):** como registrar errata numa decisão imutável.

**I-11 · IMPORTANTE · grau B · catálogo congelado: células que Baum transcreve e A1 deixou em branco**
- Baum, `ClassB95`: HD 10780 = `<7`; HD 126053 = `22?`. Catálogo A1: `P_cyc` e `FAP` vazios nas duas (`3.8-12b`). São duas das seis `CYCLE` sem período de v4 §2.
- A9-F2 explica o branco de Baum para HD 185144 por ela ser "`CYCLE` sem período nem FAP publicados em B95". HD 10780 e HD 126053 estão na mesma situação no catálogo e Baum preencheu as duas.
- Outros resíduos no catálogo, fora da lista de v4 §2: 27 linhas com resíduo de OCR em `sptype` (`3.1-17`; há mais, por exemplo `KS V` em HD 32147); duas em `star` (`3.1-18`); 15 linhas com `disagree = P_cyc`, todas grau A (`3.1-19`, `3.1-20`), contra "20 values" em A1 §2.2.
- Coluna `secondary`: 33 linhas com resíduo pelo critério "não vazio, não `Long`, não período secundário" (`3.1-15`); v4 e A6-F14 dizem 32. A diferença é `. Long` (HD 224930), que conto como resíduo e A6-F14 não lista. Diferença de critério da reprodução.
- **A corrigir (C)** ao gerar `p4_star_catalog.csv`; a linha de B95 para 10780, 126053 e 185144 pode ser relida no PDF de Baliunas, que está na raiz do repositório.

**I-12 · IMPORTANTE · grau A · o que é não-uniforme no subconjunto de Baum (A9-F5; v6 §3.1)**
- Entre as presentes, as medianas dos dois grupos são próximas: quatro `Flat`, 1 910 observações, 47.5 estações, 115 pontos HIRES-2; seis controles, 1 824 observações, 45.5 estações, 105.5 pontos HIRES-2. A maior lacuna difere: 3.68 contra 6.83 anos (`3.3-55`, `3.3-56`).
- A não-uniformidade está na presença (4/5 contra 6/13), não no N das presentes.
- v6 §3.1: "os sete controles ausentes são sistematicamente os mais vermelhos (B−V 0.96–1.18) ou binários". Ausentes: 16160 (0.98), 32147 (1.06), 160346 (0.96), 201091 (1.18), 81809 (0.64, binária), 103095 (0.75, fora da lista do Apêndice B) e a linha do Sol (`3.9-10`, `3.9-11`). A9-F5 nomeia cinco.
- **A corrigir (C):** redação do v6; **a considerar (P)** em Q1.

**I-13 · IMPORTANTE · grau A · D04 e D11 contra subsídios que já usam dados das candidatas**
- D04: "A amostra é selecionada do catálogo congelado, antes de qualquer dado real". Protocolo §1: escolhas fixadas antes de examinar os dados.
- DECISOES §C, Q2: σ_S/S medido na CLS V para quatro `Flat` (0.72 / 0.86 / 0.95 / 1.49 %), "HD 182572 falha"; v6 §3.3: "Três sobrevivem". A9 §1.7 mede o degrau por estrela. A10 recalcula variabilidade por estado em HD 166620.
- D11 (ativa): "Nenhum σ_S/S por estrela é usado para a amostra P4".
- As duas coisas estão registradas e nenhuma decisão as reconcilia. **A decidir (P):** se D04 e D11 continuam como estão, com a seleção já informada por medidas das candidatas.

**I-14 · MENOR · grau A · três leituras de A10 e do v6 sobre HD 166620**
- A10 §1.4, item 2, cita "less than this in six of the nine seasons" logo depois de 0.3 %. Nas nove estações do Keck com mais de uma observação, seis têm σ_S/⟨S⟩ abaixo de 1.2 % e nenhuma abaixo de 0.3 %; as duas menores são 0.303 % e 0.339 % (`3.4-57`, `3.4-57b`, `3.4-57c`).
- v6 §5: "S_HK a cadência bruta, 1995–2002: 132". São 132 para 1995.0 ≤ t < 2002.0 e 137 para os anos civis 1995 a 2002, que é a janela das oito médias anuais (`3.4-14`, `3.4-15`).
- A separação 107 / 1 547 não é derivável da tabela de Luhn (sem rótulo de fotômetro; em Baum, HKP-1 e HKP-2 se sobrepõem entre 1977.26 e 1977.57). Confere pela Tabela 1 de Baum e pela soma 1 654 (`3.3-48`, `3.4-06` a `3.4-06e`).

**I-15 · MENOR · grau A · dois números de A9**
- A9-F9: "39 das 59 estrelas superam 10 obs/yr". Coluna `Cadence` da Tabela 2: 36 (`3.3-13`).
- A9 §1.1: cobertura "1966.18 – 2020.19". Máximo da Tabela 1: 2020.1849, que arredonda para 2020.18; A9 §1.2 dá 2020.18 para HIRES-2 (`3.2-05`).

**I-16 · MENOR · grau A · arquivo `isaacson2024_least_active_50.csv`**
- O filtro Nobs ≥ 45 e SSD < 0.00121 dá 48 e coincide com o CSV nome a nome (`3.6-13`, `3.6-19`). SSD < 0.00125 dá 52 (`3.6-14`).
- Terceira leitura: SSD ≤ 0.00121 dá exatamente 50, contando a própria τ Cet e um empate (`3.6-15`).
- A11b-F1 diz que o critério está "documentado na própria coluna `fonte`"; a coluna só traz a referência da tabela (`3.6-22`).
- O critério é σ absoluto. Em dispersão relativa, 16 das 48 estão acima de τ Cet (`3.6-23`) e só 32 estrelas ficam abaixo dela (`3.6-16`). HD 23249 tem SSD menor que τ Cet e dispersão relativa maior (0.86 % contra 0.72 %) (`3.6-30`, `3.6-31`).

**I-17 · MENOR (favorável) · grau A · D52 confirmada por via independente**
- Aplicando as fórmulas de D52 ao B−V e ao S mediano da própria CLS V, o log R′_HK tabulado sai até a terceira casa: HD 10700, −4.958; HD 32147, −4.905; HD 166620, −5.002 (`3.7-17` a `3.7-19`). É uma segunda verificação da receita que não depende do PDF de Noyes.
- Com B−V e ⟨S⟩ do catálogo A1 (cálculo passo a passo em `saidas/03f_isaacson_noyes.txt`): HD 10700, B−V 0.72, S 0.171, log R′_HK = −4.959, R_phot/R_HK = 0.49; HD 32147, 1.06, 0.286, −4.948, 0.05; HD 201091, 1.18, 0.658, −4.764, 0.006 (`3.7-12` a `3.7-14`).
- A forma alternativa de Duncan (A12-F6) desloca log R′_HK em 0.04 (HD 10700), 0.11 (HD 32147) e 0.05 dex (HD 201091). É o teste de robustez que A12-F6 sugeria e D39 impedia. Vai na mesma direção de D54.
- D40 confere: a inclinação 1.340 × 10⁻⁴ · C′_cf é positiva para os 112 valores de B−V (`3.7-20`).

### 1.2 Consistência entre documentos

**I-18 · IMPORTANTE · grau A · incorporação pendente no caderno, e o que a instrução não cobre**
- Faltam no caderno: D41–D54 e D45b (`2a-09`), Q10 e Q11 (`2a-10`), dez linhas da §8, a linha do log (`2a-11`). `NOTEBOOK_proposta_D41_D54.md` aplica as quatro operações da instrução e nada mais (`2a-20` a `2a-24`).
- Fica como está, porque a instrução não manda mexer:
  - cabeçalho "Última entrada: 2026-08-01 (fecho da conversa de consolidação)";
  - §5: a tabela de C tem três colunas e elimina a coluna "Subsídios"; com ela somem as remissões a A6 §6.2, A1 §1.3, A4-F2, A1-F7 e a `P4_DECISION_SUPPORT_6.1.md`;
  - §6 (itens bloqueados): não recebe o depósito Radick & Pevtsov 2018b/c que v6 §10 lista (I-28);
  - §7, papéis dos documentos: não cita `DECISOES_D41_D54.md`, `data/`, nem os CSVs da segunda rodada;
  - §7, obrigações de Methods: continua "D08, D12 (N uniforme por construção — dizer explicitamente), D20–D23, D24–D26, D30, ressalva de Q6". Não menciona Baum, Luhn, D44 (junção), D45 (receita), D46 (limitação declarada), D48–D51 (objeções), D54;
  - §8: a linha "N é confundido com grupo? Não. Uniforme por construção" fica sem a restrição de A9-F5; a linha de DFA continua dizendo "Reaberta como Q9" sem o estado "reportada, devolvida".
- **A decidir (P):** se essas partes entram na incorporação. Não foram editadas na proposta.

**I-19 · MENOR · grau A · registro das decisões**
- D01–D54 definidas uma única vez cada (`2a-01`, `2a-02`); nenhuma referência a D## inexistente (`2a-07`). Há uma 55ª entrada, D45b, fora da numeração e nunca citada fora de DECISOES (`2a-03`, `2a-08`).
- As 55 têm `Status: ativa` (`2a-05`). D32 (suspensão até A9), D37 (abrir quatro unidades) e D39 (nada de conversão antes de A12) estão cumpridas e seguem "ativa"; DECISOES §C diz "D32 cumprida".
- 36 decisões não trazem campo de grau no cabeçalho (`2a-06`).
- v6 §1: "Dez decisões novas, D41–D51, mais três de método (D52–D54)". D41–D51 são onze números, doze entradas com D45b.

**I-20 · IMPORTANTE · grau A · lista de questões abertas nos três documentos**

| Q | Caderno §5 | `paper_state_v6.md` | DECISOES §C |
|---|---|---|---|
| Q1 | SUSPENSA até A9 | §3: "volta à mesa", quatro opções | aberta, desbloqueada |
| Q2 | aberta (ρ CrB) | §11 item 7 | aberta, subsídio novo + D51 |
| Q3 | aberta | §11 item 7 | aberta, inalterada |
| Q4 | aberta | §11 item 7 | aberta, reforçada (genérica) |
| Q5 | aberta | §11 item 7 | aberta, inalterada |
| Q6 | aberta, decidir apresentação | §3.3 | aberta, grande avanço |
| Q7 | aberta (subgigantes) | §11 item 7; e §11 item 5 usa "Q7" para outra coisa (I-21) | aberta, objeção publicada |
| Q8 | nova, depende de A12 | §7: aberta, recomendação não migrar | aberta, balanço invertido |
| Q9 | nova, reaberta | §6: reportada, devolvida | aberta, reportada |
| Q10 | não existe | **não aparece** | NOVA, aberta |
| Q11 | não existe | **não aparece**; §11 item 7 lista Q2–Q7 sem ela | NOVA, aberta |

- v6 não tem tabela de questões. O conteúdo de Q10 e Q11 está em v6 §4.3 e §8 item 7, sem o número.
- Ordem de dependência: DECISOES §E põe Q8 depois de Q1; v6 §11 dá Q8 sem dependência. Os itens 4 (junção) e 5 (aceitar D46) da §E não estão em v6 §11. A7 é item 4 em v6 §11 e condição do item 6 na §E.

**I-21 · MENOR · grau A · "Q7" designa duas coisas**
- Protocolo §11, questão 7: "Has anyone already claimed grand minima are unpredictable?". Caderno Q7: subgigantes no grupo `Flat`.
- Usos no sentido do protocolo: A11 ("Esta é a fonte que responde Q7"; "desafio central a Q7"), v5 §3 e §6, v6 §11 item 5 ("A8 … Contexto solar; Q7").
- Usos no sentido do caderno: A9-F8, A11a-F3, DECISOES §C.

**I-22 · MENOR · grau A · logs de auditoria (Project contra repositório)**
- Contagens de achados coerentes com os corpos dos arquivos: A1 9, A2 7, A3 6, A4 8, A5 6, A6 14, A9 10, A10 7, A11 9 (4 + 5), A12 7 (`2d-01` a `2d-10`). Nenhuma referência A#-F# aponta para achado inexistente (`2d-11`).
- A3 aparece com achados "F1–F6" no log de A3 (Project) e "—" nos logs de A5 e A6 (repositório) (`2d-13`).
- O log de A6 registra "F1–F13"; o corpo define F14 e v5 §2 diz F1–F14.
- A coluna "Unresolved" de A1 varia entre "none (2 escalated to A3)" e "none".
- A9–A12 não têm tabela de log (`2d-14`). O log do próprio protocolo (§10) mostra as oito unidades como "open" (`2d-15`); a correção de A5-F6 ao protocolo §2 (PDF de Peng é scan) não foi aplicada.
- As tabelas de log não se contradizem em estado nem em datas.

**I-23 · MENOR · grau A · A9-F1 repete HD 4628**
- Texto: "(HD 101501, 166620, 190406, 4628, mais HD 4628)". A Tabela 2 tem quatro períodos com `?`: 101501, 166620, 190406, 4628 (`3.2-30`, `3.2-31`, `3.8-17`). A contagem 10 + 4 está certa; a quinta menção é repetição.

**I-24 · MENOR · grau A · remissões que não chegam ao destino**
- `audit/baliunas_table2_full.csv` é citado em oito documentos; o arquivo está na raiz do pacote (D38).
- Caderno Q2 cita "A6 §6.2"; A6 não tem essa seção (`1-10`). O conteúdo está em `paper_state_v4.md` §6.2.
- v6 §11 item 9: "protocolo §5 regra 5"; as regras estão no protocolo §3.
- A1 §9 cita `extract_tsv.py`, `merge_table2.py`, `cell_verify.py`, `finalize.py`; nenhum está no pacote. O checksum de A1 §2.1 foi refeito aqui (`3.1-02` a `3.1-07`).
- A9, D41 e v6 chamam os TSVs de "da raiz"; no pacote estão em `data/`.
- v6 §3.1, tabela: "`Flat` limpo em CLS V: 4 (faltam 43587, 160346)". HD 160346 é controle `CYCLE`; das cinco `Flat` só HD 43587 falta (`3.6-28`).

**I-33 · MENOR · grau A · "congelado" e "decidido" no v6 contra o caderno**
- Coincidem: pipeline congelado; `baliunas_table2_full.csv` congelado (D36, D43); A1–A6 fechadas; nenhuma unidade decidiu Q1, Q8 ou D24; D34, D15 e D10 mantidas.
- Não coincidem: v6 §3.1 restringe D12 ao catálogo Baliunas, e o caderno (§7 e §8) ainda a enuncia sem restrição (I-18). v6 §10 lista `audit/a9_instrument_step.csv` como novo; o caderno §7 trata `audit/*.csv` como congelados sem distinguir.

### 1.3 Inventário e integridade

**I-25 · IMPORTANTE · grau X · arquivos ausentes e o que cada ausência bloqueia**

| Ausente | Citado em | Bloqueia |
|---|---|---|
| `P4_DECISION_SUPPORT_6.1.md` | caderno Q1 e Q7, v5 §1 | reconstruir a definição dos grupos (I-06) e as "cinco opções" de Q1 |
| `COWORK_PROMPT_A9_A12.md` | caderno D37 | conferir o escopo pedido às unidades (por exemplo "os 29 períodos") |
| `P4_SOURCE_VALUES.md`, `p4_star_catalog.csv` | sete documentos | nada: nascem na consolidação |
| `audit/A7_theory.md`, `audit/A8_usoskin.md` | protocolo, v4, README | D50 e Q10 (resposta teórica); contexto solar |
| PDFs de Baum+2022 e Luhn+2022 (nome de arquivo não citado), `bib/aa54111-25.pdf`, `bib/Isaacson_2024_ApJS_274_35.pdf`, `bib/Isaacson_2025_AJ_170_181.pdf`, `bib/Noyes1984.pdf`, `bib/aa28479-16.pdf` | A9–A12, v6 | toda citação literal de D44–D51 e D54; qual conta Luhn descreve (I-01); o texto de τ Cet (0.00125) e de HD 55575 (I-03) |
| `UNIVERSAL_PAPER_CONTEXT.md`, `FASE1_PAPERS_P1_P12.md`, `SUBMISSION_STRATEGY_TIMELINE.md` | README, v4 | nada nesta inspeção; os dois últimos existem em `kit/programas/stellar-activity-29/` |
| scripts de A1 (quatro) | A1 §9 | refazer a extração por OCR |
| `results/claude_report.md` | notebook | nada: o notebook nunca chegou a gerá-lo |

- A lista de ausências conhecida está confirmada (`1-08`). O README diz "os PDFs estão no repositório GitHub"; no clone há os nove PDFs do protocolo §2, na raiz, e nenhum da segunda rodada (`1-05`, `1-06`). O repositório remoto só tem o branch `main`.

**I-26 · MENOR · grau X · `bib/aa28479-16.pdf` (Oláh+2016)**
- A10 §6: "Está em `bib/` e disponível". v6 §11 item 6 cita o mesmo caminho. README: não apareceu na raiz do clone.
- Não existe em nenhum lugar do clone, em nenhum commit (`1-09`). Pelo que D38 registra, o lugar era `bib/` no repositório GitHub; na arquitetura do kit seria `referencias/`.

**I-27 · MENOR · grau A · disposição do repositório**
- O pacote descrito no README está em `P4/` dentro do repositório. A raiz tem cópias byte a byte de 24 dos 36 arquivos (17 com o mesmo nome e os sete TSVs com `:`) e nenhuma cópia divergente (`1-02`, `1-03`). Só existem no pacote: `CLAUDE.md`, `README_HANDOFF.md`, caderno, protocolo, `paper_state_v5.md`, A1–A4, `historico/`, `bib/LEIAME.txt`.
- `kit/docs/LAYOUT_REPO.md` espera na raiz `CLAUDE.md`, `kit.yml`, `CADERNO_PESQUISA.md`, `DECISIONS.md`, `PAPER_STATE.md`, `referencias/`, `manuscrito/`, `repositorio/`, `fora_repositorio/`. Nenhum existe com esses nomes; `kit.yml` está dentro de `kit/`.
- **A decidir (P):** qual das duas cópias é a de trabalho e como o pacote migra para o layout do kit.

**I-28 · MENOR · grau A · listas de pendências incompletas ou divergentes**
- v6 §8 lista oito itens grau X. Não traz os três X de A5 §6, os três X de A6 §7, nem os itens C de A10 §5 e de A12 §7 (tabela da seção 4).
- Depósito Dataverse: caderno §6 e v5 §7 citam "Pevtsov 2016, doi:10.7910/DVN/VF5BMO" (Ca II K solar composto); v6 §10 cita "Radick & Pevtsov 2018b/c" (dados MW, DOIs em A9 §1.1). São depósitos diferentes; cada documento lista um só.

**I-29 · MENOR · grau B · os domínios "bloqueados" respondem nesta sessão**
- Em 2026-11-14, a partir deste ambiente, `iopscience.iop.org`, `vizier.cds.unistra.fr`, `nso.edu` e `arxiv.org` devolveram HTTP 200; `dataverse.harvard.edu` e `ui.adsabs.harvard.edu`, HTTP 202. Nada foi baixado.
- O bloqueio registrado no caderno §6 era do sandbox das sessões anteriores. **A decidir (P):** se a obtenção da Tabela 4 de Egeland passa a ser feita por aqui ou pelo fluxo do kit (`REG-ACT`).

### 1.4 Arquivos derivados

**I-30 · MENOR · grau A · `audit/saar_baliunas_crossmatch.csv`**
- 70 linhas, 61 + 9, 59 no catálogo, classes 42/9/7/1/0: confere (`3.8-30` a `3.8-34`, `3.8-44`). Colunas de Baliunas idênticas ao catálogo (`3.8-43`).
- As nove linhas "Table 5 only" estão no catálogo, mas `in_bal_catalogue`, `bal_class` e `bal_S` estão vazios (`3.8-35`).
- A6 decisão 6 diz que o indicador de estrela-padrão "has been added" ao CSV; ele existe para 11 das 17 padrões, porque as outras seis não estão no arquivo (`3.8-45`, `3.8-46`).
- A6 §2.1 e §2.2: "24 de 30 idênticas" e "6 divergências". No CSV há 29 pares numéricos mais o Sol, cuja linha está vazia do lado de Baliunas (`3.8-36`, `3.8-37`): 22 idênticos (os 22 nomeados), sete diferentes. HD 100180 aparece nas duas listas de A6; HD 81809 (8.2 contra 8.17) não aparece em nenhuma (`3.8-38` a `3.8-42`).

**I-31 · MENOR · grau A · formatação dos CSVs derivados**
- `baum2022_cycle_periods.csv`: HD 190406 com `delta_sigma = 730.0`, que A9-F3 imprime como "troca de primário" (`3.8-23`); valores com ruído de ponto flutuante (`0.7000000000000011`).
- `noyes1984_validade_cor.csv` e `baum2022_59stars.csv`: B−V regravado sem zero final em 11 e 4 linhas (`0.7` por `0.70`); valores numéricos iguais ao catálogo (`3.7-02`, `3.7-02b`, `3.8-07`).
- D53 escreve "6 acima de 1.0 · 2 acima de 1.2"; são faixas disjuntas (1.0–1.2 e > 1.2). Acima de 1.0 há oito estrelas (`3.7-11`).

### 1.5 Pipeline

**I-32 · IMPORTANTE · grau A · o notebook contradiz decisões ativas em 30 pontos**
- Detalhe célula a célula em `MAPA_PIPELINE.md`. Quatro itens produziriam números inadmissíveis: p-valores de Kendall do scipy (P-01), ausência total de surrogates ARMA (P-02), `n_max = max(8, N // 4)` (P-06) e ajuste único sem crossover (P-07).
- O catálogo embutido tem 14 estrelas e não lê o CSV congelado. O grupo "Irregular" contém duas `CYCLE` (HD 3651, HD 76151) e HD 3651 está com período zero (`4-04`, `4-06`). O grupo "Flat" contém uma estrela-padrão (HD 45067) e uma binária do Apêndice B (HD 178428) (`4-05`).
- O notebook parou na célula 10 por falta do arquivo solar e não guarda nenhum resultado (`4-19`).
- Conforme: `S_SUN_MEAN = 0.1694`, exclusão de HD 4915 e de HD 190406, ⟨S⟩ das 14 estrelas igual ao catálogo (`4-02`), janela de 50 %, bloqueio de DFA abaixo de 100 pontos, núcleo da DFA fiel a Peng.
- **Nada a decidir agora:** é o mapa para o passe único pós-consolidação.

---

## 2. Etapas 1 e 2 em tabela

### 2.1 Inventário

| Item | Resultado | Checagem |
|---|---|---|
| Arquivos no pacote (sem `inspecao/`) | 36 | `1-01` |
| TSVs em `data/` casados com os nomes com `:` do README | 7 de 7, idênticos às cópias da raiz | `1-04` |
| PDFs | 9 na raiz do repositório; 0 em `bib/` | `1-05`, `1-06` |
| Nomes de arquivo citados e ausentes | 25 distintos (inclui padrões como `audit/A#_*.md`) | `1-07` |
| Listagem com tamanho e sha256 | `saidas/01_inventory.txt` | — |

### 2.2 Contagens repetidas (etapa 2c)

| Contagem | Documentos | Dados | Estado |
|---|---|---|---|
| 59 estrelas, 62 135 observações | v6, D41, A9 | iguais | confere |
| 26 em comum com Baliunas (27 por HD) | A9 §2, D43 | 26 e 27 | confere |
| 14 reclassificadas | A9 §2, D43 | 13 ou 15 | **I-04** |
| 14 períodos (10 + 4) | A9-F1, D42 | 14, 10 + 4 | confere |
| 112 linhas; 52 / 31 / 29 | v4, D09, A1 | iguais | confere |
| 82 / 17 / 6 / 2 / 5 | D53, A12 | iguais com faixa fechada | confere; ver I-07 |
| 48 estrelas | v6 §10, A11b-F1 | 48 | confere; ver I-16 |
| 710 e 138 | A11, D41 | iguais | confere |
| 52 380 linhas da Tabela 3 da CLS V | D41, A9, A11 | 52 372 | **I-10** |
| 51 estrelas, 4.47 %, 25/51, 10/51 | D44, A9 §1.7 | iguais | confere; ver I-09 |

### 2.3 Suspeitas da etapa 2d

| Suspeita | Resultado | Achado |
|---|---|---|
| (i) HD 4628 duas vezes em A9-F1 | confirmada; são quatro estrelas distintas | I-23 |
| (ii) caderno em termos de A1–A6, sem Baum/Luhn em Methods | confirmada; a instrução de incorporação não altera a §7 | I-18 |
| (iii) `bib/aa28479-16.pdf` | ausente de todo o clone; A10 §6 afirma que está em `bib/` | I-26 |
| (iv) tabelas de auditoria Project × repositório | sem contradição de estado; três divergências de preenchimento | I-22 |

---

## 3. As 27 falhas de `checks.csv`

| id | Onde está a falha | Esperado → obtido | Achado |
|---|---|---|---|
| `2d-13` | texto (logs de A5 e A6) | achados de A3 iguais em todos os logs → "F1–F6" e "—" | I-22 |
| `3.1-15` | critério da reprodução | 32 → 33 (conto `. Long`) | I-11 |
| `3.2-05` | texto de A9 §1.1 | 2020.19 → 2020.18 | I-15 |
| `3.3-13` | texto de A9-F9 | 39 → 36 | I-15 |
| `3.4-05` | contradição conhecida (A10-F1, texto de Luhn × tabela) | 158 → 119 | — |
| `3.4-52` | texto de D45 e v6 §2 | 8.78 × 10⁻⁶ → 8.68 × 10⁻³ | I-01 |
| `3.4-54` | texto de D45 e v6 §2 | 8.78 × 10⁻⁶ → 4.1 × 10⁻³ | I-01 |
| `3.6-05` | texto de D41, A9, A11 | 52 380 → 52 372 | I-10 |
| `3.6-22` | texto de A11b-F1 | critério na coluna `fonte` → não está | I-16 |
| `3.6-25`, `3.6-26` | texto de A11 §b.2 (citação do artigo × tabela) | HD 55575 → HD 187923 | I-03 |
| `3.6-27` | texto de A11 §b.3 | 0 linhas erradas → 1 (HD 3651) | I-02 |
| `3.7-10` | texto de D53 (intervalo aberto) × CSV (fechado) | 82 → 78 | I-07 |
| `3.8-09`, `3.8-10` | texto de A9 §2 | "treze" → 14 nomes; HD 190406 sem mudança de tipo | I-04 |
| `3.8-11`, `3.8-11b` | texto de A9 §2 e D43 | 14 → 15; HD 23249 além de HD 10700 | I-04 |
| `3.8-36` | dado derivado (linha do Sol vazia no CSV) | 30 → 29 | I-30 |
| `3.8-45` | dado derivado × texto de A6 decisão 6 | 17 → 11 | I-30 |
| `3.9-01` | texto de A9 §2.1 ("pós-D13") | 5 → 7 | I-06 |
| `3.9-06` | texto do caderno Q7 | 3 → 4 | I-06 |
| `3.9-16` | texto de A12-F1 × intervalo aberto de D53 | 5 → 4 | I-07 |
| `3.9-30` | texto de v5 §4 e A12 §3.1 | 0.88 → 0.87 (com o Sol) | I-05 |
| `3.9-32` | texto de v5 §4 (rótulo) | 0.73 → 0.56 | I-05 |
| `3.9-35` | texto de v5 §4 e do caderno Q8 | 0.49 → 0.525 | I-05 |
| `4-04`, `4-06` | pipeline, célula 8 | grupo "Irregular" e período de HD 3651 | I-32 |

---

## 4. Etapa 5 — bloqueios e decisões humanas

### 4.1 Itens grau X e C em aberto

| Item | Grau | Unidade | Em v6 §8? | Verificação desta inspeção |
|---|---|---|---|---|
| Reescalonamento do indicador DFA (Livina & Lenton 2007) | X | A5 §6 | não | — |
| H = (β+1)/2 sem fonte | X | A5 §6 | não | usado no pipeline (P-09) |
| Viés de comprimento finito da DFA (Peng 1993) | X | A5 §6 | não | — |
| ⟨S⟩ de HD 10476: 0.198 × 0.1896 | X | A6 §7 | não | CLS V dá Smed 0.1926 (`3.6-27`), terceira medida de época diferente |
| P_cyc de HD 3651, 4628, 149661 (Baliunas × Saar) | X | A6 §7 | não | `3.8-42` |
| ρ CrB: `Long` × flat | X | A6 §7 | via Q2 | `3.8-51` |
| Incerteza residual dos offsets de Baum; identidade das 14 estrelas | X | A9 §8 | item 1 | I-09 (`3.5-19b`), grau C |
| "29 estrelas com ciclos" | X | A9-F1, A11b-F2 | item 2 | 14 na tabela (`3.2-29`) |
| HD 185144 em B95 ou não | X | A9-F2 | item 4 | I-11 enfraquece a explicação de A9-F2 |
| P_rot das 59 estrelas | X | A9 §8 | não | — |
| Separação entre degrau instrumental e variação real | C | A9 §8 | no item 1 | I-09 |
| 158 × 119 observações `new_MW` | X | A10-F1 | item 3 | `3.4-04`, `3.4-05` |
| Dispersão sazonal pós-2004: 0.35 × 0.22 mmag | C | A10 §5 | não | 0.22 reproduzido (`3.4-20c`) |
| Dados de Oláh+2016 como comunicação privada | C | A10 §5 | não | — |
| "Hint" de 2014 (ponto único) | C | A10-F7 | não | N = 1, S = 0.1776 (`3.4-58`) |
| Massa de HD 166620: 0.78 × 0.760 | C | A10 §5 | não | — |
| "50 estrelas menos dispersas que τ Cet" | C | A11b-F1 | item 5 | 48, 52 ou 50 (I-16) |
| σ_S de τ Cet: 0.00121 × 0.00125 | C | A11 | no item 5 | tabela 0.00121 (`3.6-11`) |
| Inclinação das `Flat` | X | A11 §c.3, D51 | item 7 | — |
| [Fe/H] da amostra P4 | X | A11a-F4 | item 8 | coluna `FeH` completa em `baum2022_59stars.csv` |
| Incerteza formal de R′_HK | X | A12 §7 | item 6 | diferença entre as duas formas de R_phot: 0.04 a 0.11 dex (I-17) |
| C_cf abaixo de B−V 0.43 | C | A12 §7 | não | cinco estrelas (`3.7-07`) |
| Calibração absoluta de R_HK | X | A12 §7 | não | — |
| Coeficientes de Duncan sem verificação visual | B | A12 §7 | não | — |
| **Novos desta inspeção** | | | | |
| Qual conta é a receita de Luhn §3.1 | X | I-01 | — | exige o PDF |
| Piso instrumental da CLS V: texto × tabela | X | I-03 | — | `3.6-25` |
| Quais são as 14 reclassificadas | X | I-04 | — | `3.8-08` a `3.8-11b` |
| Regra que define as cinco `Flat` limpas | X | I-06 | — | `3.9-01`, `3.9-02` |
| B−V: catálogo A1 × CLS V | X (duas fontes grau A discordam) | I-07 | — | `3.9-21`, `3.9-24` |
| `J/ApJ/438/269` tem tabela de séries? | X | MAPA P-25 | — | não verificado |

### 4.2 Bloqueios de rede ou de dados

| Item | Para quê | Registrado como bloqueado em | Estado nesta sessão |
|---|---|---|---|
| Tabela 4 de Egeland+2017 | D18, trilha solar | caderno §6, v6 §10 | domínio IOP responde (I-29); não baixada |
| Dataverse, Pevtsov 2016 (VF5BMO) | contexto de D18 | caderno §6 | responde (HTTP 202); não baixado |
| Dataverse, Radick & Pevtsov 2018b/c | auditar offsets de Baum (D44) | v6 §10 | idem |
| Série S solar do NSO | alternativa a Egeland T4 | caderno §6, v6 §10 | `nso.edu` responde; não baixada |
| PDFs da segunda rodada e Oláh+2016 | reverificar D44–D54 | — (dados como presentes em `bib/`) | ausentes do clone (I-25, I-26) |
| Livina & Lenton 2007; Peng 1993; Brandenburg, Saar & Turpin 1998; Radick 1998; Baliunas & Jastrow 1990; fonte de H = (β+1)/2 | A5 §6, A6 §8 | A6 §8 | não testado |
| Korolik+2023 (inclinação de τ Cet); Shah+2018 | D51, D47 | citados, não auditados | não testado |
| Eddy 1976 | protocolo §2 e A7 | protocolo | não está no repositório |
| A7 e A8 | D50, Q10; contexto solar | CLAUDE.md, v6 §11 | os três PDFs (Scheffer, Held & Kleinen, Usoskin) **estão** na raiz do repositório |

### 4.3 Decisões humanas da §E, na ordem de dependência

| # | Decisão (§E de DECISOES) | Recomendação já registrada | Checagens relevantes | A reprodução muda o balanço? |
|---|---|---|---|---|
| 1 | Série anual ou série bruta é o objeto do P4 | nenhuma; "decisão-raiz" | `3.3-01` a `3.3-11` (N, estações, lacunas); `3.2-18` a `3.2-22` (flags; 473 pontos `sigma`); `3.4-12`, `3.4-13` (oito médias anuais); `3.3-55`, `3.3-56`; MAPA §3 e P-24 | não. Os números de v6 §6 reproduzem |
| 2 | Q1, composição da amostra | (ii) e (iv) não são exclusivas; HD 101501 é o objeto que melhor sobrevive | `3.9-01` a `3.9-13`; `3.3-50` a `3.3-56`; `3.8-08` a `3.8-11c`; `3.6-27` a `3.6-31`; I-02, I-06, I-12, I-13 | **qualifica**: a cobertura de HD 101501 é de um só instrumento até 1995.45 mais seis pontos (I-08). HD 3651 tem ciclo de 10.01 anos na CLS V, ao contrário do que A11 registra (I-02) |
| 3 | Q8, migrar para R′_HK | não migrar (D54) | `3.7-03` a `3.7-21`; `3.9-14` a `3.9-24`; `3.9-30` a `3.9-42` | **não inverte**. As contagens de D54 item 1 dependem da fonte de B−V e do tratamento da fronteira (I-07); a receita de D52 fica confirmada por via independente e a diferença entre as duas formas de R_phot chega a 0.11 dex (I-17) |
| 4 | Tratamento da junção 2001→2004, se (ii) | regra operacional de D44 | `3.5-01` a `3.5-22`; `3.3-48`; `3.4-06d`, `3.4-06e` | não. Acrescenta que 17 das 51 estrelas têm medianas coincidentes (I-09) |
| 5 | Aceitar D46 (teste de Dakos não executável em HD 166620) | declarar como limitação | `3.4-10` a `3.4-15`; `3.4-19`, `3.4-20` | não. 8 médias anuais e 12 estações APT conferem. I-01 afeta a comparação entre estados que D46 propõe no lugar |
| 6 | Sustentabilidade da resposta teórica a D50 | depende de A7 | nenhuma numérica | não avaliável; os PDFs de A7 estão na raiz do repositório |
| 7 | Q2, Q3, Q4, Q5, Q6, Q7, Q11 | nenhuma | Q2: `3.6-27`, `3.8-45` a `3.8-51`; Q3: `4-18`, MAPA P-14; Q5: `3.9-03`, `4-05`; Q6: `3.6-24` a `3.6-26`, `3.4-57`; Q7: `3.9-06` | Q6: o piso de 0.45 % não é o mínimo da tabela (I-03). Q2: as medidas 0.72 / 0.86 / 0.95 / 1.49 % conferem. Q7: quatro das cinco têm classe IV ou Vp, não três (I-06) |

Q10 não tem linha própria na §E; está ligada ao item 6.

---

## 5. Como refazer

```bash
PYTHON=/caminho/para/python bash inspecao/scripts/run_all.sh
```

Requer `numpy`, `pandas` e `scipy`; todos os scripts rodam com `python -I`. Duas execuções seguidas produziram `checks.csv` idênticos. As saídas auxiliares (tabelas completas, listagem numerada do notebook, cálculo passo a passo de D52) ficam em `inspecao/saidas/`. O `scipy` foi instalado num ambiente virtual fora do repositório, porque não estava disponível no ambiente da sessão.

---

## 6. Adendo — verificação contra os PDFs (2026-11-14)

Os PDFs de Baum+2022, Luhn+2022 e Isaacson+2024 (CLS V) foram guardados em `P4/bib/` com os nomes que A9–A12 já citavam (`Baum_2022_AJ_163_183.pdf`, `Luhn_2022_ApJL_936_L23.pdf`, `Isaacson_2024_ApJS_274_35.pdf`). Li o texto de Luhn inteiro, as páginas 1–4 de Baum e as páginas 1–3 de Isaacson, e conferi por busca no texto extraído as passagens de Baum, Luhn e Isaacson abaixo. Os achados acima ficam como estão; este adendo só acrescenta o que a fonte primária mostra. Continuam sem PDF: Järvinen & Strassmeier 2025, CLS VI, Noyes+1984 e Oláh+2016, de modo que D48, D50–D54 seguem sem conferência literal.

**DOI da CLS V** (primeira página do PDF): `10.3847/1538-4365/ad676c`. O DOI `10.26093/cds/vizier.22740035` que aparece nos TSVs é o do catálogo VizieR, não o do artigo.

| Achado | O que a fonte diz | Efeito |
|---|---|---|
| **I-01** | Luhn §3.1 (p. 4): o ruído é subtraído "from the **observed values**" e dá σ_S(min. 1) = 0.0027, σ_S(min. 2) = 0.0054, σ_S(grand) = 0.0019. "Seasonal" aparece só na estimativa do ruído do Keck ("lowest seasonal σ_S values approach 0.3%"). Em seguida: "Even when corrected for intrinsic noise differences … an F-test gives 8.78 × 10⁻⁶ chance that σ_S(grand) is drawn from the same distribution as σ_S(min. 1)." | O passo 1 de D45 ("dentro de cada estação") não está em Luhn; é leitura de D45/A10. E o artigo apresenta o p como posterior à correção, mas ele só reproduz com as variâncias brutas (`3.4-50`); com os σ_S corrigidos dá 8.7 × 10⁻³ (`3.4-52`). **A inconsistência está no próprio Luhn, e não só em D45 e no v6.** Continua BLOQUEANTE; a pergunta passa a ser o que Luhn calculou, que só os autores respondem |
| **I-03** | Isaacson §5.6: "Our least active star **with more than 45 observations** is HD 55575 with a relative dispersion of 0.0007/0.1562 = 0.45%." §2.2 (p. 3): "HD 55575, our least active star … 0.0007/0.156 = 0.45%." A Tabela 2 do mesmo artigo tem HD 187923 (SSD 0.00059, Smed 0.1585, 106 obs) e HD 144579 (SSD 0.00066, Smed 0.1664, 122 obs) abaixo | A contradição é interna ao artigo (texto × tabela), grau A nos dois lados, portanto grau X. Para τ Cet há três valores no mesmo artigo: 0.82 % (0.00139/0.1675, §2.2), 0.75 % (0.00125/0.1674, §5.6) e 0.72 % (Tabela 2). A11 registrava dois |
| **I-04** | Baum §4.2: "Of the 26 stars that were included in both the B95 catalog and this one, 14 stars were given new classifications"; exemplo HD 10700 (`flat?` → `flat`); "Of the three stars … originally classified as long, only HD 141004 maintained this classification. HD 9562 and HD 143761 were reclassified as flat." | O número 14 é de Baum e Baum não lista quais; a lista é de A9. O achado fica como está |
| **I-14** | Luhn §3.1: "Baliunas et al. (1995) give σ_S ≈ 1.2% … The calculated σ_S is less than this in six of the nine seasons with more than one S_HK(Keck) measurement. The lowest seasonal σ_S values approach 0.3%" | "this" é o 1.2 %, como em `3.4-57`. A ordem das frases em A10 §1.4 item 2 induz a ler 0.3 % |
| A10-F1 | Luhn §2.2: "contain 158 observations" | confirmado como texto; a tabela tem 119 |
| A9-F1 | Baum, Resumo: "We have analyzed 29 stars with periodic cycles". Isaacson §4.2.2: "We cross-check the 13 cycles from 59 stars examined in Baum et al. (2022) … find 10 of the 13 cycles. … HD 101501 and HD 152391 have fewer than 45 observations" | confirmados |
| A11b-F1 | Isaacson §5.6: "Fifty stars have a smaller S-value standard deviation than HD 10700" | confirmado |
| A11b-F3 / D47 | Isaacson §5.6: "HD 4915 is a candidate star in a Maunder minimum–like state (Shah et al. 2018), but our extended time baseline shows two cycles." | confirmado. A Tabela 4 dá P = 4.86 e Amp = 0.2046 para HD 4915 (`3.6-27`) |
| D44 | Baum §2.1.1–2.1.3 (p. 3): "shifting the median of the pre-1977 measurements"; "a constant shift"; "Fourteen stars in the post-2010 CPS data showed a clear offset … and were shifted accordingly" | confirmado |
| Baum §4.1 | "The data at face value argue that the grand minimum is not at a lower level than the local minima … However, some other stars required offsets between instruments, so this conclusion is not robust." "we estimate the cycle period … to be 17 yr" | confirmado (A9 §1.6) |

**I-34 · MENOR · grau A · janelas dos mínimos em Luhn §3.1.** O texto diz "the minimum occurring from 1971 to 1975 and the minimum occurring from 1986 to 1990" e, na frase seguinte, "The second minimum (1987.0–1991.0)". São duas janelas diferentes para o mesmo mínimo. A10 usa 1987.0–1991.0 e com ela reproduz ⟨S_HK⟩ = 0.1724 e σ = 0.0058 (`3.4-28` a `3.4-30`). Não testei 1986–1990.

**I-35 · IMPORTANTE · grau A · HD 101501 em D49 e no v6.** D49 e v6 §3.4 descrevem "dez anos de estado plano seguidos de retorno à atividade cíclica defasado em 180°". Baum §4.1 e a legenda da Figura 4 dizem: "HD 101501 experienced 10 yr of lower activity, a much lower amplitude cycle than the rest of its cycle"; "This star, while possibly still exhibiting a low-amplitude cycle, is a good example of capturing both the drop from—and return to—cyclic behavior". Baum não chama o trecho de plano e admite que o ciclo de baixa amplitude pode continuar. Isso enfraquece o papel de HD 101501 como contraexemplo de *aged out* (D49): o objeto sai de um estado de baixa amplitude, que o próprio Baum ainda trata como possivelmente cíclico. Complementa I-08 (cobertura de um só instrumento). Nenhuma recomendação nova: decidir se a redação de D49 e do v6 deve seguir a de Baum cabe ao pesquisador.

**I-25 atualizado:** Baum, Luhn e CLS V passam de ausentes a presentes em `bib/`. Continuam ausentes: Järvinen & Strassmeier 2025, CLS VI, Noyes+1984, Oláh+2016.

### 6.1 Segundo lote de PDFs (2026-11-14)

Foram baixados e guardados em `P4/bib/`: `Isaacson_2025_AJ_170_181.pdf` (CLS VI), `Noyes1984.pdf`, `Jarvinen_2025_AA_698_A93_arXiv2504.19670.pdf` e `Olah_2016_AA_590_A133_arXiv1604.06701.pdf`. Os DOIs foram conferidos no Crossref (título, volume e página batem): CLS VI `10.3847/1538-3881/adf2a8`; Järvinen & Strassmeier `10.1051/0004-6361/202554111`; Oláh+2016 `10.1051/0004-6361/201628479`; Noyes+1984 `10.1086/161945`.

Limites do que foi obtido:
- CLS VI veio do site da IOP (acesso aberto, 12 páginas).
- Järvinen & Strassmeier e Oláh vieram do arXiv. **São manuscritos, não a versão publicada**; o site da A&A respondeu 403. O manuscrito de Järvinen traz a data "April 29, 2025" e "accepted 10 April 2025".
- Noyes é o escaneamento do ADS (15 páginas) com camada de texto de OCR. O texto extraído tem glifos trocados (`B—F`, `Kr4`, `5phot`). Os coeficientes de D52 foram vistos no texto, não reverificados na imagem.

Conferido por busca no texto extraído:

| Documento | Passagem encontrada |
|---|---|
| D48 | Järvinen: "78 111 RAVE dwarf stars"; "13 RAVE stars out of 13 326 (0.1%)"; log R_IRT = −4.13, "≈20% below the solar-minimum value"; "such stars are very rare"; "at most ≈0.1%" |
| D49 | CLS VI §3.3: "noncycling stars that may have aged out of their cycles"; §4: "Whether or not stars reach a noncycling level that is inescapable or if they can begin cycling again will require addition observations" |
| D50 | CLS VI §3.3.1: "requires a stochastic process that is poorly understood"; §3.3: "suggestive of a rapid (on stellar timescales) transition"; "can occur quickly, on order of years"; "stochastic mechanism requires a bimodal distribution of S-STDs" |
| D51 | CLS VI §3.2: τ Ceti "is known to have a pole-on inclination (M. Korolik et al. 2023) that precludes us from identifying its chromospheric activity cycle or rotational modulation via S-STD" |
| D52, D53 | Noyes: `1.340`; `log R_phot = −4.898 + 1.918(B−V)² − 2.893(B−V)³ in the range 0.44 < (B−V) < 0.82`; "We have also used the same expression for B−V > 0.82"; Δlog C com 0.135, −0.814, 6.03 e x = 0.63 − (B−V); forma de Duncan `−4.02 − 1.40(B−V)`; "uncertain by as much as 20%"; "The worst discrepancy … occurs for B−V > 1.2" |
| D54 | Noyes, Apêndice *b*: "does not have a large effect for active chromosphere stars, but it can be a very significant correction for the chromospherically less active stars … important to determine the photospheric correction more rigorously than has been done here". CLS VI §5: "neither average activity metrics of S-value, log(R′_HK)-N1984, nor the revised log(R′_HK) metric … More so than these two types of log(R′_HK), the S-value itself best correlates with S-value variability"; §3.1: "the S-value plus the stellar mass is the best metric" |

Nada disso contradiz os documentos. Duas observações novas:
- **CLS VI não cita HD 101501.** D49 só atribui à CLS VI a declaração da lacuna ("can begin cycling again"), o que confere. A identificação de HD 101501 como discriminante é de Baum §4.1, com a ressalva de I-35.
- **Järvinen & Strassmeier:** a lista de alvos do manuscrito inclui HD 101501 (G8 V) numa tabela. Não li o contexto; fica registrado para quem for usar o artigo.

**I-25 atualizado de novo:** nenhum dos sete artigos da segunda rodada está mais ausente de `bib/`. As versões de Järvinen e Oláh são do arXiv; as publicadas continuam sem acesso. `bib/LEIAME.txt` ("Pasta vazia de propósito") deixou de descrever a pasta e não foi editado.
