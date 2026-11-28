# Submissão à New Astronomy (Elsevier): lista para o pesquisador (2026-11-28)

Revista decidida: **New Astronomy** (D129), submissão direta, sem consulta prévia ao editor. Conferida contra `kit/revistas/new-astronomy/ficha.md` (guia lido em 2026-11-25; reconfirme no formulário).

## Já conferido no manuscrito v2
- Resumo: 248 palavras no PDF (limite 250). Palavras-chave: 7 (limite 1 a 7). Highlights: 5 itens de 66 a 79 caracteres (limite 85), arquivo separado `highlights.docx`.
- Inglês americano (varredura de grafias britânicas: só "catalogue" no agradecimento padrão do VizieR, texto fixo do CDS). Agradecimentos em seção própria antes das referências; declaração de IA antes das referências (marcador para você escrever).
- Referências: 37, todas citadas; DOIs de [9] e [14] conferidos; conjuntos de dados citados como tal onde há registro.
- Dados e código: o pacote `repositorio_zenodo_v2.0.0.zip` reproduz o manuscrito (`REPRODUCTION OK` em pasta limpa, modos padrão e `--full`). O arquivo de Vaquero não vai no pacote (termos de uso não conferidos); a série anual derivada vai.

## Arquivos para enviar
- **`submissao_new_astronomy.zip`** (gerado por `make_submission_folder.py`; compila sozinho, 33 páginas): `main.tex`, `calibration_macros.tex`, `cal_table_stars.tex`, `cal_table_simulations.tex`, `references.bib`, `highlights.docx` e `.tex`, `alt_text.md` e `figures/Figure_1 … Figure_11` (PDF e EPS, nomes lógicos na ordem do texto).
- `highlights.docx` como arquivo separado (o guia pede "highlights" no nome).
- `cover_letter_new_astronomy.md` (rascunho em inglês para editar).
- Ferramenta de declaração de interesses da Elsevier: preencher e anexar o `.docx` gerado.
- Aviso: vários painéis por arquivo (Figs. 1 a 4, 8, 9 e 10); o guia desaconselha, salvo imagens feitas para comparação, que é o caso. Se o editor pedir, separo.

## Falta, e é seu
1. Endereço postal e CEP da afiliação; e-mail do autor correspondente (marcadores no `main.tex`).
2. Declaração de IA (você escreve no Overleaf; modelo no guia); financiamento e CRediT conferidos.
3. Publicar o pacote no Zenodo (`ZENODO_DEPOSITO.md`) e pôr o DOI na seção de dados e em `CITATION.cff`; depois repetir `make_repositorio.py`, `make_overleaf_zip.py`, `make_submission_folder.py` e a prova em pasta limpa.
4. Biblioteca do IFTM: o instituto participa do acordo CAPES–Elsevier e a New Astronomy está na lista de elegíveis (o acordo cobre só periódicos híbridos, artigos aceitos de 2026 a 2028)? Sem isso, escolha entre assinatura (sem taxa) e acesso aberto (APC de lista US$ 2 900).
5. Termos de uso e URL do catálogo de Vaquero antes de qualquer cópia pública do arquivo.
6. Título: mantido; se quiser mais concisão, "Can critical slowing down indicators detect the loss of a stellar activity cycle? Size, power and positive controls".
7. Opcional: preprint no arXiv (permitido; não conta como publicação prévia).
