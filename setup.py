from setuptools import setup

with open('README.md', 'r') as arq:
    readme = arq.read()

setup(
    name="MCEpy",
    long_description=readme,
    long_description_content_type="text/markdown",
    description="Biblioteca para interpretação e criação de dados e gáficos, com o objetivo de trabalhar com números complexos e circuitos elétricos",
    version="0.4.10",
    author="Maurício Paiva da Silva",
    license="MIT Licence",
    install_requires=[
        'numpy==1.26.3',
        'matplotlib==3.8.2',
        'pytest==8.0.0',
        'Pillow',
        'PyQt5',
    ],
    packages=['.'],
    keywords=[
        "Números Complexos",
        "Circuitos Elétricos",
    ],
)
