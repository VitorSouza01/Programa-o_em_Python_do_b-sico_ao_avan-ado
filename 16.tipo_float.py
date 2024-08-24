"""
Tipo Float

Tipo real, decimal

Casas decimais

Observação: O separador de casas decimais na programação é o ponto e não a virgula (baseado no idioma inglês)

'Float = Ponto Flutuante'

"""

# Errado do ponto de vista do Float, mas gera uma "Tupla"
valor = 1,44
print(valor)
print(type(valor))


# Certo do ponto de vista Float
valor = 1.44
print(valor)
print(type(valor))


# É possível fazer dupla atribuição
valor1, valor2 = 1, 44
print(valor1)
print(type(valor1))
print(valor2)
print(type(valor2))


# Podemos converter um 'Float' para um 'Int'
# Observação: Ao converter valores Float para Int, nós perdemos precisão.
print(valor)
resultado = int(valor)
print(resultado)
print(type(resultado))


# Tambem é possivel conveter número Inteiro 'Int' para Float
num = 2022
print (num)
2022
print(float(num))
2022.0




# Podemos trabalhar com números complexos
# Os números complexos são representados pela letra 'j'
"""
variavel = 5j
variavel = 5j
print(variavel)
5j
type(5j)
<class 'complex'>
"""







