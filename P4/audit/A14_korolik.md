# Audit A14 — Korolik et al. 2023, AJ 166, 123 (τ Ceti, inclinação)

| | |
|---|---|
| **Data** | 2026-11-14 |
| **Estado** | **fechada** (leitura das seções relevantes a D51/Q11; resto do artigo, interferometria e dinâmica, só lido por títulos) |
| **Arquivo** | `bib/Korolik_2023_AJ_166.pdf` (9 páginas; título "Refining the Stellar Parameters of τ Ceti: a Pole-on Solar Analog" e DOI `10.3847/1538-3881/ace906` conferidos na página 1; `bib/MANIFEST.json`) |
| **Método** | texto nativo (`pdftotext -layout`); páginas = página do PDF |
| **Motivo da unidade** | pedida pelo pesquisador para subsidiar Q11 ("Auditar Korolik antes"); fonte da afirmação de D51 sobre τ Ceti |

## Valores extraídos

| Quantidade | Valor | Local | Grau |
|---|---|---|---|
| Alvo | τ Ceti = HD 10700, G8 V, 3.652 ± 0.002 pc; "inactive", idade 4.4–12.4 Gyr (citações) | p. 1 (§1) | A |
| Velocidade de rotação projetada | v sin i = 0.1 ± 0.1 km s⁻¹ ("consistent with little to no rotational velocity — potentially an indication of a pole-on orientation"); ajuste final 0.08 ± 0.03, incerteza ampliada para 0.1 pela modelagem | pp. 4–5 (§3.3, §3.5) | A |
| Raio interferométrico | R = 0.793 ± 0.004 R☉ | p. 4 (§3.1) | A |
| Período de rotação por girocronologia | P_rot = 46 ± 4 d (idade de Di Folco+2004 e relação de Barnes 2007) | p. 5 (§3.5) | A |
| Período do periodograma de Mount Wilson (1 784 medidas de S, 1967–1995, versão NSO de 1995) | 32 ± 9 d, FAP = 0.004; erro por bootstrap (1 000 reamostragens); "other significant peaks … are included within this range" | p. 5 (§2.3, §3.5.1) | A |
| Período do periodograma APT | 43 ± 7 d; "the power in the periodogram is very low … The false-alarm probability of all peaks in this periodogram is near 1, which is consistent with a pole-on star and little rotational variation" | p. 5–6 (§3.5.2) | A |
| Período de RV (EXPRES) | 23 d; "no strong" sinal | p. 6 (§3.5.3, Fig. 3) | A |
| Inclinação | **7° ± 7°** (combinando raio, v sin i e período); 5° ± 5° com o período do Mount Wilson e 6° ± 6° com o do APT | Resumo; pp. 5–6; Tabela 3 | A |
| Consequência declarada | "With this range of inclinations, rotational variations may be visible, but only on the stellar limb"; "difficulties in reliably determining a rotation period" | p. 5; Conclusão | A |
| Disco de detritos | inclinação 35° ± 10° (Lawler+2014); desalinhamento com a estrela | Resumo; §5 | A |

## Verificações
- Título, autores, DOI e volume conferidos na página 1 → passa.
- Crossref (DOI `10.3847/1538-3881/ace906`): título e volume 166 conferidos; o registro não traz relação de errata (`update-to` vazio). A consulta adicional por `updates:` não respondeu e não foi repetida.
- A frase de D51, "pole-on inclination (Korolik et al. 2023) that precludes us from identifying its chromospheric activity cycle or rotational modulation via S-STD", é da **CLS VI** (citada em `audit/A11_raridade.md`, ressalva sobre τ Ceti, §3.2 da CLS VI), não de Korolik; Korolik **não afirma** que o ciclo cromosférico seja suprimido nem trata de ciclo. Afirma que o sinal de rotação é fraco ou só no limbo e que o período é difícil de determinar.

## Achados

**A14-F1 · a inclinação de τ Cet é próxima de zero, mas a incerteza é do tamanho do valor. `A`**
7° ± 7° (Resumo, Tabela 3) cobre 0° a 14° a 1 σ. O que a fonte sustenta é "nearly pole-on", não um valor preciso. As três estimativas de inclinação (5°, 6°, 7°) compartilham o v sin i = 0.1 ± 0.1 km s⁻¹, que é consistente com zero; não são independentes entre si.

**A14-F2 · o período de rotação de τ Cet não está determinado. `A`**
Quatro valores: 46 ± 4 d (girocronologia, não observado), 32 ± 9 d (Mount Wilson, FAP 0.004), 43 ± 7 d (APT, FAP ≈ 1) e 23 d (RV). A diferença entre o P_rot de Mount Wilson e o de outras fontes não está resolvida; Baum+2022 e Saar & Osten 1997 também são citados (p. 1).

**A14-F3 · D51 está apoiado para τ Ceti em geometria, mas a ligação "inclinação → ausência de ciclo" não é de Korolik. `A` (fato) / leitura própria**
O que Korolik dá: geometria polar e modulação rotacional fraca. A ponte para "o ciclo de atividade não é identificável" é da CLS VI (A11, ressalva sobre τ Ceti), a partir de S-STD; Korolik usa os dados de Mount Wilson (versão NSO de 1995) só para o periodograma de rotação. A atividade de τ Cet nos dados de Mount Wilson tem periodograma com pico significativo (FAP 0.004), o que é compatível com uma modulação fraca e não com ausência dela.

**A14-F4 · a inclinação das outras estrelas do `Flat` não está medida aqui. `X`**
Korolik trata só de τ Ceti. Para HD 3651, HD 32147, HD 43587 e as demais, nenhuma fonte auditada traz inclinação: D51 continua grau X para elas (Q11).

## Decisões tomadas, com base
1. **D51 recebe a fonte primária da inclinação de τ Cet (grau A) e a ressalva de A14-F3**: a ligação com o ciclo vem da CLS VI. *Base:* acima. *(→ D76 no caderno)*
2. **Q11 continua aberta**: o que se sabe de τ Cet não se estende às demais estrelas.

## Não resolvido (grau C ou X)
| Quantidade | Por que | Resolução proposta |
|---|---|---|
| Inclinação das demais `Flat` e dos controles | **X** — nenhuma fonte auditada | v sin i e P_rot de cada estrela (Baum, CLS V, Saar e Osten 1997) e raio; só como subsídio, sem medir inclinação própria (regra 8) |
| Seções de interferometria e dinâmica (§3.1–3.2, §4) | não lidas página a página | não são citadas |
