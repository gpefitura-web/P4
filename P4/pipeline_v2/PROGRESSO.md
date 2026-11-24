# PROGRESSO — pipeline_v2

| Passo | Estado | Commit/nota |
|---|---|---|
| 0. Hashes de APROVACAO_2026-11-24.md | OK (5/5 batem) | venv em scratchpad; statsmodels 0.15.0 instalado |
| 1. Entrada de dados (`p4io.py`) | PRONTO | `test_step1.py`: 62135 / 61662 / 59 (Baum), 35 (v2001), 6349 (Egeland) |
| 2. Séries anuais (`annual.py`) | PRONTO | `test_step2.py`: segmentos MW e Keck das 27 estrelas = catálogo e 17 §2 (regra de flag do catálogo; ACHADOS #3) |
| 3. Indicadores (`indicators.py`) | PRONTO | `test_step3.py`: SD do AR(1) 0.249 (w=12), 0.181 (w=24) ≈ √((1−c²)/w) |
| 4. Remoção de tendência (`detrend.py`) | PRONTO | `test_step4.py`: reproduz 17 (3) exatamente (L=30 e 54; none, σ=1,3,5) |
| 5. Surrogates (`surrogates.py`) | PRONTO | autoteste: taxa de rejeição 3.2 % (p_upper) e 4.2 % (p_D22), na faixa 3–7 % (`results/autotest_step5.txt`) |
| 6. H1 (`state_comparison.py`) | PRONTO | `test_step6.py`: σ_S conta A 0.0027/0.0054/0.0019, B 0.0028/0.0048/0.0015; F-test p = 8.80e-6 (bruto), 8.68e-3 (corrigido A) |
| 7. R′_HK (`rhk.py`) | PRONTO | `test_step7.py`: log R′_HK −4.959 / −4.948 / −4.764 e R_phot/R_HK 0.486 / 0.054 / 0.006 (3.7-12 a 3.7-14) |
| 8. Execução única (`run_all.py`) | PRONTO | uma execução oficial; saídas em `results/` (seed 20261124) |
| 9. Relatório de fatos (`report.py` → `results/REPORT.md`) | PRONTO | sem interpretação |
