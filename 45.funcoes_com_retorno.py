"""
Funções com retorno

numeros = [1, 2, 3]

ret_pop = numeros.pop()

print(f'Retorno de pop: {ret_pop}')

ret_pr = print(numeros)

print(f'Retorno de print: {ret_pr}')




# Exemplo função
# Só imprime, não retorna nada
def quadrado_de_7():
    print(7 * 7)

ret = quadrado_de_7()

print(f'Retorno: {ret}')

# Obs: Em Python, quando uma função não retorna nenhum valor, o retorno é 'None'.




# Vamos refatorar esta função para que ela retorna o valor
# refatorar = reescrever

def quadrado_de_7():
    return 7 * 7

# Criamos uma variável para receber o retorno da função
ret = quadrado_de_7()

print(f'Retorno: {ret}')

# Obs: Funções Python que retornam valores, devem retornar estes valores com a
# palavra reservada 'return'

# Obs: Não precisamos necessariamente criar uma variável para receber o retorno
# de uma função. Podemos passar a execução da função para outras funções.



# Refatorando a primeira função
# 'return' gera mais flexibilidade para utilizar um dado.

def diz_oi():
    return 'Oi '

alguem = 'Pedro!'

print(diz_oi())
print(alguem)

"""

"""
Sobre a palavra reservada 'return';

1 - Ela finaliza a função, ou seja, ela sai da execução da função.
2 - Podemos ter, em uma função, diferentes retutns.
3 - Podemos, em uma função, retornar qualquer tipo de dado e até mesmo múltiplos valores.

# Exemplo 1

def diz_oi():
    print("Estou sendo executado antes do retorno...")
    return "oi!"
    print("Estou sendo executado após o retorno...")


print(diz_oi())


# Exemplo 2

def nova_funcao():
    variavel = None
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return 'b'

print(nova_funcao())


# Exemplo 3

def outra_funcao():
    return 2, 3, 4, 5

#num1, num2, num3, num4 = outra_funcao()
#print(num1, num2, num3, num4)

print(outra_funcao())
print(type(outra_funcao()))



# Vamos criar uma função para jogar a moeda

from random import random


def joga_moeda():

    # Gera um número pseudo-randômico entre 0 e 1
    if random() > 0.5:
        return 'Cara'
    return 'Coroa'


print(joga_moeda())
"""

# Erros comuns na utilização do retorno, que na verdade ne, é erro, mas sim
# codificação desnecessária.

def eh_impar():
    numero = 6
    if numero % 2 != 0:
        return True
    return False
    # Esse 'return' está substituindo o 'else'


print(eh_impar())






