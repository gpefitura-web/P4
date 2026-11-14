# MAPA_PIPELINE — `p4_pipeline.ipynb` contra as decisões ativas

Leitura estática, sem executar e sem alterar o notebook. As células são numeradas pelo índice de `nb['cells']` (começa em 0); `célula:linha` remete à listagem `inspecao/saidas/04_pipeline_cells.txt`, gerada por `scripts/04_dump_notebook.py`. As checagens automáticas citadas (`4-xx`) estão em `checks.csv`.

## 1. Estado do arquivo

| Fato | Evidência |
|---|---|
| 29 células (13 de código). Só as células 2, 4, 6, 8 e 10 têm contagem de execução | `4-19` |
| A última execução parou na célula 10 com `FileNotFoundError: data/nso_solar_sindex.txt`. As células 12 a 27 não têm saída guardada | `10:ERR` |
| Nenhum resultado numérico está gravado no notebook e a pasta `results/` não existe no pacote. Nada do notebook pode ser citado como resultado | inventário |
| `USE_SYNTHETIC = False` | `4:004` |
| O notebook não lê nenhum arquivo de `data/` nem os CSVs do pacote. O catálogo está digitado na célula 8 e as séries estelares viriam do VizieR `J/ApJ/438/269` | `8:002`, `12:054` |
| O catálogo embutido é uma versão intermediária: já incorpora A1 (HD 4915 fora, HD 166620 como cíclica, HD 190406 fora) mas não A6 nem a segunda rodada | `8:003–025` |

## 2. O que contradiz uma decisão ativa

Gravidade no sentido do relatório: BLOQUEANTE = produziria um número inadmissível no manuscrito; IMPORTANTE = precisa mudar na reconstrução; MENOR = texto ou comentário.

