"""
Tipo string

Em Python, um dado é considerado do tipo string sempre que:

- Estiver entre àspas simples -> 'uma string', '234', 'a', 'True', '42.3'
- Estiver entre àspas duplas -> "uma string", "234", "a", "True", "42.3"
- Estiver entre àspas simples triplas-> '''uma string''', '''234''', '''a''', '''True''', '''42.3'''

nome = 'Geek University'
print(nome)
print(type(nome))


nome = "Gina's Bar"
print(nome)
print(type(nome))


nome = 'Angelina \nJolie'
print(nome)
print(type(nome))


nome = "Angelina \" Jolie"
print(nome)
print(type(nome))


---

# Transforma toda a string em maiscula
nome = 'Geek University'
print(nome.upper())


# Transforma toda a string em minuscula
nome = 'Geek University'
print(nome.lower())


# Transforma em uma lista de strings;
nome = 'Geek University'
print(nome.split())

# [  0,   1,   2,   3,  4,   5,   6,   7,   8,   9,   10, 11,  12,  13,  14,]
# [ 'G', 'e', 'e', 'k', '', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']
nome = 'Geek University'
print(nome[0:4]) # Slice de tring

print(nome[5:15]) # Slice de tring


# ['Geek', 'university']
# [     0,       1     ]
print(nome.split())

print(nome.split()[0])

print(nome.split()[1])

# [::-1] -> Comece do primeiro elemento, vá até o último elemento e inverta
print(nome[::-1])   #Inversão da String, Método Pythônico

texto = 'socorram me subino onibus em marrocos' # Palindromo
print(texto)

print(texto[::-1])

texto ='ana'    #Palindromo
print(texto)

print(nome[::-1])


"""
# - Estiver entre àspas duplas triplas -> """uma string""", """234""", """a""", """True""", """42.3"""


nome = 'Geek University'




print(nome. replace('G', 'P')) # Substituir um valor da String para outro valor

