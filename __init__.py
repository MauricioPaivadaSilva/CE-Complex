#
#   Declaração da versão
#

__version__='0.4.5'

#
#   Chamada do router
#

#
#   Chamada das dependências necessárias
#

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from sys import argv as inp
import os


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

#
#   Inicio do código de erro
#

class Err:
    def __init__(self):
        pass

    def ErroGenerico():
        return("\n      \033[1;31;40mERRO!\033[m   \n")
    
    def FuncaoNaoImplementada():
        return("\n      \033[1;31;40mERRO!\033[m \033[3;33mFunção não implementada\033[m   \n")
    
    def ValorInseridoIncorretamente():
        return("\n      \033[1;31;40mERRO!\033[m \033[0;31;40mValor inserido de forma incorreta.\033[m\n")


################################################################
######      Início do código de criação do gráfico        ######
################################################################
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


######################################################
######      Início do código de animação        ######
######################################################

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
        self.gf1.set_xlim(0, 1010)
        self.gf1.set_xticks([0, 250, 500, 750, 1000])
        self.gf1.set_xticklabels(['0,00','0,25','0,50','0,75','1'])
        self.gf1.set_ylim(-1.2, 1.2)
        self.gf1.set_xlabel('t (segundos)')
        self.gf1.set_yticks([-1, 0, 1])
        self.gf1.set_yticklabels(['-127V', '0V', '127V'])

        eixo_x = mpatches.FancyArrowPatch(
            (0, 0),
            (1010, 0),
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

        a, b = ((150 / self.frequencia)), 0

        for i in range(0, 1000):
            t = i
            r = (np.pi * t)/3150
            sin.append(np.sin(2 * np.pi * (r/periodo)))
            time.append(t)

            ####    Lógica de funcionamento da animação do ciclo trigonométrico
            ####
            ####    !!!NÃO APAGAR!!!
            ####

            cic_lim = (150)
            cic_lim_ = -1 * (150)

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
            plt.pause(1 / 60) # Taxa de atualização = 60 fps
        
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

#   Recepção e interpretação dos dados para serem enviados a biblioteca

class MCEpy:
    def __init__(self, complexo, test):
        if(test == "None"):
            if("Hz" not in complexo):
                if(("i" in complexo) or ("j" in complexo)):
                    complexo = complexo[:-1]
                    cont_sig = complexo.count('-')

                    if(cont_sig == 2):
                        complexo = complexo.split('-')
                        R = -float(complexo[1])
                        Im = -float(complexo[2])
                        GraphCreate.Calculate(R, Im, False)
                    elif(cont_sig == 1):
                        if('+' in complexo):
                            complexo = complexo.split("+")
                            R = float(complexo[0])
                            Im = float(complexo[1])
                            GraphCreate.Calculate(R, Im, False)
                        else:
                            complexo = complexo.split("-")
                            if(len(complexo) == 2):
                                R = float(complexo[0])
                                Im = -float(complexo[1])
                                GraphCreate.Calculate(R, Im, False)
                            else:
                                R = float(0)
                                Im = -float(complexo[1])
                                GraphCreate.Calculate(R, Im, False)
                    elif(complexo.count('+') == 1):
                        complexo = complexo.split("+")
                        R = float(complexo[0])
                        Im = float(complexo[1])
                        GraphCreate.Calculate(R, Im, False)
                    else:
                        R = float(0)
                        Im = float(complexo[0])
                        GraphCreate.Calculate(R, Im, False)
                else:
                    if(complexo == "x" or complexo == "y"):
                        GraphCreate.Calculate(complexo, 0, False)
                    else:
                        try:
                            real = float(complexo)
                            return(GraphCreate.Calculate(real, 0.0, False))
                        except ValueError:
                            print(Err.ValorInseridoIncorretamente())
            elif("Hz" in complexo):
                frequencia = complexo[:-2]
                frequencia = float(frequencia)
                fig, (gf2, gf1) = plt.subplots(
                    nrows=2, 
                    ncols=1, 
                    figsize=(8, 6)
                )
                Animate(frequencia, gf1, gf2, None)
            else:
                print(Err.ValorInseridoIncorretamente())
        else:
            if(("i" in complexo) or ("j" in complexo)):
                complexo = complexo[:-1]
                cont_sig = complexo.count('-')

                if(cont_sig == 2):
                    complexo = complexo.split('-')
                    R = -float(complexo[1])
                    Im = -float(complexo[2])
                    GraphCreate.Calculate(R, Im, True)
                elif(cont_sig == 1):
                    if('+' in complexo):
                        complexo = complexo.split("+")
                        R = float(complexo[0])
                        Im = float(complexo[1])
                        GraphCreate.Calculate(R, Im, True)
                    else:
                        complexo = complexo.split("-")
                        if(len(complexo) == 2):
                            R = float(complexo[0])
                            Im = -float(complexo[1])
                            GraphCreate.Calculate(R, Im, True)
                        else:
                            R = float(0)
                            Im = -float(complexo[1])
                            GraphCreate.Calculate(R, Im, True)
                elif(complexo.count('+') == 1):
                    complexo = complexo.split("+")
                    R = float(complexo[0])
                    Im = float(complexo[1])
                    GraphCreate.Calculate(R, Im, True)
                else:
                    R = float(0)
                    Im = float(complexo[0])
                    GraphCreate.Calculate(R, Im, True)
            else:
                if(complexo == "x" or complexo == "y"):
                    GraphCreate.Calculate(complexo, 0.0, True)
                else:
                    try:
                        real = float(complexo)
                        GraphCreate.Calculate(real, 0.0, True)
                    except ValueError:
                        print(Err.ValorInseridoIncorretamente())

if __name__ == "__main__":
    MCEpy(inp[1], inp[2])
