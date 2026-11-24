# Recomendação: tamanho mínimo de segmento para o CSD em janelas anuais

**Pedido do pesquisador (2026-11-24):** "Sugira uma recomendação para o tamanho mínimo de segmento. Que seja defensável quantitativamente e qualitativamente." Esta é uma **recomendação de Claude, não uma decisão**; fica registrada como tal (D99) e só vale depois do aceite do pesquisador. Números de `inspecao/saidas/16_min_segment.txt` (`3.18-01` a `3.18-06`; script `16_min_segment.py`; AR(1) sintético, sem valores de S, sementes fixas).

## 1. Recomendação
1. **Piso para calcular o indicador: segmento de pelo menos 24 anos (após a regra de D98), com janela de 50 % de pelo menos 12 pontos** (D20) e pelo menos 13 janelas.
2. **Segmentos com menos de 24 anos não recebem o indicador temporal**: ficam só descritos (série e σ por estado), sem τ de Kendall.
3. **Rótulo de precisão:** 24–39 anos = "precisão baixa"; **≥ 40 anos = "precisão adequada"** (SD do AR(1) ≤ 0.2 para c ≈ 0.5). Resultados em segmentos de precisão baixa são **exploratórios** no texto.
4. **Calibração por surrogates:** em todo segmento, o p do τ vem da distribuição nula dos surrogates ARMA com as mesmas posições de lacuna e interpolação (D22, D98), nunca de um limiar fixo de τ.
5. **Declarar em Methods** que, mesmo no melhor caso, o teste em série anual tem poder baixo (§2.2), de modo que um resultado nulo não refuta a hipótese de D90.

## 2. Base quantitativa
### 2.1 Precisão do AR(1) por tamanho de janela (4000 simulações; `16_min_segment.txt` §1)
| Janela w (pontos) | SD da estimativa (c = 0.5) | Fórmula de Held & Kleinen √((1−c²)/w) | viés (c = 0.5) |
|---|---|---|---|
| 8 | 0.295 | 0.306 | −0.37 |
| 10 | 0.268 | 0.274 | −0.30 |
| **12** | **0.249** | **0.250** | −0.25 |
| 20 | 0.198 | 0.194 | −0.15 |
| 24 | 0.184 | 0.177 | −0.12 |
| 40 | 0.146 | 0.137 | −0.07 |
A fórmula do artigo (δc² ∝ (1−c²)Δt/T, Held & Kleinen p. 3) **reproduz** a simulação (diferença ≤ 0.01 para c = 0.5). Com w = 12, o desvio-padrão da estimativa é 0.25, **dois terços** do efeito de uma tendência de c de 0.3 a 0.7 (Δc = 0.4); com w = 20 cai para 0.20 (metade do efeito). O viés negativo de amostra finita (−0.25 em w = 12) é grande, mas é comum a todas as janelas de mesmo tamanho e afeta pouco o τ, que usa a ordem.

### 2.2 Poder do τ de Kendall em função do segmento (600 simulações; janela de 50 %)
| Segmento L (anos) | janela | nº de janelas | AUC (tendência > nulo) | SD do τ nulo |
|---|---|---|---|---|
| 10 | 5 | 6 | 0.52 | 0.44 |
| 20 | 10 | 11 | 0.57 | 0.47 |
| **24** | **12** | **13** | **0.59** | 0.46 |
| 30 | 15 | 16 | 0.60 | 0.46 |
| 40 | 20 | 21 | 0.63 | 0.47 |
| 50 | 25 | 26 | 0.67 | 0.47 |
**Não há joelho na curva**: o poder cresce devagar com L e **nunca é bom** (AUC máxima 0.67 em 50 anos; 0.5 é acaso). A causa é que as janelas se sobrepõem (o τ nulo tem SD ≈ 0.45 mesmo com 26 janelas). Por isso o piso **não pode ser escolhido para "garantir poder"**: nenhum L ≤ 54 garante. Ele é escolhido como o ponto abaixo do qual a precisão do AR(1) e o número de janelas tornam o indicador **indistinguível do acaso** (L = 10: AUC 0.52; L = 20: 0.57), e acima do qual os ganhos são marginais.

