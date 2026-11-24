# ACHADOS — atritos e pontos não cobertos pelas decisões

1. **Nome do módulo.** O prompt manda `io.py`, mas esse nome sombreia o módulo `io` da biblioteca padrão. Arquivo chamado `p4io.py`. Sem efeito sobre decisões.
2. **Filtro de HD em Baum.** Quatro estrelas têm sufixo de letra (145958A/B, 178911B, 219834B); o primeiro filtro `isdigit` as descartava (1 543 linhas). Corrigido na 1ª tentativa; contagens batem com `3.2-01`/`3.2-22`.
