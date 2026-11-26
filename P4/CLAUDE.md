# CLAUDE.md — Paper P4 (Critical Slowing Down Near Stellar Activity Minima)

Pesquisador: Prof. Airton M. S. Borin Junior (IFTM, Uberaba). Conversa em português; **todo código, comentário de código e saída de script em inglês**.

## Estado do projeto
Fase de auditoria. O pipeline (`p4_pipeline.ipynb`) está **congelado** até a consolidação ser assinada. Nenhum código é alterado sem pedido explícito. O estado corrente está em `paper_state_v6.md`; a memória longa de decisões, em `P4_RESEARCH_NOTEBOOK.md` (D01–D40) e `DECISOES_D41_D54.md` (D41–D54).

## Regras que valem sempre (do P4_AUDIT_PROTOCOL.md)
1. Ler, não lembrar. Nenhum valor astronômico vem de memória de treinamento; todo número remonta a uma tabela, seção ou página de uma fonte, ou a um arquivo deste diretório.
2. Todo valor leva grau: A (duas verificações independentes ou checksum), B (leitura limpa, uma fonte), C (figura, OCR incerto, inferido), X (não obtido ou fontes discordam). C e X não chegam ao manuscrito.
3. Contradição é achado, não obstáculo. Registrar as duas versões; nunca escolher em silêncio.
4. Decisões `D##` são imutáveis. Uma decisão revogada recebe `status: revogada` e uma entrada nova. Questões em §8 do caderno não são reabertas sem fonte nova.
5. Questões `Q#` abertas são decisão humana. Claude levanta subsídios e não decide.
6. Catálogos estendidos ficam ao lado de `baliunas_table2_full.csv` (congelado), nunca fundidos (D36).
7. Dados de entrada ficam como estão. Python sempre com `python -I script.py` para ler arquivos de `data/`; scripts novos vão em pasta própria, não dentro de `data/`.
8. Proibido derivar fotometria própria (digitalizar figuras, fotometria de abertura). Só dados públicos já reduzidos.

## Estrutura
- `audit/` — A1 a A6 e A9 a A12 (extrações graduadas) e CSVs de cruzamento
- `data/` — TSVs do VizieR (nomes com `_` no lugar de `:`; ver README_HANDOFF.md)
- raiz — catálogos CSV, estado, caderno, protocolo, pipeline
- `historico/` — `paper_state_v2.md` (superado; não usar como fonte)
- `bib/` — vazio no zip; os PDFs estão em github.com/gpefitura-web/P4

## Pendentes que não dependem de você
A7 (Scheffer 2009 + Held & Kleinen 2004) e A8 (Usoskin 2017) não foram executadas. A tabela 4 de Egeland+2017 (série solar) ainda não foi obtida.

## Estado atual (2026-11-26) e regra 9
O pipeline novo, o manuscrito (New Astronomy) e o pacote de reprodução existem e foram verificados (D105–D122). O estado corrente está em `paper_state_v14.md` (manuscrito v2, eixo 1: calibração e poder do CSD; v1 congelada no commit `72191da`; não reexecutar `run_all.py` sem pedido). Análises novas em `pipeline_v2/calibration/` (saídas completas em `pipeline_v2/results_calibration/`, D125–D127); pacote 2.0.0 em `repositorio/`.
9. **Tudo que vai para o manuscrito precisa ser sustentado no repositório (`repositorio/`):** números vêm de macros gerados de `pipeline_v2/results/`, figuras e tabelas vêm de scripts do pacote, e afirmações sobre dados ou código têm arquivo no pacote ou são citações com PDF e página. Depois de qualquer mudança: `make_repositorio.py`, depois `reproduce.sh` numa cópia limpa.

