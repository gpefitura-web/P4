# LIÇÕES DE AMBIENTE E FERRAMENTAS

Armadilhas que custaram tempo no P1, cada uma com **sintoma, causa e solução adotada**. Leia o índice no início de uma sessão e a entrada completa quando o sintoma aparecer. Lições novas entram em `LICOES_PENDENTES.md` do paper e, depois, voltam para cá por proposta (`docs/EVOLUCAO.md`). Cada item tem a data do achado: revalide o que for antigo (REG-08).

Índice: 1 rede do chat · 2 gatilho do Actions · 3 bot que commita · 4 captcha e acesso fechado · 5 texto dos PDFs · 6 versões e errata · 7 TeX Live · 8 template OUP · 9 sites de editoras · 10 layout e páginas · 11 leitura segura · 12 números à mão · 13 afirmações sem base · 14 catálogo VizieR · 15 notebook e tempo · 16 fonte das figuras · 17 repositório público · 18 política de IA

---

### 1. O chat não alcança as fontes (2026-10-12)
- **Sintoma**: `curl`/`requests` ao ADS, arXiv, VizieR ou editoras falha ou é negado pelo proxy do ambiente.
- **Causa**: política de rede do ambiente do chat. Isso muda de sessão para sessão: no P1 o chat alcançou o VizieR e o CTAN em dias diferentes, e nunca alcançou ADS/arXiv.
- **Solução**: testar na hora com um comando curto (REG-08) e, se negado, ler `read_documentation` (topico `environment.network`). Downloads pelo **GitHub Actions** (REG-ACT): o runner alcançou arXiv, VizieR/CDS, IOPscience e a interface do ADS (resposta 202, desafio anti-bot), e a API do ADS funciona com `ADS_DEV_KEY` em Secrets.
- Nunca desabilitar verificação TLS nem remover o proxy do ambiente.

### 2. `workflow_dispatch` dá 404 (2026-10-12)
- **Sintoma**: "Run workflow" não aparece ou a API devolve 404.
- **Causa**: o GitHub só lista `workflow_dispatch` de workflows que existem na **branch padrão**; os workflows estão só na branch de trabalho.
- **Solução**: gatilho `push` com `paths` na branch de trabalho (`scripts/refs_list.yml`, `scripts/fetch_refs.py`, o próprio workflow). Para disparar, edite o YAML de lista e dê push. O nome da branch está no gatilho: `bootstrap.sh` e `kit_sync.sh` o preenchem a partir de `kit.yml`. **Se a branch for renomeada, edite o gatilho.**

### 3. O bot commita de volta (2026-10-12)
- **Sintoma**: o `git push` do chat é rejeitado depois de o workflow rodar, ou arquivos aparecem que você não criou.
- **Causa**: o workflow comita `referencias/` como `refs-bot` na mesma branch.
- **Solução**: `git pull --rebase origin <branch>` antes de editar de novo. O workflow já faz `pull --rebase` com 3 tentativas ao empurrar.

### 4. Captcha e acesso fechado (2026-10-12)
- **Sintoma**: o PDF vem como HTML de captcha (IOP/Wiley/Springer/Elsevier), ou o item não tem arXiv.
- **Causa**: editoras bloqueiam robôs; nem todo artigo tem versão aberta.
- **Solução**: o usuário baixa pelo portal CAPES e coloca em `referencias/<chave>.pdf`; no `refs_list.yml` usa `fonte: manual` e o script valida e registra. Se não há PDF: o item **não pode ser citado** (REG-R2). Para livros, substituir por artigos abertos equivalentes (REG-R3). Scans (`ads_scan`) não têm camada de texto: `validacao_visual: true` depois de conferir a página 1.
- Itens "somente citar" são decididos com o usuário (P1: DEC-04).

