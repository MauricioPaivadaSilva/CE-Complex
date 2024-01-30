#
#   Iniciando os a chamada das libs necessárias.
#

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

##  Criação de variáveis globais

x = []
X = []
y = []
Y = []

xlim = 180
ylim = 1.5
xlim_ = -xlim
ylim_ = -ylim

PI = 3.141592653589793

class GraphCreate():
    def __init__(self):
        pass

    def Calculate(num1, num2):  #   Calculando os valores do gráfico para todo x e todo y.
        
        #   Chamada das variáveis globais

        global x
        global X
        global y
        global Y

        if((type(num1) == type("x")) and (num1 == "x")): #   Criação dos valores para x até um valor com que irá sempre aparecer no gráfico.
            a = 0
            b = 0
            i = True
            while i:
                a -=1
                b += 1
                x.append(a)
                X.append(b)
                if(b == 360*8): 
                    i = False
            x.sort()
            x.append(0)
            ex = x+X
        
        elif((type(num1) == "y") and (num1 == "y")): #   Criação dos valores para y até um valor com que irá sempre aparecer no gráfico.
            a = 0
            b = 0
            i = True
            while i:
                a -= 1
                b += 1
                y.append(a)
                Y.append(b)
                if(b == 360*8):
                    i = False
                y.sort()
                y.append(0)
                Y.sort()
                ey = y+Y
        
        elif((type(num1) == type(0.0)) and (type(num2) == type(0.0))): #   Verificando os valores para fazer a representação dos números complexos.
            return("\n  Função ainda não implementada\n")
        else:
            return("\n  Erro!\n")