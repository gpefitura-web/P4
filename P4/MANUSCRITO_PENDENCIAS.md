# Manuscrito: pendências (rascunho de 2026-11-25)

Rascunho em `P4/manuscrito/` (layout neutro, em inglês), gerado a partir de `pipeline_v2/results/` por `manuscrito/build.sh` (macros, tabela e figuras são geradas; nenhum resultado é digitado no texto). Compilado uma vez com pdflatex: 7 páginas, sem citação indefinida; erros de macro corrigidos.

## Escolhas do pesquisador que o rascunho não faz
1. **Revista e template.** Nenhuma D## registra a revista (MAPA_PIPELINE P-30). O `main.tex` é neutro; o limite de páginas, o resumo, o estilo bibliográfico e as larguras de figura dependem da escolha.
2. **Texto de Introdução, Discussão e Conclusões.** Escritos com o que as decisões D90/R3/R15 e os resultados sustentam; o enquadramento do resultado nulo e do Sol é seu. O resumo está vazio de propósito.
3. **Declarações finais:** conflitos de interesse, financiamento, agradecimentos e a declaração de uso de IA (REG-IA: decisão e redação manuais do pesquisador). `sec_backmatter.tex` traz só uma frase de disponibilidade de dados.
4. **Autores e afiliação** (bloco de título é um marcador).

## Pendências técnicas
- `references.bib` tem só os campos lidos de `bib/MANIFEST.json` e dos nomes de arquivo (sem lista completa de autores nem títulos). Completar com o BibTeX do ADS e conferir contra os PDFs (REG-R2, REG-R6) antes de submeter. Rascunho cita 10 chaves.
- Figuras: agora em cor e em Courier Prime (D111). Falta o texto alternativo, que depende da revista.
- Os números fixos citados no texto vêm de `make_macros.py`; as constantes de projeto (24 anos, janela de 50 %, σ = 1, 3, 5, 1 000 surrogates) estão escritas no texto de Métodos como decisões, não como resultado.
- Notebook no formato do Kit (jupytext), repositório público, DOI e `check_manuscript.py` do Kit não foram feitos.
- Material de apoio já pronto: tabelas de varredura de janela e de testes entre grupos completos em `pipeline_v2/results/REPORT.md` (podem virar material suplementar).

## Atualização de 2026-11-25 (após seis revisões independentes; ver `REVISOES_INDEPENDENTES.md`)
- Texto revisado e compilado (10 páginas, fontes Type 1). Resumo escrito (enquadra H2 como não testável como projetado; é seu para ajustar).
- BibTeX preenchido a partir da primeira página dos PDFs do projeto; as listas de autores de Baliunas e Isaacson estão truncadas com "and others" e a de Baliunas não tem DOI. Completar do ADS.
- Decisões suas ainda abertas: **revista** (`RECOMENDACAO_REVISTA.md`), **título** (sugestões em `REVISOES_INDEPENDENTES.md`), declarações finais (conflitos, financiamento, agradecimentos, uso de IA), bloco de autores, link do repositório.
- Fora do escopo desta rodada (análise nova): curva de poder com ciclo injetado, sensibilidade à interpolação, taxa nula da regra de 3 de 4, bootstrap em blocos para H1.

## Atualização de 2026-11-25 (main.tex único)
- `manuscrito/main.tex` agora contém **todo o manuscrito** (resumo, seções, tabelas, legendas, constantes de projeto). Só as figuras (`figures/`) e `references.bib` são arquivos separados, como exige o LaTeX.
- Os números continuam vindo de macros, mas as definições ficam em um bloco marcado dentro do próprio `main.tex` (`%%% BEGIN/END GENERATED MACROS`) e a Tabela 2 em outro (`%%% BEGIN/END GENERATED TABLE`). `build.sh` regrava esses dois blocos a partir de `pipeline_v2/results/`; **edite o texto à vontade fora dos blocos marcados**. Os arquivos `sec_*.tex`, `results_macros.tex`, `results_extra.tex` e `tab_segments.tex` foram removidos.
- Subsídios para a escolha da revista (inclui New Astronomy): `SUBSIDIOS_REVISTA.md`.

