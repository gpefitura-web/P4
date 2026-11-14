# Varredura do site da EPL na OUP (2026-10-21)

Fonte: leitura das páginas por WebFetch no chat. O WebFetch devolve resumo feito por um modelo pequeno, não o texto literal, e páginas longas foram truncadas em 100000 caracteres. Tratar como orientação e conferir a página original antes de submeter. Os arquivos .txt desta pasta, do site epletters.net, são anteriores e dizem coisas diferentes em alguns pontos (ver "Diferenças").

## Páginas lidas
- https://academic.oup.com/epl (início, menus, editor-chefe Richard A. Blythe, Edimburgo)
- https://academic.oup.com/epl/pages/author-guidelines
- https://academic.oup.com/epl/pages/about
- https://academic.oup.com/epl/pages/editorial-board
- https://academic.oup.com/journals/pages/open_access
- https://academic.oup.com/pages/open-research/research-data
- https://www.overleaf.com/latex/templates/oup-general-template/ybpypwncdxyb
- Não existem (404): /epl/pages/general-instructions, /epl/pages/editorial-policy, /journals/pages/open_access/read_and_publish
- Sem texto útil (só menus): /pages/for-authors e a política de autoarquivamento (self_archiving_policy_b)
- Formulário de submissão: https://mc04.manuscriptcentral.com/epl

## Requisitos das diretrizes dos autores
- Template: OUP General Template no Overleaf, muito recomendado. Há modelo Word, menos preciso para estimar o tamanho. Arquivos em outros formatos são convertidos para LaTeX.
- Limite: Letters e Perspectives até 7 páginas tipografadas, incluindo título, resumo, referências e tudo mais. A Letter deve sustentar uma única afirmação central. A orientação é cortar, não comprimir.
- Resumo: não estruturado, 120 a 160 palavras, sem citações nem abreviações, símbolos e equações no mínimo (o texto do resumo sai em negrito). Texto de destaque opcional (teaser) de até 150 palavras. Palavras-chave: a página não menciona.
- Título: curto, sem abreviações, só a primeira palavra em maiúscula. Todos os autores com afiliação e um autor correspondente com endereço postal completo e e-mail.
- Seções finais obrigatórias na Letter: Conflicts of interest, Funding e Data availability. Agradecimentos opcionais.
- Referências: estilo Oxford SCIMED, numéricas em ordem de primeira citação, entre parênteses na descrição da página. Sem limite de número. Arquivo de estilo do EndNote disponível.
- Figuras: .jpeg, .jpg, .png, .tiff, .pdf, .eps. Cada figura em arquivo separado, legenda no manuscrito e não no arquivo, painéis com letras A, B, C no canto superior esquerdo. Texto alternativo (Alt text) obrigatório sob cada legenda. Resoluções mínimas de 300 a 1200 dpi conforme o tipo. Tabelas editáveis, numeradas e citadas em ordem.
- Material suplementar: enviado junto, em arquivos separados e nomeados (suppl1.pdf). O artigo deve ser compreensível sem ele, e o suplemento deve ser independente, sem remissões cruzadas. Não é revisado e só é hospedado pela OUP.
- IA: ferramentas de IA não são autoras. O uso para conteúdo, imagens, código, processamento de dados ou tradução deve ser declarado na carta de apresentação e nos Métodos ou nos Agradecimentos. A página cita a declaração do COPE.
- Dados: seção "Data availability" separada no fim, com link ou identificador. Repositórios com DOI são preferidos (Zenodo, repositório institucional). Exemplo de redação para o caso sem dados novos. Dados e software devem ser citados na lista de referências com identificador persistente.
- Licença e custo: licença padrão sem cobrança, ou acesso aberto CC BY com taxa pelo portal SciPris. Sem taxa por página nem por cor. A decisão editorial não depende do pagamento.

## Sobre o periódico
- Dez seções desde janeiro de 2022: General physics, Statistical physics and networks, Mathematical and interdisciplinary physics, Fluid and nonlinear dynamics, Nuclear and plasma physics, particles and fields, Atomic, molecular and optical physics, Condensed matter and materials physics, Biological and soft matter physics, Quantum information, Gravitation, cosmology and astrophysics.
- Tipos: Letters, Perspectives (só por convite) e Focus issues (só por convite).
- Indexação: Web of Science, Scopus, Inspec, INSPIRE-HEP, NASA ADS, entre outros. ISSN online 1286-4854. Publicada sob controle científico da European Physical Society.
- APC do acesso aberto CC BY: £1.600, €1.810 ou US$1.990, sem impostos. Cobrada só em artigos aceitos. Há descontos, isenções e acordos transformativos ("Read & Publish" para mais de 1000 instituições). A página consultada não menciona Brasil nem CAPES.

## Conselho editorial (nomes e afiliações, sem área de atuação na página)
Editor-chefe: Richard A. Blythe (Edimburgo). Vice-editores: Dario Benedetti, Pablo S. Cornaglia, Chantal Valeriani. A página não tem uma seção de Co-Editors. Membros ligados ao Brasil: Matheus Araújo Marques (UFPB), Maria Carolina de Oliveira Aguiar (UFMG), Vívian V. França (UNESP), Eduardo Miranda (Unicamp), Francisco A. Rodrigues (USP). Candidatos por afiliação a astrofísica, cosmologia e gravitação (a confirmar): Micol Benetti, Daniela Doneva, Zhoujian Cao, Giulia Gubitosi, Daniele Oriti, Edward Wilson-Ewing. Candidatos a física estatística e redes (a confirmar): Francisco A. Rodrigues, Cristina Masoller, Sakuntala Chatterjee, Jae Dong Noh, Sebastian Deffner.

## Diferenças em relação às páginas do epletters.net guardadas nesta pasta
- Citações: o epletters.net pedia colchetes e estilo ISO 690. A página da OUP descreve o estilo Oxford SCIMED, numérico, em ordem de primeira citação, entre parênteses. Conferir no formulário de submissão qual vale. A ordem de citação vale nos dois.
- Seções finais obrigatórias (conflitos de interesse, financiamento, disponibilidade de dados) e texto alternativo das figuras: só na página da OUP.
- IA: a página da OUP exige declaração também na carta de apresentação.
- Material suplementar: as duas fontes pedem independência do texto principal.

## Template do Overleaf
O OUP General Template (Overleaf, CC BY 4.0, código sob LPPL) usa a classe oup-authoring-template, a mesma do CTAN que adotamos (DEC-41). Opções de classe: estilos contemporary, modern e traditional, tamanhos large, medium, mediumone e small, mais unnumsec e webpdf. Referências embutidas em thebibliography ou arquivo .bib com oup-plain (numérico) ou oup-abbrvnat (autor e data). A página não dá número de versão nem data exata ("há 3 meses"), então não dá para comparar com o pacote que baixamos do CTAN (copyright 2026, sha256 025434f5).
