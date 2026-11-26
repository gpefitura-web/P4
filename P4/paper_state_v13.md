# paper_state_v13.md

**Paper P4** · **Estado em:** 2026-11-26, fecho da fase "manuscrito completo v1" · **Substitui:** `paper_state_v12.md` · **Commit de referência da v1:** `72191da` (pacote refeito; `REPRODUCTION OK` em pasta limpa)

## 1. Onde estamos
- Manuscrito v1 completo e verificado: `manuscrito/main.tex` (New Astronomy, 23 páginas, 36 referências), `repositorio/` (115 arquivos, MIT), `manuscrito_overleaf.zip`, `repositorio_zenodo_v1.0.0.zip`. Leitura final feita sobre o PDF recompilado; números conferidos contra `pipeline_v2/results/`.
- Resultados vigentes (D121/D122): H1 só sustentada em relação ao mínimo 2 (IC da razão σ 1,7–4,2; mínimo 1: 0,8–2,2); H2 não testável como projetado (registro de HD 166620 termina em 1995); varredura nula em 23 segmentos + Sol (2 de 192 células marcadas, esperado ~6–10); teste de tamanho 3,2 % e 4,2 %, sem poder com ciclo; controle positivo (Hopf supercrítico): ao perder o ciclo, autocorrelação e variância **caem**.
- **O pesquisador anunciou mudanças radicais no paper** (ainda não especificadas). A v1 serve de base e de ponto de retorno.

## 2. Pendências
- Do pesquisador: endereço e e-mail; declaração de IA; Zenodo e DOI; confirmar financiamento, conflito de interesses e CRediT; licenças de Baum e Luhn; acordo CAPES–Elsevier; título final; Wilson 1978 (sem PDF); decidir se a lista volta a 30 referências.
- Análises não feitas (limites declarados na v1): Hopf subcrítico e ruído multiplicativo; curva de poder com ciclo real; efeito da interpolação; amplitude do ciclo (só 4 de 23 estrelas).
- Rastreabilidade: `RASTREABILIDADE_PENDENTE.md`.

## 2b. Subsídios da reestruturação (D125, exploratórios)
- Memorando: `DECISAO_REESTRUTURACAO.md`. Resumo: H1 só vale frente ao mínimo 2 (o mín. 1 inverte em f ≈ 1,58 %); o teste detecta a perda de ciclo pela cauda inferior (variância: AUC 0,96, rejeição 34 %), mas tem poder baixo para CSD verdadeiro (AUC 0,55–0,61); a era HKP-2 sozinha muda τ em 31 % das células. Eixo do artigo, revista e novas rodadas aguardam o pesquisador.

## 2c. Decisões do pesquisador (D126)
- **Eixo 1** (calibração e poder do CSD em séries anuais do índice S), reescrita do zero com pipeline e 36 referências; CSD mantido como ideia, com possíveis dados novos (Vaquero entregue; séries de outros objetos a fornecer); revista em aberto. Análises D126 prontas em `pipeline_v2/results_explore/` (controle positivo completo, curva de projeto, degrau, QQ, Dalton); resumo em `DECISAO_REESTRUTURACAO.md` §6b. Próximo: plano curto de reescrita e fluxo da regra 1; termos de uso de Vaquero a conferir.

## 2d. Reescrita do eixo 1, passo 1 concluído (2026-11-26)
- Análises promovidas: `pipeline_v2/calibration/` (scripts) e `pipeline_v2/results_calibration/` (saídas completas, com `CALIBRATION_MANIFEST.sha256`); os caminhos `explore/` e `results_explore/` citados em D125 e D126 passaram a esses nomes (git mv, conteúdo igual). Modo `--quick` (~4 min no total) em `results_calibration_quick/`; `verify_calibration.py --manifest --quick` confere o hash das saídas completas e a concordância do modo reduzido (24+80+96+28+8 taxas dentro de 4 erros-padrão; τ dos dados idêntico): **OK**.
- Geradores sem número digitado: `make_macros_calibration.py` → `manuscrito/calibration_macros.tex` (353 macros), `make_figures_calibration.py` (`figstyle.py`) → `manuscrito/figures/cal_fig1…7` (PDF e EPS), `make_tables_calibration.py` → `cal_table_simulations.tex`, `cal_table_stars.tex`. Duas execuções seguidas dão arquivos idênticos byte a byte. `fetch_vaquero.py` aceita só `--from` com sha256 e cabeçalho conferidos.
- **Achado (regra 3, a registrar no texto):** na tabela estelar o rótulo "subgigante" do catálogo congelado contradiz o log g de Baum em dois casos: HD 10700 (rótulo sim, log g 4,60, G8V) e HD 217014 (rótulo não, G2IV, log g 4,32). As quatro estrelas Flat têm rótulo ou tipo evoluído (HD 23249 log g 3,75; HD 182572 IV; HD 190360 IV-V), o que apoia o ponto 5 do Revisor 2. HD 3795 tem mediana de 8 observações por ano (mínimo 1). Tipos espectrais só vêm de Baum (grau A); as 10 estrelas do HK v2001 ficam com "--".
- Falta: passos 2 a 5 (texto novo, leitura do PDF, `make_repositorio.py` com os scripts novos, `reproduce.sh` com modo reduzido e `--full`, prova em pasta limpa, zips) e `check_manuscript_constants.py` para o texto novo. Termos de uso e URL de Vaquero seguem pendentes.

## 3. Próxima etapa
`PROMPT_PROXIMO_CHAT_REESTRUTURACAO.md`.
