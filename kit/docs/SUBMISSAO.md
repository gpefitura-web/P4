# PORTÃO DE SUBMISSÃO (E10)

Checklist genérico + seção por revista (`revistas/<rev>/ficha.md`). Marque cada item com a data. Itens que dependem só do usuário são listados e **não bloqueiam o fechamento** da etapa (REG-E10), mas a submissão só ocorre quando estiverem resolvidos.

## Manuscrito
- [ ] Limite de páginas/palavras da revista (contar com o layout final; orçamento em `PAPER_STATE.md`)
- [ ] Resumo dentro do limite (EPL 120 a 160 palavras; ApJ ≤ 250; MNRAS ≤ 200); sem figura, tabela, equação ou referência no resumo quando a revista exige
- [ ] Título no padrão da revista (EPL: só a primeira palavra em maiúscula), título curto se necessário
- [ ] Autores no formato da revista (EPL: inicial do prenome + sobrenome), afiliação reconhecida pela ONU quando exigida, autor correspondente
- [ ] Todas as figuras e tabelas citadas no texto; equações numeradas; "table" por extenso, "fig." e "eq." abreviados quando a revista pede
- [ ] Referências no estilo e ordem da revista (numéricas em ordem de citação na EPL), com DOI ou número de preprint; conjunto de dados e código citados
- [ ] Seções finais exigidas (Conflicts of interest, Funding, Data availability, Acknowledgements), **textos finais** do usuário
- [ ] Seção `Software` ou frase equivalente com os pacotes usados
- [ ] `scripts/check_manuscript.py` sem problemas; `build_manuscript.sh` sem avisos de citação indefinida

## Figuras
- [ ] EPS e PDF, largura e linha mínima da revista, fontes incorporadas, nomes `figureN`
- [ ] Texto alternativo por figura
- [ ] Sem número/legenda dentro do arquivo; diferenciação sem cinza

## Dados, código e reprodutibilidade
- [ ] Notebook executa do zero (modo completo) e reproduz os macros; duas execuções idênticas
- [ ] `publish_repositorio.sh` passou; repositório público criado; DOI no Zenodo
- [ ] Material suplementar autocontido se a revista pedir

## Política de IA (REG-IA)
- [ ] Decisão do usuário sobre a declaração (nome, versão, modelo, fonte), feita **manualmente** por ele
- [ ] Declaração na seção que a revista pedir (Métodos ou Agradecimentos) e na carta de apresentação quando exigido
- [ ] Verificação de marcas de IA em `manuscrito/` e `repositorio/` coerente com a decisão (`kit.yml: verificacao.marcas_ia`)

## Revista e custos
- [ ] Seção/área da revista e até N editores sugeridos
- [ ] Custo: publicação por assinatura gratuita? APC do acesso aberto? Acordo CAPES/instituição (**verificar; não presumir**)
- [ ] Taxa de página/cor, licença (CC BY), transferência entre revistas
- [ ] Carta de apresentação (com declaração de IA se pedida)
- [ ] arXiv: postar no dia da submissão quando a revista permite (astro-ph.SR)
- [ ] Conferência final **no formulário** da revista (as páginas das editoras mudam)

## Erratas e fontes
- [ ] Todas as referências com PDF validado (REG-R2) e errata considerada (REG-R11)
- [ ] Valores copiados à mão listados com origem (REG-MAC)
