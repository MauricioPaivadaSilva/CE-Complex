from setuptools import setup

with open('README.md', 'r') as arq:
    readme = arq.read()

setup(
    name="MCEpy",
    long_description=readme,
    long_description_content_type="text/markdown",
    description="Biblioteca para interpretação e criação de dados e gáficos, com o objetivo de trabalhar com números complexos e circuitos elétricos",
    version="0.0.2",
    author="Maurício Paiva da Silva",
    license="MIT Licence",
    install_requires=[
        'numpy==1.22.0',
        'matplotlib==3.4.3',
        'pytest==8.0.0',
        'Pillow==10.1.0',
    ],
    packages=['MCEpy'],
    keywords=[
        "Números Complexos",
        "Circuitos Elétricos",
    ],
)