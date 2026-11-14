# ESTILO DE FIGURAS (Super Mongo, preto e branco)

Valores de partida do programa (`UNIVERSAL_PAPER_CONTEXT.md` seção 4) já ajustados pelo que o P1 aprendeu (DEC-18, E7d). A **revista manda** nas medidas e no formato: confira `revistas/<revista>/ficha.md`.

## Regras (REG-FIG)
- Preto e branco; ticks **para dentro nos 4 lados**; **sem grade**; minor ticks em escala log.
- **Uma fonte só** em todo texto da figura: Courier Prime (licença OFL; arquivos em `repositorio/fonts/` com `OFL.txt`). O notebook falha com aviso se a fonte não for encontrada e verifica que o EPS tem só essa fonte. A fonte não tem letras gregas: escreva `alpha`, `beta` por extenso e não use mathtext.
- Diferenciar curvas por **estilo de linha e símbolo**, nunca por cinza; hachura para preenchimentos.
- Sem número de figura nem legenda dentro do arquivo; painéis com letras maiúsculas A, B se a revista pedir.
- Linhas com espessura ≥ 0,3 pt após a redução; fontes incorporadas.
- Formatos: **EPS** (obrigatório para LaTeX na EPL) e **PDF**; nomes `figure1.eps`, `figure1.pdf`... No manuscrito compilado localmente use só PDF vetorial (`\DeclareGraphicsExtensions{.pdf,.png}`), nunca EPS rasterizado.
- Larguras (EPL): 80 mm (1 coluna) ou 165 mm (2 colunas). Para ApJ/MNRAS: 3,5", 5,0", 7,0"; altura máxima 9,0".
- Texto alternativo (`\figalttext` na OUP) para cada figura.

## Código de partida

```python
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

# ============================================================
# CONFIGURAÇÃO SUPER MONGO — aplicar ANTES de qualquer plot
# ============================================================
def apply_super_mongo_style():
    mpl.rcParams.update({
        # Fonte
        'font.family':       'monospace',
        'font.monospace':    ['Courier Prime', 'Courier New',
                             'DejaVu Sans Mono', 'Courier'],
        'font.size':         12,
        'axes.labelsize':    12,
        'axes.titlesize':    12,
        'xtick.labelsize':   12,
        'ytick.labelsize':   12,
        'legend.fontsize':   11,

        # Cores — preto e branco APENAS
        'axes.prop_cycle':   mpl.cycler(color=['black']),
        'lines.color':       'black',
        'patch.edgecolor':   'black',
        'text.color':        'black',
        'axes.edgecolor':    'black',
        'axes.labelcolor':   'black',
        'xtick.color':       'black',
        'ytick.color':       'black',
        'figure.facecolor':  'white',
        'axes.facecolor':    'white',

        # Ticks voltados para DENTRO, nos 4 lados
        'xtick.direction':   'in',
        'ytick.direction':   'in',
        'xtick.top':         True,
        'ytick.right':       True,
        'xtick.major.size':  6,
        'xtick.minor.size':  3,
        'ytick.major.size':  6,
        'ytick.minor.size':  3,
        'xtick.major.width': 0.8,
        'ytick.major.width': 0.8,

        # Sem grade
        'axes.grid':         False,

        # Linhas
        'lines.linewidth':   1.2,
        'lines.markersize':  5,

        # Layout
        'figure.dpi':        150,
        'savefig.dpi':       300,
        'savefig.bbox':      'tight',
        'savefig.format':    'pdf',
    })

apply_super_mongo_style()

# ============================================================
# LINHAS PADRÃO para distinguir curvas (sem cores)
# ============================================================
LINE_STYLES = [
    {'ls': '-',  'lw': 1.5,  'color': 'black'},          # sólido
    {'ls': '--', 'lw': 1.5,  'color': 'black'},          # tracejado
    {'ls': ':',  'lw': 1.5,  'color': 'black'},          # pontilhado
    {'ls': '-.', 'lw': 1.5,  'color': 'black'},          # traço-ponto
    {'ls': '-',  'lw': 0.8,  'color': 'black'},          # sólido fino
]

MARKERS = ['o', 's', '^', 'D', 'v', 'p', '*']           # símbolos para scatter

# ============================================================
# SALVAR — sempre PDF + EPS para submissão
# ============================================================
def save_figure(fig, basename):
    """Salva em EPS (LaTeX) e PDF."""
    fig.savefig(f"{basename}.pdf", format='pdf', dpi=300, bbox_inches='tight')
    fig.savefig(f"{basename}.eps", format='eps', dpi=300, bbox_inches='tight')
    print(f"Salvo: {basename}.pdf  e  {basename}.eps")
```

Observações sobre o bloco acima:
- `font.monospace` lista Courier Prime primeiro, mas `Courier New` e `DejaVu Sans Mono` são **fallback silencioso**. No notebook do P1 isso foi trocado por um carregamento explícito de `repositorio/fonts/CourierPrime-*.ttf` com erro se faltar (REG-FIG).
- Para EPS, use `ps.fonttype = 42` e `pdf.fonttype = 42` e verifique com `grep -a FontName figureN.eps`.
- Formato final de cada figura: conferir tamanho em milímetros (`fig.set_size_inches(80/25.4, ...)`).
