# PAPER_STATE — P1 (visão geral do paper; versão 6, 2026-10-21)

## Status
E0-E10 concluídas e aprovadas. Manuscrito completo em manuscrito/ (6 páginas, 21 referências, todas as seções aprovadas). E10 (portão de submissão) concluída, ver DEC-44 e DEC-45. Submissão depende de pendências do usuário. Manuscrito com 7 páginas após as seções finais. Mensagem do manuscrito aprovada. Notebook, figuras (4), macros (187) e analysis_results.md em repositorio/, executados com dados reais. Análise principal em energia escalada pela luminosidade (CR-01). Revista: EPL (DEC-19, DEC-22). Política de IA da EPL decidida só antes da submissão. Estilo do manuscrito: sem ponto e vírgula e sem travessões na prosa (DEC-21, DEC-31). Resultados numéricos existem mas dependem de decisões de apresentação (ver Riscos).

## Pergunta central
O expoente alpha da distribuição de energia de flares estelares, dN/dE ~ E^-alpha, é o mesmo para estrelas M, K e G? Se for, isso sugere um mecanismo comum; sua magnitude (~2) confronta o valor de criticalidade auto-organizada (SOC) 3/2 (Aschwanden 2016, 2014).

## Hipóteses
- H0: alpha_M = alpha_K = alpha_G (expoente comum).
- H1: os alphas diferem entre classes.
- Comparações: alpha vs 3/2 (FD-SOC), vs Yang & Liu 2019 (OLS: G 1,96; K 1,78; M 2,13), vs Okamoto 2021 (G).

## Dados (DEC-10: o notebook baixa do VizieR por código)
- Flares: Yang & Liu 2019, J/ApJS/241/29, table2 (162.262 flares, logE) e table1 (3420 estrelas); erratum 2020 só altera L_flare/L_bol.
- Parâmetros estelares: Mathur+2017, J/ApJS/229/30 (Teff, log g, raio; DEC-17); corte de anãs; teste com e sem corte.
- Classes: M (Teff < 3850 K), K (3850 a 5300 K), G (5300 a 5900 K) por Pecaut & Mamajek 2013, sensibilidade com Yang e ±200 K. F (5900 a 7200 K) como extensão secundária, fora do teste principal (DEC-28).
- Filtro de anãs: log g >= 4,0 e raio <= 1,5 vezes a mediana por intervalo de Teff de 200 K, com variantes. Estrelas não classificadas do Mathur são excluídas (DEC-29).

## Método (especificado na E6)
MLE contínuo com xmin por KS (Clauset 2009), powerlaw (Alstott 2014), modelo truncado (tamanho finito), bootstrap, aderência semi-paramétrica (p>0,1), razão de verossimilhanças contra lognormal e lei de potência com corte, teste aninhado de igualdade do alpha entre classes, sensibilidade a xmin, fronteiras, filtro de anãs e erro de energia (~0,2 dex).

## Estrutura do manuscrito (EPL: máx. 7 páginas A4 em 2 colunas, tudo incluído)
| Parte | Páginas (orçamento) | Conteúdo |
|---|---|---|
| Título + resumo (120-160 palavras) | 0,4 | pergunta, dados, método, resultado, implicação |
| Introdução | 0,8 | SOC e flares solares (Lu & Hamilton; Crosby), flares estelares no Kepler, lacuna: teste estatístico formal de igualdade entre classes |
| Dados e métodos | 1,5 | Yang & Liu, Mathur, seleção de anãs, classes, MLE+KS+truncamento+bootstrap, teste de igualdade |
| Resultados | 2,0 | Tabela 1 (N, xmin, alpha, erro, p de aderência, modelo preferido); Figs. 1-3; sensibilidades |
| Discussão | 1,3 | alpha vs 3/2 e causas (Aschwanden; Bonachela), comparação com Yang e Okamoto, limitações (sem injeção, energia ~60%) |
| Conclusões | 0,3 | 3-4 pontos |
| Referências | 0,7 | ~25-30 numeradas (ISO 690, eplbib) |
Capacidade medida do layout da OUP (opção large, duas colunas): cerca de 850 palavras por página, ou 5000 a 5500 palavras em 7 páginas incluindo figuras, tabelas e referências (orçamento aproximado, a contagem oficial é a da EPL).
Figuras (Super Mongo, sem grade, Courier Prime; EPS; 80 mm ou 165 mm): Fig. 1 CCDF por classe com ajustes e xmin; Fig. 2 alpha por classe com variantes de sensibilidade, linha em 3/2 e valores do Yang; Fig. 3 distribuições bootstrap das diferenças de alpha / estatística do teste de igualdade.

