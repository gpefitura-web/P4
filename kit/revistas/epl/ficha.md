# Ficha da revista: EPL (Europhysics Letters), via OUP

**Verificado em 2026-10-21** no P1 (E10). Fontes e ressalvas: `OUP_EPL_varredura_2026-10-21.md` (WebFetch, resumos) e páginas antigas do epletters.net/IOP (`referencias/web/` do P1, datadas de 2026-10-12). As duas fontes divergem em pontos marcados abaixo. **Reconfira no formulário e nas páginas atuais antes de submeter** (REG-E10). Não verificado: acordo CAPES/instituição; página `academic.oup.com/epl/pages/author-guidelines` responde 403 a robôs.

## Tamanho e estrutura
- Letters e Perspectives: **até 7 páginas** A4 em 2 colunas, incluindo título, resumo, referências e tudo mais. Uma única afirmação central; cortar em vez de comprimir.
- Resumo: parágrafo único, **120 a 160 palavras**, sem citações, abreviações, figuras, tabelas nem equações.
- Título: curto, sem abreviações, só a primeira palavra em maiúscula; título curto se > 80 caracteres.
- Autores: inicial do prenome + sobrenome; afiliação reconhecida pela ONU; autor correspondente com endereço postal completo e e-mail.
- Seções finais obrigatórias (OUP): **Conflicts of interest, Funding, Data availability**; Agradecimentos opcionais.
- Texto: ortografia britânica preferida, consistente; abreviar fig., eq., ref.; "table" por extenso; equações numeradas entre parênteses; notas de rodapé mínimas.

## Referências
- Numeradas em ordem de primeira citação. Antigo (epletters): [1], ISO 690, `eplbib.bst` (não existe no pacote atual da classe). OUP: Oxford SCIMED, descrito entre parênteses. O P1 usou colchetes e `oup-unsrt.bst` (cópia sem ordenação do `oup-plain`), registrado com o usuário no DEC-45; para parênteses, trocar o `\bibpunct`.
- Incluir DOI ou número de preprint; citar conjuntos de dados e software com identificador persistente.

## Figuras
- EPS (obrigatório para LaTeX nas normas antigas) e PDF/PNG/TIFF/JPG; largura impressa máxima **80 mm** (1 coluna) ou **165 mm** (2 colunas); linhas ≥ 0,3 pt após a redução; diferenciar por hachura e não por cinza; fontes padrão ou incorporadas; sem número, legenda ou nome de arquivo dentro do arquivo; nomes `figure1.eps`; ponto decimal.
- Painéis: A, B, C no canto superior esquerdo (OUP; as normas antigas diziam a), b), c) em romano). **Texto alternativo obrigatório** sob cada legenda (OUP).

## Template
- Classe `oup-authoring-template` (CTAN, LPPL) com `\documentclass[unnumsec,webpdf,contemporary,large]`, via Overleaf "OUP general template". Esqueleto em `latex/`. Achados do template: `docs/LICOES_AMBIENTE.md` item 8.
- A página de templates do epletters.net passou a dizer "EPL and OUP"; o pacote `epl2` das normas antigas não é mais o oficial.

## Submissão e custo
- ScholarOne: https://mc04.manuscriptcentral.com/epl; PDF completo; sugerir até 3 Co-Editors; o escritório confere tamanho e completude antes da revisão.
- Híbrida: publicação por assinatura **gratuita**; acesso aberto CC BY com APC (antigo IOP: £1680/€1900/US$2090; OUP: £1.600/€1.810/US$1.990). Acordos transformativos detectados pela instituição do autor correspondente (**CAPES/instituição não verificado**).
- Seções do formulário (escolher UMA; lista de epletters.net ?p=2949 em 2026-10-12, reconferir): General physics; Statistical physics and networks; Mathematical and interdisciplinary physics; Fluid and nonlinear dynamics; Nuclear and plasma physics, particles and fields; Atomic, molecular and optical physics; Condensed matter and materials physics; Biological and soft matter physics; Quantum information; Gravitation, cosmology and astrophysics.
- Transferência para: J. Phys., EPJ, CQG, PPCF, PSST, Physica Scripta, J. Opt., Nanotechnology, NJP, Nonlinearity, Semicond. Sci. Technol., Supercond. Sci. Technol., Mater. Res. Express (não inclui ApJ/AAS nem A&A).

## Política de IA
- LLMs não podem ser autores. Declaração de nome, versão, modelo e fonte do LLM usado para ideias ou redação **dentro do artigo** (Métodos ou Agradecimentos) e, pela OUP, também na **carta de apresentação**. Guardar rascunhos e prompts. Conflita com "zero marcas de IA": REG-IA e SUBMISSAO.md. Decisão do usuário.

## Material suplementar
- Hospedado junto, independente do artigo, não revisado; o artigo deve ser compreensível sem ele.
