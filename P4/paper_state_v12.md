# paper_state_v12.md

**Paper P4** · **Estado em:** 2026-11-26, bibliografia expandida e lida, análises que faltavam feitas, manuscrito para leitura final · **Substitui:** `paper_state_v11.md` · **Último commit de conteúdo antes do fecho:** ver `git log -3`

## 1. Onde estamos
- Estado de v11 (segunda rodada estelar com série padronizada, D121) continua valendo. **D122** (esta etapa): **29 referências**, todas com PDF validado e lidas (`audit/A15_leitura_referencias_D122.md`); 8 referências sugeridas ficaram pendentes por falta de PDF aberto (`bib/DOWNLOAD_LOG.md`).
- **Resultados novos que mudam o texto:** (i) **H1 só é sustentada em relação ao mínimo 2** (bootstrap por temporada: σ(mín 2)/σ(grande) IC 1,7–4,2; σ(mín 1)/σ(grande) IC 0,8–2,2); (ii) **controle positivo:** num oscilador de Hopf que perde o ciclo, a autocorrelação e a variância **caem**, o contrário do assumido nas hipóteses unilaterais; (iii) **poder:** nulo em toda a grade de períodos (8–16 anos) e amplitudes do ciclo; com ciclo forte o teste fica conservador; (iv) só 4 de 23 estrelas têm amplitude de ciclo homogênea, então "atribuímos ao ciclo" segue não testável.
- Correções de fatos citados: 111 estrelas e o Sol (Baliunas); cinco configurações de quatro instrumentos (Egeland); origem e natureza dos ruídos de Luhn; rótulos "sigma" e "1 day" (Baum).
- Manuscrito: `main.tex` (resumo de 246 palavras), figuras com barras de incerteza (Fig. 1) e faixas nulas (Fig. 4), `alt_text.md`, highlights (5 itens). Pacote `repositorio/` com `reproduce.sh` (~30 min); prova em pasta limpa: **`REPRODUCTION OK`** (115 arquivos, 22 páginas, 29 referências), zips atualizados.

## 2. Regra que governa a próxima etapa
Regra 9 (`CLAUDE.md`). **Não reexecutar `run_all.py` no projeto sem pedido explícito** (já houve duas rodadas, D105 e D121; a D122 só acrescentou colunas).

## 3. Pendências
- **Do pesquisador (manual):** declaração de IA, e-mail e endereço, financiamento, conflito de interesses e CRediT; Zenodo e DOI (depois refazer o pacote); licenças de Baum e Luhn; acordo CAPES–Elsevier; título final; copiar `alt_text.md` e `highlights.docx` no formulário; **subir os PDFs pendentes** se quiser citá-los (Vaughan+1978, Wilson 1978, Baliunas & Jastrow 1990, Radick+2018, Dakos+2008, Lenton+2011, Wiesenfeld 1985, Duncan+1991; Lenton+2012 e Boettner & Boers 2022 foram obtidos na segunda rodada e são citados).
- **Análises ainda não feitas (limites declarados no texto):** controles positivos adicionais (Hopf subcrítico, ruído multiplicativo); curva de poder com propriedades de ciclo reais; efeito da interpolação sobre os indicadores; reanálise com amplitude do ciclo (falta fonte).
- **Rastreabilidade:** `RASTREABILIDADE_PENDENTE.md` (agora também: "15.8 yr" e "10 yr" de Saar & Brandenburg, "seven of 32 stars" de Lockwood, "1986–1990" de Luhn, digitados com página no A15).