### 2.3 O que o piso deixa de pé nas 10 estrelas (`3.18-01` a `3.18-04`; segmentos em `16_min_segment.txt` §3)
| Piso | Segmentos que passam | Estrelas com pelo menos um |
|---|---|---|
| ≥ 12 anos | 14 | 10/10 |
| ≥ 20 anos | 12 | 10/10 |
| **≥ 24 anos** | **10** | **10/10** |
| ≥ 30 anos | 7 | 7/10 |
| ≥ 40 anos | 4 | 4/10 |
Segmentos (anos) por estrela com D98: HD 10700 [29, 20]; 23249 [54]; 182572 [45, 5]; 190360 [54]; 10476 [54]; 152391 [36, 11]; 166620 [32, 17]; 26965 [29, 20]; 4628 [30, 14]; 101501 [28, 9]. Com o piso de 24 anos **toda estrela mantém um segmento** e perde-se só o que é curto demais (5, 9, 11, 14, 17 e 20 anos). Um piso de 30 anos já tira três estrelas; um de 40, seis.

## 3. Base qualitativa
| Argumento | Fonte |
|---|---|
| Janela de 25–75 % do registro (D20) | Dakos et al. 2012, p. 17 (`3.11-41`) |
| Janela de ACF de 10 % da série em outro método, que supõe séries com milhares de pontos | Livina & Lenton p. 2 (`3.11-55`, `3.11-56`) |
| O erro de κ cai com a raiz do comprimento e é preciso muitos tempos de decaimento (δκ ≈ √(2κ/T)); o tempo de decaimento estelar é desconhecido | Held & Kleinen p. 3 (`3.11-53`); A7b-F2 |
| "the detection of increased autocorrelation may require long time series"; resultados dependem da filtragem e da janela | Scheffer et al. 2009 pp. 5–6 (A7 itens 11–12) |
| A incerteza do expoente cai com √N independentemente do ruído; é preciso comparar com controle sintético de mesmo comprimento | Peng+1993 pp. 2–4 (`3.11-59`, `3.11-60`) |
| Dado perdido: segmentos separados, e não interpolação longa, evitam o viés de suavização | Liu et al. pp. 7–8; Rehfeld+2011 (`3.11-78`, `3.11-79`); D98 |
**Leitura qualitativa:** as fontes não dão um número de pontos; todas dizem que séries curtas e janelas curtas são o ponto fraco do CSD. Um piso de 24 anos com janela de 12 pontos não é uma regra delas, e sim a menor janela cuja precisão (SD 0.25) fica na faixa da fórmula publicada e do efeito que se quer ver; por isso o piso é acompanhado do rótulo de precisão e da calibração por surrogates, que é o que a literatura exige (Scheffer, Dakos).

## 4. Limites da recomendação
- A simulação é de AR(1) estacionário, sem ciclo, ruído de medida nem remoção de tendência (D21); em dados reais o poder é, no mínimo, igual ou pior.
- O critério "SD ≤ metade do efeito" levaria a segmentos de ≥ 40 anos (4 de 10 estrelas); o piso de 24 anos é um compromisso entre precisão e cobertura, declarado.
- O número 24 vem da combinação (w = 12 por 50 % do segmento) e do corte natural nos dados (todo o conjunto mantém um segmento até 24 anos e perde três estrelas em 30); outro corte entre 20 e 24 daria o mesmo conjunto de estrelas.

## 5. Alternativas (para o pesquisador)
| Alternativa | Efeito |
|---|---|
| **Recomendada: piso de 24 anos, rótulo de precisão, surrogates** | 10 segmentos, 10 estrelas; resultados de 24–39 anos exploratórios |
| Piso de 20 anos | 12 segmentos, 10 estrelas; janela de 10 pontos (SD 0.27, AUC 0.57) |
| Piso de 40 anos | 4 segmentos, 4 estrelas (HD 23249, 190360, 10476, 182572); precisão adequada, cobertura pequena |
| Sem piso, só surrogates | todos os segmentos, incluindo os de 5 a 11 anos, onde o indicador é indistinguível do acaso |

Estado: **recomendação entregue; tamanho mínimo de segmento pendente do aceite do pesquisador (D99).**
