# LICOES_PENDENTES.md — lições da inspeção de 2026-11-14

Formato do kit: o que aconteceu, a regra que teria evitado, onde a regra deve entrar. **Pendentes**: nenhuma foi incorporada ao kit; o pesquisador decide.

| # | O que aconteceu | Evidência | Regra proposta | Onde entra |
|---|---|---|---|---|
| L1 | Um PDF chamado "Held & Kleinen 2004" era outro artigo (Boulton+2014) e entrou num commit sem conferência | I-38; A7-F1; D63 | Validar título e DOI nas páginas 1–2 de todo PDF antes de aceitar (REG-R2 já pede; falta aplicar ao que chega por upload) | caderno D63; kit REG-R2 |
| L2 | O texto e a tabela do mesmo artigo discordam e a frase foi citada como fato ("piso 0.45 %") | I-03; D67 | Quando texto e tabela do mesmo artigo discordam, é grau X até o pesquisador escolher; registrar as duas | kit REG-03 |
| L3 | Um número foi propagado sem conferir: "710 estrelas" da CLS V atribuído à CLS VI; "52 380 linhas" | I-36, I-10; D55, D60 | Todo número que passa de um documento a outro leva remissão ao ponto de origem; reconferir na fonte ao reusar | kit REG-CR |
| L4 | A receita descrita (σ por estação) não é a receita reproduzida (σ do intervalo) | I-01; D57 | Ao registrar uma receita como "reproduzida exatamente", declarar qual conta produz o valor publicado | protocolo §4 |
| L5 | B−V de definições diferentes (fotométrico × derivado de T_eff) foram comparados como se fossem a mesma grandeza | I-07; D62 | Toda grandeza comparada entre fontes leva a definição de cada fonte na mesma linha | protocolo §6 |
| L6 | Dados "da fonte" eram digitalizados de figura por terceiros e só a leitura do manuscrito do arXiv mostrou isso | I-44; D58 | Para dado sem origem instrumental clara, ler também o manuscrito do arXiv e comparar com a versão publicada | kit REG-DADOS |
| L7 | O checksum "reproduzido" não sustentava grau A porque o número vinha do texto | I-04; D56 | Checksum só vale se a identidade dos itens, e não só a contagem, é reproduzida | protocolo §4 |
| L8 | A instrução de incorporação de DECISOES não cobria cabeçalho, §6, §7 nem a coluna "Subsídios" | I-18 | Instrução de incorporação lista o que NÃO altera, além do que altera | kit, modelo de DECISOES |
| L9 | Auditorias previstas (A7, A8) ficaram de fora por semanas sem aparecer em lista alguma | I-25, I-28 | Todo pendente conhecido entra no caderno §6 com dono e dependência | kit REG-06 |
| L10 | Conversa muito longa, resumida várias vezes, com muitas decisões encadeadas; risco de perda de detalhe e de repetir perguntas (o pesquisador pediu "evitar loops a todo custo") | sessão de 2026-11-24 | Encerrar a etapa com handoff (`PROMPT_PROXIMO_CHAT.md`), antiloop explícito (2 tentativas, um passo por vez, nada decidido se reabre) e abrir conversa nova para a etapa de código | kit REG-06, `CHECKLIST_RETOMADA` |
| L11 | Uma checagem de inventário falhou em silêncio quando o número de D## mudou (faixa fixa em `01_inventory.py`) | D55–D104 | Derivar a faixa do próprio caderno em vez de um número fixo | scripts de verificação |
| L12 | Texto com crases num heredoc sem aspas foi executado pelo shell e apagou trechos do log e de D83 | D83 | Heredoc sempre entre aspas (`<<'EOF'`) ao escrever Markdown com crases | `LICOES_AMBIENTE` |
| L13 | Um arquivo de dados e um script foram adicionados ao repositório por fora do fluxo (id de checagem duplicado `3.14-xx`) | commit `0c7b853` | Antes de criar ids de checagem, listar os existentes; conferir `git status` antes de `git add -A` | processo |
| L14 | O nome de um PDF baixado (Boettiger) estava errado e só foi visto ao ler a primeira página | A7c | Nomear o arquivo só depois de validar autores e título na página 1 (D63) | kit REG-R2 |
| L15 | Dois critérios "pronto" de passos diferentes pediam regras diferentes para o mesmo flag de dados (`sigma` contra `1day/sigma`) e só a verificação do passo 2 mostrou | `pipeline_v2/ACHADOS.md` #3 | Ao escrever critérios de verificação, declarar a regra de filtro de cada contagem de referência | prompts de etapa |
| L16 | Um módulo chamado `io.py` sombrearia a biblioteca padrão | `pipeline_v2/ACHADOS.md` #1 | Não nomear módulos com nomes da biblioteca padrão | prompts de etapa |
| L17 | D22 define p = P(τ* ≤ τ), que não é a cauda usual de um teste de tendência crescente | `pipeline_v2/ACHADOS.md` #4 | Definir a cauda do p e a direção da hipótese na mesma decisão | caderno D22 (por nova D##) |
