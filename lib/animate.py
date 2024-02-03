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
    def __init__(self, frequencia, tipo, test):
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

        if(frequencia != 0.0):
            num1 = frequencia
            xlim_sin = num1 + 2
        else:
            num1 = 60.0
            xlim_sin = num1 + 2

        a = 0
        b = 0
        i = True
        Y.append(b)
        while i:
            b += 1
            Y.append(b)
            if(b == num1):
                i = False
        Y.sort()
        ey = Y

        if(tipo == "sin"):
            Animate.ConvertInRad(num1, ey, test)
        else:
            Animate.animmate_cic(test)
    
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

        # print(temp)   #   Condição para leitura de dados

        sin.clear()
    
    def animmate_cic(test):

        plt.ion()
        temp = 0
        num1 = 10
        num2 = 0

        while temp <= 60.1:
            plt.cla()
            plt.clf()

            raio = 1
            theta = np.linspace(0, 2*np.pi, 100)
            x = raio*np.cos(theta)
            y = raio*np.sin(theta)
            p = np.sqrt((num1**2)+(num2**2))

            
            vec_x = num1/p
            vec_y = num2/p

            if(((num1 > 0) and (num1 < 11)) and (num2 >= 0)):
                num1 -= 1
                num2 += 1
            elif(((num1 <= 0) and (num1 > -11)) and (num2 > 0)):
                num1 -= 1
                num2 -= 1
            elif(((num1 < 0) and (num1 >= -10))):
                num1 += 1
                num2 -= 1
            elif(((num1 >= 0) and (num1 < 11)) and (num2 > -11)):
                num1 += 1
                num2 += 1

            plt.plot(x, y, color='black')
            plt.quiver(
                0, 
                0, 
                vec_x, 
                vec_y, 
                angles='xy', 
                scale_units='xy', 
                scale=1, 
                color='black',
            )

            # Plota o ponto vermelho
            plt.scatter(0, 0, color='red', label='Ponto Vermelho')
            
            plt.xlim(-1.5, 1.5)
            plt.ylim(-1.5, 1.5)

            #  Adicionando o eixo x.
            eixo_x = mpatches.FancyArrowPatch(
                (( -1.5), 0), 
                (( + 1.5), 0), 
                color='black', 
                mutation_scale=15, 
                arrowstyle='->'
            )
            plt.gca().add_patch(eixo_x)

            #   Adicionando o eixo y.
            eixo_y = mpatches.FancyArrowPatch(
                (0, -1.5),
                (0, 1.5),
                color="black",
                mutation_scale=15,
                arrowstyle='->'
            )
            plt.gca().add_patch(eixo_y)
            plt.gca().set_aspect('equal', adjustable='box')

            temp += 0.1
            plt.pause(0.05)

        plt.ioff()

        plt.show()