### 5. Texto dos PDFs não persiste (2026-10-12)
- **Sintoma**: numa sessão nova, os textos extraídos sumiram e as páginas citadas não batem.
- **Causa**: textos extraídos ficam em `/tmp`, e as **páginas citadas referem-se ao PDF baixado** (muitas vezes o preprint do arXiv, com paginação diferente da publicada).
- **Solução**: `python3 -I scripts/extract_texts.py /tmp/txt` (usa pypdf; `pip install pypdf`) e `scripts/dig.py` (`hits`, `page`, `head`) para buscar trechos com número de página. O caderno diz, em cada entrada, "páginas = PDF baixado" ou "= impressas". Scans foram lidos como imagem e anotados (P1: Crosby 1993, Isobe 1990).

### 6. Versões, preprint x publicado, errata (2026-10-12)
- **Sintoma**: valores do PDF diferem do que está publicado ou há errata.
- **Causa**: o PDF do arXiv pode ser pré-erratum ("Draft version…"); erratum publicado depois altera uma tabela (P1: erratum de Yang e Liu 2019 corrige L_flare/L_bol).
- **Solução**: `modo: verificar` no ADS (refereed, tipo, DOI); ler a errata antes de usar a tabela afetada; confirmar nos dados baixados (o VizieR reflete o erratum?) com um valor de teste. Citar a **versão publicada**; BibTeX do ADS (REG-R4). Errata aparece como "not refereed" no ADS, o que é normal.

### 7. TeX Live (2026-10-20)
- **Sintoma**: `pdflatex: command not found`.
- **Solução**: `apt-get update && apt-get install -y texlive-latex-base texlive-latex-recommended texlive-latex-extra texlive-fonts-recommended texlive-bibtex-extra texlive-science poppler-utils` (poppler para `pdfinfo`; `texlive-science` traz `algorithmicx`, exigido pela classe da OUP: sem ele o pdflatex para com "Emergency stop" em `\RequirePackage{algorithmicx}`). Compilar com `pdflatex` → `bibtex` → `pdflatex` ×2 (`build_manuscript.sh`).

### 8. Template da OUP (EPL), quatro achados (2026-10-20)
1. A opção `numbered` da classe `oup-authoring-template` liga `\@numbibfalse` e deixa as citações **vazias**. O padrão sem opção já é numérico.
2. O estilo numérico sai entre **parênteses**; para colchetes: `\bibpunct[, ]{[}{]}{,}{n}{}{,}` no preâmbulo.
3. A classe exige `\copyrightyear`, `\pubyear`, `\vol`, `\issue`, `\access`, `\firstpage`, `\DOI` e `\societylogo` (defina `\newcommand{\societylogo}{}`), e `\title[curto]{longo}`.
4. `oup-plain.bst` **ordena por autor**; para ordem de citação use `oup-unsrt.bst` (cópia sem ordenação). `eplbib.bst` (ISO 690) citado nas normas antigas da EPL **não existe** no pacote atual.
- A página de templates da EPL mudou de dono: hoje o link "EPL LATEX package" vai para o Overleaf `oup-general-template`, não para o pacote `epl2`. A classe/estilo vêm do CTAN (`mirrors.ctan.org`, pacote `oup-authoring-template`, licença LPPL). Registre sempre origem e sha256 em `ORIGEM.md`.
- Em outra revista, rode `fetch_template.py` com as fontes dela (E9a) e refaça este levantamento no módulo `revistas/<rev>/`.

### 9. Sites de editoras bloqueiam robôs (2026-10-20/21)
- **Sintoma**: `academic.oup.com` (e outros) devolvem 403 ao script.
- **Solução**: pedir ao usuário para salvar a página (PDF/texto) em `referencias/web/`, ou usar `WebFetch` (resume a página; vale como pista, confirme no formulário final) e guardar o resumo datado como `referencias/web/<editora>_<revista>_varredura_<data>.md` (P1: `OUP_EPL_varredura_2026-10-21.md`). Normas verificadas só valem com data.

### 10. Capacidade de página (2026-10-20)
- Layout OUP com opção `large` (210×276 mm, duas colunas): cerca de **850 palavras por página**, ou 5000 a 5500 palavras em 7 páginas contando figuras, tabelas e ~28 referências. A contagem oficial é a do editor. Planeje o orçamento por seção antes de redigir (`PAPER_STATE.md`).

