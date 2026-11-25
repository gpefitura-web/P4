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
