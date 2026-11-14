# paper_state_v7.md

**Paper P4 — *Critical Slowing Down Near Stellar Activity Minima***
**Estado em:** 2026-11-14, fecho da inspeção e da resolução do que não depende de mérito
**Substitui:** `paper_state_v6.md` (que permanece como registro) · **Memória longa:** `P4_RESEARCH_NOTEBOOK.md` (agora com D01–D80) · **Relatório:** `inspecao/RELATORIO_INSPECAO.md`

---

## 1 · O que mudou desde o v6

- **D41–D54 estão no caderno** (§4c), junto com Q10 e Q11 (§5) e as linhas de §8 e §9. A pendência de documentação do hand-off está fechada (`inspecao/checks.csv`, 2a-09 a 2a-13).
- **D55–D67 (§4d)** registram fatos conferidos e corrigem, por inclusão, texto de decisões e auditorias anteriores. Nenhuma Q# foi decidida e nenhuma recomendação registrada foi alterada.
- **A7, A8 e A13 foram executadas** (`audit/`). A7 parcial: falta Held & Kleinen 2004 (o arquivo com esse nome era outro artigo, D63).
- **A Tabela 4 de Egeland+2017 foi obtida** (D65): 6 349 linhas, 1966–2016, ciclos 20–24.
- **Os PDFs de Baum, Luhn, CLS V, CLS VI, Järvinen, Noyes, Oláh, Shah, Brandenburg, Korolik, Egeland e as versões do arXiv de Luhn e Baum estão em `bib/`**, com sha256 e título validado (`bib/MANIFEST.json`).
- **Errata** em `audit/ERRATA_2026-11-14.md`; **reparos do catálogo** em `consolidacao/rascunho_reparos_catalogo.csv` (arquivo lateral; o catálogo congelado não foi tocado).

## 2 · Números corrigidos (valem no lugar dos do v6)

| Assunto | v6 / documentos antigos | Valor conferido | Onde |
|---|---|---|---|
| Linhas de dados da Tabela 3 da CLS V | 52 380 (Δ = 8) | **52 372** | D55; `3.6-05` |
| Estrelas analisadas na CLS VI | 710 | **91**, em quatro faixas de massa; 710 é a CLS V | D60; `3.11-19` |
| Observações de Mount Wilson de HD 166620 em 1995–2002 | 158 (A10) | **119, digitalizadas de figura (grau C)**; 158 é o texto da versão publicada | D58; `3.4-61` |
| p do F-test de Luhn, 8.78 × 10⁻⁶ | "σ_S corrigido cai de 0.0027/0.0054 para 0.0019, com F-test de 8.78 × 10⁻⁶" | reproduz-se com variâncias **brutas** (8.80 × 10⁻⁶); com σ_S corrigidos p = 8.68 × 10⁻³ (bilateral) | D57; `3.4-50`, `3.4-52` |
| Ciclo de HD 3651 na CLS V | "não" (A11 §b.3) | **10.01 anos** | D67; `3.6-27` |
| Menor SSD/Smed com Nobs ≥ 45 | HD 55575, 0.45 % | HD 187923 **0.372 %**, HD 144579 0.397 %, HD 55575 0.448 % (o 0.45 % é o texto do artigo; a tabela difere, grau X) | D67; `3.6-24` a `3.6-26` |
| Reclassificações de Baum (D43) | "14, checksum reproduzido" | 13 mudam de tipo; 15 com `flat?` → `flat`; o 14 é o texto de Baum §4.2; grau B | D56; `3.8-08` a `3.8-11` |
| Medianas de B−V por grupo | `Long` 0.49; `Flat` 0.73 | `Long` 0.525; `Flat` limpas (5) 0.73; `Flat`+`Flat?` (15) 0.56 | D67; `3.9-30` a `3.9-41` |
| Série solar de Egeland | ciclos 15–24, ~20 440 pontos | **1966–2016, ciclos 20–24, 6 349 linhas** | D65; `3.12-01` a `3.12-13` |
| HD 3651 | candidata a transição | quatro períodos: B95 13.8, Saar 14.6, Oláh 11.6, CLS V 10.01 | A13-F1 |
| Períodos `CYCLE` perdidos pelo catálogo | "sem período" (6 estrelas) | impressos em B95 (grau B) | D64 |
| Faixa de validade de D53 | 0.44 < B−V < 0.82 | 78 estrelas dentro pela leitura aberta (82 pela fechada); o B−V da CLS V é derivado | D62; `3.7-09`, `3.7-10` |

## 3 · Q1–Q11, tabela única

Todas **abertas** e todas do pesquisador. "Estado" é o do caderno §5; a coluna "Novo" é o que esta rodada acrescentou.

