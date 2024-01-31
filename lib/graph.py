#
#   Iniciando os a chamada das libs necessárias.
#

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

#
#   Iniciando os a chamada dos plug-ins necessários.
#

from lib.err import Err as Err

##  Criação de variáveis globais

x = []
X = []
y = []
Y = []

rad = []

xlim = 180
ylim = 1.5
xlim_ = -xlim
ylim_ = -ylim

PI = 3.141592653589793


##########################################
######      Início do código        ######
##########################################
class GraphCreate:
    def __init__(self):
        pass

    def Calculate(num1, num2):  #   Calculando os valores do gráfico para todo x e todo y.
        
        #   Chamada das variáveis globais

        global x
        global X
        global y
        global Y

        if((type(num1) == type("x")) and (num1 == "x")): #   Criação dos valores para x (como grau).
            a = 0
            b = 0
            i = True
            while i:
                a -=1
                b += 1
                x.append(a)
                X.append(b)
                if(b == 360): 
                    i = False
            x.sort()
            x.append(0)
            ex = x+X
            GraphCreate.GraphCreate(num1, None)

        elif((type(num1) == "y") and (num1 == "y")): #   Criação dos valores para y (como grau).
            a = 0
            b = 0
            i = True
            while i:
                a -= 1
                b += 1
                y.append(a)
                Y.append(b)
                if(b == 360):
                    i = False
                y.sort()
                y.append(0)
                Y.sort()
                ey = y+Y
                GraphCreate.GraphCreate(num1, None)
        
        elif((type(num1) == type(0.0)) and (type(num2) == type(0.0))): #   Verificando os valores para fazer a representação dos números complexos.

            GraphCreate.GraphCreate(num1, num2)

            # return(Err.FuncaoNaoImplementada())
        else:
            return(Err.ErroGenerico())
    
    def ConvertInRad(eq):   #   Conversão dos valores de grau em radianos.

        #   Importação das variáveis globais.

        global rad
        global PI

        pi = PI

        for i in eq:
            r = (i*pi)/180
            rad.append(r)
        
    def GraphCreate(num1, num2):    #   Criação do gráfico
        
        #   Importação das variáveis globais

        global rad
        global xlim
        global xlim_
        global ylim
        global ylim_

        #   Gerando as variáveis locais

        sin = []

        if(((type(num1) == type("x")) and (num1 == "x")) or ((type(num1) == type("x"))) and (num1 == "y")):    #   Gerando o gráfico para todo valor em x que foi convertido.
            try:
                for i in rad:
                    si = np.sin(i)
                    sin.append(si)
            except:
                pass
            plt.plot(num2, sin)
            plt.xlim(xlim_, xlim)
            plt.ylim(ylim_, ylim)

            #   Adicionando o eixo x.
            eixo_x = mpatches.FancyArrowPatch(
                ((xlim_ - 2), 0), 
                ((xlim + 2), 0), 
                color='black', 
                mutation_scale=15, 
                arrowstyle='->'
            )
            plt.gca().add_patch(eixo_x)

            #   Adicionando o eixo y.
            eixo_y = mpatches.FancyArrowPatch(
                (0, ylim_),
                (0, ylim),
                color="black",
                mutation_scale=15,
                arrowstyle='->'
            )
            plt.gca().add_patch(eixo_y)
            plt.show()

        elif((type(num1) == type(0.0)) and (type(num2) == type(0.0))):  #   Gerando o gráfico de vetor com números complexos
            plt.plot(num1, num2)
            plt.xlim(xlim_, xlim)
            plt.ylim(ylim_, ylim)

            #   Adicionando o eixo x.
            eixo_x = mpatches.FancyArrowPatch(
                ((xlim_ - 2), 0), 
                ((xlim + 2), 0), 
                color='black', 
                mutation_scale=15, 
                arrowstyle='->'
            )
            plt.gca().add_patch(eixo_x)

            #   Adicionando o eixo y.
            eixo_y = mpatches.FancyArrowPatch(
                (0, ylim_),
                (0, ylim),
                color="black",
                mutation_scale=15,
                arrowstyle='->'
            )
            plt.gca().add_patch(eixo_y)
            plt.show()
        else:
            return(Err.ErroGenerico())