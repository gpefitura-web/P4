# Subsídios para defender a escolha da receita de σ_S (item 7 do memorando; I-01, D57)

**Pedido do pesquisador (2026-11-14):** "Subsídios para defesa." Este arquivo **não escolhe** a receita e não recomenda nenhuma. Para cada alternativa traz o que a sustenta e o que a enfraquece, com id de checagem (`inspecao/checks.csv`) e fonte.
**Contexto fixo:** Luhn+2022 §3.1 compara σ_S entre três estados de HD 166620 (mínimo 1971–75, mínimo 1987.0–1991.0, grande mínimo 2001–2004 e seguintes, conforme A10 §1.3). Valores publicados: 0.0027, 0.0054 e 0.0019; ⟨S_HK⟩ 0.1810, 0.1724 e 0.1705 (`3.4-22`, `3.4-29`, `3.4-36`). Ruído instrumental subtraído: 1.2 % de ⟨S_HK⟩ para Mount Wilson, 0.3 % para Keck.

## Conta A — σ do intervalo inteiro, menos o ruído em quadratura
**Valores:** 0.0027 / 0.0054 / 0.0019 (`3.4-25`, `3.4-32`, `3.4-39`); com cinco casas, 0.00269 / 0.00542 / 0.00195 (`3.4-26`, `3.4-33`, `3.4-40`).
**Sustenta:**
- Reproduz exatamente os três valores publicados, sem ajuste (grau A, A10 §1.4).
- É a conta que os números de Luhn de fato seguem; citar Luhn como precedente fica coerente com o que o artigo reporta.
- Usa N grande por estado (44, 315 e 103 observações; `3.4-21`, `3.4-28`, `3.4-35`).
**Enfraquece:**
- Não é "dentro de cada estação", como o passo 1 de D45 e a leitura do v6 dizem. Se o P4 descrever a receita como D45 a escreve, a descrição não corresponde à conta.
- Mistura variância intra-sazonal com variação entre estações dentro do intervalo (o intervalo inteiro de um estado abrange anos). Num ciclo ainda em curso, isso inclui a modulação lenta; é uma observação sobre a conta, não um resultado medido aqui.
- Os 119 pontos `new_MW` de 1995–2002 (digitalizados, grau C, D58) **não** entram nos três estados; os estados usam Mount Wilson exato e HIRES (A13-F3), então a conta A não depende de dado C.

## Conta B — σ dentro de cada estação, ruído subtraído por estação (leitura literal do passo 1 de D45)
**Valores:** média sobre estações 0.0028 / 0.0048 / 0.0015; mediana 0.0025 / 0.0049 / 0.0014 (`3.4-27`, `3.4-34`, `3.4-41`); nº de estações com mais de 1 observação: 4, 4 e 9 (`3.4-56`).
**Sustenta:**
- É a leitura literal de D45 e da expressão "variabilidade intra-sazonal" que D45 usa.
- Separa a variabilidade de curto prazo da modulação lenta, que é o que um indicador de CSD (variância de resíduos) quer medir.
- Concorda com a ordem dos três estados (σ do mínimo 2 > mínimo 1 > grande mínimo) e com a razão aproximada.
**Enfraquece:**
- **Não reproduz** os valores publicados: 0.0028 contra 0.0027, 0.0048 contra 0.0054 e 0.0015 contra 0.0019 (média), com diferença de até 30 % no grande mínimo.
- Só 4, 4 e 9 estações por estado (`3.4-56`); a σ por estação com poucas observações é mais ruidosa (a contagem de observações por estação não foi medida aqui).
- Nenhuma fonte publicada diz que é esta a conta de Luhn; citar Luhn como precedente dela seria atribuir ao artigo uma receita que ele não reproduz.

## O F-test (p = 8.78 × 10⁻⁶) — a que variâncias se refere
- Com variâncias **brutas** do intervalo, mínimo 1 contra grande mínimo, bilateral: p = 8.80 × 10⁻⁶ (`3.4-50`, passa contra 8.78 × 10⁻⁶); unilateral 4.40 × 10⁻⁶ (`3.4-51`).
- Com σ_S **corrigidos** (conta A): p = 8.68 × 10⁻³ bilateral e 4.34 × 10⁻³ unilateral (`3.4-52`, `3.4-53`); com os valores arredondados publicados, 4.1 × 10⁻³ (`3.4-54`).
- O texto de Luhn (arXiv, PDF p. 5; `3.11-46`) diz que o resultado vale mesmo "corrected for intrinsic noise differences". Isto é uma afirmação do artigo; o p que o artigo imprime reproduz-se com as variâncias brutas, não com as corrigidas. As duas coisas são fatos; não se sabe qual dos dois Luhn tinha em mente.
- Consequência para o P4: se o P4 citar o p de Luhn, deve dizer que ele corresponde à variância bruta; se recalcular com os corrigidos, o valor é 8.7 × 10⁻³ e a diferença deve ser declarada.
- Mínimo 2 contra grande mínimo, corrigidos: p = 2.8 × 10⁻²⁵ (`3.4-55`); **não está nos documentos**, é cálculo desta inspeção.

## Fatos que valem para qualquer das contas
- A fração de estações Keck com σ_S/⟨S⟩ abaixo de 1.2 %: 6 de 9, como a frase de Luhn; abaixo de 0.3 %: 0 de 9; as duas menores são 0.303 % e 0.339 % (`3.4-57`, `3.4-57b`, `3.4-57c`). O piso de 0.3 % para Keck é, portanto, compatível com os dados, mas o dado está colado no piso.
- Janela do mínimo 2: o texto diz "1986 to 1990" e logo depois "1987.0–1991.0" (I-34); A10 e esta inspeção usam a segunda (`3.4-28` a `3.4-30`).
- A data de 2014 tem uma observação (`3.4-58`); estações com uma observação não têm σ.
- O desvio-padrão da fotometria APT em 2004 e 2016–2020 é 0.22 mmag (ddof = 1) nesta inspeção; o texto de Luhn diz 0.35 (`3.4-20c`): divergência não resolvida e independente da conta de σ_S.

## O que cada escolha obriga a declarar em Methods
| Escolha | Declarar |
|---|---|
| A | que σ_S é o desvio-padrão do intervalo menos o ruído em quadratura; que o p de Luhn é de variâncias brutas; **corrigir a redação de D45 passo 1** por nova D## |
| B | que a receita é uma variante da de Luhn, não a de Luhn; que não reproduz os valores publicados; o número de estações por estado |
| Ambas | as duas colunas lado a lado, como nesta tabela, e a razão entre elas por estado (1.04, 0.89 e 0.79 para a razão B/A com as médias; calculada de `3.4-27/34/41` sobre `3.4-25/32/39`) |

Estado: **I-01 com subsídios entregues; escolha pendente (D70).**
