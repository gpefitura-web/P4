# CHANGELOG do kit

## 0.3.0 (2026-11-14)
Hooks de verificação trazidos da branch da extensão 1 do P1 (`claude/p1-ext-trabalho`, onde nasceram em 2026-11-10 e 11), sem mudar o núcleo. Todos são opcionais e se ativam em `kit.yml: verificacao.extra`.
- `ordem_floats`: figuras e tabelas citadas na ordem do aparecimento (confere `main.aux`).
- `eprime`: manuscrito em E-Prime, sem nenhuma forma de 'to be' (uso opcional, depende da decisão do paper).
- `limites_elsevier`: limites do guia de autores da New Astronomy (resumo, destaques, palavras-chave), como exemplo de hook por revista.
- `numeros_via_macro`: agora também confere `manuscrito/main.tex` (depois de `\begin{document}`), além de `sec_*.tex`, para manuscrito em arquivo único.
- Não trazidos: `revistas/newastronomy` e `revistas/comparacao_2026-11-11`, específicos da extensão 1 (podem virar módulo de revista numa proposta futura).
- Origem das cópias: commits a942782, 66208b3 e a158143 da branch da extensão 1. Testados lá, não retestados em rede real aqui.

## 0.2.0 (2026-10-21)
Teste de fumaça real (PROP-000) aprovado no GitHub Actions: gatilho parametrizado, download e validação, commit de volta, build com referência real. Correções: `build_manuscript.sh` avisa só pelo último passe; `fetch_template.py` sem links repetidos.

## 0.1.0 (2026-10-21)
Primeira extração do P1 (branch `claude/confident-hawking-fb9tzg`, commit f777987).
- Regras de processo (REG-*), arquitetura E0 a E11, lições de ambiente (18 itens), checklist de retomada, estilo de figuras, padrão do notebook, portão de submissão, layout do repositório, evolução do kit.
- Pipeline: fetch_refs, fetch_template (parametrizado por revista), extract_texts, dig, make_references_bib, check_manuscript (configurável por kit.yml), build_manuscript, sync_overleaf, apply_journal, publish_repositorio, kit_sync; workflows com branch parametrizada; bootstrap.sh.
- Módulos: revistas/epl, revistas/_TEMPLATE, programas/stellar-activity-29, exemplos/p1.
- Todas as regras entram como `[estável]` quando vistas de ponta a ponta no P1 e `[experimental]` quando criadas na extração (REG-R11, REG-PROMOCAO, REG-HUM, REG-LAYOUT, REG-EVO, E11).
- Não testado em rede real fora do P1: ver evolucao/PROPOSTAS/PROP-000_teste_de_fumaca.md.

### Verificação a seco da 0.1.0 (2026-10-21, sem rede externa)
- `bootstrap.sh` em diretório de teste; `build_manuscript.sh` compilou o esqueleto da EPL (1 página, 0 problemas de estilo); `check_manuscript.py` com regras ligadas e desligadas por `kit.yml`; `sync_overleaf.sh` gera o zip; `publish_repositorio.sh` exporta e recusa menções privadas e falhas de estilo; `kit_sync.sh` compara versões; hook `numeros_via_macro`.
- Bugs achados e corrigidos pelo teste: `make_references_bib.py` quebrava sem `MANIFEST.json`; `publish_repositorio.sh` usava `rsync` (ausente); a classe da OUP exige `algorithmicx` (`texlive-science`), que a lista de pacotes do P1 não trazia; `apply_journal.sh` copiava o pacote de exemplo da OUP para `manuscrito/`.
- Workflows no GitHub Actions: testados depois, ver 0.2.0 e PROP-000.