## Saídas do notebook (inglês, DEC-29)
analysis_results.md e results_macros.tex (132 macros, um por número do manuscrito). Figuras em EPS e PDF, Courier Prime, sem grade, 80 ou 165 mm (figure1 distribuição complementar com ajustes de corte, figure2 índices por classe, figure3 distribuições bootstrap).

## Resultados da execução completa (a validar com o usuário)
Variável principal E_L = E / (L / L_sol), limite inferior log E_L = 34,5. Índice do modelo de corte (bootstrap por estrela): M 2,01±0,03, K 1,93±0,11, G 1,95±0,06, F 2,27±0,21. Igualdade M, K, G: p = 0,63 (H0 não rejeitada), mas 4 de 27 variantes rejeitam (limites de classe do Yang e menos 200 K, janela 34,3 a 35,3, energia de G vezes 1,25), então o veredito não é robusto pela regra adotada. A janela truncada e a lei de potência pura rejeitam a igualdade (p = 0,001). 3/2 rejeitado nas três classes. Heterogeneidade forte entre estrelas (dispersão de 0,2 a 0,5). A reprodução do Yang diverge (K 1,61 contra 1,78, G 1,73 contra 1,96). O ajuste de corte tem aderência rejeitada com KS D de 0,02 a 0,03.

E8 (faixas de Teff, 12 faixas de cerca de 239 estrelas): o índice de corte varia de 1,65±0,05 (4539 K) a 2,54±0,14 (6021 K). A igualdade entre as faixas é rejeitada em todas as 12 variantes (estatística 75,7, p = 0,001), ao contrário do teste por classes da E7c, que tinha pouco poder. A tendência linear (menos 0,061±0,024 por 1000 K) não é robusta (10 de 12 variantes significativas, muda com o limite inferior) e a janela truncada tem inclinação compatível com zero. Um degrau por classe descreve a maior parte da estrutura mas não toda (χ² 21,5 com 7 graus de liberdade). O pico da distribuição de E_L não depende de Teff. A rotação cai com Teff (mediana de 8,7 d a 2,7 d) e confunde qualquer tendência.

## Riscos
- Resultados podem reproduzir 'alpha ~ 2' (contribuição de robustez metodológica).
- Sem completude por flare no Yang (LC perde ~60% dos flares da cadência curta, Yang 2018).
- Política de IA da EPL (DEC-20) pendente.
- Mistura de rotação entre classes pode simular diferença de α (análise fora do P1).
- Veredito por classes não robusto às definições de classe e à janela. A E8 mostra variação de α com Teff entre faixas, sem tendência linear robusta.
- Rotação confunde a dependência com Teff (mediana de Prot de 8,7 d a 2,7 d) e não é analisada (BACKLOG P9).
- L_bol em vez de L_Kp e incerteza de 27% no raio entram em E_L.
- Contaminação por pulsadores em F (extensão apenas).

## Títulos candidatos (EPL: só a primeira palavra em maiúscula)
1. Is the power-law index of stellar flare energies universal across spectral types?
2. A formal test of universality in the flare energy distribution of Kepler stars
3. Stellar flare energy distributions are steeper than self-organized criticality predicts

## Mensagem do manuscrito (rascunho 1, 2026-10-20, aprovada pelo usuário no DEC-40)

### Mensagem central

Em português: os flares de anãs M, K e G observadas pelo Kepler têm cauda com índice próximo de 2, acima do valor 3/2 da criticalidade auto-organizada, mas o índice não é universal no sentido estrito. Ele varia com a temperatura efetiva, entre cerca de 1,65 e 2,5, e as diferenças superam os erros estatísticos.

Em inglês, para o resumo e a conclusão: Flare energy distributions of Kepler M, K and G dwarfs have a tail index near 2, steeper than the value 3/2 expected from self-organized criticality. The index is not strictly universal, because it changes with effective temperature by more than the statistical errors.

Título decidido no DEC-40: Is the power-law index of stellar flare energies universal across spectral types? (título 1 da lista abaixo, a reavaliar no E10).

### Como a E7c e a E8 se combinam

A E7c compara três classes e a E8 compara 12 faixas de Teff. Elas não se contradizem. Os testes por classes têm pouco poder, porque o ajuste de corte tem erro grande nas classes largas (K, 0,11) e a média dentro de cada classe esconde a variação. Por faixas, o erro do índice fica entre 0,04 e 0,06 nas faixas de M e K (até 4960 K) e a variação aparece. Por isso o manuscrito apresenta o resultado por classes como inconclusivo e o resultado por faixas como a evidência principal contra a universalidade estrita. A regra de robustez é a mesma nos dois: o veredito vale se não muda nas variantes.

### Afirmações principais e sua base

