# REGRAS DE PROCESSO (kit v0.1.0)

Regras portáveis destiladas do P1 (`exemplos/p1/DECISIONS_P1.md`). Cada regra tem um código `REG-*`, a origem no P1 e uma marca de maturidade:

- `[estável]`: aplicada de ponta a ponta no P1 sem problema.
- `[experimental]`: surgiu no fim do P1 ou foi adaptada ao kit e ainda não foi confirmada por um segundo paper.
- `[configurável]`: o valor padrão está em `kit.yml`; o usuário pode mudar por paper.
- `[superada por REG-xx]`: mantida só para histórico.

Mudar uma regra `[estável]` segue o rito do Change Request (REG-CR) e do `evolucao/` (ver `docs/EVOLUCAO.md`). Regras do **paper** (decisões de física, de método, de texto) não entram aqui: ficam em `DECISIONS.md` do paper.

---

## A. Condução do trabalho

**REG-01 [estável] Etapas com parada e aprovação escrita.** Todo o trabalho é dividido em etapas (ver `docs/ARQUITETURA.md`). Cada etapa termina com uma parada e só avança com aprovação escrita do usuário. Sem aprovação, nada avança, mesmo que a próxima etapa pareça óbvia. (P1: DEC-01.)

**REG-02 [estável] No máximo 2 rodadas de correção por item** (seção, figura, tabela). A terceira exige decisão do usuário sobre o caminho. (P1: DEC-05.)

**REG-03 [estável] Ler antes de calcular.** As referências são lidas antes da física. Nenhum valor de literatura entra no manuscrito, na especificação ou no notebook sem uma entrada no `CADERNO_PESQUISA.md` com **página** do PDF baixado. Baixar e ler são etapas separadas. Fatos entram no caderno só depois de lidos. (P1: DEC-03, R9.)

**REG-04 [estável] Decisões nascem de memorando.** Toda decisão de método que muda um resultado (limites de classe, definição de energia, estimador, completude) é precedida de um **memorando de decisão**: pergunta, subsídios do caderno com página, alternativas, recomendação, e a escolha do usuário. Só então vira `DEC-xx` congelada. (P1: memorando E5, D-A a D-J, DEC-15 e DEC-24.)

**REG-CR [estável] Mudança em decisão congelada só por Change Request**, registrado em `DECISIONS.md` com motivo e impacto (o que muda, o que fica mantido, limites novos). Aprovação do usuário. (P1: CR-01.)

**REG-ACT [estável] Downloads pelo GitHub Actions.** O ambiente de chat costuma bloquear ADS, arXiv, VizieR e sites de editores. Downloads de PDFs, BibTeX, ReadMe de catálogos e páginas de normas rodam em workflows do GitHub Actions disparados por `push` com `paths` na branch de trabalho (não por `workflow_dispatch`, que dá 404 quando o workflow não está na branch padrão); o workflow commita o resultado de volta. O token do ADS fica em GitHub Secrets (`ADS_DEV_KEY`). PDFs de editores com captcha são subidos manualmente pelo usuário. (P1: DEC-04, E1.)

**REG-05 [estável] Escopo.** Extensões que não respondem à pergunta do paper vão para `BACKLOG.md`, com o paper do programa a que pertencem, e ficam fora. (P1: DEC-06.)

**REG-06 [estável] Fim de sessão.** Antes de encerrar: atualizar `CADERNO_PESQUISA.md` (estado atual e log de chats), `DECISIONS.md` e `PAPER_STATE.md`, registrar lições novas em `LICOES_PENDENTES.md`, commit e push na branch de trabalho. Nada importante pode depender da memória da sessão. (P1: `PROMPT_PROXIMO_CHAT.md`, item 7.)

**REG-07 [estável] Uma tarefa por sessão quando possível.** Uma seção do manuscrito por sessão e não misturar análise numérica com escrita. Limite prático de cerca de 15 trocas antes de abrir sessão nova com o prompt de retomada. (P1: `UNIVERSAL_PAPER_CONTEXT` 6.3, mantido na prática.)

**REG-08 [estável] Verificar o ambiente na hora, nunca assumir.** Rede, token, TeX, versões de pacote e o que o ambiente alcança mudam de sessão para sessão. Testar com um comando curto antes de planejar em cima disso. Ver `docs/LICOES_AMBIENTE.md`. (P1: E1, E9a.)

## B. Referências (REG-R1 a REG-R10, origem DEC-09)

**REG-R1 [estável]** Só fontes legais e abertas: PDF do arXiv para artigos publicados (a citação usa a versão publicada, registrada no ADS), ADS com acesso livre ou Unpaywall. Nada de sites piratas.

**REG-R2 [estável]** Sem PDF baixado e validado em `referencias/`, o item **não** pode ser citado no manuscrito nem usado no notebook. Sem exceções automáticas.

