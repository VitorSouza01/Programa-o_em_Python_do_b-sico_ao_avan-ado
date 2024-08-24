"""
Map

Com map, fazemos mapeamento de valores para função.

import math

def area(r):
# calcula a área de um círculo com raio 'r'
	return math.pi * (r ** 2)

print(area(2))
print(area(5.3))




Outro exemplo;

Forma 1 - Comum
import math

def area(r):
	return math.pi * (r ** 2)

raios = [2, 5, 7.1, 0.3, 10, 44]

areas = []
for r in raios:
  areas.append(area(r))

print(areas)




Forma 2 - Map

Map é uma função que recebe dois parâmetros: o primeiro a função, o segundo um iterável. Retorna um Map Object

import math

def area(r):
	return math.pi * (r ** 2)

raios = [2, 5, 7.1, 0.3, 10, 44]

areas = map(area, raios)

print(areas)
print(type(areas))

print(list(areas))




Forma 3 - Map com Lambda

import math

def area(r):
	return math.pi * (r ** 2)

raios = [2, 5, 7.1, 0.3, 10, 44]

print(list(map(lambda r: math.pi * (r ** 2), raios)))



Obs: Após utilizar a função map() depois da primeira utilização do resultado, ele zera!



Para fixar - Map

Temos dados iteráveis;

dados: a1, a2, …, an

Temos uma função;

fução: f(x)

Utilizamos a função map(f, dados) onde map irá ‘mapear’ cada elemento dos dados e aplicar a função.

O Map Object: f(a1), f(a2), f(…), f(fn)




Mais um exemplo

# converter temperatura celsius para fahrenheit

cidades = [('Berlim', 29), ('Cairo', 36), ('Buenos Aires', 19), ('Los Angeles', 26), ('Tokio', 27), ('Nova York', 28), ('Londres', 22)]

print(f"{cidades}\n")

# f = 9/5 * c + 32

# Lambda

c_para_f = lambda dado: (dado[0], (9/5) * dado[1] + 32)

print(list(map(c_para_f, cidades )))
"""