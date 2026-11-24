# PROMPT_PROXIMO_CHAT — reconstrução do pipeline do P4 (passada única)

**Para colar na abertura da próxima conversa.** Branch de trabalho: `claude/focused-ramanujan-rchb37`. Pacote: `P4/` (subpasta). Português nas conversas; código, comentários e saídas de script em inglês; `python -I` para ler `data/`.

## 0. Antes de qualquer coisa (ordem fixa, sem pular)
1. `git pull`; ler **só** estes arquivos, nesta ordem: `P4/CLAUDE.md` → `P4/paper_state_v7.md` → `P4/consolidacao/APROVACAO_2026-11-24.md` → `P4/consolidacao/LISTA_FINAL_ESTRELAS_2026-11-24.md` → `P4/consolidacao/P4_SOURCE_VALUES.md` → `P4/inspecao/MAPA_PIPELINE.md` → este arquivo. O caderno (`P4_RESEARCH_NOTEBOOK.md`, D01–D104, §4d) é consulta: **buscar por D## com Grep**, não reler inteiro.
2. Conferir os hashes de `APROVACAO_2026-11-24.md` (`sha256sum`). Se algum não bater, **parar e avisar** (a aprovação perdeu a validade).
3. Criar o venv de trabalho em `/tmp` (scratchpad): numpy, pandas, scipy, statsmodels. Duas tentativas de instalação; se `statsmodels` falhar nas duas, usar ARMA por `scipy` (AR(p) por Yule–Walker, MA ignorado) e **registrar a troca em `ACHADOS.md`**; não insistir.

## 1. O que está decidido e NÃO se reabre (D68–D104; detalhe em `paper_state_v7.md` §5)
Série **anual** para o CSD temporal, **bruta** só para σ por estado; períodos **publicados**; DFA **fora**; interpolação linear **só de lacunas de 1–2 anos** (pontos marcados), lacunas ≥ 3 anos **dividem** a série; **segmento ≥ 24 anos** (janela de 50 % ≥ 12 pontos, ≥ 13 janelas), 24–39 anos "precisão baixa", ≥ 40 "adequada"; indicador só na **era Mount Wilson** (sem atravessar a junção; sem correção de degrau); p do τ por **1 000 surrogates ARMA** com as **mesmas lacunas e interpolação**; τ reportado na série original **e** nos resíduos (D23); remoção de tendência: **σ ∈ {1, 3, 5} anos mais "sem remoção"**, σ = 1 padrão, destaque só com concordância em ≥ 3 de 4; índice **S e R′_HK** (D52 com faixa de D53, B−V declarado: CLS V quando existe, senão B95); σ_S pela **conta A** (principal) e **B** (sensibilidade); subgigantes **com e sem**; exclusões D13, R11; Sol por Egeland (exploratório). **H1** (comparação de estados de HD 166620) e **H2** (CSD temporal exploratório, n = 1, "não suportado" ≠ refutação).

