# paper_state_v11.md

**Paper P4** · **Estado em:** 2026-11-26, segunda rodada estelar (série padronizada), revisões implementadas, manuscrito para leitura final · **Substitui:** `paper_state_v10.md` · **Último commit de conteúdo antes do fecho:** ver `git log -3` (o fecho vem depois)

## 1. Onde estamos
- **Pipeline executado duas vezes** (D105 e D121). A segunda, **oficial**, ajusta o ARMA dos surrogates na série padronizada (a primeira, em escala bruta, escolhia a ordem do AIC conforme a escala; ver D120). Mesma semente (20261124). Resultado: τ idêntico; as mesmas 2 células marcadas a 50 % (HD 23249 e HD 217014); p dos surrogates mudam até 0,51 (8 % das células por mais de 0,05); ordem do ARMA igual entre S e R'HK. H1, H2 (não suportada e não testável como projetada), grupos: sem mudança de conclusão. A 1ª rodada fica em `pipeline_v2/archive/` só para `compare_runs.py`.
- **Acrescentado pela D121:** poder do teste com ciclo (praticamente nulo: rejeição de 4,5 % tanto para série constante quanto crescente, contra 5,5 % e 7,5 % sem ciclo); cobertura de observações por ano (18 de 23 segmentos têm algum ano com menos de 5); sensibilidade à interpolação; AR(1) esperado do ruído branco após o filtro σ = 1 (−0,55; a mediana observada, −0,31, fica acima). Tudo com macros e arquivos em `results/`.
- **Manuscrito:** `manuscrito/main.tex` (`elsarticle`, New Astronomy), 18 páginas em formato de revisão, resumo de 243 palavras, 4 figuras maiores (largura do texto), `alt_text.md`, highlights, `references.bib` (Crossref; Kuehn 2011 e 2013, Bury 2020 acrescentados). **Pacote:** `repositorio/` (107 arquivos), `reproduce.sh` (~12 min), `MANIFEST.sha256`, zips do Zenodo e do Overleaf. Prova em pasta limpa: ver D121.
- Decisões D105–D121 no caderno; pareceres e avaliações em `REVISOES_INDEPENDENTES.md` (três rodadas).

## 2. Regra que governa a próxima etapa
Regra 9 (`CLAUDE.md`): edite a fonte, `python3 P4/make_repositorio.py`, `reproduce.sh` numa cópia limpa (venv com `requirements.txt`, `fonttools==4.68.0`; exige `REPRODUCTION OK`), só então os zips. **Não reexecutar `run_all.py` no projeto sem pedido explícito.**

## 3. Pendências
- **Do pesquisador (manual):** declaração de IA no Overleaf; e-mail do autor correspondente e endereço postal; confirmar financiamento, conflito de interesses e CRediT; publicar no Zenodo e pôr o DOI (`ZENODO_DEPOSITO.md`; depois refazer o pacote); licença dos artigos de Baum e de Luhn; lista de elegíveis do acordo CAPES–Elsevier e participação do IFTM; título final; copiar `alt_text.md` e `highlights.docx` no formulário; consulta opcional ao editor.
- **Fora do escopo declarado no manuscrito (análise nova, exige insumo ou decisão):** controle positivo com modelo dinâmico (Hopf estocástico); curva de poder sobre período e amplitude do ciclo; correlação da variância normalizada com a amplitude do ciclo (falta amplitude tabelada); barras de incerteza na Figura 1 e intervalo nulo na Figura 4; referências adicionais sugeridas (Metcalfe e van Saders, Wright 2004, Baliunas e Jastrow 1990, Henry et al. 1996, Dakos 2008, Boettner e Boers 2022) só com PDF lido.
- **Rastreabilidade ainda aberta:** `RASTREABILIDADE_PENDENTE.md` (limiares de classe de Baliunas, faixa da Tabela 4 de Egeland, "afeta duas estrelas" da regra 1day/sigma, páginas das paráfrases de Kuehn e Bury).
