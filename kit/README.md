# paper-workflow (kit de método)

Kit privado extraído do paper P1 (distribuição de energia de flares estelares, EPL) para repetir o procedimento "baixar os artigos, lê-los na sessão, registrar fatos com página, decidir por etapas com aprovação, implementar, escrever e submeter" em outros papers e outras sessões do Claude Code, sem repetir os loops de erro.

## Começar um paper novo (5 passos)
1. Clone esta branch (`kit/paper-workflow`) em qualquer lugar.
2. Crie um repositório **privado** vazio para o paper e clone-o.
3. `bash bootstrap.sh P2 /caminho/do/repo-do-paper [branch-de-trabalho]`
4. No GitHub: crie a branch de trabalho e o secret `ADS_DEV_KEY`.
5. Abra o Claude Code na raiz do repositório do paper e cole `PROMPT_PROXIMO_CHAT.md`.

## Conteúdo
Ver `CLAUDE.md` (mapa) e `docs/`. O que o kit **não** tem: PDFs, dados, resultados ou texto de qualquer paper (só `exemplos/p1/` como formato).

## Evoluir
`docs/EVOLUCAO.md`: capture lições em `LICOES_PENDENTES.md`, proponha no fim do paper (E11), aprove, atualize `VERSION` e `evolucao/CHANGELOG.md`; outros papers sincronizam com `scripts/kit_sync.sh`.

Versão atual: ver `VERSION` (0.3.0: quatro hooks de verificação vindos da extensão 1 do P1).
