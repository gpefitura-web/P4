# Hooks de verificação

Um paper pode plugar verificações próprias em `scripts/check_manuscript.py` sem editar o núcleo:

1. Crie `kit/pipeline/hooks/<nome>.py` (ou, no repositório do paper, `kit/pipeline/hooks/` é cópia: coloque o hook também em
   `PROP-NNN` para voltar ao kit se for útil a outros papers).
2. Defina `def check(root): ...` que recebe o `Path` da raiz do repositório do paper e devolve uma lista de strings
   (cada uma é um problema). Lista vazia = passou.
3. Ative em `kit.yml`: `verificacao.extra: [<nome>]`.

Exemplos úteis: conferir que todo número do manuscrito vem de macro; conferir limite de palavras do resumo;
conferir que nenhum número de `fora_repositorio/` aparece em `manuscrito/` (REG-PROMOCAO).

## Hooks que acompanham o kit (0.3.0)
| Hook | O que confere |
|---|---|
| `numeros_via_macro` | número solto na prosa de `manuscrito/main.tex` e `sec_*.tex` que não vem de macro |
| `ordem_floats` | figuras e tabelas citadas na ordem em que aparecem |
| `eprime` | ausência de formas de 'to be' (só para papers em E-Prime) |
| `limites_elsevier` | limites do guia da New Astronomy (exemplo de hook por revista) |