| # | Questão | Novo nesta rodada |
|---|---|---|
| Q1 | Composição da amostra | I-06: a regra de exclusão por binaridade define as "cinco `Flat`"; I-12: a não-uniformidade está na presença (4/5 contra 6/13); I-13: D04 e D11 contra subsídios que já usam dados das candidatas |
| Q2 | O que conta como `Flat` | D51; HD 3651 tem ciclo na CLS V (D67) |
| Q3 | Largura de banda gaussiana | — |
| Q4 | Componente de 44 anos | — |
| Q5 | Binárias | — |
| Q6 | Medida do grupo `Flat` | o piso instrumental depende de qual número se cita (D67) |
| Q7 (caderno) | Subgigantes no `Flat` | — |
| Q8 | Migrar para R′_HK | D60 (CLS VI: 91 estrelas, por faixa de massa), D61 (escopo de Noyes), D62 (B−V); a recomendação registrada permanece: **não migrar** |
| Q9 | DFA no subconjunto Baum | ver "série anual ou bruta" (item 1 da §5) |
| Q10 | A transição é lenta o bastante para ter precursor? | A7-F3: as duas fontes de CSD lidas põem a condição de forçamento lento; A8-F2: precursores solares só qualitativos e sem tipo CSD |
| Q11 | Inclinação estelar | Korolik+2023 em `bib/` (τ Ceti), ainda não auditado |

**Desambiguação de "Q7".** No caderno, Q7 = subgigantes no grupo `Flat`. No protocolo §11, "questão 7" = "alguém já afirmou que grandes mínimos são imprevisíveis?" (respondida em A11/CLS VI e A8-F1). Este arquivo usa Q7 só no sentido do caderno e escreve "pergunta 7 do protocolo" para a outra (I-21).

## 4 · Bloqueios (ver caderno §6)

- **O pesquisador sobe:** Held & Kleinen 2004 (DOI 10.1029/2004GL020972), Livina & Lenton 2007 (10.1029/2006GL028672), Peng+1993 (10.1103/PhysRevE.47.3730).
- **Dados reais de Mount Wilson de HD 166620, 1995–2002** (Oláh e Soon): sem eles essas 119 linhas são grau C.
- **Opcionais:** versões publicadas de Järvinen & Strassmeier e Oláh; Dataverse.
- **Grau X que permanece:** incerteza dos offsets de Baum (D44); períodos de B95 relidos só uma vez (D64); A8 sem §3 e §5 de Usoskin; Vaquero+2011, Miyahara+2004, Nagaya+2012 não auditados.
- **Contradições abertas** (protocolo, regra 4): A9-F2 (HD 185144); 0.45 % contra a tabela da CLS V; 158 contra 119 resolvida como fato (D58), sem decisão sobre o uso.

## 5 · Decisões humanas: respondidas e pendentes

**Respondidas em 2026-11-14 (caderno §4d):** item 1 → **D68** (anual e bruta; papéis: **D76**, subsídios em `SUBSIDIOS_PAPEIS_SERIES.md`); item 3 / Q8 → **D69** (S e R′_HK); itens 4 e 5 → **D72**, **D73** (subsídios em `SUBSIDIOS_JUNCAO_E_D46.md`); item 6 → **D74** (esperar Held & Kleinen); item 7 → **D70** (subsídios em `SUBSIDIOS_RECEITA_SIGMA_S.md`); item 8 → **D75** (piso 0.37–0.45 %); item 10 → **D77** (subsídios em `SUBSIDIOS_LAYOUT_KIT.md`); item 11 → **D71**; Q2–Q7 → **D78** (abertas); Q1 → **D79** (espera os papéis). A14 (Korolik) executada para Q11.

**Pendentes, todas do pesquisador:** a distribuição dos papéis das séries (D76) e, depois dela, Q1; as escolhas adiadas dos itens 4, 5, 7 e 10 (D72, D73, D70, D77); o item 6 após Held & Kleinen (D74); Q2–Q7 e Q11. Nenhuma Q# está fechada.

## 6 · Estado dos arquivos

- **Alterado:** `P4_RESEARCH_NOTEBOOK.md` (só por inclusão, exceto a substituição prevista da tabela da §5 e da §6, e o cabeçalho "Última entrada"; a coluna "Subsídios" da §5 deixa de existir, como a instrução de incorporação mandava: a informação está nos documentos de origem). `bib/LEIAME.txt` foi reescrito porque dizia "pasta vazia".
- **Novos:** `audit/A7_theory.md`, `A8_usoskin.md`, `A13_olah.md`, `A14_korolik.md`, `SUBSIDIOS_*.md` (quatro), `audit/ERRATA_2026-11-14.md`, `consolidacao/rascunho_reparos_catalogo.csv`, `data/Egeland2017_table4_apjaa4e49t4_mrt.txt`, PDFs e `MANIFEST.json`/`DOWNLOAD_LOG.md` em `bib/`, `inspecao/`, `LICOES_PENDENTES.md`, `P4_MEMORANDO_DECISOES_2026-11-14.md`, este arquivo.
- **Congelados e inalterados:** `p4_pipeline.ipynb`, `baliunas_table2_full.csv`, A1–A6 e A9–A12, CSVs existentes, D01–D54.

**O pipeline permanece congelado.** Nenhuma linha foi tocada.
