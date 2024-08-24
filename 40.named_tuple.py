"""
Módulo COllections - Named Tuple

# Recap Tupla;
tupla = (1, 2, 3)
print(tupla[1])

# Named Tuple -> (Tupla Nomeada) São tuplas diferenciadsa, onde,
especificamos um nome para a mesma e também parâmetros.
"""

# Importando

from collections import namedtuple

# Precisamos definir o nome e parâmetros.

# Forma 1 - Declaração Named Tuple

cachorro = namedtuple('cachorro', 'idade raca nome')

# Forma 2 - Declaração Named Tuple

cachorro = namedtuple('cachorro', 'idade, raca, nome')

# Forma 3 - Declaração Named Tuple

cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])


# Usando

ray = cachorro(idade=2, raca='Pinscher', nome='Ray')
print(ray)

# Acessando os dados

# Forma 1

print(ray[0])  # idade
print(ray[1])  # raça
print(ray[2])  # nome

# Forma 2

print(ray.idade)  # idade
print(ray.raca)  # raca
print(ray.nome)  # nome


# Indice
print(ray.index('Pinscher'))
# Ocorrência
print(ray.count('Pinscher'))