## 2. Plano em 10 passos (fazer na ordem; um commit por passo)
Pasta nova `P4/pipeline_v2/` (o notebook antigo `p4_pipeline.ipynb` **não é editado**: é a referência congelada). Cada passo tem **entrada → saída → critério de pronto**; ao terminar, marcar em `P4/pipeline_v2/PROGRESSO.md`.
1. **Entrada de dados** (`io.py`): lê `p4_star_catalog.csv` (`status_amostra = incluida`), Baum Tabela 1 (remove linhas com flag `sigma`, como em `N_obs_limpo`), v2001 `.mgd` (campo 2 = S, campo 3 = JD − 2444000, campo 8 = instrumento), Egeland Tabela 4. *Pronto:* contagens iguais a `3.2-01`, `3.15-01`, `3.12-01`.
2. **Séries anuais** (`annual.py`): média por ano civil (D08), por era (Mount Wilson = HKP-1/2, Keck = HIRES-1/2), regra D98, segmentos. *Pronto:* segmentos iguais a `inspecao/saidas/17_recommendation_support.txt` §2 e à coluna `serie_MW_segmento_max_anos` do catálogo.
3. **Indicadores** (`indicators.py`): AR(1) lag-1, variância, rolling 50 % (varredura 25–75 %, D20), τ de Kendall. *Pronto:* reproduz `inspecao/saidas/16_min_segment.txt` §1 em simulação (SD do AR(1) ≈ √((1−c²)/w)).
4. **Remoção de tendência** (`detrend.py`): σ ∈ {1, 3, 5} e nenhuma. *Pronto:* reproduz `inspecao/saidas/17_recommendation_support.txt` (3).
5. **Surrogates** (`surrogates.py`): ARMA(p,q) por AIC sobre os resíduos, 1 000 por segmento, com a máscara de lacunas e a interpolação de D98. *Pronto (autoteste obrigatório):* em AR(1) sintético nulo, a taxa de rejeição a 5 % fica entre 3 % e 7 %; se não ficar, **parar** (ver §3).
6. **H1** (`state_comparison.py`): σ_S de HD 166620 pela conta A e B, F-test com variâncias brutas e corrigidas. *Pronto:* reproduz V22 e V25 de `P4_SOURCE_VALUES.md` (`3.4-25`, `3.4-32`, `3.4-39`, `3.4-50`).
7. **R′_HK** (`rhk.py`): D52 com validade de D53. *Pronto:* reproduz `3.7-12` a `3.7-14`.
8. **Execução única nas estrelas** (`run_all.py`): para cada estrela incluída com `indicador_elegivel_D100 = sim`, os indicadores (S e R′_HK), as quatro configurações de tendência, τ na série original e nos resíduos, p por surrogates; H2 para HD 166620. Sol: mesma rotina, rotulada exploratória. Sementes fixas. **Uma única execução oficial**, sem ajustes depois de ver o resultado (D04).
9. **Relatório de fatos** (`results/REPORT.md`): só números com arquivo de origem e a contagem de configurações concordantes; **sem interpretação**. Testes entre grupos (Flat, CYCLE+Excellent, Var, Long): copiar a lógica da célula 20 do notebook antigo sem mudar, e **sinalizar em `ACHADOS.md`** qualquer ponto que as decisões não cubram.
10. **Fecho (REG-06):** `paper_state_v8.md`, linha no log do caderno (nova D## do que foi feito), `LICOES_PENDENTES.md`, commit e push. **Parar.** Não escrever figuras nem manuscrito.

## 3. ANTILOOP (regras duras)
1. **Não reabrir nada decidido** (§1). Se um passo esbarrar numa decisão, **aplicar a decisão como está** e registrar o atrito em `P4/pipeline_v2/ACHADOS.md`; **não perguntar** ao pesquisador, a menos que o passo fique impossível, e então **uma pergunta só**, com as opções, e seguir com os passos independentes.
2. **No máximo 2 tentativas por falha.** Na segunda falha de um passo: escrever `P4/pipeline_v2/BLOQUEIO.md` (o que falhou, o que já foi tentado, saída do erro) e **parar o passo**; não há terceira tentativa, nem "só mais um ajuste".
3. **Um passo por vez, em ordem; commit ao fim de cada um.** Não voltar a um passo concluído, salvo se a verificação do passo seguinte provar erro; nesse caso, 1 correção e seguir.
4. **Sem ajuste de parâmetros olhando resultados.** O autoteste do passo 5 e os critérios "pronto" são os únicos testes; nada é calibrado com as estrelas reais.
5. **Não reler arquivos grandes duas vezes**: guardar notas em `P4/pipeline_v2/NOTAS.md` (fatos e números, com o arquivo de origem).
6. **Sem espera ativa**: não usar `sleep`, polling nem reexecução repetida do mesmo comando. Uma execução de cada script por vez; `run_all.sh` (inspeção) rodado **duas vezes só no passo 10**.
7. **Não editar** o pipeline antigo, o catálogo congelado, as D##, as auditorias nem a referência congelada (hashes em `APROVACAO_2026-11-24.md`). Mudança neles = **parar**.
8. **Orçamento:** se os 10 passos não couberem, parar no último passo concluído, atualizar `PROGRESSO.md` e entregar o estado; **não** comprimir passos.
9. **Fim:** terminou o passo 10 (ou um BLOQUEIO) → relatório curto em português, lista dos arquivos criados, o que ficou pendente. **Nada de novas frentes.**

## 4. Entregáveis esperados
`P4/pipeline_v2/` (código, `PROGRESSO.md`, `ACHADOS.md`, `NOTAS.md`, `results/`), `paper_state_v8.md`, nova D## no caderno, `LICOES_PENDENTES.md` atualizado.
