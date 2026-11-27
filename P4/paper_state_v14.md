# paper_state_v14.md

**Paper P4** · **Estado em:** 2026-11-26, manuscrito v2 (eixo 1) · **Substitui:** `paper_state_v13.md` · **v1 congelada:** commit `72191da`

## 1. Onde estamos
- Manuscrito v2: `manuscrito/main.tex` (New Astronomy, 33 páginas no formato de revisão, 37 referências), título "Can critical slowing down indicators detect the loss of a stellar activity cycle? Size, power and positive controls on annual S-index series". Eixo escolhido pelo pesquisador: calibração e poder do CSD, com a ideia do CSD mantida (dados longos como condição).
- Resultados (todos exploratórios exceto H1/H2, que foram declaradas antes): ver `DECISAO_REESTRUTURACAO.md` §6b e D125–D127. Em síntese: teste com tamanho próximo do nominal e conservador com ciclo; perda de ciclo derruba variância e autocorrelação (cauda inferior detecta, AUC da variância 0,90–0,99); poder baixo para CSD verdadeiro (AUC 0,61 em 30 anos, 0,82 em 200 sem ruído nem ciclo); degrau instrumental desloca τ; varredura estelar sem excesso; HD 166620 só frente ao mínimo 2 (o mínimo 1 inverte em f ≈ 1,58 %); Dalton sem sinal.
- Pacote 2.0.0: `repositorio/` (169 arquivos), `reproduce.sh` (padrão ~12 min; `--full` ~1,5 h), prova em pasta limpa: `REPRODUCTION OK` nos modos padrão e `--full`. Zips: `repositorio_zenodo_v2.0.0.zip`, `manuscrito_overleaf.zip` (`make_overleaf_zip.py`).
- Análises: `pipeline_v2/calibration/`, saídas completas em `pipeline_v2/results_calibration/`.

## 2. Pendências
- Do pesquisador: afiliação (endereço, CEP), e-mail, declaração de IA, financiamento, conflito de interesses e CRediT; Zenodo e DOI; termos de uso e URL do catálogo de Vaquero; séries de outros objetos; revista; Wilson 1978 (sem PDF).
- Análises não feitas: nulo com ciclo explícito; Keck 2004–2021 e HD 4915; varredura estelar com 10^4 surrogates; médias por estação; estágio evolutivo por Gaia; entrada em Maunder (não analisável em médias anuais).
- Rastreabilidade: `RASTREABILIDADE_PENDENTE.md`; pendências do manuscrito: `MANUSCRITO_PENDENCIAS.md`.

## 3. Próxima etapa
Handoff: `PROMPT_PROXIMO_CHAT_SUBMISSAO_V2.md`. Passo 5 concluído (D128): pareceres e estado da v2 em `REVISOES_INDEPENDENTES.md` (quinta rodada), nova leitura de revisão feita, texto com uma frase nova sobre os 119 pontos digitalizados de 1995–2002 da tabela de Luhn (não usados). Decisões abertas: revista, Vaquero, séries de outros objetos, análises não feitas, placeholders.
