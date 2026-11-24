# Subsídios para as demais perguntas abertas

**Pedido do pesquisador (2026-11-24):** "Subsídios para as demais perguntas." Cobre Q2, Q3, Q4, Q5, Q6, Q7, Q9, Q10, Q11 e as sub-perguntas de Q1. Já têm subsídios próprios: receita de σ_S (`SUBSIDIOS_RECEITA_SIGMA_S.md`, D70), junção (`SUBSIDIOS_JUNCAO_E_D46.md`, D72), D46 (idem, D73), layout (`SUBSIDIOS_LAYOUT_KIT.md`, D77), anos faltantes (`SUBSIDIOS_INTERPOLACAO.md`, D96). **Nada aqui escolhe ou recomenda.** Fonte de cada fato entre parênteses.

## Sub-perguntas de Q1 (D95)
**a) Regra de binaridade das "cinco `Flat` limpas" (I-06).** D13 sozinha dá **sete** `Flat`/`Flat?` fora das padrões (HD 10700, 23249, 43587, 158614, 178428, 182572, 190360; `3.9-01`); as cinco são 10700, 23249, 43587, 182572 e 190360. A regra que tira HD 158614 e HD 178428 estava num arquivo ausente. *Fatos:* HD 158614 está no v2001 (28 anos distintos, lacunas de 3, 2, 2 e 1 ano; `11_dataverse_v2001_runs.txt`) e HD 178428 não. Alternativas: (i) **cinco**, com a regra a reconstruir e registrar; (ii) **sete**, só com D13; (iii) outra regra explícita (por exemplo, binária resolvida contra não). Cada alternativa muda N de `Flat` em Baum (4 de 5, ou 4 de 7).
**b) D04 e D11 contra medidas já feitas (I-13).** D04: seleção "antes de qualquer dado real"; D11: nenhum σ_S/S por estrela para a amostra. Já foram medidos σ_S/S das quatro `Flat` na CLS V (0.72 / 0.86 / 0.95 / 1.49 %; HD 182572 falha) e o degrau de cada estrela (A9 §1.7). Alternativas: (i) manter D04/D11 e declarar que a seleção foi informada por essas medidas; (ii) registrar uma exceção em nova D##; (iii) refazer a seleção sem usá-las (as medidas existem e foram vistas).
**c) O que a amostra entrega à hipótese de D90.** Só HD 166620 e HD 101501 têm transição ciclo → plano documentada (D49, D50); HD 4915 é contestada (D47). `Flat` e controles dão comparação de nível de variabilidade entre estrelas (não transição). Escolher entre comparar estados entre estrelas e acompanhar a transição em poucas é do pesquisador.

## Q2 — O que conta como `Flat`
*Fatos:* ρ CrB (HD 143761): Tabela 2 de Baliunas = `Long`; Tabela 1, σ_S/S = 1.0 % (dentro da definição `Flat`); Saar a lista como flat/Maunder (A6 §6.2, A1 §1.3; as três afirmações grau A). Baum não tem limiar numérico para `flat` ("no observed variation in activity"; tabela de definições de A9); B95 usa σ_S/S < 1–1.5 %. HD 10700 é `flat?` em B95 e `flat` em Baum (I-04). Piso instrumental e limiar: ver Q6. D51: inclinação como confundidor (Q11).
*Alternativas:* (i) definição de B95 (limiar numérico); (ii) a de Baum (qualitativa, época-dependente, D43); (iii) interseção das duas; (iv) manter `Flat`/`Flat?` como estão e declarar a dependência de definição.

