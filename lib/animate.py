#
#   Iniciando os a chamada das libs necessárias.
#

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import os

#
#   Iniciando os a chamada dos plug-ins necessários.
#

from err import Err as Err

##  Criação de variáveis globais

x = []
X = []
y = []
Y = []

rad = []

xlim_cic = 1.5
ylim_cic = 1.5
xlim_cic_ = -xlim_cic
ylim_cic_ = -ylim_cic

xlim_sin = 62
ylim_sin = 1.5
xlim_sin_ = 0
ylim_sin_ = -ylim_cic


##########################################
######      Início do código        ######
##########################################

class Animate:
    def __init__(self, frequencia, test):
        global x
        global X
        global y
        global Y
        global rad

        global xlim_sin
        global ylim_sin
        global xlim_sin_
        global ylim_sin_

        x.clear()
        X.clear()
        y.clear()
        Y.clear()
        rad.clear()

        plt.cla()
        plt.clf()

        num1 = float(frequencia[:-2])

        a = 0
        b = 0
        i = True
        Y.append(b)
        while i:
            b += 1
            Y.append(b)
            if(b == 60):
                i = False
        Y.sort()
        ey = Y

        Animate.ConvertInRad(num1, ey, test)
    
    def ConvertInRad(num1, eq, test):   #   Conversão dos valores de grau em radianos.

        #   Importação das variáveis globais.

        global rad

        for i in eq:
            r = (i*np.pi)/180
            rad.append(r)
        
        Animate.animmate_sin(num1, eq, test)

    def animmate_sin(num1, num2, test):

        sin = []

        plt.ion()
        temp = 0

        try:
            for i in rad:
                si = np.sin(i * (num1/4))
                sin.append(si)
        except:
            pass

        while temp <= 60.0:

            plt.cla()
            plt.clf()

            plt.plot(num2, sin, color="blue")
            plt.plot([0, temp], [0, 0], color="red", lw=2)
            plt.xlim(xlim_sin_, xlim_sin)
            plt.ylim(ylim_sin_, ylim_sin)
            plt.xlabel('s (segundos)')

            #   Adicionando o eixo x.
            eixo_x = mpatches.FancyArrowPatch(
                ((xlim_sin_), 0), 
                ((xlim_sin), 0), 
                color='black', 
                mutation_scale=15, 
                arrowstyle='->',
            )
            plt.gca().add_patch(eixo_x)

            #   Adicionando o eixo y.
            eixo_y = mpatches.FancyArrowPatch(
                (0, ylim_sin_),
                (0, ylim_sin),
                color="black",
                mutation_scale=15,
                arrowstyle='->'
            )
            plt.gca().add_patch(eixo_y)

            temp += 0.1
            plt.pause(0.05)
        
        plt.ioff()

        plt.show()

        print(temp)

        sin.clear()

if __name__ == "__main__":
    Animate("60Hz", None)