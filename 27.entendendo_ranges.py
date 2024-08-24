"""
Ranges

- Precisamos conhecer o loop for para usar os ranges.
- Precisamos conhecer o range para trabalhar melhor com loops for.

A função range(); Ela permite especificar o inicio de uma sequência, o passo (ou pulo) e valor final.
Com isso, o Python nos retorna uma sequência de números para que possamos iterar!

Ranges são utilizados para gerar sequências numéricas, não de forma aleatório,
mas sim de maneira especificada.

Formas gerais:

# Forma 1
range(valor_de_parada)
Obs; valor_de_parada não inclusive (inicio padrão 0, e passo de 1 em 1)

# Exemplo Forma 1
for num in range(11):
    print(num)


# Forma 2
range(valor_de_inicio, valor_de_parada)
Obs; valor_de_parada não inclusive (início especificado pelo usuário, e passo de 1 em 1)

# Exemplo Forma 2
for num in range(1, 11):
    print(num)


# Forma 3
range(valor_de_inicio, valor_de_parada, passo)
Obs; valor_de_parada não inclusive (início especificado pelo usuário, e passo especificado pelo usuário)

# Exemplo Forma 3
for num in range(1, 10, 2):
    print(num)


# Forma 4 (Inversa)
range(valor_de_inicio, valor_de_parada, passo)
Obs; valor_de_parada não inclusive (inicio especificado pelo usuário, e passo especificado pelo usuário)

# Exemplo Forma 4
for num in range(10, 0, -1):
    print(num)


Uso do Range no Terminal;
>>> range(10)
range(0, 10)
>>> range(2, 10)
range(2, 10)
>>> range(2,10,2)
range(2, 10, 2)
>>> lista = range(10)
>>> print(lista)
range(0, 10)
>>> lista = list(range(10))
>>> lista
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

Para gerar uma lista com range tem que utilizar o "list" para converter o range em lista!

"""
# Exemplo Forma 4
for num in range(10, 0, -1):
    print(num)

