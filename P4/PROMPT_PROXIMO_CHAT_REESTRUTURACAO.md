# PROMPT_PROXIMO_CHAT_REESTRUTURACAO: mudanças radicais no manuscrito P4 (2026-11-26)

**Para colar na abertura da próxima conversa.** Português nas conversas; código, comentários e saídas de script em inglês; `python -I` ao ler `data/`. Repositório gpefitura-web/P4, pacote em `P4/`. **Branch de trabalho: a que o sistema indicar** (a etapa anterior terminou na `claude/gracious-carson-bjbqo2`). Não criar pull request.

## 0. Situação
Existe uma **versão completa v1 do manuscrito, verificada e congelada no commit `72191da`**: `manuscrito/main.tex` (New Astronomy, 23 páginas, 36 referências), pacote `repositorio/` com `REPRODUCTION OK` em pasta limpa, zips atualizados. O pesquisador **pretende fazer mudanças radicais no paper e ainda não as especificou**. A v1 é a base e o ponto de retorno (`git show 72191da:P4/manuscrito/main.tex`).

## 1. Primeira coisa: perguntar, não presumir
Abrir a conversa pedindo ao pesquisador que descreva as mudanças. Perguntas úteis (uma rodada, curtas): (a) a mudança é de **pergunta/enquadramento** (por exemplo, abandonar a hipótese unilateral de subida de autocorrelação e variância, já que o controle positivo mostra queda ao perder o ciclo), de **método** (novo indicador, novo modelo, novos controles positivos), de **dados** (outra amostra, outra fonte) ou de **revista/formato**? (b) o que da v1 deve ser mantido (pipeline, bibliografia lida, pacote)? (c) quais resultados da v1 continuam valendo como estão? Só então planejar. Não começar a reescrever antes da resposta.

## 2. O que a v1 estabeleceu (para decidir o que reaproveitar)
- **Pipeline** (`pipeline_v2/`, semente 20261124, duas rodadas estelares; D105 e D121): indicadores móveis (AR(1) e variância), 4 configurações de remoção de tendência, surrogates ARMA com as mesmas lacunas, janelas de 25 a 75 %. 23 segmentos de 28–36 anos + Sol (51 anos). **Não reexecutar `run_all.py` no projeto sem pedido explícito**; reproduzir em cópia limpa.
- **Resultados:** H1 (HD 166620, variabilidade por estado) só sustentada em relação ao mínimo 2; H2 não testável (registro termina em 1995); varredura nula: 2 de 192 células marcadas; teste com tamanho nominal (3,2 % e 4,2 %) e poder baixo, nulo com ciclo; **controle positivo (Hopf supercrítico): ao perder o ciclo, autocorrelação e variância caem**; só 4 de 23 estrelas têm amplitude de ciclo homogênea.
- **Bibliografia:** 36 itens com PDF validado e lidos (`audit/A15_leitura_referencias_D122.md`; `bib/`). Wilson 1978 segue sem PDF.
- **Análises declaradas como limite e não feitas:** Hopf subcrítico, ruído multiplicativo, curva de poder com propriedades de ciclo reais, efeito da interpolação, amplitude do ciclo.
- Candidatos naturais a eixo de uma reestruturação (apenas hipóteses para discutir, não decisões): centrar o artigo no controle positivo e no poder do teste (resultado metodológico); trocar a hipótese por teste bilateral; transformar a varredura nula em limite superior de detecção; separar H1 num artigo próprio.

## 3. Regras que continuam valendo
1. **Regra 9 / Seção 0 do handoff anterior:** tudo que vai para o manuscrito é sustentado no repositório. Números: macros gerados de `pipeline_v2/results/`; figuras e tabelas: scripts do pacote; literatura: citação com PDF validado e página. Fluxo: editar a fonte → `python3 P4/make_repositorio.py` → `bash repositorio/reproduce.sh` em cópia limpa fora do projeto (exige `REPRODUCTION OK`, ~30 min, em segundo plano) → só então os zips. Mudança radical de texto sem mudança de análise ainda passa por esse fluxo.
2. **Mudança de hipótese ou de análise depois de ver os dados:** registrar em D## nova, declarar no manuscrito como decidida depois da rodada (como na Seção 2.7 da v1) e **não** reapresentar como confirmatória. Hipóteses H1/H2 da v1 foram declaradas antes; novas serão exploratórias.
3. **Não reabrir D01–D124.** Revogar = nova D## e `status: revogada` na antiga. Congelados: `p4_pipeline.ipynb`, `baliunas_table2_full.csv`, `consolidacao/*` (hashes em `consolidacao/APROVACAO_2026-11-24.md`; conferir no início). Nova rodada estelar ou novo pipeline exige pedido explícito do pesquisador e arquivo da saída antiga para comparação.
4. **ANTILOOP:** no máximo 2 tentativas por falha; sem `sleep` nem polling; tarefas longas em segundo plano.
5. **Downloads só por vias legais e abertas**; nunca disfarçar o cliente; validar a primeira página e o hash de todo PDF (lições L30–L32).
6. Nenhum nome de ferramenta ou de modelo de IA em arquivos do repositório, do pacote ou do manuscrito. Declaração de IA, financiamento, conflito de interesses e CRediT são do pesquisador.
7. Commits com as linhas de atribuição da sessão; push na branch; nenhum PR; commitar fontes e registros e deixar `repositorio/` e zips para depois do `REPRODUCTION OK`.

## 4. Ambiente (some entre sessões)
`python3 -m venv <scratchpad>/venv && pip install -r P4/repositorio/requirements.txt` (Python 3.13; `fonttools==4.68.0` fixado). TeX: `apt-get update` e `apt-get install -y --no-install-recommends texlive-latex-base texlive-latex-recommended texlive-fonts-recommended texlive-publishers lmodern cm-super poppler-utils`. Download da Tabela 4 de Egeland: `SSL_CERT_FILE=/root/.ccr/ca-bundle.crt`. Compilar com `pdflatex`, `bibtex`, `pdflatex` duas vezes, e conferir a data do PDF contra o fonte antes de ler.

## 5. Leitura inicial (só isto)
`git pull`; `P4/CLAUDE.md` → `paper_state_v13.md` → `MANUSCRITO_PENDENCIAS.md` (seção final) → `RASTREABILIDADE_PENDENTE.md` → `repositorio/README.md` → este arquivo. Caderno (D01–D124): consulta por Grep de D##. Pareceres: `REVISOES_INDEPENDENTES.md`. Lições: `LICOES_PENDENTES.md`.

## 6. Entregáveis desta etapa
Plano acordado com o pesquisador (curto, em português) antes de qualquer edição grande; depois, execução pelo fluxo da regra 1, com `MANUSCRITO_PENDENCIAS.md`, `paper_state` (v13 → v14), caderno (nova D##), `LICOES_PENDENTES.md` e `RASTREABILIDADE_PENDENTE.md` em dia.
