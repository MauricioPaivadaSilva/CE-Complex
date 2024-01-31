#
#   Direcionamento e tratamento das informações que irão para a biblioteca.
#
#   Iniciando a chamada da lib e do dicionário de erros.
#

from lib.graph import GraphCreate as GC
from lib.err import Err as Err

#   Recepção e interpretação dos dados para serem enviados a biblioteca

class Tratamento:
    def __init__():
        pass

    def Complex(complex):
        if(("i" in complex) or ("j" in complex)):
            complex = complex[:-1]
            cont_sig = complex.cont('-')

            if(cont_sig == 2):
                complex = complex.split('-')
                R = -float(complex[1])
                Im = -float(complex[2])
                ...
            elif(cont_sig == 1):
                if('+' in complex):
                    complex = complex.split("+")
                    R = float(complex[0])
                    Im = float(complex[1])
                    ...
                else:
                    complex = complex.split("-")
                    R = float(complex[0])
                    Im = -float(complex[1])
                    ...
            else:
                complex = complex.split("+")
                R = float(complex[0])
                Im = float(complex[1])
        else:
            if(complex == "x" or complex == "y"):
                GC.Calculate(complex)
            else:
                try:
                    real = float(complex)
                    return(...)
                except ValueError:
                    return(Err.ValorInseridoIncorretamente())