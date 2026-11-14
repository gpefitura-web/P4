# ARQUITETURA DO TRABALHO (etapas E0 a E11)

Sequência observada no P1 (50 commits, 3 dias úteis de sessões, 10 etapas) e generalizada. Cada etapa tem entrada, saída, critério de aprovação e arquivos tocados. **Toda etapa termina em parada com aprovação escrita do usuário (REG-01).** A numeração de subetapas (E7a a E7d, E9a, E9b) pode variar por paper.

```
E0  infraestrutura ──► E1 teste do Actions ──► E2 piloto de download ──► E3 lista de refs (resolver)
                                                                         │
E4 download em lotes ◄───────────────────────────────────────────────────┘
 │
 ▼
E5 leitura completa + memorando de decisões ──► E6 especificação da física ──► E7 implementação (a..d)
                                                                                │
        E8+ análises adicionais ◄───────────────────────────────────────────────┘
 │
 ▼
E9a infraestrutura do manuscrito ──► E9b redação por seção ──► E10 portão de submissão ──► E11 retrospectiva
```

## E0. Infraestrutura
- **Entrada**: `bootstrap.sh` executado, `kit.yml` preenchido, repositório privado criado, branch de trabalho criada, `ADS_DEV_KEY` em Secrets, `FICHA_PAPER.md` preenchida (pergunta, dados, pipeline, figuras, resultados esperados, outline, revista-alvo provisória).
- **Saída**: `CADERNO_PESQUISA.md`, `DECISIONS.md` (DEC-01 a DEC-0x do bootstrap), `PAPER_STATE.md` versão 1 com status e riscos.
- **Aprovação**: usuário confirma pergunta, restrições (`docs/00_PROGRAMA.md`) e lista de etapas. Registro: `DEC-01`, `DEC-0x`.
- **Armadilhas**: criar a branch de trabalho antes de editar o workflow (ver LICOES_AMBIENTE 2); GitHub Actions precisa estar habilitado pelo usuário (P1: DEC-08).

## E1. Teste do ambiente e do Actions
- **Entrada**: workflows copiados em `.github/workflows/`.
- **Saída**: registro no caderno do que o chat alcança e do que o Actions alcança (arXiv, ADS, VizieR, editor, CTAN), com data. Confirmar que o `push` com `paths` dispara o workflow e que o commit do bot volta.
- **Aprovação**: usuário confirma o mecanismo (REG-ACT).

## E2. Piloto de download (1 artigo)
- **Entrada**: `scripts/refs_list.yml` com 1 item, `modo: baixar`.
- **Saída**: `referencias/<chave>.pdf`, `referencias/bib/<chave>.bib`, `MANIFEST.json` (sha256, bibcode, arXiv, validação), `DOWNLOAD_LOG.md`.
- **Critério**: título confere nas páginas 1 e 2; BibTeX do ADS; páginas citadas referem-se ao PDF baixado.

## E3. Lista de referências (resolver)
- **Entrada**: lista proposta (papel de cada item, REG-R7), `modo: resolver`.
- **Saída**: `referencias/RESOLVE_<lote>.md` (bibcode, arXiv, DOI, acesso, similaridade de título, candidatos). Substituições de livros por artigos abertos (REG-R3).
- **Aprovação**: usuário aprova a lista (lotes de até 10) e registra em `DECISIONS.md`.

## E4. Download em lotes
- **Entrada**: lista aprovada, `modo: baixar` ou `ambos`.
- **Saída**: PDFs validados; reprovados em `_pendentes/`; itens com captcha ou sem acesso aberto listados para o usuário subir (`fonte: manual`, ver LICOES_AMBIENTE 4); `modo: verificar` para refereed/erratum (REG-R11); catálogos VizieR: só ReadMe.
- **Aprovação**: usuário confirma a coleção.

## E5. Leitura completa e memorando de decisões
- **Entrada**: coleção validada. Textos extraídos por `extract_texts.py <dir>` (não persistem entre sessões).
- **Saída**: no `CADERNO_PESQUISA.md`, uma entrada por artigo com **fatos e página** (REG-03), discrepâncias entre documentos de estratégia e literatura, e o **memorando** com as decisões que faltam (D-A, D-B, …), cada uma com subsídios, alternativas e recomendação.
- **Aprovação**: usuário decide cada item (P1: "seguir todas as recomendações"); as decisões viram `DEC-xx` congeladas.
- **Dicas**: ler em blocos (método, teoria, dados); usar `dig.py` para achar trechos com página; PDFs escaneados lidos como imagem e anotados no caderno.

