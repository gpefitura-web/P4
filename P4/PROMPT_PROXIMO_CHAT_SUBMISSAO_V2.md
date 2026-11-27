# PROMPT_PROXIMO_CHAT_SUBMISSAO_V2: fechar a submissão do manuscrito v2 (2026-11-27)
Para colar na abertura da próxima conversa. Português nas conversas; código, comentários e saídas de script em inglês; `python -I` ao ler `data/`. Repositório gpefitura-web/P4, pacote em `P4/`. Branch de trabalho: a que o sistema indicar (a etapa anterior terminou na `claude/gracious-carson-bjbqo2`). Não criar pull request.

## 0. Situação
- **Manuscrito v2** (eixo 1: calibração e poder do CSD): `manuscrito/main.tex`, 33 páginas, New Astronomy, 37 referências. Título: "Can critical slowing down indicators detect the loss of a stellar activity cycle? Size, power and positive controls on annual S-index series". A v1 está congelada no commit `72191da`.
- **Pacote 2.0.0** (`repositorio/`, `repositorio_zenodo_v2.0.0.zip`): `REPRODUCTION OK` em pasta limpa no modo padrão (~12 min) e no modo `--full` (~1,5 h). `manuscrito_overleaf.zip` por `make_overleaf_zip.py`.
- Registros: D125–D128 em `P4_RESEARCH_NOTEBOOK.md`; estado em `paper_state_v14.md`; pareceres e o que a v2 fez em `REVISOES_INDEPENDENTES.md` (quinta rodada); lições até L34; pendências em `MANUSCRITO_PENDENCIAS.md` e `RASTREABILIDADE_PENDENTE.md`.
- Análises: `pipeline_v2/calibration/`, saídas completas em `pipeline_v2/results_calibration/` (manifesto de hashes), modo `--quick` em `results_calibration_quick/`.

## 1. Primeira coisa: perguntar, não presumir
Abrir pedindo ao pesquisador, em uma rodada curta: (a) **revista** (New Astronomy mantida por ora; alternativa: periódico de métodos ou análise de dados, o que muda formato e escopo); (b) **termos de uso e URL do catálogo de Vaquero** (SILSO/HASO); (c) se há **séries de outros objetos** para dar poder ao CSD (origem aberta, cadência, termos); (d) quais **análises não feitas** valem a pena antes de submeter: nulo com ciclo explícito, médias por estação, decomposição da variância intra/entre estações, ponderação pela incerteza, série Keck 2004–2021 e HD 4915, varredura com 10^4 surrogates, intervalo do método B por enumeração, Gaia; (e) os **placeholders dele**: endereço e CEP, e-mail, declaração de IA, financiamento, conflito de interesses, CRediT, DOI do depósito (Zenodo). Só então planejar.

## 2. Regras que continuam valendo
1. **Regra 9:** tudo que vai para o manuscrito é sustentado no repositório. Números por macro; figuras e tabelas por script do pacote; literatura só com PDF validado. Fluxo: editar a fonte → `python3 P4/make_repositorio.py` → `python3 P4/make_overleaf_zip.py` → prova em **cópia limpa fora do projeto** (`SSL_CERT_FILE=/root/.ccr/ca-bundle.crt PYTHON=<venv>/bin/python [VAQUERO_FILE=<csv>] bash reproduce.sh`, ~12 min, segundo plano com Monitor; exige `REPRODUCTION OK`) → só então commit de `repositorio/` e zips.
2. Análise nova depois de ver os dados: D## nova, declarada no texto como decidida depois e exploratória. H1 e H2 foram declaradas antes e assim ficam.
3. Não reabrir D01–D127. Revogar = nova D## e `status: revogada` na antiga. Congelados: `p4_pipeline.ipynb`, `baliunas_table2_full.csv`, `consolidacao/*`, `pipeline_v2/run_all.py` e `results/` (não reexecutar sem pedido explícito, arquivando a saída antiga).
4. ANTILOOP: no máximo 2 tentativas por falha; sem `sleep` nem polling; tarefas longas em segundo plano com Monitor; `OMP_NUM_THREADS=1` em jobs com `multiprocessing`.
5. Downloads só por vias legais e abertas; validar a primeira página e o hash de todo PDF (L30–L32); nunca adivinhar identificadores.
6. Nenhum nome de ferramenta ou de modelo de IA em arquivos do repositório, do pacote ou do manuscrito. Declaração de IA, financiamento, conflito de interesses e CRediT são do pesquisador.
7. Commits com as linhas de atribuição da sessão; push na branch; nenhum PR; `repositorio/` e zips só depois do `REPRODUCTION OK`.
8. Antes de aceitar uma frase de ordem cronológica no texto, conferir contra o registro (L34). Prosa em inglês: aplicar a skill de humanização.

## 3. Ambiente (some entre sessões)
`python3 -m venv <scratchpad>/venv && pip install -r P4/repositorio/requirements.txt` (Python 3.13; `fonttools==4.68.0` fixado). TeX: `apt-get update` e `apt-get install -y --no-install-recommends texlive-latex-base texlive-latex-recommended texlive-fonts-recommended texlive-publishers lmodern cm-super poppler-utils`. Compilar com `pdflatex`, `bibtex`, `pdflatex` duas vezes; conferir a data do PDF contra o fonte antes de ler. Download da Tabela 4 de Egeland: `SSL_CERT_FILE=/root/.ccr/ca-bundle.crt`.

## 4. Leitura inicial (só isto)
`git pull`; `P4/CLAUDE.md` → `paper_state_v14.md` → `MANUSCRITO_PENDENCIAS.md` (seção final) → `RASTREABILIDADE_PENDENTE.md` → `REVISOES_INDEPENDENTES.md` (quinta rodada) → `repositorio/README.md` → este arquivo. Caderno (D01–D128): Grep de D##. Lições: `LICOES_PENDENTES.md`.

## 5. Entregáveis da próxima etapa
Plano curto acordado com o pesquisador antes de edição grande; depois execução pelo fluxo da regra 1; `MANUSCRITO_PENDENCIAS.md`, `paper_state` (v14 → v15), caderno (nova D##), `LICOES_PENDENTES.md` e `RASTREABILIDADE_PENDENTE.md` em dia. Se a revista mudar, adaptar formato, highlights e guia de autores sem mexer nos números.
