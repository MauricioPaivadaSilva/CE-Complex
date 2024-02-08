#
#   Chamando os arquivos das libs para teste
#

from ..__init__ import MCEpy as rt
from ..__init__ import GraphCreate as GC

##  Declarando as vaiáveis globais

num1 = "5"
num2 = "10"
num3 = 5.0
num4 = 10.0
let = "a"

##  Realizando teste das respostas de erro

###   Teste para a resposta de valor inserido incorretamente

# TESTE ANULADO DEVIDO A RETORNO EM FORMATO DE OBJETO <MCEpy.__init__.MCEpy object at 0x0000020DF663C620>

# def test_Valor_Inserido_Incorretamente_ROUTER__init__():
#     result = rt(let, True)
#     esp = "\n      \033[1;31;40mERRO!\033[m \033[0;31;40mValor inserido de forma incorreta.\033[m\n"

#     assert result == esp, f"\n      \033[1;31;40mERRO!\033[m {result} != {esp}"

###   Teste para a resposta de Erro genérico

def test_Resposta_Generica_GRAPH_Calculate():
    result = GC.Calculate(num3, let, True)
    esp = "\n      \033[1;31;40mERRO!\033[m   \n"
    assert result == esp, f"\n      \033[1;31;40mERRO!\033[m {result} != {esp}"

def test_Resposta_Generica_GRAPH_GraphCreate():
    result = GC.Graphcreate(num1, num2, True)
    esp = "\n      \033[1;31;40mERRO!\033[m   \n"
    assert result == esp, f"\n      \033[1;31;40mERRO!\033[m {result} != {esp}"

###   Teste para a resposta de Erro genérico

def test_Funcao_Nao_Implementada_GRAPH_Calculate():
    result = GC.Calculate(num1, num2, True)
    esp = "\n      \033[1;31;40mERRO!\033[m   \n"
    assert result == esp, f"\n      \033[1;31;40mERRO!\033[m {result} != {esp}"