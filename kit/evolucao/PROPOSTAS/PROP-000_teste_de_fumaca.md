# PROP-000: teste de fumaça real do kit (CONCLUÍDO em 2026-10-21)
- Data: 2026-10-21 | origem: extração do P1
- Tipo: script/doc
- **O quê**: instanciar o kit num repositório privado de teste (ou no próximo paper), subir 1 item em `scripts/refs_list.yml` e confirmar que o workflow dispara por `push` na branch parametrizada, baixa e valida o PDF e comita de volta; compilar o esqueleto do módulo da revista; rodar `publish_repositorio.sh` num `repositorio/` de teste.
- **Por quê**: a parametrização dos workflows e a nova ordem de pastas (macros e figuras copiados para `manuscrito/`) não rodaram com rede real; só foram verificadas a seco (sintaxe, bootstrap em diretório temporário, build LaTeX do esqueleto).
- **Risco**: baixo; é só verificação.
- Maturidade: o kit fica `0.1.0` (experimental) até este teste passar; então vira `0.2.0`.
- Decisão do usuário: solicitada pelo usuário; executada.
- Aplicada na versão: 0.2.0

## Resultado (2026-10-21)
Feito numa branch descartável do repositório privado de testes `kit/smoke-test-prop000` (bootstrap.sh SMOKE, branch parametrizada, `refs_list.yml` com 1 item: clauset2009):
- O `push` disparou **os dois workflows** na branch parametrizada (fetch_refs, fetch_template), sem `workflow_dispatch`.
- fetch_refs: ADS resolveu 2009SIAMR..51..661C, PDF do arXiv:0706.1062 validado (título 100%), `MANIFEST.json` com sha256, BibTeX do ADS, `DOWNLOAD_LOG.md`; o bot comitou de volta (`refs-bot`).
- fetch_template: 3 páginas e 3 arquivos (EPLgraphics, EPLmultimedia, Word) baixados com manifesto e log; o zip do Overleaf deu 404 (como já no P1, ver LICOES 8); o bot comitou.
- Os dois jobs comitaram na mesma branch quase ao mesmo tempo e o `pull --rebase` resolveu a corrida.
- `git pull` no clone trouxe tudo; `build_manuscript.sh` com `\cite{clauset2009}` compilou: `[1]` resolvido, bibliografia gerada; uma chave sem BibTeX faz `make_references_bib.py` sair com código 1.
- Ajustes feitos por causa do teste: o `build_manuscript.sh` agora avisa só pelo último passe do pdflatex (os intermediários sempre acusam citações indefinidas); o `fetch_template.py` deixou de repetir links da própria página.
- Não coberto: `ADS_DEV_KEY` em repositório novo (aqui o secret já existia), repositório de teste separado, Actions em conta sem minutos.
