#
#   Chamando as bibliotecas necessáras
#

from PIL import Image
import numpy as np
import os
import sys

#
#   Chamando os arquivos das libs para teste
#

from ..__init__ import MCEpy as rt

##  Declarando as vaiáveis globais

let_1 = "x"
let_2 = "y"
num1 = "5"
num2 = "10i"
comp_1 = "2+2j"
comp_2 = "-2-2j"
comp_3 = "2-2j"

##  Verificando o sistema operacional

sistema_operacional = sys.platform

if(sistema_operacional.startswith('win')):
    separador = '\\'
elif(sistema_operacional.startswith('linux') or sistema_operacional.startswith('darwin')):
    separador = '/'
else:
    raise OSError("Sistema operacional não suportado.")

##  Realizando teste das gerações de gráficos

###   Teste para a geraçãodo gráfico de sin

def test_da_geracao_de_grafico_de_sin_com_x():
    rt(let_1, True)

    diretorio_script = os.path.dirname(os.path.abspath(__file__))
    origin_sin = os.path.join(diretorio_script, f'..{separador}img', 'origin_sin.png')
    test_img = os.path.join(diretorio_script, f'..{separador}temp', 'test_comparar_grafico_sin.png')

    imagem_grafico1 = Image.open(origin_sin)
    imagem_grafico2 = Image.open(test_img)

    assert np.array_equal(np.array(imagem_grafico1), np.array(imagem_grafico2))
    
    caminho_arquivo = os.path.join(diretorio_script, f'..{separador}temp', 'test_comparar_grafico_sin.png')
    os.remove(caminho_arquivo)

def test_da_geracao_de_grafico_de_sin_com_y():
    rt(let_2, True)
    
    diretorio_script = os.path.dirname(os.path.abspath(__file__))
    origin_sin = os.path.join(diretorio_script, f'..{separador}img', 'origin_sin.png')
    test_img = os.path.join(diretorio_script, f'..{separador}temp', 'test_comparar_grafico_sin.png')

    imagem_grafico1 = Image.open(origin_sin)
    imagem_grafico2 = Image.open(test_img)

    assert np.array_equal(np.array(imagem_grafico1), np.array(imagem_grafico2))
    
    caminho_arquivo = os.path.join(diretorio_script, f'..{separador}temp', 'test_comparar_grafico_sin.png')
    os.remove(caminho_arquivo)

###   Teste para a geraçãodo gráfico de número complexo

def test_da_geracao_de_grafico_de_vetor_1():
    rt(comp_1, True)
    
    diretorio_script = os.path.dirname(os.path.abspath(__file__))
    origin_sin = os.path.join(diretorio_script, f'..{separador}img', 'origin_vec_1.png')
    test_img = os.path.join(diretorio_script, f'..{separador}temp', 'test_comparar_grafico_vec.png')

    imagem_grafico1 = Image.open(origin_sin)
    imagem_grafico2 = Image.open(test_img)

    assert np.array_equal(np.array(imagem_grafico1), np.array(imagem_grafico2))
    
    caminho_arquivo = os.path.join(diretorio_script, f'..{separador}temp', 'test_comparar_grafico_vec.png')
    os.remove(caminho_arquivo)

def test_da_geracao_de_grafico_de_vetor_2():
    rt(comp_2, True)
    
    diretorio_script = os.path.dirname(os.path.abspath(__file__))
    origin_sin = os.path.join(diretorio_script, f'..{separador}img', 'origin_vec_2.png')
    test_img = os.path.join(diretorio_script, f'..{separador}temp', 'test_comparar_grafico_vec.png')

    imagem_grafico1 = Image.open(origin_sin)
    imagem_grafico2 = Image.open(test_img)

    assert np.array_equal(np.array(imagem_grafico1), np.array(imagem_grafico2))
    
    caminho_arquivo = os.path.join(diretorio_script, f'..{separador}temp', 'test_comparar_grafico_vec.png')
    os.remove(caminho_arquivo)

def test_da_geracao_de_grafico_de_vetor_3():
    rt(num1, True)
    
    diretorio_script = os.path.dirname(os.path.abspath(__file__))
    origin_sin = os.path.join(diretorio_script, f'..{separador}img', 'origin_vec_3.png')
    test_img = os.path.join(diretorio_script, f'..{separador}temp', 'test_comparar_grafico_vec.png')

    imagem_grafico1 = Image.open(origin_sin)
    imagem_grafico2 = Image.open(test_img)

    assert np.array_equal(np.array(imagem_grafico1), np.array(imagem_grafico2))
    
    caminho_arquivo = os.path.join(diretorio_script, f'..{separador}temp', 'test_comparar_grafico_vec.png')
    os.remove(caminho_arquivo)

def test_da_geracao_de_grafico_de_vetor_4():
    rt(num2, True)
    
    diretorio_script = os.path.dirname(os.path.abspath(__file__))
    origin_sin = os.path.join(diretorio_script, f'..{separador}img', 'origin_vec_4.png')
    test_img = os.path.join(diretorio_script, f'..{separador}temp', 'test_comparar_grafico_vec.png')

    imagem_grafico1 = Image.open(origin_sin)
    imagem_grafico2 = Image.open(test_img)

    assert np.array_equal(np.array(imagem_grafico1), np.array(imagem_grafico2))
    
    caminho_arquivo = os.path.join(diretorio_script, f'..{separador}temp', 'test_comparar_grafico_vec.png')
    os.remove(caminho_arquivo)

def test_da_geracao_de_grafico_de_vetor_5():
    rt(comp_3, True)

    diretorio_script = os.path.dirname(os.path.abspath(__file__))
    origin_sin = os.path.join(diretorio_script, f'..{separador}img', 'origin_vec_5.png')
    test_img = os.path.join(diretorio_script, f'..{separador}temp', 'test_comparar_grafico_vec.png')

    imagem_grafico1 = Image.open(origin_sin)
    imagem_grafico2 = Image.open(test_img)

    assert np.array_equal(np.array(imagem_grafico1), np.array(imagem_grafico2))
    
    caminho_arquivo = os.path.join(diretorio_script, f'..{separador}temp', 'test_comparar_grafico_vec.png')
    os.remove(caminho_arquivo)
