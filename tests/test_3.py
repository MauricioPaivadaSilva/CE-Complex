#
#   Importando a lib os
#

import os

#
#   Chamando os arquivos das libs para teste
#

from ..__init__ import MCEpy as rt
from ..__init__ import GraphCreate as GC

##  Declarando as vaiáveis globais

num_1 = "1,3+2j"
num_2 = "1,45+j2"

###   Teste para a resposta de Erro genérico

def test_Resposta_trocando_virgula_por_ponto_1():
    result = rt(num_1, True)
    esp = "1.3"
    assert result == esp, f"\n      \033[1;31;40mERRO!\033[m {result} != {esp}"

def test_Resposta_trocando_virgula_por_ponto_2():
    result = rt(num_2, True)
    esp = "1.45"
    assert result == esp, f"\n      \033[1;31;40mERRO!\033[m {result} != {esp}"