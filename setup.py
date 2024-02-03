from setuptools import setup

with open('README.md', 'r') as arq:
    readme = arq.read()

setup(
    name="MCEpy",
    long_description=readme,
    long_description_content_type="text/markdown",
    description="Biblioteca para interpretação e criação de dados e gáficos, com o objetivo de trabalhar com números complexos e circuitos elétricos",
    version="0.2.2",
    author="Maurício Paiva da Silva",
    license="MIT Licence",
    install_requires=[
        'numpy',
        'matplotlib',
        'pytest',
        'Pillow',
    ],
    packages=['MCEpy'],
    keywords=[
        "Números Complexos",
        "Circuitos Elétricos",
    ],
)