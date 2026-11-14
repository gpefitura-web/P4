# COMO O KIT EVOLUI

O kit melhora a cada paper. Nada é editado no kit no meio da escrita de um paper; as lições são capturadas na hora, avaliadas depois e voltam para o kit com aprovação do usuário.

## Fluxo
```
durante o paper ──► LICOES_PENDENTES.md (no repo do paper, uma linha por lição)
fim do paper    ──► E11 retrospectiva ──► evolucao/PROPOSTAS/PROP-NNN.md (kit)
usuário aprova  ──► aplicar no kit (branch kit/paper-workflow ou kit/prop-NNN) ──► VERSION + CHANGELOG
outros papers   ──► scripts/kit_sync.sh traz a versão nova (pipeline, docs) sem tocar no estado
```

## 1. Capturar (`LICOES_PENDENTES.md` no paper)
Formato de linha: `AAAA-MM-DD | tipo (armadilha|regra|script|doc|template|revista) | sintoma | causa | solução | arquivo(s) do kit que mudaria`. Faça isso assim que o problema acontece e antes de seguir.

## 2. Propor (E11)
Para cada lição relevante, crie `evolucao/PROPOSTAS/PROP-NNN.md` com: **o quê** muda; **por quê** (evidência no paper X: commits, loops de erro, tempo perdido); **onde** no kit; **risco** para papers em andamento; **teste** de fumaça necessário; **maturidade proposta** (`[experimental]` por padrão). Use `evolucao/PROPOSTAS/_TEMPLATE.md`.

## 3. Aprovar e aplicar
O usuário aprova ou rejeita cada PROP. Aprovadas: aplicar na branch do kit (ou numa branch `kit/prop-NNN` com PR, se o usuário quiser revisão), subir `VERSION` (semver) e acrescentar ao `CHANGELOG.md`. Mudança em regra `[estável]` segue o rito do CR (REG-CR): motivo, impacto, aprovação.

## 4. Versionamento
- `VERSION`: `MAJOR.MINOR.PATCH`. PATCH: correção de texto/script sem mudar comportamento. MINOR: regra, doc, módulo ou script novos compatíveis. MAJOR: muda o fluxo ou a estrutura de pastas.
- Cada paper registra `kit_version` em `kit.yml`. `scripts/kit_sync.sh <clone_do_kit>` compara, mostra o CHANGELOG pendente e (com confirmação) atualiza `kit/`, `scripts/` e os workflows, nunca o estado do paper.

## 5. Pontos de extensão (sem editar o núcleo)
| Para… | Faça… |
|---|---|
| Escrever para outra revista | Copie `revistas/_TEMPLATE/` para `revistas/<nome>/`, preencha `ficha.md` e `fontes.yml`, ponha o esqueleto em `latex/`, troque `kit.yml: revista` |
| Trabalhar outra sequência de papers | Crie `programas/<nome>/` com `PROGRAMA.md` e as fichas; `kit.yml: programa` |
| Outro tipo de análise (série temporal, espectros) | Adicione `templates/repositorio/<tipo>/` e uma seção em `PADRAO_NOTEBOOK.md` |
| Verificação extra | `pipeline/hooks/<nome>.py` com `check(root)`; ativar em `kit.yml: verificacao.extra` |
| Fonte de referências além de ADS/arXiv | Novo valor de `fonte:` em `fetch_refs.py` com teste (REG anti-regressão) |

## 6. Maturidade das regras
Cada regra em `REGRAS_PROCESSO.md` tem `[estável]`, `[experimental]`, `[configurável]` ou `[superada por REG-xx]`. Uma regra `[experimental]` passa a `[estável]` depois que **um segundo paper** a usa sem problema; isso é anotado no CHANGELOG.

## 7. Anti-regressão
Toda PROP que altera um script de `pipeline/` ou um workflow exige: `python3 -m py_compile`, `bash -n`, YAML válido, `bootstrap.sh` em diretório de teste e, quando mexer em download ou build, o **teste de fumaça real** (um item de referência baixado pelo Actions; compilação do esqueleto LaTeX). Só então a versão é marcada estável.