## Q3 — Largura de banda gaussiana
*Fatos:* σ = 1 ano é ~1.8 % do registro de 55 anos; o padrão de Dakos é 10 % (A4-F2; a janela de 25–75 %, `3.11-41`). σ = 1 ano remove o ciclo de 11 anos, que **não** é o detrending monótono para o qual o passo de Dakos foi desenhado; 5.5 anos deixaria a maior parte do ciclo nos resíduos. A11b-F5: ciclos múltiplos e longos são a regra. D21: suavização gaussiana só nas trilhas de AR(1) e variância. D92: a série anual é a do CSD temporal, com 39–49 estações nos grupos, de modo que σ de 1 ano e janela de 50 % (≈ 23 pontos) interagem.
*Alternativas:* (i) varredura de sensibilidade em σ (como D20 faz para a janela), declarada como varredura e não como aplicação de Dakos; (ii) fixar σ por argumento físico (o ciclo de cada estrela é desconhecido para muitas); (iii) remover o ciclo ajustado antes e usar banda de 10 %. Nenhuma foi testada aqui.

## Q4 — A componente de 44 anos
*Fatos:* Saar atribui ao Sol P_cyc(L) = 44 anos; o registro solar de Egeland tem 1966–2016 (50 anos, D65), mais curto que o de 55 anos que A6-F12 usava; a componente é maior que a metade do registro e quase degenerada com tendência monótona, e nem a gaussiana de σ = 1 ano nem a tendência linear a removem (A6-F12). A11b-F5: componentes longas junto do ciclo são o caso típico (Järvinen & Strassmeier §5.5; Oláh+2016 marca tendências `lt` em várias estrelas, A13). D30: a componente entra nas obrigações de Methods.
*Alternativas:* (i) declarar como confundidor e não controlar (A6-F12 diz que controlar "is doubtful"); (ii) ajustar e remover a componente longa antes do τ; (iii) restringir o teste a janelas mais curtas que a componente. A quantidade de dado solar (D65) é menor que o que A6-F12 supunha.

## Q5 — Binárias
*Fatos:* HD 81809: registro composto; o ciclo suave de 8.17 anos pode ser da componente de menor massa (A1-F7); **está no v2001** (35 anos, sequência de 23, lacuna de 1; D85) e ausente de Baum. HD 219834A/B: par resolvido; Saar rejeita o ciclo de A e mantém o de B (A6 §2.3); HD 219834B consta em `baum2022_59stars.csv` e **não tem linhas na Tabela 1 sob esse id**. D13 exclui as estrelas-padrão; a regra de binaridade das `Flat` é a sub-pergunta (a).
*Alternativas:* (i) excluir binárias não resolvidas (HD 81809); (ii) mantê-las com sinalização; (iii) tratar caso a caso (219834A fora, B dentro).

## Q6 — Apresentação do grupo `Flat`
*Fatos:* limiar `Flat` (< 1–1.5 %) está dentro da precisão de longo prazo de B95 (1.4 %, ou 1.2 % sem quatro padrões variáveis) e acima do piso instrumental antigo de 0.8 % (A6-F6/F7/F13, A2-F6); piso moderno decidido em D75 como faixa de 0.37–0.45 % (CLS V); D45: subtração do ruído em quadratura, com 1.2 % para Mount Wilson e 0.3 % para Keck (Luhn); nenhuma `Flat` tem segunda medida na literatura auditada.
*Alternativas:* (i) apresentar o limiar com o piso (0.37–0.45 %) e a precisão de B95 lado a lado; (ii) usar o σ corrigido de D45/D70 (depende da receita); (iii) tratar a `Flat` como "não distinguível do piso" em vez de uma classe.

## Q7 — Subgigantes no `Flat`
*Fatos:* o caderno diz que três das cinco `Flat` limpas são IV/Vp; a checagem `3.9-06` conta **quatro** com 'IV' ou 'Vp' no tipo espectral do catálogo (HD 10700 `G8 Vp`; HD 23249 `K0 IV?`; HD 182572 `G8 IV`; HD 190360 `G6 IV?`; só HD 43587 é `G0 V`; tipos lidos com resíduo de OCR). A contradição (3 contra 4) é de leitura do tipo e não está resolvida. Três fontes: Wright 2004 ("the low-activity flat stars were all subgiants"), Baum §1.3 e §5.5 (A9-F8), Järvinen & Strassmeier §1 e §6, 11 de 13 candidatas eliminadas por serem evoluídas (A11a-F3). A metalicidade cria um artefato de ±14 % em B−V 0.53–0.73 sem correção (A11a-F4); [Fe/H] está em `baum2022_59stars.csv` (Brewer+2016) e na CLS V.
*Alternativas:* (i) excluir subgigantes da `Flat` por construção (reduz N); (ii) mantê-los como subgrupo declarado; (iii) controlar com log g e [Fe/H] como covariáveis. A Q7 do caderno é a dos subgigantes (não a pergunta 7 do protocolo).