| # | Decisão | Onde | O que o código faz | O que a decisão exige | Gravidade |
|---|---|---|---|---|---|
| P-01 | **D22** | `14:092–099` (`kendall_tau`), usado em `16:036–037`, `16:049`, `23:024`, `23:038`, `27:029–037` | p-valor de `stats.kendalltau` para a tendência de φ₁ e de σ² em janela deslizante | 1 000 surrogates ARMA(p,q) escolhidos por AIC, ajustados aos resíduos, p = P(τ\* ≤ τ), sobre toda a grade largura de banda × janela | BLOQUEANTE |
| P-02 | **D22** | notebook inteiro | não há nenhum código de ARMA nem de surrogates (`4-09`: nenhuma célula) | idem | BLOQUEANTE |
| P-03 | **D23** | `16:035` | τ só sobre os resíduos (`s_resid`). O τ da série original não é calculado nem reportado | τ reportado na série original e nos resíduos, inclusive o negativo | IMPORTANTE |
| P-04 | **D21** | `16:027–028`, reportado em `27:019` | `dfa_hurst(s_resid)`: DFA aplicada aos resíduos do filtro gaussiano ("H of residuals") | suavização gaussiana nunca antes de DFA | IMPORTANTE |
| P-05 | **D21** / A4 §1.2 | `16:004–017` | DFA sobre a série inteira e por década, com detrend linear da série toda antes | detrending polinomial dentro de cada janela deslizante (janela = metade do registro) | IMPORTANTE |
| P-06 | **D26** | `14:027` | `n_min, n_max = 4, max(8, N // 4)`; docstring `14:013–014` justifica N/4 | n_max reduzido; faixa de ajuste, número de escalas e número de caixas reportados com cada α | BLOQUEANTE para qualquer α |
| P-07 | **D26** | `14:049` | uma única regressão em log-log sobre todas as escalas; nenhuma checagem de crossover (`4-11`: nenhuma célula) | checagem de crossover obrigatória; α ajustado dentro de um único regime | BLOQUEANTE para qualquer α |
| P-08 | **D25** | `14:010`, `14:054–066`, `14:128–129`, `16:005–030`, `27:017–019` | α é chamado de "H" e de "Hurst exponent" em docstrings, variáveis, impressões e relatório | α na convenção crua de Peng, com a convenção explicitada | IMPORTANTE |
| P-09 | **D28** | `14:114` (docstring), `16:058`, `16:060`, `27:041–042` | calcula e reporta `H = (beta+1)/2` | relação abandonada, salvo nova fonte | IMPORTANTE |
| P-10 | **D29** | `4:031–036`, `14:130–132`; menções em `0:024–025` e `2:003–008` | `nolds` é importado se existir e usado como checagem cruzada opcional | "o pipeline não o usa"; sai da lista de referências | MENOR |
| P-11 | **D20** | `16:034` | cinco tamanhos de janela: 25, 40, 50, 60, 75 % | 50 % como padrão e sensibilidade sobre 25–75 %. Os extremos estão certos; a grade tem cinco pontos e não é cruzada com a largura de banda (D22) | IMPORTANTE |
| P-12 | **D20** | `16:045–053` | subjanela 2000–2012 escolhida à mão, com janela de 50 % dentro dela; é o "resultado-chave 1" do relatório (`27:067–070`) | nenhuma decisão registra essa subjanela. É a origem do "p < 0.0001" que D22 manda substituir | IMPORTANTE |
| P-13 | **D20** | `18:004–010` | o lado estelar não usa janela deslizante: φ₁ e variância da série inteira, depois Mann-Whitney entre grupos (`20:001–018`) | D20–D23 descrevem tendência em janela. O teste entre grupos de `20:014` é o desenho de `paper_state_v2`, que o caderno §8 registra como "não é evidência de CSD" | IMPORTANTE |
| P-14 | **Q3** (aberta) | `14:101–108`, `16:025`, `23:013` | largura de banda fixa `sigma_yr=1.0`, em anos; sem varredura | A4 decisão 8: declarar como percentual do comprimento e varrer pelo menos 0.5–20 %. A escolha continua aberta (Q3) | IMPORTANTE |
| P-15 | **D01** | `8:002–022` | catálogo digitado no código (14 estrelas) | catálogo reconstruído das fontes; o congelado é `baliunas_table2_full.csv`, que o notebook não lê | IMPORTANTE |
| P-16 | **D09** | `7:007`, `8:014–016` | grupo "Irregular" é definido no texto como `Long` ou `Var`, mas contém HD 3651 (`CYCLE`, 13.8 ± 0.4, Good) e HD 76151 (`CYCLE`, 2.52 ± 0.02, Fair); só HD 9562 é `Long` (`4-04`) | membership pela classe primária da Tabela 2 | IMPORTANTE |
| P-17 | **D09** | `8:014` | HD 3651 com `P_cyc = 0.00`; o catálogo dá 13.8 (`4-06`) | idem | IMPORTANTE |
| P-18 | **D13** | `8:019`, `8:015` | HD 45067 no grupo "Flat" e HD 9562 no "Irregular": ambas são estrelas-padrão (A6 §3) | padrões excluídos da amostra | IMPORTANTE |
| P-19 | **Q5** (aberta) | `8:005`, `8:009`, `8:020` | HD 81809 e HD 178428 (lista de binárias do Apêndice B, A1 §2.5) entram sem marca; HD 219834B é indexada como `219834`, sem distinguir A de B | binárias registradas e decididas na consolidação | IMPORTANTE |
| P-20 | A1-F1 | `7:010–012`, `8:004–021` (coluna `S_std`) | `S_std_ref` estimado dos painéis da Figura 1 | valor de figura é grau C. O notebook diz que só parametriza o gerador sintético; com isso todo resultado sintético herda grau C | MENOR |
| P-21 | **D17** / A3-F2 | `4:025–026` (comentário) | "Baliunas et al. 1995 quoted 0.179 using the HKP-1 calibration, which carries a systematic +0.007 offset (Egeland+2017 Sec. 6)" | D17: 0.179 vem de transformação-proxy não publicada, alto 5 % na média e inflado ~76 % na amplitude. 0.179 − 0.1694 = 0.0096, não 0.007 | MENOR (comentário) |
| P-22 | **D18** | `10:052–067` | espera `data/nso_solar_sindex.txt` em duas colunas; a instrução impressa manda buscar "Table 1 (composite daily S-index)" de Egeland | D18 e A3-F5: a série calibrada é a **Tabela 4** de Egeland | IMPORTANTE |
| P-23 | **D30** / Q4 | `16:023–043` | nenhum tratamento nem menção da componente de 44 anos | obrigação de Methods: dizer se pode ser tratada num registro de 55 anos | IMPORTANTE |
| P-24 | **D08** | `12:098–118` | no caminho real, usa a série que o VizieR devolver, sem média anual, e substitui `S_mean_ref` pela média medida | ⟨S⟩ é a média anual sobre todos os anos da Tabela 2 | IMPORTANTE |
| P-25 | A1 §1.6 | `12:050–058`, `12:077–096` | pressupõe que `J/ApJ/438/269` tenha uma tabela de séries temporais | A1 §1.6: o artigo não tabula as séries (só a Figura 1). A existência dessa tabela no VizieR não foi verificada em nenhum arquivo do pacote (grau X) | IMPORTANTE |
| P-26 | protocolo §1 | `12:119–122` | se o VizieR falhar, cai em dados sintéticos sem interromper; só o rótulo `STAR_SOURCE` muda | o protocolo exige cadeia de proveniência; um fallback silencioso mistura real com sintético no mesmo relatório | IMPORTANTE |
| P-27 | D22 (expectativa) | `10:016–019`, `10:038–040`, `12:008–011`, `12:032–046` | os geradores sintéticos embutem a hipótese: φ sobe de 0.35 a 0.72 em torno de 2007 no Sol; φ por grupo é sorteado em faixas escolhidas (Irregular 0.50–0.75, Flat 0.02–0.15) | resultado sintético é circular por construção; não pode servir de validação do método | IMPORTANTE |
| P-28 | A8 não executada | `4:028` | `S_CYCLE_DAYS = 4018  # 11.0 yr, Usoskin et al. 2017` | constante atribuída a uma fonte ainda não auditada (grau X) | MENOR |
| P-29 | — | `20:028`, `27:069`, `27:072` | imprime "CSD signal detected" e "evidence of CSD before Maunder-like collapse" quando p < 0.05 | conclusão automática a partir de p-valor inadmissível (P-01) e de grupos sem base (P-16) | IMPORTANTE |
| P-30 | D38, kit | `0:005`, `28:016` | "Target journal: Solar Physics (Springer)", formato `svjour3` | a revista não está registrada em nenhuma decisão `D##`; na arquitetura do kit é decisão do usuário | MENOR |