## Atualização de 2026-11-25 (formato New Astronomy, D112)
- `main.tex` agora usa `elsarticle` (`preprint,12pt`, `\journal{New Astronomy}`) com `frontmatter` e `elsarticle-num`. Compila em 13 páginas (formato de revisão em coluna única). Autor e afiliação preenchidos (IFTM, Uberaba; confira a grafia da afiliação); **e-mail do autor correspondente em branco**, para você inserir.
- Seções de declarações criadas com marcadores "[To be completed by the author.]": CRediT, conflito de interesses, financiamento, agradecimentos, e a declaração de uso de IA (decisão e redação suas).
- Highlights escritos e **comentados** no `frontmatter`; descomente se o guia da revista pedir.
- **Não confirmado** (o guia da New Astronomy não foi achado nas buscas): limite do resumo e de páginas, número de palavras-chave, estilo de referência (numerado, em uso, ou autor-ano; trocar por `elsarticle-harv`), resumo gráfico, exigência de highlights. Lista em `kit/revistas/new-astronomy/ficha.md`.
- Ainda abertos: título, biblioteca do IFTM (lista de elegíveis do acordo CAPES–Elsevier e participação), BibTeX com autores truncados (Baliunas, Isaacson), texto alternativo das figuras.

## Estado em 2026-11-25 (após a revisão de leitura)
- Texto revisado e compilado (14 páginas em formato de revisão da New Astronomy), título provisório v2 em uso (`SUGESTOES_TITULO.md`).
- **Falta, e é seu:** e-mail do autor correspondente; CRediT, conflito de interesses, financiamento, agradecimentos e declaração de uso de IA (marcadores no texto); link do repositório na seção de dados; confirmação das regras da revista (`kit/revistas/new-astronomy/ficha.md`); lista de elegíveis do acordo CAPES–Elsevier; título definitivo.
- **Falta, técnico:** BibTeX com autores completos de Baliunas e Isaacson e DOI de Noyes (do ADS); texto alternativo das figuras.

## Atualização de 2026-11-25 (BibTeX e título)
- `references.bib` refeito a partir do **Crossref** (o ADS exige token pessoal de API, que não existe aqui), com autores completos, DOI, volume e páginas; cada registro conferido contra a primeira página do PDF do projeto. Títulos protegidos com chaves para o estilo numerado não os passar para minúsculas. Resolvido: autores de Baliunas e Isaacson e DOI de Noyes. Se quiser as chaves do ADS (bibcode), forneça um token de API do ADS.
- Título provisório trocado para a versão 2 (sem "null").

## Atualização de 2026-11-25 (declarações finais e título)
- Título em uso, redação sua: "Testing critical slowing down in Mount Wilson S-index of Sun-like stars" (observação sobre "series" em `SUGESTOES_TITULO.md`).
- Declarações preenchidas em `main.tex`: CRediT (autor único, todos os papéis), conflito de interesses, financiamento, disponibilidade de dados (com o repositório), declaração de IA e agradecimentos.
- **Confirmar antes de submeter (são afirmações suas, não fatos que o projeto prove):**
  1. **Financiamento:** usei o texto padrão da Elsevier "sem apoio específico". Se houve bolsa, CNPq, CAPES, FAPEMIG ou IFTM, troque.
  2. **Conflito de interesses:** texto padrão "nenhum conhecido".
  3. **CRediT:** todos os papéis listados para o autor único; ajuste se quiser.
  4. **Declaração de IA:** só falta o nome e a versão da ferramenta, `[name and version of the AI tool...]` (deixei em branco porque identificar o modelo em arquivo do repositório não deve ser feito por mim, e a regra do Kit pede que a declaração seja sua). A frase "o autor revisou e editou" é uma afirmação sua.
  5. **Dados:** o repositório `github.com/gpefitura-web/P4` precisa estar público (ou ser trocado por DOI do Zenodo) na submissão.
- Agradecimentos: texto exigido pelos autores do HK Project (README dos dados v2001, com o nome HK_Project_v2001_NSO) e o agradecimento padrão do VizieR com o DOI (conferido no DataCite). Acrescente o que quiser (instituição, colegas).

## VERSÃO FINAL FECHADA (2026-11-25, D113)
- **Pacote para o Overleaf:** `P4/manuscrito_overleaf.zip` (`main.tex`, `references.bib`, `figures/figure1-3.pdf` e `.eps`). Classe `elsarticle` (já existe no Overleaf), compilar `main.tex` com pdfLaTeX e BibTeX. 15 páginas no formato de revisão.
- **Declaração de IA:** deixada para você no Overleaf (a seção existe, com o marcador "[To be written by the author in Overleaf.]").
- **Ainda é seu, antes de submeter:** e-mail do autor correspondente (linha `\ead` comentada no `frontmatter`); confirmar financiamento, conflito de interesses e CRediT; repositório público ou DOI do Zenodo; regras da New Astronomy (`kit/revistas/new-astronomy/ficha.md`) e lista de elegíveis do acordo CAPES–Elsevier; texto alternativo das figuras; título final (em uso o seu: "…S-index of Sun-like stars").
- Para regerar números, tabela e figuras e recompilar: `PYTHON=<python> bash P4/manuscrito/build.sh`; os blocos entre `%%% BEGIN/END GENERATED` do `main.tex` são regravados e o resto do texto não.

