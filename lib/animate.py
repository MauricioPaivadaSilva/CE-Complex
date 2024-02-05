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

        self.setup_plots()
        self.animate()

    ##   Definição de configurações dos gráfcos que são plotados
    
    def setup_plots(self):

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
        self.gf1.set_xlim(0, 61)
        self.gf1.set_ylim(-1.2, 1.2)
        self.gf1.set_xlabel('t (segundos)')
        self.gf1.set_yticks([-1, 0, 1])
        self.gf1.set_yticklabels(['-127V', '0V', '127V'])

        eixo_x = mpatches.FancyArrowPatch(
            (0, 0),
            (61, 0),
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
            scale_units='xy',
            scale=1,
            color='blue'
        )
        self.gf2.scatter(
            0,
            0,
            color='red'
        )
        self.gf2.set_xlim(-1.2, 1.2)
        self.gf2.set_xticks([-1, 0, 1])
        self.gf2.set_xticklabels(['-1', '0', '1'])
        self.gf2.set_ylim(-1.2, 1.2)
        self.gf2.set_yticks([-1, 0, 1])
        self.gf2.set_yticklabels(['-i', '0', 'i'])

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

        periodo = 1 / self.frequencia

        a, b = ((150 / (self.frequencia))), 0

        for i in range(0, 600):
            t = i / 10.0
            r = (np.pi * t)/180
            sin.append(np.sin(2 * np.pi * (r/periodo)))
            time.append(t)

            ####    Lógica de funcionamento da animação do ciclo trigonométrico
            ####
            ####    !!!NÃO APAGAR!!!
            ####

            cic_lim = ((150)/(self.frequencia))
            cic_lim_ = -1 * ((150 / (self.frequencia)))

            if(((a > 0) and (a < (cic_lim + 1))) and (b >= 0)):
                a -= 1
                b += 1
            elif(((a <= 0) and (a > (cic_lim_ - 1))) and (b > 0)):
                a -= 1
                b -= 1
            elif(((a < 0) and (a >= cic_lim_))):
                a += 1
                b -= 1
            elif(((a >= 0) and (a < (cic_lim + 1))) and (b > (cic_lim_ - 1))):
                a += 1
                b += 1
            
            self.update(time, sin, a, b)
            plt.pause(1 / 60) # Taxa de atualização = 60 Hz
        
        plt.show()

    ##  Função que atualiza os gráficos
    
    def update(self, time, sin, a, b):

        ### Atualiza o gráfico senoidal

        self.sin_line.set_data(time, sin)
        self.time_line.set_data([0, time[-1]], [0, 0])

        ### Atualiza o gráfico da função trigonométrica

        theta = np.linspace(0, 2* np.pi, 100)
        x = np.cos(theta)
        y = np.sin(theta)
        p = np.sqrt((a**2) + (b**2))

        vec_x = a/p
        vec_y = b/p

        self.circle.set_data(x, y)
        self.quiver.set_UVC(vec_x, vec_y)

        plt.tight_layout()