# paper_state_v8.md

**Paper P4 — *Critical Slowing Down Near Stellar Activity Minima***
**Estado em:** 2026-11-24, fecho da reconstrução do pipeline (D105)
**Substitui:** `paper_state_v7.md` (permanece como registro). Referência congelada: `consolidacao/APROVACAO_2026-11-24.md` (hashes conferidos, 5/5).

## 1 · O que mudou desde o v7
- Pipeline novo em `pipeline_v2/` (notebook antigo intocado). Passos 1–10 concluídos; critérios "pronto" cumpridos (`pipeline_v2/PROGRESSO.md`).
- Execução única: 24 segmentos (23 estrelas elegíveis + Sol exploratório); 4 configurações de tendência (none, σ = 1, 3, 5 anos); janelas 25–75 %; AR(1) e variância; S e R′_HK; 1 000 surrogates ARMA(p,q) (p, q ≤ 2, AIC); semente 20261124.
- Autoteste dos surrogates: rejeição de 3.2 % (p_upper) e 4.2 % (p_D22) em AR(1) nulo.

## 2 · Fatos (de `pipeline_v2/results/REPORT.md`; sem interpretação)
- H1 (HD 166620): σ_S conta A 0.0027 / 0.0054 / 0.0019; conta B 0.0028 / 0.0048 / 0.0015; F-test mínimo 1 contra grande mínimo p = 8.80 × 10⁻⁶ (variâncias brutas), 8.68 × 10⁻³ (corrigidas, conta A).
- Indicador temporal (janela 50 %): nenhum segmento chega a concordância ≥ 3 de 4 configurações (τ > 0 e p_upper < 0.05), nem para AR(1) nem para variância. H2 (HD 166620) entra nessa contagem; n = 1, exploratório; "não suportado" ≠ refutação (D90).
- τ de R′_HK = τ de S em todas as comparações (R′_HK é linear em S).
- Testes entre grupos: ver `REPORT.md` §6 (desenho a confirmar, `ACHADOS.md` #7).

## 3 · Pendências para o pesquisador (`pipeline_v2/ACHADOS.md`)
1. ~~Linhas `1day/sigma` de Baum~~ — resolvido em D106: entram (HD 190360 segue elegível); a execução oficial já as incluía.
2. ~~Cauda do p~~ — resolvido em D107: P(τ* ≥ τ).
3. ~~Testes entre grupos~~ — D108/D109: par primário p = 0.887; Holm por métrica × configuração, 2 de 30 com p_Holm < 0.05 (variância de ciclo, CYCLE_Excellent > Flat; confundidor declarado) (`REPORT.md` §7).
4. ~~`inspecao/run_all.sh`~~ — rodado uma vez após o fecho (ACHADOS #12); hashes congelados intactos.
5. Figuras e manuscrito: não iniciados (fora do escopo desta etapa).
- Verificação final e recomendações: `RECOMENDACOES_POS_PIPELINE.md`.