**REG-R3 [estável]** Livros e artigos sem versão aberta ficam bloqueados até o usuário subir o PDF ou as páginas usadas (portal CAPES, biblioteca). Pode-se substituir por um artigo aberto equivalente (P1: Binney 1992 por Pelissetto 2002 e Hinrichsen 2000; Bak 1987 por Watkins 2016). O PDF subido é registrado como `fonte: manual`.

**REG-R4 [estável]** BibTeX vem sempre do ADS (exportação do bibcode da **versão publicada**), nunca digitado. Cada entrada é conferida contra a primeira página do PDF (título, autores, ano, periódico, volume/página) e contra o par arXiv↔bibcode.

**REG-R5 [estável]** Chave natbib `autorAno` em minúsculas (`davenport2016`), com o bibcode guardado em `refs_list.yml`. Macros de periódico (`\apj`) só se o template as definir; `make_references_bib.py` gera `journal_macros.tex`.

**REG-R6 [estável]** `manuscrito/references.bib` é **gerado por script** (`make_references_bib.py`) a partir do ADS; sem `ADS_DEV_KEY` não há BibTeX e a etapa bloqueia. Verificação automática: toda chave citada existe no `.bib`, tem PDF e consta no `MANIFEST.json`.

**REG-R7 [estável]** A lista (`refs_list.yml`) precisa de aprovação do usuário antes do download; cada entrada tem **papel** no paper. Lotes de até 10 artigos por aprovação.

**REG-R8 [estável]** PDF que falha na validação vai para `referencias/_pendentes/` e não conta. Máximo de 2 tentativas por item.

**REG-R9 [estável]** (ver REG-03) Baixar e ler são etapas separadas.

**REG-R10 [estável]** PDFs ficam só em `referencias/` (nunca em `repositorio/` ou `manuscrito/`). Alterar a lista aprovada exige registro em `DECISIONS.md`.

**REG-R11 [experimental] Verificar status refereed e errata** de todos os itens do MANIFEST (`modo: verificar`) antes de citar, e registrar exceções (P1: DEC-12 e DEC-13, erratum de Yang e Liu que muda L_flare/L_bol; preprint pré-erratum x versão publicada).

## C. Dados, análise e repositório

**REG-DADOS [estável] Dados por código, nada bruto versionado.** O notebook baixa os catálogos (VizieR, MAST etc.) pelo próprio código, registra versão, data de acesso e checksum na execução e guarda cache em pasta ignorada pelo git. Os ReadMe/listagens dos catálogos ficam só em `referencias/`. (P1: DEC-10.)

**REG-PROG [estável] Restrições do programa** (ver `docs/00_PROGRAMA.md`): sem redução fotométrica, só dados públicos já reduzidos, leis de potência por MLE e nunca por regressão log-log, incertezas por bootstrap ou propagação, nunca omitidas.

**REG-SPEC [estável] Especificação antes do código.** A física é escrita em um documento (`repositorio/ESPECIFICACAO_FISICA.md` ou nome equivalente) em rascunhos aprovados: hipóteses, dados, filtros, estimadores, testes, sensibilidades, critérios de decisão, saídas e figuras. O código só implementa o que foi aprovado e é entregue em subetapas, cada uma com aprovação (P1: E6 em 3 rascunhos, E7a a E7d).

**REG-VAL [estável] Validar o método antes de confiar nos resultados.** Dados simulados com a verdade conhecida (tamanho do teste, poder, viés do estimador). Falhas ficam registradas como limitação, não escondidas. Validações que não passam aparecem como ATTENTION na saída.

**REG-ROB [estável] Veredito só vale se robusto.** Define-se antes qual variante de análise (cortes, janelas, fontes de parâmetro) pode mudar o veredito; se mudar, o resultado é descrito como inconclusivo no corpo do manuscrito, não só no suplemento. (P1: seção 13 da especificação e DEC-35.)

**REG-MAC [estável] Todo número do manuscrito vem de macro.** O notebook escreve `results_macros.tex`; o texto usa `\NomeDoMacro`. Exceção só registrada (P1 teve 12 números copiados à mão em `results_extra.tex`, com a origem anotada). Recomenda-se o hook `numeros_via_macro` para conferir.

**REG-EXEC [estável] Execução completa registrada.** Antes de usar um resultado no texto, o notebook roda por completo, duas vezes com saída idêntica, com 0 validações em ATTENTION, e as saídas versionadas (`analysis_results.md`, macros, figuras). Há modo rápido (`<PAPER>_MODE=fast`) que marca as saídas como não válidas para publicação.

**REG-PROMOCAO [experimental] Exploração fora do repositório público, depois promoção.** Cálculos exploratórios vivem em `fora_repositorio/`. Nenhum número de lá entra no manuscrito: primeiro é formalizado (promovido) no notebook de `repositorio/`, que o reproduz. (P1: E7 e E8 "diagnóstico exploratório fora do notebook, a formalizar".)

## D. Texto, figuras e saída

