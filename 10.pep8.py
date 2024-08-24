""""
PEP8 - Python Enhancement Proposal

São propostas de melhorias para a Linguagem Python

-Para acessar o "The Zen of Python" use o comando (import this)

        The Zen of Python (O Zen de Python)
        De: Tim Peters

    Bonito é melhor que feio.
    Explícito é melhor que implícito.
    Simples é melhor que complexo.
    Complexo é melhor do que complicado.
    Plano é melhor do que aninhado.
    Esparso é melhor do que denso.
    A legibilidade conta.
    Casos especiais não são especiais o suficiente para quebrar as regras.
    Embora a praticidade supere a pureza.
    Os erros nunca devem passar silenciosamente.
    A menos que explicitamente silenciado.
    Diante da ambiguidade, recuse a tentação de adivinhar.
    Deve haver uma - e de preferência apenas uma - maneira óbvia de fazer isso.
    Embora essa maneira possa não ser óbvia no início, a menos que você seja holandês.
    Agora é melhor do que nunca.
    Embora nunca seja melhor do que *agora*.
    Se a implementação é difícil de explicar, é uma má ideia.
    Se a implementação for fácil de explicar, pode ser uma boa ideia.
    Namespaces são uma ótima ideia -- vamos fazer mais desses!


A ideia da PEP8 é que possamos escrever códigos Python de forma Pythônica.


[1] - Utilize Camel Case para nomes de classe;

class Calculadora:
    pass

clas CalculadoraCientifica:
    pass


[2] - Utilize nomes em minúsculo, separados por underline para funções ou variáveis;

def soma():
    pass

def soma_dois():
    pass

numero = 4

numero_impar = 5


[3] - Utlize 4 espaços para identação!

if 'a' in 'banana':
    print('tem')


[4] - Linhas em branco
- Separar funções e definições de classe com duas linhas em branco;
- Métodos dentro de uma classe devem ser separados com uma única linha em branco;


[5] - Imports
- Imports devem ser sempre feitos em linhas separadas;

# Import Errado

import sys, os

# Import Certo

import sys
import os

# Não há problemas em utilizar:

from types import StringType, ListType

# Caso tenha muitos imports de um mesmo pacote, recomenda-se fazer:

from types import (
    StringType,
    ListType,
    SetType,
    OutroType
)

# Imports devem ser colocados no topo do arquivo, logo depois de quaisquer comentários ou docstring e
# antes de constantes ou variáveis globais.


[6] - Espaços em expressões e instruções

# Não faça:

funcao( algo[ 1 ], { outro: 2 } )

# Faça:

funcao(algo[1], {outro: 2})

# Não faça:

algo (1)

# Faça:

algo(1)

# Não faça:

dict ['chave'] = list [indice]

# Faça:

dict['chave'] = lista[indice]

# Não faça:

x               = 1
y               = 3
variavel_longa  = 5

# Faça

x = 1
y = 3
variavel_longa = 5


[7] - Termine sempre uma instrução com uma nova linha
"""
import this











