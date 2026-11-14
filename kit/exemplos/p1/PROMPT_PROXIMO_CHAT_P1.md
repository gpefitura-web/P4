# Prompt de abertura do próximo chat (submissão)

Cole o texto abaixo no primeiro mensagem do novo chat.

---
Paper 1 (P1): consulte, nesta ordem, CADERNO_PESQUISA.md, DECISIONS.md e PAPER_STATE.md na raiz do repositório (branch claude/confident-hawking-fb9tzg). Os PDFs estão em referencias/ e as normas da EPL em referencias/web/.
Status atual: E0 a E10 concluídas e aprovadas. Manuscrito completo em manuscrito/ (compila com bash scripts/build_manuscript.sh, 7 páginas no limite da EPL, referências em ordem de citação, figuras em PDF, seções finais da OUP). Prosa sem travessões e sem ponto e vírgula (DEC-31). Revista EPL, submissão no formulário https://mc04.manuscriptcentral.com/epl.
Tarefa desta conversa: ajudar com as pendências do usuário listadas no DEC-45 (autores e afiliação, declaração de IA e carta de apresentação, Funding e Conflicts of interest, repositório com DOI, seção e Co-Editores, erratum do Yang e Liu, custo e CAPES/IFTM), depois montar o pacote final. Atenção: oito números das faixas e os valores publicados do Yang estão em manuscrito/results_extra.tex, copiados à mão.
Regras: aprovação do usuário a cada etapa, máximo de 2 rodadas de correção por item, fatos só do caderno com página, zero marcas técnicas de IA em manuscrito/ e repositorio/, commits sem trailer. Não avançar sem aprovação.
---

## Como o novo chat recupera o contexto (checklist para quem abre o chat)
1. Estar na branch claude/confident-hawking-fb9tzg (git pull). Tudo importante está versionado: nada depende da memória deste chat.
2. Ler, nesta ordem: CADERNO_PESQUISA.md (fatos da literatura com página, discrepâncias, normas da EPL, memorando E5, log de chats), DECISIONS.md (DEC-01 a DEC-31, congeladas), PAPER_STATE.md (visão geral do paper), plano em PROMPT_PROXIMO_CHAT.md.
3. PDFs: referencias/*.pdf (46 itens), BibTeX do ADS em referencias/bib/, MANIFEST.json (hashes), DOWNLOAD_LOG.md, catálogos VizieR (só ReadMe) em referencias/vizier/, normas da EPL em referencias/web/.
4. Textos extraídos NÃO persistem entre chats: regenerar com `python3 -I scripts/extract_texts.py /tmp/txt` (usa pypdf; pip install pypdf se faltar) e usar scripts/dig.py para buscar trechos com página.
5. Rede do ambiente: ADS, arXiv, VizieR e editores são bloqueados no ambiente de chat. O download passa pelo GitHub Actions: editar scripts/refs_list.yml (modos baixar, resolver, readme, verificar, buscar via 'consultas', 'paginas', 'ambos'), fazer push, e o workflow fetch_refs.yml commita o resultado; o token ADS_DEV_KEY já está nos secrets do repositório. Os PDFs de editores com captcha são subidos manualmente pelo usuário.
6. Regras que valem sempre: aprovação do usuário por etapa; sem trailer de co-autoria nos commits; sem marcas técnicas de IA em manuscrito/ e repositorio/; texto sem travessões e sem ponto e vírgula; figuras Super Mongo sem grade com Courier Prime em EPS; só fatos do caderno com página; máximo de 2 rodadas por item.
7. Ao final do chat: atualizar CADERNO_PESQUISA.md (estado atual, log de chats), DECISIONS.md e PAPER_STATE.md, commit e push.