## Conferência com o guia da New Astronomy (2026-11-25, D114)
Feito: palavras-chave (6, sem "and"), resumo de 226 palavras (limite 250), highlights em `highlights.docx` e `highlights.tex` (4 itens, 67 a 73 caracteres), notas da tabela abaixo dela, figuras `Figure_N`, legendas com título, seção de IA com o título exato do guia, referência `[dataset]` do HK Project, estilo de referência (qualquer estilo consistente; o da revista entra na prova).
**Exigências do guia que dependem de você:**
1. **Endereço postal** da afiliação e **e-mail** do autor correspondente (campos com marcador na página de título).
2. **Dados de pesquisa, Opção C:** depositar dados processados e código num repositório (Zenodo, por exemplo) e informar o link na submissão; a seção de dados tem o marcador para o DOI.
3. **Ferramenta de declarações da Elsevier** (conflito de interesses), com o `.docx` anexado.
4. **Enviar `highlights.docx` como arquivo separado** na submissão.
5. **Declaração de IA** (você escreve no Overleaf). O guia dá o modelo e a dispensa para verificadores de gramática, ortografia e referências. As figuras são gráficos derivados dos dados por código reprodutível, o que o guia permite.
6. Figura 2 reúne quatro painéis num arquivo; o guia desaconselha combinar imagens, com exceção das feitas para comparação. Se o editor pedir, separo em dois arquivos.
7. Opcional: consulta prévia ao editor-chefe sobre o escopo (o guia convida a isso).

## Pasta para o repositório (2026-11-25, D115)
- **`P4/repositorio/`** é a pasta a enviar: 92 arquivos, 11 MB, `README.md` com o mapa manuscrito → código → saída, `reproduce.sh` (cerca de 6 minutos), `MANIFEST.sha256`. Verificada em cópia limpa fora do projeto: `REPRODUCTION OK` (resultados numericamente iguais; texto, tabela e as oito figuras idênticos byte a byte).
- Se mudar qualquer fonte (código, dados, texto), rode `python3 P4/make_repositorio.py` e depois `bash repositorio/reproduce.sh` numa cópia limpa antes de enviar.
- **Antes de tornar público (Opção C da New Astronomy):** (1) licença do código, marcada "[to be chosen by the author]" no README; (2) termos de uso de cada fonte de dados (cópias sem alteração; o agradecimento exigido pelos autores do HK Project está no README); (3) DOI do depósito (por exemplo, Zenodo) para a seção de dados do manuscrito.
- Figura 2 dividida em duas (HD 166620, Sol); pendência 6 da conferência com o guia resolvida. Figuras agora numeradas 1 a 4; o `manuscrito_overleaf.zip` foi atualizado.

## Licença e Zenodo (2026-11-25, D116)
- **MIT** escolhida e aplicada ao código, às saídas e às figuras (`repositorio/LICENSE`); `CITATION.cff` e `.zenodo.json` criados; pacote `repositorio_zenodo_v1.0.0.zip` pronto.
- **Falta, e é seu:** publicar no Zenodo (roteiro e riscos em `ZENODO_DEPOSITO.md`), pôr o DOI na seção de dados do manuscrito e na bibliografia, e decidir sobre a cópia da Tabela 4 de Egeland et al. (direitos reservados no artigo original).

## Tabela 4 de Egeland fora do pacote; prova refeita (2026-11-25, D117)
- `repositorio/` e o zip do Zenodo **não contêm mais a Tabela 4**; `fetch_egeland_table4.py` a baixa e confere o sha256. Prova em pasta limpa refeita: **`REPRODUCTION OK`** (resultados numericamente iguais; texto, tabela e as oito figuras idênticos byte a byte).
- Novo sha256 do zip: `b77db449155e17acbfd04cc7494f0bf8cee39891622a412cbcf082b17db7e8b0` (95 arquivos mais o manifesto). Quem reproduz precisa de rede uma vez (ou `--from` com cópia local).
- Pendente, seu: a seção de dados do manuscrito pode dizer que a série solar é baixada de Egeland et al. (já está citada); decidir se acrescenta isso em uma frase.
