#
#   Direcionamento e tratamento das informações que irão para a biblioteca.
#
#   Iniciando a chamada da lib e do dicionário de erros.
#

from .lib.graph import GraphCreate as GC
from .lib.err import Err as Err

#   Recepção e interpretação dos dados para serem enviados a biblioteca

class Tratamento:
    def __init__():
        pass

    def Complex(complexo):
        if(("i" in complexo) or ("j" in complexo)):
            complexo = complexo[:-1]
            cont_sig = complexo.count('-')

            if(cont_sig == 2):
                complexo = complexo.split('-')
                R = -float(complexo[1])
                Im = -float(complexo[2])
                return(GC.Calculate(R, Im))
            elif(cont_sig == 1):
                if('+' in complexo):
                    complexo = complexo.split("+")
                    R = float(complexo[0])
                    Im = float(complexo[1])
                    return(GC.Calculate(R, Im))
                else:
                    complexo = complexo.split("-")
                    if(len(complexo) > 2):
                        R = float(complexo[0])
                        Im = -float(complexo[1])
                        return(GC.Calculate(R, Im))
                    else:
                        R = float(0)
                        Im = -float(complexo[1])
                        return(GC.Calculate(R, Im))
            elif(complexo.count('+') == 1):
                complexo = complexo.split("+")
                print(complexo)
                R = float(complexo[0])
                Im = float(complexo[1])
                return(GC.Calculate(R, Im))
            else:
                print(complexo)
                R = float(0)
                Im = float(complexo[0])
                return(GC.Calculate(R, Im))
        else:
            if(complexo == "x" or complexo == "y"):
                GC.Calculate(complexo, 0)
            else:
                try:
                    real = float(complexo)
                    return(GC.Calculate(real, 0))
                except ValueError:
                    return(Err.ValorInseridoIncorretamente())