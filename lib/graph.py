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

from .err import Err as Err

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


##########################################
######      Início do código        ######
##########################################
class GraphCreate():
    def __init__(self):
        pass

    def Calculate(num1, num2, test):  #   Calculando os valores do gráfico para todo x e todo y.
        
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
            X.sort()
            ex = x+X
            GraphCreate.ConvertInRad(num1, ex, test)

        elif((type(num1) == type("y")) and (num1 == "y")): #   Criação dos valores para y (como grau).
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
            GraphCreate.ConvertInRad(num1, ey, test)
        
        elif((type(num1) == type(0.0)) and (type(num2) == type(0.0))): #   Verificando os valores para fazer a representação dos números complexos.

            GraphCreate.Graphcreate(num1, num2, test)
        else:
            # GraphCreate.Graphcreate(num1, num2, test)
            return(Err.ErroGenerico())

        x.clear()
        X.clear()
        y.clear()
        Y.clear()
    
    def ConvertInRad(num1, eq, test):   #   Conversão dos valores de grau em radianos.

        #   Importação das variáveis globais.

        global rad

        for i in eq:
            r = (i*np.pi)/180
            rad.append(r)
        
        GraphCreate.Graphcreate(num1, eq, test)
        
    def Graphcreate(num1, num2, test):    #   Criação do gráfico

        plt.clf()
        
        #   Importação das variáveis globais

        global rad
        global xlim
        global xlim_
        global ylim
        global ylim_

        #   Gerando as variáveis locais

        sin = []

        if(((type(num1) == type("x")) and (num1 == "x")) or (((type(num1) == type("y"))) and (num1 == "y"))):    #   Gerando o gráfico para todo valor em x que foi convertido.
            try:
                for i in rad:
                    si = np.sin(i)
                    sin.append(si)
            except:
                pass

            plt.plot(num2, sin, color="blue")
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

            if(test == True):
                file = os.path.join('temp', 'test_comparar_grafico_sin.png')
                plt.savefig(file)
            else:
                plt.show()

        elif((type(num1) == type(0.0)) and (type(num2) == type(0.0))):  #   Gerando o gráfico de vetor com números complexos

            plt.clf()
            
            raio = 1
            theta = np.linspace(0, 2*np.pi, 100)
            x = raio*np.cos(theta)
            y = raio*np.sin(theta)
            p = np.sqrt((num1**2)+(num2**2))

            
            vec_x = num1/p
            vec_y = num2/p

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

            if(test == True):
                file = os.path.join('temp', 'test_comparar_grafico_vec.png')
                plt.savefig(file)
            else:
                plt.show()
        else:
            return(Err.ErroGenerico())

        rad.clear()
        sin.clear()