## Q9 — DFA no subconjunto Baum
*Fatos:* D92 mantém o DFA fora; só entra pela série bruta se Q9 for decidida a favor. Livina & Lenton: "at least of order a thousand points" e "several hundred points per window" (p. 3; `3.11-56`); 22 de 59 estrelas passam de mil observações brutas, incluindo as quatro `Flat` e os seis controles de Baum (`3.16-01`); a calibração DFA → c é de AR(1) regular de 20 000 pontos, e o próprio artigo diz que pode ser inadequada para dados não lineares (p. 3). A série bruta é irregular, com tripletos noturnos (README, `3.11-76`). A flutuação do expoente cai com √N e não depende do ruído (Peng+1993). D24: piso > 100 pontos (satisfeito só pela série bruta); D25/D26: convenção de α e n_max.
*Alternativas:* (i) manter o DFA fora (D24, D92); (ii) admitir o DFA nas 22 estrelas com ≥ 1 000 observações, com crossover e controle sintético de mesmo comprimento (Peng+1993); (iii) adiar até haver método para a série irregular.

## Q10 — A transição é lenta o bastante para ter precursor detectável?
*Fatos:* CLS VI: transição "on order of years" a partir de uma lacuna de S-STD entre estrelas, não de uma série (D50, `3.11-21`); A10-F2: 8 pontos anuais na aproximação do único caso amostrado, dependentes de dado grau C (D58, D86); A7-F3 e A7b: o CSD pede forçamento lento e muitos tempos de decaimento (δκ ≈ √(2κ/T), Held & Kleinen p. 3), e o tempo de decaimento estelar **não é conhecido**; Boulton: sem equilíbrio os sinais "should not work as well"; A8: o Sol atual não aproxima um grande mínimo. D90 trata a questão como hipótese a testar. Se a resposta for não, a tese não é testável com os dados existentes (§5 do caderno).
*Alternativas:* (i) tratar como parte da hipótese (a falsificação é o resultado); (ii) estimar o tempo de decaimento das séries cíclicas (AR(1) da série anual, sob a regra de anos faltantes) como etapa preliminar; (iii) declarar como limitação e restringir a conclusão à comparação de estados.

## Q11 — Inclinação e o grupo `Flat`
*Fatos (A14):* τ Ceti (HD 10700) tem inclinação 7° ± 7° (Korolik 2023, resumo e Tabela 3), v sin i = 0.1 ± 0.1 km/s, P_rot indeterminado (46 ± 4, 32 ± 9, 43 ± 7 e 23 dias); a ligação "inclinação → ciclo não identificável" é da CLS VI, não de Korolik; a inclinação das outras `Flat` não está em nenhuma fonte auditada (grau X). HD 10700 é uma das `Flat` limpas e a estrela-padrão de dispersão (D51).
*Alternativas:* (i) declarar o confundidor para HD 10700 e deixar as demais como X; (ii) coletar v sin i e P_rot das demais em fontes já auditadas (Baum, CLS V, Saar & Osten) e estimar inclinação só como subsídio, sem medir (regra 8); (iii) excluir HD 10700 do `Flat`.

## O que depende do quê
Q1 (sub-perguntas a e b) → N de cada grupo; Q9 → papel do DFA em D92; Q10 → enunciado da hipótese de D90; Q3 e a regra de anos faltantes → configuração do indicador; Q2, Q5, Q7 e Q11 → quais estrelas entram em `Flat`.

Estado: **subsídios entregues; todas as perguntas acima seguem abertas (D97).**