## 3. O que o notebook não tem e as decisões D41–D54 passam a exigir

| Decisão | Ausência |
|---|---|
| D41 | não lê as séries locais de Baum, Luhn ou Isaacson |
| D44 | não há tratamento da junção instrumental 2001→2004; `sliding_ews` (`14:074–090`) janela por índice e atravessaria a junção |
| D45 | a receita de variabilidade intra-sazonal com subtração de ruído em quadratura não está implementada |
| D46 | nenhum bloqueio impede aplicar a janela deslizante a uma série de 8 pontos; `sliding_ews` aceita qualquer N ≥ 4 (`14:081`) |
| Q9 | `dfa_hurst` libera DFA para qualquer série com N ≥ 100 (`14:063–066`). Com a cadência bruta de Baum (mediana 698, `3.3-01`) o bloqueio de D24 deixaria de atuar sem que ninguém decidisse Q9 |
| amostragem | todas as janelas são contadas em pontos, não em tempo. Com cadência irregular (lacuna mediana de 7.17 anos, `3.3-09`) isso muda o significado de φ₁ |

## 4. O que já está conforme

| Decisão | Onde | Observação |
|---|---|---|
| D16 | `4:027` | `S_SUN_MEAN = 0.1694` |
| D17 | código inteiro | 0.179 não é usado como valor (`4-14`: nenhuma célula); só aparece no comentário de P-21 |
| D07 | `8:023–025` | HD 4915 excluída, com a razão correta (`4-07`) |
| D10 | `8:023–025` | HD 190406 excluída; o comentário identifica 2.60 como primário e 16.9 como secundário |
| D08 | `8:004–021` | os 14 valores de ⟨S⟩ coincidem com o catálogo congelado (`4-02`); o gerador sintético usa N = 26 pontos anuais (`12:004`) |
| D09 (parcial) | `8:004–010` | as sete "Cycling" são `CYCLE` com FAP Good ou Excellent no catálogo (`4-03`) |
| D34 | `8:008` | HD 166620 como cíclica, 15.8 anos, coerente com 1966–1991 |
| D20 (padrão) | `14:074`, `14:083` | janela de 50 %, deslizante e sobreposta; os extremos 25 % e 75 % estão na varredura |
| D21 (parcial) | `13:005–012`, `16:004`, `16:025` | o filtro gaussiano só alimenta a trilha AR(1)/variância; a trilha A não o usa (exceto P-04) |
| D24 | `14:063–066`, `17:003–010`, `18:021–023`, `20:019` | DFA devolve NaN para N < 100 e não entra no teste estelar |
| A5 §3.1 | `14:024–049` | perfil, caixas não sobrepostas, detrend linear por caixa, F(n) e n_min = 4 fiéis a Peng (seis de oito elementos) |
| D27 | — | a frase riscada ("insensível ao ciclo de ~11 anos…") não aparece no notebook |
| D29 (parcial) | `0:024–025` | DFA é nativa; `nolds` não é dependência |

## 5. Dependências entre os itens

Os itens P-01, P-02, P-06 e P-07 dependem só de decisões já ativas. P-13, P-15 a P-19 e P-24 a P-26 dependem de Q1 e da decisão-raiz (série anual ou bruta). P-14 depende de Q3. P-22 depende da obtenção da Tabela 4 de Egeland. O protocolo §3 regra 5 e `paper_state_v6.md` §11 item 9 mandam fazer tudo num único passe, depois da consolidação.
