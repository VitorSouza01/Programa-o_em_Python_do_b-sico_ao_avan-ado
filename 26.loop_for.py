"""
Loop For

Loop -> Estrutura de repetição.
For -> Uma dessas estruturas.

#Funcão FOr no C ou Java;

for(int i = 0; i < 10; i++){
    //execução do loop
}

#Funcão For em Python

for item in interavel:
    //execução do loop

For -> Significa "Para"

Utilizamos loops para iterar sobre sequêcias ou sobre valores iteráveis.

Exemplos de iteráveis:
- String
    nome = 'Geek University'

- Lista
    lista = [1, 3, 5, 7, 9]

- Range
    numeros = range(1, 10)



# Exemplo de for 1 (Iterando em uma string)

for letra in nome:
    print(letra)

# Exemplo de for 2 (Iterando sobre uma lista)

for numero in lista:
    print(numero)

# Exemplo de for 3 (iterando sobre um range)

range(valor-inicial, valor_final)
Obs: O valor final não é inclusivel.
1
2
3
4
5
6
7
8
9
10 - Não

for numero in range(1, 10):
    print(numero)

#Como saber o indice de uma variavel
#i = indice / v = valor

Enumerate: Pra cada sequencia do interável ele atribui um indice, pega cada letra e transforma numa tupla;
(0, seq[0]), (1, seq[1]), (2, seq[2]), ...
(0, 'G'), (1, 'e'), (2, 'e'), (3, 'k'), (4, ' '), (5, 'U') ...

for indice, letra in enumerate(nome):
    print(nome[indice])

Ou;

for indice, letra in enumerate(nome):
    print(letra)

Ou;


for _, letra in enumerate(nome):
    print(letra)

Underline (_) = Faz parte linguagem Python, Quando não precisamos de um valor, podemos descartá-lo utilizando
um underline.
Pois ja sabemos os dois valores de Enumerate pois não precisamos do valor de indice e somente o valor de letra.

nome = 'vitor souza'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10) # Temos que transformar em uma lista

for valor in enumerate(nome):
    print(valor[1])

-----

#For tambem pode ser usado em outros casos

quantidade = int(input("Quantas vezes esse loop deve rodar?"))
for n in range (1, quantidade+1):
    print(f'Imprimindo {n}')

#For tambem pode ser usado em outros casos

quantidade = int(input("Quantas vezes esse loop deve rodar?"))
soma = 0

for n in range (1, quantidade+1):
   num = int(input(f'Informe o {n}/{quantidade} valor:'))
   soma = soma + num
print(f'A soma é {soma}')

#Como executar com o For sem o valor ficar pulando linha e deixar tudo somente numa única linha
nome = 'Geek Universsity'
for letra in nome:
    print(letra, end='')


#Complementos para a String
#Concatenação de string
nome = 'Geek'
nome + ' University'
print(nome + ' University')

-----

Tabela de Emojis Unicode: https//apps.timwhitlock.info/emoji/tables/unicode

#Original: U+1F60D
#Modificado: U0001F60D
#\ -> é um caractere de scape
for _ in range(3):
    for num in range(1,7):

        print('\U0001F60D' * num)
"""

nomes = ['Pedro', 'João', 'Leticia']
for n in nomes:
     print(n)
else:
     print("\nTodos os nomes foram listados com sucesso")