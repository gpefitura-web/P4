# PADRÃO DO NOTEBOOK (repositorio/)

O notebook do P1 (≈3000 linhas) é a referência de estrutura, não de conteúdo. O kit **não** leva o código de física; leva este padrão.

## Formato
- `repositorio/<paper>.py` em **jupytext percent** é a fonte; o `.ipynb` é gerado (`jupytext --to ipynb`) e versionado. Executar com `jupyter nbconvert --execute` a partir de `repositorio/`.
- `requirements.txt` com limites mínimos (numpy, pandas, scipy, astropy, astroquery, powerlaw, matplotlib, jupytext, ipykernel, nbconvert; acrescentar o que o paper usar).
- `README.md` curto em inglês: como rodar, tempo, modo rápido, saídas, fonte.
- Textos do notebook, rótulos de figura e `analysis_results.md` em inglês (REG-IDIOMA); a especificação continua em português.

## Seções recomendadas (P1 entre parênteses)
1. Setup, parâmetros e registro da execução: semente, modo (`<PAPER>_MODE` = `full` ou `fast`), versões de pacotes, data, número de núcleos. (§1)
2. Download dos dados por código (REG-DADOS) com versão do catálogo, data de acesso, linhas e **checksum**. (§2)
3. Verificações de integridade: contagens contra o artigo-fonte, duplicatas, tipos, intervalos, valor de conferência de erratum. (§3)
4. Seleção da amostra: funil com contagens por etapa, filtros, classes, variantes. (§4)
5. Estimadores: implementação própria ou `powerlaw`, validada. (§5)
6. **Validação com dados simulados** (tamanho do teste, poder, viés, cobertura, tempo) com **tolerâncias definidas antes** dos testes; falhas marcadas `ATTENTION` e relatadas como limitação (REG-VAL). (§6)
7. Linha de base como publicada na literatura (para comparar). (§7, §10)
8. Variável principal e ajuste principal, bootstrap **por unidade correlacionada** (estrela, não flare), testes de hipótese. (§8, §9)
9. Sensibilidades (todas as variantes da especificação). (§11)
10. Diagnósticos adicionais (heterogeneidade, reprodução da literatura). (§12)
11. Veredito e robustez: regra escrita na especificação (REG-ROB). (§13)
12. Análises adicionais definidas depois (P1: faixas de Teff). (§14)
13. Figuras (REG-FIG). (§15)
14. Macros e checagens finais: `results_macros.tex` e `analysis_results.md`. (§16)

## Saídas
- `results_macros.tex`: um macro por número do manuscrito. Nomes só com letras (grandeza + letra da classe), ponto decimal, `\ensuremath{-}` para menos, p-valores no piso (`\ensuremath{<}0.001`). Cabeçalho com data, modo, semente, checksums. No modo rápido o cabeçalho diz "não vale para publicação" e `\RunValid` = "no, fast mode".
- `analysis_results.md`: todas as tabelas da análise, resumo das validações, limitações encontradas pela execução.
- `figures/figureN.eps` e `.pdf`.

## Critérios de entrega (REG-EXEC)
- 0 validações em `ATTENTION`; duas execuções completas idênticas; verificação de estilo sem problemas; checksums dos dados iguais aos do primeiro download.
- Todo valor da literatura usado no notebook cita `bibkey` e página no código ou na saída.
- Nenhuma menção a arquivos privados, ao kit ou ao caderno (o `publish_repositorio.sh` recusa).
