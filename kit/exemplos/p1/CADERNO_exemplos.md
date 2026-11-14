# Exemplos de entradas do CADERNO (P1)

Duas entradas reais para mostrar o nível de detalhe esperado: (1) artigo com camada de texto, (2) scan lido como imagem. Fonte: CADERNO_PESQUISA.md do P1.

### davenport2016 (ApJ 829, 23)
- p1: 851.168 flares candidatos acima do limiar de completude de 68%, em 4041 estrelas (1,9% das estrelas Kepler); energia média detectada ~1e35 erg (p8: logE = 34,6).
- p2-3: usa todas as curvas de luz Kepler Q0-17 (DR24), cadência longa (30 min) e curta (1 min), fluxo SAP; 3.144.487 arquivos de 207.617 alvos.
- p5: para cada flare guarda início, fim, pico, amplitude máxima, FWHM, χ², KS e duração equivalente (ED). A energia NÃO é medida diretamente: E = ED × L_Kp (p5, seção 3.3), com L_Kp da fotometria g-Ks do KIC v10 e isócrona PARSEC de 1 Gyr, Z=0,019, sem extinção; assume que todas as estrelas estão na sequência principal (distância errada para gigantes/subgigantes). A energia é a emitida na banda Kepler, sem correção espectral.
- p5: Teff não é usado; a cor g-i é o proxy de temperatura (p7: g-i vs massa).
- p6: completude medida por injeção de 100 flares artificiais por segmento contínuo; limites de 68% e 90% (em ED) guardados junto de cada flare (valor -99 se não atingido).
- p7: amostra final exige >=100 candidatos por estrela e >=10 acima do limiar de 68%. Corte em log g não aplicado (KIC log g não confiável); a amostra pode conter não-anãs (p7).
- p8-9: FFD cumulativa por estrela, truncada pelo limiar de 68%, bins de 0,1 dex, incerteza de Poisson (Gehrels 1986); ajuste de lei de potência por mínimos quadrados ponderados (NÃO MLE). Exemplo GJ 1243: inclinação -0,98; KIC 11551430 mostra quebra em alta energia.
- p9: o próprio autor nota possível quebra/ruptura da lei de potência em alta energia (e abaixo de logE~31 em Hawley+2014, não verificável).
- p13: energias máximas chegam a 1e39 erg, possivelmente por erro de de-trending ou de luminosidade (autor alerta).
- p14, Tabela 1 (na versão arXiv; o texto p7 a chama de 'Table 7'): só RESUMO POR ESTRELA para as 4041 estrelas: KID, g-i, massa, Prot (McQuillan), N_flares, N_flares(E>E68), L_fl/L_Kp, α, β. 'A tabela inteira em formato legível por máquina online.' O artigo não lista energias por flare.
- p14: rótulos α/β da Tabela 1 (ex.: α=18,83; β=-0,55) parecem trocados em relação à Fig. 6 (α = inclinação, β = intercepto: α=-0,98; β=31,08). Conferir no ReadMe do VizieR.
- p3: código aberto em github.com/jradavenport/appaloosa.


### crosby1993 (Sol. Phys. 143, 275; scan sem texto; páginas lidas como imagem: PDF p8-9 = impressas 282-283)
- p282, Tabela II: inclinações de ajustes de lei de potência às distribuições de parâmetros de flares em raios X duros (SMM/HXRBS): taxa de pico P: -1,73±0,01 (1980-82; faixa -1,67 a -1,73 entre períodos); duração D: -1,95 a -2,22 (conforme faixa); fluxo de fotões de pico I(25 keV): -1,62±0,02 (1980-82); fluxo integral Φ(>25 keV): -1,59±0,01; fluxo de energia de elétrons F: -1,67±0,04; energia total em elétrons W(>25 keV): -1,53±0,02 (1980-82), -1,48 a -1,53 nos outros períodos.
- Texto p282: 'a inclinação de -1,73 está ligeiramente abaixo de -1,8 de Dennis (1985)'.
- => α solar = 1,53 do documento de estratégia corresponde à energia total em elétrons (W, > 25 keV), não ao pico de fluxo.


## Exemplo de entrada de log de chat com uso de IA (REG-IA)
- chat N (cont.): usuário aprovou as propostas da seção 11 e RAD_MAX relativo à mediana (rascunho 2). Lacunas checadas: clauset2009 p17 (precisão do p-valor, 1/4 ε^-2 conjuntos), alstott2014 p8, p9, p12 (nested automático, truncated = corte exponencial), EPLgraphics p1 e p2 (figuras compostas, fontes padrão). Sem fonte na coleção: bootstrap por estrela, Holm, Q de Cochran, calibração por simulação (descritos sem citação), fórmula da bissetriz de isobe1990 (scan). Pergunta do usuário: por que M, K, G e não F, G, K, M. Evidência da coleção sobre F: yang2019 p1 (FFDs de F a 
