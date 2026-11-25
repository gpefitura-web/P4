# Depósito no Zenodo: roteiro (2026-11-25)

**Nada foi enviado ao Zenodo.** Não há credencial aqui e a publicação é irreversível; este roteiro deixa tudo pronto para você fazer.

## Já pronto
- **Licença:** MIT (`repositorio/LICENSE`, © 2026 Airton M. S. Borin Junior). Vale para o código e para as saídas e figuras que ele produz. **Não vale** para os dados de entrada (termos de cada fonte), nem para as fontes Courier Prime (OFL 1.1), nem para o texto do manuscrito (README, seção "License").
- **Metadados:** `repositorio/.zenodo.json` (título, criador, descrição, palavras-chave, licença `mit`, versão 1.0.0) e `repositorio/CITATION.cff`. Pelo Zenodo, quando os dois existem na integração com o GitHub, **só o `.zenodo.json` é usado**.
- **Pacote para upload manual:** `P4/repositorio_zenodo_v1.0.0.zip` (95 arquivos mais o manifesto, 3 MB; pasta raiz `p4-repositorio-v1.0.0`), sha256 `7e2fe1c8d0d6df2418880eef7b83804d88690e3301a1bac7a187f0efbc4740da`. Conferi que descompacta e que `MANIFEST.sha256` e `test_step1` passam na cópia descompactada. A reprodução completa (`REPRODUCTION OK`) foi feita na versão anterior do pacote; desde então só foram acrescentados `LICENSE`, `CITATION.cff`, `.zenodo.json` e o texto de licença do README, sem mudar código nem dados.

## Duas rotas
**A. Upload manual (mais simples, e deixa pôr o DOI no manuscrito antes de publicar)**
1. Em zenodo.org, "New upload". Teste antes no **Sandbox** (sandbox.zenodo.org): o Zenodo recomenda, porque registro publicado não se apaga.
2. Envie `repositorio_zenodo_v1.0.0.zip`.
3. Campos (copie de `.zenodo.json`): tipo *Software*; título; criador *Borin Junior, Airton M. S.*, afiliação IFTM (acrescente o ORCID, se tiver); descrição; palavras-chave; licença *MIT*; versão *1.0.0*; acesso aberto.
4. Reserve o DOI no próprio rascunho (na interface há um botão "Reserve DOI"; **não consegui confirmar isso nas buscas, confira na tela**).
5. **Antes de publicar**, coloque o DOI no manuscrito (ver abaixo), regere o pacote (`python3 P4/make_repositorio.py`), refaça o zip e envie a versão final. Depois de publicado, os arquivos não mudam; os metadados podem ser editados.

**B. Integração GitHub–Zenodo**
1. **Crie um repositório novo e público só com o conteúdo de `repositorio/` na raiz.** O repositório atual do projeto (`gpefitura-web/P4`) tem auditorias, notas e material de trabalho que não são parte do artigo; a integração arquiva o repositório inteiro, não uma pasta.
2. Em Zenodo, "GitHub": ative o repositório. Cada *release* gera um registro e um DOI.
3. Crie a release `v1.0.0`. O Zenodo usa o `.zenodo.json` da raiz.
4. Atualize `repository-code` no `CITATION.cff`, o link do README e a URL na seção de dados do manuscrito para o novo repositório (eu faço, se você me der o nome).

## Colocar o DOI no manuscrito
1. Em `manuscrito/main.tex`, seção *Data availability*, troque `[repository and DOI, to be added by the author before submission]` por `Zenodo, \url{https://doi.org/10.5281/zenodo.NNNNNNN}`; mantenha o resto.
2. Acrescente a referência de dados em `manuscrito/references.bib` (o guia da New Astronomy pede `[dataset]` e `[software]` antes do título, com autor, título, repositório, versão, ano e DOI):
```
@misc{borin2026,
  author       = {Borin Junior, Airton M. S.},
  title        = {[software] Reproduction package: testing critical slowing down in {Mount} {Wilson} S-index of {Sun}-like stars},
  howpublished = {Zenodo, version 1.0.0},
  year         = {2026},
  doi          = {10.5281/zenodo.NNNNNNN}}
```
   e cite-a na seção de dados (`\cite{borin2026}`).
3. Rode `python3 P4/make_repositorio.py` e `bash P4/repositorio/reproduce.sh` numa cópia limpa (o `main.tex` faz parte do pacote e do teste).
4. Envie o zip final ao Zenodo e publique.

## O que conferir antes de publicar (riscos)
1. **Termos dos dados (o ponto mais importante).** O Zenodo guarda **uma licença por registro**; o registro diz MIT, mas os dados de terceiros estão dentro do pacote. O README e a descrição avisam, e isso é a mitigação. Fontes: *HK_Project_v2001_NSO* é aberto com agradecimento obrigatório (já no README e no manuscrito); Baum et al. e Luhn et al. são artigos da AAS (confira a licença do artigo; costuma ser CC BY, **não verificado aqui**); a **Tabela 4 de Egeland et al. (2017)** vem de um artigo cujo cabeçalho diz "All rights reserved" (AAS, 2017). Se houver dúvida, a saída segura é tirar o arquivo `data/Egeland2017_table4_…txt` do depósito e substituí-lo por instrução de download com hash; o pacote deixa de ser autossuficiente nesse arquivo, e a prova de reprodução precisa ser refeita.
2. **Afiliação e ORCID** no `.zenodo.json` (afiliação sem acento por simplicidade: "Triangulo"). Acrescentar ORCID é opcional.
3. **Versão e data:** 1.0.0, 2026-11-25. Se publicar em outra data, ajuste `publication_date` e `date-released`.
4. **Um DOI por versão:** nova versão gera novo DOI, com um DOI "conceito" que aponta sempre para a mais recente. Cite o DOI da versão do artigo.

## Fontes consultadas (2026-11-25)
- [Zenodo: arquivo .zenodo.json](https://help.zenodo.org/docs/github/describe-software/zenodo-json)
- [Zenodo: arquivo CITATION.cff](https://help.zenodo.org/docs/github/describe-software/citation-file/) e [como o CITATION.cff afeta os metadados](https://support.zenodo.org/help/en-gb/24-github-integration/96-how-does-a-citation-cff-file-affect-metadata-of-my-github-release)
- [Zenodo: descrever o software](https://help.zenodo.org/docs/github/describe-software)
- [Guia GitHub–Zenodo](https://rue-a.github.io/github-zenodo-integration/documentation)
- Guia para autores da New Astronomy (PDF enviado por você): dados Opção C, referência `[dataset]`