1. A completude depende da luminosidade da estrela, e por isso as energias em erg não são comparáveis entre classes. O pico da distribuição de energia vai de 32,7 (M) a 34,3 (F) em log E, uma dispersão de 1,6 dex, e fica entre 34,1 e 34,3 em log E_L (0,2 dex). Em erg, o índice depende do limite inferior de forma drástica, de 0,5 a 2,1 conforme a classe e o limite (variantes S1 do analysis_results.md, seção 10). Base: seções 7 e 10 do analysis_results.md, davenport2016 p5 para E = ED x L_Kp. Os valores dos picos não têm macro próprio e precisam de um antes da escrita do texto.
2. Em E_L, o índice de corte é de 2,01±0,03 em M, 1,93±0,11 em K e 1,95±0,06 em G (macros AlphaCutM, AlphaCutK, AlphaCutG com os erros AlphaCutErr). A igualdade entre as três classes não é rejeitada (p = 0,63), mas o veredito muda em 4 de 27 variantes e deve ser dado como inconclusivo. O valor 3/2 fica fora do intervalo de 99 por cento nas três classes (macro RejectThreeHalves).
3. Entre 12 faixas de Teff a igualdade é rejeitada, com estatística 75,7 para 10 graus de liberdade (p = 0,001, o piso do bootstrap), e a rejeição vale nas 12 variantes (macros PEqualBandsCut, BandsVariantsChanged). O índice varia de 1,65±0,05 (4539 K) a 2,54±0,14 (6021 K). Não há tendência linear robusta: a inclinação de menos 0,061±0,024 por 1000 K não é significativa com limites inferiores mais altos e a janela truncada dá mais 0,021±0,018 (macros SlopeBandsCut, SlopeBandsWin, BandsSlopeRobust). Um valor por classe descreve a maior parte da estrutura (qui-quadrado 21,5 contra 75,7 da constante) mas não toda.
4. Metodologia que pesa nos resultados: um teste de Wald que trata os flares como independentes rejeita a hipótese nula verdadeira em 19 por cento dos casos com nível nominal de 5 por cento em dados simulados com estrelas heterogêneas, e o bootstrap por estrela mantém o tamanho em 5 por cento (seção de validação). Os flares da mesma estrela são correlacionados, com efeito de desenho de 2,1 a 3,0 no erro padrão. O índice também varia entre estrelas de uma mesma classe, com dispersão de 0,22 a 0,47 em M, K e G.

### O que o manuscrito não afirma

* Que o índice pertença a uma classe de universalidade de modelos de sandpile. Os expoentes do BTW em 2D não são conhecidos analiticamente e a interpretação é controversa (lubeck2004 p113).
* Que a lei de potência com corte descreva bem os dados. O teste KS a rejeita nas quatro classes, com distância de 0,02 a 0,03, e o teste trata flares como independentes.
* Que o índice cresça ou decresça de forma monótona com Teff, nem que haja um mínimo entre 4500 e 4900 K. O vale depende da janela e some com o limite inferior mais alto.
* Que a dependência com Teff seja física. A rotação cai com Teff (mediana do período de cerca de 9 a 11 d nas anãs M para 2,7 d na faixa mais quente) e não é analisada, e a luminosidade usada em E_L é bolométrica, não a da banda Kepler, com incerteza de 27 por cento no raio.
* Que os valores do Yang e Liu sejam reproduzidos. Com a mesma amostra (contagens iguais), o mesmo método e as mesmas faixas obtemos 1,61 em K e 1,73 em G contra 1,78 e 1,96 publicados, e a diferença não depende do bin, do limiar de contagens nem dos pesos.
* Que os valores p estejam corrigidos entre análises. Cada teste foi feito sem essa correção.

### Estrutura narrativa e figuras

Introdução: SOC e flares solares (Lu e Hamilton, Crosby), flares estelares no Kepler, a pergunta de universalidade e a lacuna, que é um teste formal com dados por flare. Dados e métodos: Yang e Liu, Mathur, filtro de anãs, escalonamento por luminosidade, ajuste de corte, bootstrap por estrela, teste de igualdade. Resultados em três passos: (1) completude e escalonamento, (2) classes, (3) faixas de Teff. Discussão: 3/2, causas possíveis do excesso (Aschwanden 2016 p83 e Bonachela 2009), limites, ausência de injeção.

Figuras no limite de 7 páginas: figura 1 (distribuições em E_L com os ajustes) e figura 4 (índice por faixa de Teff) são as essenciais. A figura 2 (índices por classe e variantes) e a 3 (distribuições bootstrap) competem por espaço e a escolha fica para o E9.

### Uma ressalva de honestidade a manter

A mensagem depende de três escolhas de análise que o leitor pode questionar: o escalonamento por L_bol, o limite inferior comum de 34,5 e o modelo de corte como principal. Os resultados por faixas valem com limites inferiores de 34,6 e 34,8 e relativos ao pico, e o resultado por classes é descrito como inconclusivo justamente porque depende da janela. O manuscrito deve dizer isso no corpo, e não só no material suplementar.

