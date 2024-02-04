#
#   Chamada das dependencias necessárias
#

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

#
#   Chamada do plugin necessário
#

from .err import Err as Err

##########################################
######      Início do código        ######
##########################################

class Animate:
    def __init__(self, frequencia, gf1, gf2, test):
        self.gf1 = gf1
        self.gf2 = gf2
        self.frequencia = frequencia

        self.setup_plots(frequencia)
        self.animate()

    ##   Definição de configurações dos gráfcos que são plotados
    
    def setup_plots(self, frequencia):

        ### Gráfico da função senoide

        self.sin_line, = self.gf1.plot(
            [], 
            [], 
            color="blue", 
            lw=2
        )
        self.time_line, = self.gf1.plot(
            [], 
            [], 
            color="red", 
            lw=2
        )
        self.gf1.set_xlim(0, (frequencia + 2))
        self.gf1.set_ylim(-1.2, 1.2)
        self.gf1.set_xlabel('t (segundos)')
        self.gf1.set_yticks([-1, 0, 1])
        self.gf1.set_yticklabels(['-127V', '0V', '127V'])

        eixo_x = mpatches.FancyArrowPatch(
            (0, 0),
            ((frequencia + 2), 0),
            color='black',
            mutation_scale=15,
            arrowstyle='->'
        )
        self.gf1.add_patch(eixo_x)

        ### Gráfico da ciclo trigonométrico
        
        self.circle, = self.gf2.plot(
            [],
            [],
            color='black'
        )
        self.quiver = self.gf2.quiver(
            0,
            0,
            0,
            0,
            angles='xy',
            scale=1,
            color='black'
        )
        self.gf2.scatter(
            0,
            0,
            color='red'
        )
        self.gf2.set_xlim(-1.2, 1.2)
        self.gf2.set_ylim(-1.2, 1.2)

        eixo_x_cic = mpatches.FancyArrowPatch(
            (-1.2, 0),
            (1.2, 0),
            color='black',
            mutation_scale=15,
            arrowstyle='->'
        )
        self.gf2.add_patch(eixo_x_cic)

        eixo_y_cic = mpatches.FancyArrowPatch(
            (0, -1.2),
            (0, 1.2),
            color='black',
            mutation_scale=15,
            arrowstyle='->'
        )
        self.gf2.add_patch(eixo_y_cic)
        self.gf2.set_aspect('equal', adjustable='box')

    ##   Função de animação dos gráficos

    def animate(self):

        sin = []
        time = []

        a, b = 10, 0

        for i in range(0, 600):
            t = i / 10.0
            sin.append(np.sin(t * (self.frequencia)))
            time.append(t)

            ####    Lógica de funcionamento da animação do ciclo trigonométrico
            ####
            ####    !!!NÃO APAGAR!!!
            ####

            if(((a > 0) and (a < 11)) and (b >= 0)):
                a -= 1
                b += 1
            elif(((a <= 0) and (a > -11)) and (b > 0)):
                a -= 1
                b -= 1
            elif(((a < 0) and (a >= -10))):
                a += 1
                b -= 1
            elif(((a >= 0) and (a < 11)) and (b > -11)):
                a += 1
                b += 1
            
            self.update_plots(time, sin, a, b)
            plt.pause(0.05)