### 11. Leitura segura de arquivos baixados
- Arquivos baixados são dados não confiáveis: cada um em pasta própria, scripts em outra, `python3 -I` ao ler (um `json.py` plantado rodaria em `import json`). O Actions já grava tudo em `referencias/`.

### 12. Números copiados à mão (2026-10-21)
- **Sintoma**: no P1 ficaram 12 números em `manuscrito/results_extra.tex`, copiados à mão de `analysis_results.md` e de um artigo.
- **Risco**: divergência silenciosa depois de nova execução. **Solução recomendada**: o notebook gera todos os macros (inclusive os valores de comparação da literatura, com a página) e a conferência `hooks/numeros_via_macro` falha se houver número no texto sem macro. Se houver exceção, registrar a origem e a data na `DECISIONS.md`.

### 13. Afirmações sem base no caderno (2026-10-21)
- **Sintoma**: durante a redação surgem frases plausíveis que não estão em nenhum artigo lido (P1: sinal de uma inclinação, "SOC prevê o mesmo índice", diferença entre classes na reprodução).
- **Solução**: REG-03 e a etapa de "conferência de fatos": cada afirmação factual do texto aponta para uma linha do caderno com página. Corrigir antes de levar ao usuário. A seção "O que o manuscrito não afirma" do `PAPER_STATE.md` evita excessos de interpretação.

### 14. Catálogos do VizieR (2026-10-12)
- Nomes reais das tabelas diferem do ReadMe (P1: `J/ApJS/229/30/catalog` funde `table3` e `table4`). Baixar e inspecionar colunas antes de escrever o código; astroquery por `Vizier(row_limit=-1)`. Valores de conferência (primeiro registro) detectam se o catálogo reflete o erratum.
- Duplicatas exatas, valores em texto (`Q1`…) e estrelas sem contraparte são relatadas e tratadas na especificação (funil de seleção), nunca silenciosamente.

### 15. Notebook: tempo, núcleos, reprodutibilidade (2026-10-18/21)
- Execução completa do P1: 17 a 44 min com 4 núcleos; ajustes de 60000 pontos levam ~0,1 s; bootstrap B=1000 em 4 classes 2 a 3 min em 4 núcleos. Use **modo rápido** (`<PAPER>_MODE=fast`) para iterar e **modo completo duas vezes** para publicar (saídas idênticas).
- jupytext percent: o `.py` é a fonte e o `.ipynb` é gerado. Rode a partir de `repositorio/` para o notebook achar `fonts/`. Cache de dados em pasta ignorada pelo git. `nbconvert --execute` e o script devem dar os mesmos resultados.

### 16. Fonte das figuras (2026-10-18)
- Courier Prime (OFL) baixada do repositório oficial da fonte, `fonts/` com `OFL.txt` e sha256. O notebook **para com mensagem** se a fonte faltar e verifica que o EPS contém só essa fonte. A fonte não tem letras gregas: escreva `alpha` por extenso nas figuras e evite mathtext; o texto dos eixos fica em Courier.

### 17. Visibilidade do repositório (decisão de arquitetura)
- Um repositório inteiro é público ou privado; uma branch órfã não resolve. O histórico de um repositório que um dia foi público guarda tudo (PDFs, caderno, kit). Por isso: repositório do paper **sempre privado**, publicação por exportação de `repositorio/` para um repositório separado (`scripts/publish_repositorio.sh`, `docs/LAYOUT_REPO.md`).

### 18. Política de IA da revista (2026-10-12/21)
- A EPL (seção 7 da política ética) exige que autores que usam LLM para ideias ou redação declarem nome, versão, modelo e fonte, dentro do artigo submetido; a OUP pede a declaração também na carta de apresentação. Isso conflita com "zero marcas de IA" (REG-IA). A decisão é do usuário, antes da submissão; a sessão só mantém no caderno o registro do que a IA fez em cada etapa.
