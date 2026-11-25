# paper_state_v9.md

**Paper P4** · **Estado em:** 2026-11-25, fecho da etapa de pipeline, figuras, manuscrito e pacote de reprodução · **Substitui:** `paper_state_v8.md` (registro) · **Último commit de conteúdo antes deste fecho:** be93d62 P4: prova em pasta limpa refeita sem a Tabela 4 de Egeland (REPRODUCTION OK), D117

## 1. Onde estamos
- **Pipeline reconstruído e executado uma vez** (D105): 24 segmentos (23 estrelas e o Sol exploratório), 4 configurações de tendência, 5 janelas, AR(1) e variância, 1 000 surrogates ARMA. Resultados em `pipeline_v2/results/`.
- **Resultado:** H1 (variabilidade de HD 166620 menor no grande mínimo) descritiva; H2 não suportada e **não testável como projetada** (o registro de Mount Wilson termina em 1995, antes da transição); teste com tamanho nominal e poder baixo; nenhum segmento com ≥ 3 de 4 configurações. Detalhe em `pipeline_v2/results/REPORT.md` e no manuscrito.
- **Decisões de execução registradas no caderno:** D105 (pipeline), D106 (linhas `1day/sigma` entram), D107 (cauda do p: P(τ* ≥ τ)), D108 e D109 (testes entre grupos: par primário e Holm por bloco), D110 (manuscrito), D111 (cor, Courier Prime, revisões independentes), D112 (revista: New Astronomy), D113 (versão para leitura final), D114 (conferência com o guia da revista), D115 (pasta para o repositório), D116 (licença MIT, Zenodo), D117 (Tabela 4 de Egeland fora do pacote), D118 (fecho).
- **Manuscrito:** `manuscrito/main.tex` (classe `elsarticle`, formato New Astronomy, todo o texto em um arquivo; macros e Tabela 2 em blocos gerados), `references.bib` (Crossref), 4 figuras em PDF e EPS, highlights. Título em uso: "Testing critical slowing down in Mount Wilson S-index of Sun-like stars". `manuscrito_overleaf.zip`.
- **Pacote para o repositório:** `repositorio/` (95 arquivos; gerado por `make_repositorio.py`), `reproduce.sh`, `MANIFEST.sha256`, `LICENSE` (MIT), `CITATION.cff`, `.zenodo.json`; `repositorio_zenodo_v1.0.0.zip`. **Prova em pasta limpa: `REPRODUCTION OK`.**

## 2. Regra que governa a próxima etapa
**Tudo que vai para o manuscrito precisa ser sustentado no repositório** (`repositorio/`): todo número vem de macro gerado de `pipeline_v2/results/`; toda figura e tabela vem de script do pacote; toda afirmação sobre dados, código ou escolhas de análise tem arquivo no pacote que a sustente ou é declarada como citação com PDF e página. Mudou algo? Edite a fonte, rode `python3 P4/make_repositorio.py` e `reproduce.sh` numa cópia limpa **antes** de atualizar o Overleaf ou o zip do Zenodo. Lacunas conhecidas: `RASTREABILIDADE_PENDENTE.md`.

## 3. Pendências
- **Do pesquisador (manual):** declaração de IA no Overleaf; e-mail do autor correspondente e endereço postal; confirmar financiamento, conflito de interesses e CRediT; publicar no Zenodo e pôr o DOI (`ZENODO_DEPOSITO.md`); licença dos artigos de Baum e de Luhn (dados no pacote); lista de elegíveis do acordo CAPES–Elsevier e participação do IFTM; título final; consulta opcional ao editor da New Astronomy.
- **Técnicas (próximo chat):** rastreabilidade (`RASTREABILIDADE_PENDENTE.md`: macros para as contagens digitadas à mão e um teste das constantes de projeto); texto alternativo das figuras; revisão final de leitura; BibTeX já completo (Crossref); manter as chaves e os DOIs conferidos.
- **Fora de escopo declarado no manuscrito (análise nova, exige decisão):** curva de poder com ciclo injetado; sensibilidade à interpolação; taxa nula da regra de 3 de 4; bootstrap em blocos para H1.
