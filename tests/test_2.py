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

from ..router import Tratamento as rt

##  Declarando as vaiáveis globais

let_1 = "x"
let_2 = "y"
num1 = "5"
num2 = "10i"
comp_1 = "2+2j"
comp_2 = "-2-2j"

##  Realizando teste das gerações de gráficos

###   Teste para a geraçãodo gráfico de sin

def test_da_geracao_de_grafico_de_sin_com_x():
    rt.Complex(let_1, True)

    if sys.platform.startswith('win'):
        diretorio_script = os.path.dirname(os.path.abspath(__file__))
        origin_sin = os.path.join(diretorio_script, '..\\img', 'origin_sin.png')
        test_img = os.path.join(diretorio_script, '..\\temp', 'test_comparar_grafico_sin.png')

        imagem_grafico1 = Image.open(origin_sin)
        imagem_grafico2 = Image.open(test_img)

        assert np.array_equal(np.array(imagem_grafico1), np.array(imagem_grafico2))
        
        caminho_arquivo = os.path.join(diretorio_script, '..\\temp', 'test_comparar_grafico_sin.png')
        os.remove(caminho_arquivo)
    else:
        diretorio_script = os.path.dirname(os.path.abspath(__file__))
        origin_sin = os.path.join(diretorio_script, '../img', 'origin_sin.png')
        test_img = os.path.join(diretorio_script, '../temp', 'test_comparar_grafico_sin.png')

        imagem_grafico1 = Image.open(origin_sin)
        imagem_grafico2 = Image.open(test_img)

        assert np.array_equal(np.array(imagem_grafico1), np.array(imagem_grafico2))
        
        caminho_arquivo = os.path.join(diretorio_script, '../temp', 'test_comparar_grafico_sin.png')
        os.remove(caminho_arquivo)

def test_da_geracao_de_grafico_de_sin_com_y():
    rt.Complex(let_2, True)
    
    diretorio_script = os.path.dirname(os.path.abspath(__file__))
    origin_sin = os.path.join(diretorio_script, '..\\img', 'origin_sin.png')
    test_img = os.path.join(diretorio_script, '..\\temp', 'test_comparar_grafico_sin.png')

    imagem_grafico1 = Image.open(origin_sin)
    imagem_grafico2 = Image.open(test_img)

    assert np.array_equal(np.array(imagem_grafico1), np.array(imagem_grafico2))
    
    caminho_arquivo = os.path.join(diretorio_script, '..\\temp', 'test_comparar_grafico_sin.png')
    os.remove(caminho_arquivo)

###   Teste para a geraçãodo gráfico de número complexo

def test_da_geracao_de_grafico_de_vetor_1():
    rt.Complex(comp_1, True)
    
    diretorio_script = os.path.dirname(os.path.abspath(__file__))
    origin_sin = os.path.join(diretorio_script, '..\\img', 'origin_vec_1.png')
    test_img = os.path.join(diretorio_script, '..\\temp', 'test_comparar_grafico_vec.png')

    imagem_grafico1 = Image.open(origin_sin)
    imagem_grafico2 = Image.open(test_img)

    assert np.array_equal(np.array(imagem_grafico1), np.array(imagem_grafico2))
    
    caminho_arquivo = os.path.join(diretorio_script, '..\\temp', 'test_comparar_grafico_vec.png')
    os.remove(caminho_arquivo)

def test_da_geracao_de_grafico_de_vetor_2():
    rt.Complex(comp_2, True)
    
    diretorio_script = os.path.dirname(os.path.abspath(__file__))
    origin_sin = os.path.join(diretorio_script, '..\\img', 'origin_vec_2.png')
    test_img = os.path.join(diretorio_script, '..\\temp', 'test_comparar_grafico_vec.png')

    imagem_grafico1 = Image.open(origin_sin)
    imagem_grafico2 = Image.open(test_img)

    assert np.array_equal(np.array(imagem_grafico1), np.array(imagem_grafico2))
    
    caminho_arquivo = os.path.join(diretorio_script, '..\\temp', 'test_comparar_grafico_vec.png')
    os.remove(caminho_arquivo)

def test_da_geracao_de_grafico_de_vetor_3():
    rt.Complex(num1, True)
    
    diretorio_script = os.path.dirname(os.path.abspath(__file__))
    origin_sin = os.path.join(diretorio_script, '..\\img', 'origin_vec_3.png')
    test_img = os.path.join(diretorio_script, '..\\temp', 'test_comparar_grafico_vec.png')

    imagem_grafico1 = Image.open(origin_sin)
    imagem_grafico2 = Image.open(test_img)

    assert np.array_equal(np.array(imagem_grafico1), np.array(imagem_grafico2))
    
    caminho_arquivo = os.path.join(diretorio_script, '..\\temp', 'test_comparar_grafico_vec.png')
    os.remove(caminho_arquivo)

def test_da_geracao_de_grafico_de_vetor_4():
    rt.Complex(num2, True)
    
    diretorio_script = os.path.dirname(os.path.abspath(__file__))
    origin_sin = os.path.join(diretorio_script, '..\\img', 'origin_vec_4.png')
    test_img = os.path.join(diretorio_script, '..\\temp', 'test_comparar_grafico_vec.png')

    imagem_grafico1 = Image.open(origin_sin)
    imagem_grafico2 = Image.open(test_img)

    assert np.array_equal(np.array(imagem_grafico1), np.array(imagem_grafico2))
    
    caminho_arquivo = os.path.join(diretorio_script, '..\\temp', 'test_comparar_grafico_vec.png')
    os.remove(caminho_arquivo)