## E6. Especificação da física (rascunhos)
- **Entrada**: decisões congeladas do E5.
- **Saída**: `repositorio/ESPECIFICACAO_FISICA.md` (hipóteses, dados, filtros, estimadores, testes, sensibilidades, critérios de decisão, saídas, figuras), em rascunhos 1 a 3 com perguntas ao usuário no fim de cada um.
- **Aprovação**: versão final aprovada (P1: DEC-30). Idioma do documento: processo (pt-BR); resultados e notebook: inglês.

## E7. Implementação em subetapas (a..d)
- **Subetapas típicas**: (a) dados, integridade, funil de seleção e classes; (b) estimadores e **validação com dados simulados** (REG-VAL); (c) análise principal, bootstrap, testes e sensibilidades; (d) figuras, macros, `analysis_results.md`, modo rápido, execução completa duas vezes.
- **Saída**: `repositorio/<paper>.py` (jupytext, fonte), `.ipynb` gerado, `requirements.txt`, `README.md`, `results_macros.tex`, `analysis_results.md`, `figures/`, `fonts/`.
- **Critério**: 0 validações em ATTENTION; execuções completas idênticas; veredito e robustez seguindo REG-ROB. Resultados incômodos (não robusto, divergência com a literatura) são levados ao usuário **antes** de qualquer enquadramento do texto (P1: DEC-35).
- **Armadilhas**: pesquisa exploratória vai para `fora_repositorio/` e é promovida (REG-PROMOCAO); alteração de decisão de método = CR (REG-CR).

## E8+. Análises adicionais
- Definidas pelo usuário depois de ver o resultado (P1: α por faixas de Teff). Mesmo rito: desenho aprovado na especificação, implementação, execução completa, aprovação.

## E9a. Infraestrutura do manuscrito (último ponto em que a revista pode mudar)
- **Entrada**: mensagem do manuscrito aprovada em `PAPER_STATE.md` ("Mensagem central", "O que o manuscrito não afirma", orçamento de páginas).
- **Saída**: escolha da revista (`kit.yml: revista`), módulo `kit/revistas/<revista>/` (ficha + esqueleto LaTeX), `fetch_template.py` via Actions para baixar normas e template **atuais**, `main.tex` compilável com seções `sec_*.tex` vazias, `build_manuscript.sh` e `check_manuscript.py` funcionando, plano de redação com orçamento por seção.
- **Aprovação**: usuário aprova infraestrutura e plano de redação.
- **Nota**: o texto dos `sec_*.tex` é neutro quanto à revista. Trocar de revista depois é trocar o módulo (esqueleto, bst, limites) e reajustar o tamanho.

## E9b. Redação
- Ordem: Métodos, Resultados, Discussão e Conclusões, Introdução, Resumo (REG-HUM).
- Por seção: rascunho, humanização, `check_manuscript.py`, conferência de fatos contra o caderno, aprovação do usuário (no máximo 2 rodadas, REG-02).
- Saída: `manuscrito/sec_*.tex` e `\abstract`, compilando dentro do limite de páginas.

## E10. Portão de submissão
- Checklist em `docs/SUBMISSAO.md` e na ficha da revista. Varredura das normas atuais, estilo bibliográfico exigido, figuras no formato, texto alternativo, seções finais da editora (Conflitos de interesse, Financiamento, Disponibilidade de dados), política de IA (REG-IA), repositório público com DOI (REG-LAYOUT), custo e acordos CAPES/instituição.
- **Saída**: pendências do usuário listadas (autores, afiliações, declarações, textos provisórios) e etapa fechada com aprovação.

## E11. Retrospectiva (nova, `[experimental]`)
- **Entrada**: paper submetido (ou etapa E10 fechada).
- **Saída**: `evolucao/PROPOSTAS/PROP-NNN.md` por lição que merece voltar ao kit (ver `docs/EVOLUCAO.md`), lidas de `LICOES_PENDENTES.md`, `DECISIONS.md`, log de chats e de qualquer retrabalho ou loop de erro ocorrido.
- **Aprovação**: usuário decide quais PROP entram no kit; a sessão aplica na branch do kit e sobe a versão.

---

## Regra de leitura de retomada

Qualquer sessão nova lê, nesta ordem (ver `docs/CHECKLIST_RETOMADA.md`): `CLAUDE.md` → `CADERNO_PESQUISA.md` (seção "Estado atual") → `DECISIONS.md` → `PAPER_STATE.md` → `PROMPT_PROXIMO_CHAT.md`. O estado vive nesses arquivos versionados.
