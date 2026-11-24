# PROGRESSO — pipeline_v2

| Passo | Estado | Commit/nota |
|---|---|---|
| 0. Hashes de APROVACAO_2026-11-24.md | OK (5/5 batem) | venv em scratchpad; statsmodels 0.15.0 instalado |
| 1. Entrada de dados (`p4io.py`) | PRONTO | `test_step1.py`: 62135 / 61662 / 59 (Baum), 35 (v2001), 6349 (Egeland) |
| 2. Séries anuais (`annual.py`) | PRONTO | `test_step2.py`: segmentos MW e Keck das 27 estrelas = catálogo e 17 §2 (regra de flag do catálogo; ACHADOS #3) |
| 3. Indicadores (`indicators.py`) | PRONTO | `test_step3.py`: SD do AR(1) 0.249 (w=12), 0.181 (w=24) ≈ √((1−c²)/w) |
| 4. Remoção de tendência (`detrend.py`) | PRONTO | `test_step4.py`: reproduz 17 (3) exatamente (L=30 e 54; none, σ=1,3,5) |
| 5. Surrogates (`surrogates.py`) | PRONTO | autoteste: taxa de rejeição 3.2 % (p_upper) e 4.2 % (p_D22), na faixa 3–7 % (`results/autotest_step5.txt`) |