## Plano de redação do E9b (executado e aprovado em 2026-10-21, ver DEC-43)

Língua: inglês, ortografia britânica consistente, sem travessões nem ponto e vírgula na prosa, números só por macros de results_macros.tex, citações numéricas entre colchetes. Cada seção passa pela skill de humanização, por scripts/check_manuscript.py e pela conferência dos fatos contra o caderno com página. Aprovação do usuário por seção, no máximo 2 rodadas por item.

### Orçamento (capacidade medida de cerca de 850 palavras por página no layout da OUP, 7 páginas)

| Parte | Páginas | Palavras de texto | Conteúdo |
|---|---|---|---|
| Título, autores, resumo | 0,4 | 150 no resumo | pergunta, dados, método, resultado, implicação |
| Introdução | 0,8 | 650 | SOC e flares solares, flares estelares no Kepler, a pergunta e a lacuna |
| Dados e métodos | 1,5 | 1200 | amostra, classes, energia escalada, ajuste de corte, bootstrap por estrela, testes |
| Resultados | 2,0 | 950 mais figuras e tabela | completude, classes, faixas de Teff |
| Discussão | 1,3 | 1050 | 3/2 e causas, comparação com a literatura, limites |
| Conclusões | 0,3 | 250 | 3 a 4 pontos |
| Referências | 0,7 | cerca de 28 entradas | |
Total de texto cerca de 4250 palavras, com cerca de 1,5 página para figuras e a tabela.

### Ordem de redação

1. Dados e métodos, que fixa as definições e os macros usados depois.
2. Resultados, seguindo os três passos da mensagem (completude e escalonamento, classes, faixas de Teff).
3. Discussão e Conclusões.
4. Introdução, escrita sabendo o que o artigo mostra.
5. Resumo, por último.

### Conteúdo e base de cada seção

* Introdução: SOC com watkins2016 p20 a p28 (fenótipo, evidência difícil, BTW não resolvido), flares solares com lu1991 p1 e crosby1993 p282 (índices de raios X duros), previsão 3/2 de aschwanden2014 p8 e aschwanden2016 p18, flares no Kepler com davenport2016, shibayama2013, maehara2012, okamoto2021, hawley2014 e yang2019 (α próximo de 2 em G, K e M, com α dependente da faixa de energia, yang2019 p8), a lacuna: nenhum teste formal de igualdade por dados de flare com completude tratada.
* Dados e métodos: yang2019 (catálogo, p3 a p5), mathur2017 (parâmetros, p1 e p7), pecaut2013 p9 (limites de classe), notsu2019 p27 e berger2018 p1 (subgigantes), clauset2009 p5 a p20 e alstott2014 (estimadores), isobe1990 p106 (bissetriz, só para comparar com o Yang). Energia escalada pela luminosidade com davenport2016 p5. Bootstrap por estrela e teste de igualdade, descritos como procedimentos próprios.
* Resultados: macros de PeakE e PeakEL, AlphaCut, PEqualCut, RejectThreeHalves, PEqualBandsCut, SlopeBandsCut, PeakSlope e os demais, e as figuras 1 e 4, com a 2 ou a 3 se couberem.
* Discussão: o excesso acima de 3/2 (aschwanden2016 p82 e p83, aschwanden2015 p13, bonachela2009 p1, lubeck2004 p113), por que classes e faixas diferem em poder, a divergência com o Yang e Liu dita como não explicada, e as limitações listadas em 'O que o manuscrito não afirma'.
* Software: harris2020, virtanen2020, astropy2018, ginsburg2019 (astroquery) e hunter2007, em uma frase.

### Referências (cerca de 28)

SOC e flares solares: watkins2016, lu1991, crosby1993, aschwanden2014, aschwanden2016, aschwanden2015, bonachela2009, lubeck2004. Dados e estrelas: koch2010, mathur2017, pecaut2013, berger2018, notsu2019, yang2018. Catálogos e distribuições de flares: davenport2016, yang2019, yang2020erratum, shibayama2013, maehara2012, okamoto2021, hawley2014, wu2015. Métodos: clauset2009, alstott2014, isobe1990. Software: harris2020, virtanen2020, astropy2018, ginsburg2019, hunter2007. Ficam de fora, salvo necessidade: dickman2000, tu2020, gunther2020, vandoorsselaere2017, balona2015, covey2007.

### Decisões que o plano pede ao usuário

Autores e afiliação, quais figuras entram nas 7 páginas (a 1 e a 4 são as essenciais), se o erratum do Yang e Liu entra como referência, e a conferência dos requisitos atuais da EPL na página da OUP (bloqueada a robôs).

