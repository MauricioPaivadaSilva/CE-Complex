#
#   Chamada das dependências necessárias
#

import matplotlib.pyplot as plt

#
#   Direcionamento e tratamento das informações que irão para a biblioteca.
#
#   Iniciando a chamada da lib e do dicionário de erros.
#

from .lib.graph import GraphCreate as GC
from .lib.animate import Animate
from .lib.err import Err as Err

#   Recepção e interpretação dos dados para serem enviados a biblioteca

class Tratamento:
    def __init__():
        pass

    def Complex(complexo, test):
        if(test == None):
            if("Hz" not in complexo):
                if(("i" in complexo) or ("j" in complexo)):
                    complexo = complexo[:-1]
                    cont_sig = complexo.count('-')

                    if(cont_sig == 2):
                        complexo = complexo.split('-')
                        R = -float(complexo[1])
                        Im = -float(complexo[2])
                        return(GC.Calculate(R, Im, False))
                    elif(cont_sig == 1):
                        if('+' in complexo):
                            complexo = complexo.split("+")
                            R = float(complexo[0])
                            Im = float(complexo[1])
                            return(GC.Calculate(R, Im, False))
                        else:
                            complexo = complexo.split("-")
                            if(len(complexo) > 2):
                                R = float(complexo[0])
                                Im = -float(complexo[1])
                                return(GC.Calculate(R, Im, False))
                            else:
                                R = float(0)
                                Im = -float(complexo[1])
                                return(GC.Calculate(R, Im, False))
                    elif(complexo.count('+') == 1):
                        complexo = complexo.split("+")
                        print(complexo)
                        R = float(complexo[0])
                        Im = float(complexo[1])
                        return(GC.Calculate(R, Im, False))
                    else:
                        print(complexo)
                        R = float(0)
                        Im = float(complexo[0])
                        return(GC.Calculate(R, Im, False))
                else:
                    if(complexo == "x" or complexo == "y"):
                        GC.Calculate(complexo, 0, False)
                    else:
                        try:
                            real = float(complexo)
                            return(GC.Calculate(real, 0.0, False))
                        except ValueError:
                            return(Err.ValorInseridoIncorretamente())
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
                return(Err.ValorInseridoIncorretamente)
        else:
            if(("i" in complexo) or ("j" in complexo)):
                complexo = complexo[:-1]
                cont_sig = complexo.count('-')

                if(cont_sig == 2):
                    complexo = complexo.split('-')
                    R = -float(complexo[1])
                    Im = -float(complexo[2])
                    return(GC.Calculate(R, Im, True))
                elif(cont_sig == 1):
                    if('+' in complexo):
                        complexo = complexo.split("+")
                        R = float(complexo[0])
                        Im = float(complexo[1])
                        return(GC.Calculate(R, Im, True))
                    else:
                        complexo = complexo.split("-")
                        if(len(complexo) > 2):
                            R = float(complexo[0])
                            Im = -float(complexo[1])
                            return(GC.Calculate(R, Im, True))
                        else:
                            R = float(0)
                            Im = -float(complexo[1])
                            return(GC.Calculate(R, Im, True))
                elif(complexo.count('+') == 1):
                    complexo = complexo.split("+")
                    print(complexo)
                    R = float(complexo[0])
                    Im = float(complexo[1])
                    return(GC.Calculate(R, Im, True))
                else:
                    print(complexo)
                    R = float(0)
                    Im = float(complexo[0])
                    return(GC.Calculate(R, Im, True))
            else:
                if(complexo == "x" or complexo == "y"):
                    GC.Calculate(complexo, 0.0, True)
                else:
                    try:
                        real = float(complexo)
                        return(GC.Calculate(real, 0.0, True))
                    except ValueError:
                        return(Err.ValorInseridoIncorretamente())