**REG-ESTILO [configurável] Estilo da prosa.** Padrão do P1: claro, coeso e conciso; sem travessões (em dash, en dash, `--`), sem ponto e vírgula, hífen só em palavras compostas, intervalos numéricos com "to". Vale para manuscrito, textos do notebook, `analysis_results.md`. Verificação automática: `scripts/check_manuscript.py` (regras em `kit.yml`). Roda desde a primeira linha de redação. (P1: DEC-21 e DEC-31, DEC-41.)

**REG-HUM [experimental] Humanização e conferência.** Cada seção passa pela skill de humanização (quando disponível), pelo `check_manuscript.py` e pela conferência dos fatos contra o caderno com página, antes da aprovação do usuário. Ordem de redação: Métodos, Resultados, Discussão e Conclusões, Introdução, Resumo.

**REG-FIG [configurável] Figuras.** Preto e branco, ticks para dentro nos 4 lados, **sem grade**, fonte única (Courier Prime, OFL), diferenciação por estilo de linha/hachura e não por cinza, sem número de figura nem legenda dentro do arquivo, EPS + PDF, larguras da revista, fonte incorporada. Detalhes em `docs/ESTILO_FIGURAS.md`. A revista pode sobrepor medidas (`revistas/<rev>/ficha.md`). Falhar com aviso se a fonte não estiver disponível. (P1: DEC-18.)

**REG-IDIOMA [configurável] Idioma.** Documentos de processo em português; manuscrito, notebook, rótulos de figuras e `analysis_results.md` em inglês (P1: DEC-29). A variante (britânica ou americana) segue a revista.

**REG-LAYOUT [experimental] Layout de pastas.** `manuscrito/` autocontido (vai ao Overleaf), `repositorio/` única pasta pública, `fora_repositorio/` privada, `kit/` e arquivos de estado privados na raiz. Ver `docs/LAYOUT_REPO.md`. O repositório do paper nunca se torna público: a publicação é por exportação de `repositorio/` (`scripts/publish_repositorio.sh`).

## E. Política de IA, commits e portão de submissão

**REG-IA [configurável] Marcas de IA e declaração.** Padrão do P1: zero marcas de ferramentas de IA (trailers, metadados, comentários de ferramenta, nomes de ferramenta) em arquivos de `manuscrito/` e `repositorio/` (P1: DEC-02), verificado por `check_manuscript.py`. **Conflito conhecido**: revistas como a EPL exigem **declaração** (nome, versão, modelo, fonte) do LLM usado para ideias ou redação. A decisão de como declarar é **do usuário**, tomada antes da submissão (portão E10), e a declaração é feita pelo usuário. Enquanto isso, a sessão registra no caderno o uso de IA no processo (qual etapa serviu para quê) para alimentar a declaração. (P1: DEC-20, DEC-22, DEC-44.)

**REG-COMMIT [configurável] Commits.** O P1 usou commits sem trailer de co-autoria (DEC-07). Algumas plataformas exigem trailer na sessão; o valor padrão do kit vem de `kit.yml` (`commits.trailer_coautoria`). Em qualquer caso, nunca em arquivos de `manuscrito/` e `repositorio/` (e o repositório do paper é privado; a exportação pública é feita com a autoria do usuário).

**REG-E10 [estável] Portão de submissão.** Antes de submeter: limite de páginas da revista, estilo e referências em ordem exigida, figuras no formato, política de IA, seção e editores, custo e acordos (CAPES), material suplementar, repositório público e DOI, conferência final no formulário da revista. Checklist em `docs/SUBMISSAO.md`. Itens que dependem só do usuário (autores, afiliações, declarações, financiamento) ficam listados e não bloqueiam o fechamento da etapa.

## F. Evolução do kit

**REG-EVO [experimental]** Lições novas durante um paper vão para `LICOES_PENDENTES.md` do paper (não se edita o kit no meio da escrita). Ao fechar o paper, a etapa E11 gera propostas `PROP-NNN` que voltam ao kit com aprovação. Ver `docs/EVOLUCAO.md`.

---

## Mapa de origem (P1 → kit)

| P1 | Kit |
|---|---|
| DEC-01 | REG-01 |
| DEC-02, DEC-20, DEC-22, DEC-44 | REG-IA |
| DEC-03 | REG-03 |
| DEC-04 | REG-ACT |
| DEC-05 | REG-02 |
| DEC-06 | REG-05 |
| DEC-07 | REG-COMMIT |
| DEC-09 (R1 a R10) | REG-R1 a REG-R10 |
| DEC-10 | REG-DADOS |
| DEC-12, DEC-13 | REG-R11 |
| DEC-15, DEC-24 | REG-04 |
| DEC-18 | REG-FIG |
| DEC-21, DEC-31, DEC-41 | REG-ESTILO |
| DEC-29 | REG-IDIOMA |
| DEC-32 | REG-SPEC, REG-EXEC |
| DEC-33, DEC-34 | REG-VAL |
| DEC-35, DEC-40 | REG-ROB |
| DEC-45 | REG-E10 |
| CR-01 | REG-CR |
