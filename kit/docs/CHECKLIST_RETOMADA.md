# CHECKLIST DE RETOMADA (sessão nova ou "fria")

1. Estar na branch de trabalho do paper (`kit.yml: branch`) e rodar `git pull`.
2. Ler, nesta ordem: `CLAUDE.md` → `CADERNO_PESQUISA.md` (seção "Estado atual" e o fim, "Log de chats") → `DECISIONS.md` → `PAPER_STATE.md` → `PROMPT_PROXIMO_CHAT.md`. Decisões congeladas não se discutem de novo (REG-CR).
3. Ler `kit/docs/LICOES_AMBIENTE.md` (índice) e `LICOES_PENDENTES.md` do paper.
4. Recursos: PDFs em `referencias/` (`MANIFEST.json` tem sha256), BibTeX em `referencias/bib/`, ReadMe de catálogos em `referencias/vizier/`, normas da revista em `referencias/web/`.
5. Textos extraídos **não** persistem: `python3 -I scripts/extract_texts.py /tmp/txt` (instalar `pypdf` se faltar) e usar `scripts/dig.py` para achar trechos com página.
6. Testar a rede na hora (REG-08). Downloads só por Actions (REG-ACT).
7. Regras que valem sempre: aprovação por etapa; no máximo 2 rodadas; fatos só do caderno com página; nada citado sem PDF validado; estilo e política de IA conforme `kit.yml`; commits conforme `kit.yml`.
8. Antes de encerrar: atualizar `CADERNO_PESQUISA.md` (estado atual, log de chats e uso de IA no processo), `DECISIONS.md`, `PAPER_STATE.md`, `LICOES_PENDENTES.md`; commit e push na branch de trabalho (REG-06).
