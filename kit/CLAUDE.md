# CLAUDE.md do kit de método (paper-workflow)

Você está no kit de método extraído do paper P1. Ele não contém conteúdo de nenhum paper além de `exemplos/p1/`. Para começar um paper novo: `bash bootstrap.sh <PAPER_ID> <diretório_do_repo_privado> [branch]`, depois siga os passos que o script imprime. Dentro de um repositório de paper, este arquivo está em `kit/CLAUDE.md` e o `CLAUDE.md` da raiz aponta para ele.

## Leia primeiro
1. `docs/REGRAS_PROCESSO.md` (todas as regras REG-*)
2. `docs/ARQUITETURA.md` (etapas E0 a E11)
3. `docs/LICOES_AMBIENTE.md` (armadilhas; leia o índice agora, a entrada completa quando o sintoma aparecer)
4. No repositório do paper: `CADERNO_PESQUISA.md`, `DECISIONS.md`, `PAPER_STATE.md`, `PROMPT_PROXIMO_CHAT.md` (`docs/CHECKLIST_RETOMADA.md`)

## Regras duras (resumo)
- Etapa só avança com **aprovação escrita** do usuário (REG-01); no máximo 2 rodadas por item (REG-02). Não decida sozinho o que é do usuário: revista, declaração de IA, autores, afiliações, custos.
- **Fatos só do caderno com página** (REG-03). Nenhum valor de literatura sem entrada; nenhuma frase factual no manuscrito sem base.
- **Nada citado sem PDF validado** em `referencias/` (REG-R2). BibTeX sempre do ADS, por script (REG-R4, R6). Lista aprovada antes de baixar (REG-R7).
- **Downloads só pelo GitHub Actions** (REG-ACT); o chat costuma não alcançar ADS/arXiv/editoras. Teste a rede na hora (REG-08). Nunca desabilite TLS nem contorne o proxy.
- Números do manuscrito **só por macro** (REG-MAC); nenhum número de `fora_repositorio/` no manuscrito (REG-PROMOCAO).
- Repositório do paper **privado**; só `repositorio/` é publicado, por exportação (docs/LAYOUT_REPO.md). Não exponha caderno, kit, PDFs.
- Política de IA, estilo da prosa e commits: `kit.yml` e REG-IA/ESTILO/COMMIT. Não escreva marcas de IA em `manuscrito/` e `repositorio/` quando `verificacao.marcas_ia: true`; o uso de IA é registrado no caderno.
- Mudança em decisão congelada só por CR (REG-CR). Resultado incômodo (não robusto, divergente da literatura) vai ao usuário **antes** do enquadramento do texto.
- Ao fim da sessão: atualizar CADERNO, DECISIONS, PAPER_STATE, LICOES_PENDENTES; commit e push na branch de trabalho (REG-06).

## Se acontecer…
| Sintoma | Leia |
|---|---|
| Rede negada, token, TLS | LICOES_AMBIENTE 1 |
| Workflow não dispara / 404 | LICOES_AMBIENTE 2 |
| Push rejeitado depois do bot | LICOES_AMBIENTE 3 |
| PDF não baixa, captcha, scan, livro | LICOES_AMBIENTE 4, REG-R3 |
| Páginas do PDF não batem | LICOES_AMBIENTE 5 |
| Errata / valores diferentes do publicado | LICOES_AMBIENTE 6, REG-R11 |
| `pdflatex` ausente, citações vazias, bibliografia fora de ordem | LICOES_AMBIENTE 7 e 8 |
| Site da editora devolve 403 | LICOES_AMBIENTE 9 |
| Estourou o limite de páginas | LICOES_AMBIENTE 10 |
| Quer tornar algo público | LICOES_AMBIENTE 17, docs/LAYOUT_REPO.md |
| Revista pede declaração de IA | LICOES_AMBIENTE 18, REG-IA |
| Quer trocar de revista | `revistas/_TEMPLATE`, `scripts/apply_journal.sh --force-main` |
| Descobriu uma lição nova | `LICOES_PENDENTES.md` (docs/EVOLUCAO.md) |

## Estrutura do kit
`docs/` regras e guias · `templates/` arquivos de estado e README de pastas · `pipeline/` scripts, workflows e hooks · `revistas/` módulos por revista (EPL pronto) · `programas/` sequências de papers (stellar-activity-29) · `evolucao/` CHANGELOG, propostas · `exemplos/p1/` referência de formato.
Versão: arquivo `VERSION`. O kit é privado (contém o método do usuário).
