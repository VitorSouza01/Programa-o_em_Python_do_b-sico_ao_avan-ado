"""
Min e Max

Max() → Retorna o maior valor em um iterável ou o maior de dois ou mais elemento.

Exemplos;

```python
lista = [1, 8, 4, 99, 34, 129]
print(max(lista))

tupla = (1, 8, 4, 99, 34, 129)
print(max(tupla))

conjuntos = {1, 8, 4, 99, 34, 129}
print(max(conjuntos))

dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}
print(max(dicionario))

dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}
print(max(dicionario.values()))
```

```
129
129
129
f
129
```

```python
# Faça um programa que receba dois valores de usuário e mostre o maior
valor_1 = int(input("Digite o 1º valor: "))
valor_2 = int(input("Digite o 2º valor: "))
print(max(valor_1, valor_2))
```

```
Digite o 1º valor: 23
Digite o 2º valor: 12
23
```

```python
print(max(4, 67, 54))

print(max('a', 'b', 'c', 'g'))

print(max(3.145, 5.789))

print(max('Geek Univiersity'))
```

```
23
67
g
5.789
y
```

---

Min() → Retorna o menor valor em um iterável ou o menor de dois ou mais elementos

```python
lista = [1, 8, 4, 99, 34, 129]
print(min(lista))

tupla = (1, 8, 4, 99, 34, 129)
print(min(tupla))

conjuntos = {1, 8, 4, 99, 34, 129}
print(min(conjuntos))

dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}
print(min(dicionario))

dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}
print(min(dicionario.values()))
```

```
1
1
1
a
1
```

```python
# Faça um programa que receba dois valores de usuário e mostre o menor
valor_1 = int(input("Digite o 1º valor: "))
valor_2 = int(input("Digite o 2º valor: "))
print(min(valor_1, valor_2))
```

```
Digite o 1º valor: 12
Digite o 2º valor: 27
12
```

```python
print(min(4, 67, 54))

print(min('a', 'b', 'c', 'g'))

print(min(3.145, 5.789))

print(min('Geek Univiersity'))
```

```
4
a
3.145

```

---

Outros exemplos;

```python
nomes = ['Arya', 'Samson', 'Dora', 'Tim', 'Olivander']

print(max(nomes))
print(min(nomes))

print(max(nomes, key=lambda nome: len(nome)))
print(min(nomes, key=lambda nome: len(nome)))
```

```
Tim
Arya
Olivander
Tim
```

```python
musicas = [
  {"título": "Thunderstruck", "tocou": 3},
  {"título": "Dead Skin Mask", "tocou": 2},
  {"título": "Back in Black", "tocou": 4},
  {"título": "Too old to rock' in roll", "tocou": 32}
]

print(max(musicas, key=lambda musica: musica['tocou']))
print(min(musicas, key=lambda musica: musica['tocou']))
```

```
{'título': "Too old to rock' in roll", 'tocou': 32}
{'título': 'Dead Skin Mask', 'tocou': 2}
```

---

- DESAFIO! Imprima somente o título da música mais e menos tocada;

```python
musicas = [
  {"título": "Thunderstruck", "tocou": 3},
  {"título": "Dead Skin Mask", "tocou": 2},
  {"título": "Back in Black", "tocou": 4},
  {"título": "Too old to rock' in roll", "tocou": 32}
]

print(max(musicas, key=lambda musica: musica['tocou'])['título'])
print(min(musicas, key=lambda musica: musica['tocou'])['título'])
```

```
Too old to rock' in roll
Dead Skin Mask
```

- DESAFIO! Como encontrar a música mais tocada e a menos tocada sem usar o max() e o min();

```python
musicas = [
  {"título": "Thunderstruck", "tocou": 3},
  {"título": "Dead Skin Mask", "tocou": 2},
  {"título": "Back in Black", "tocou": 4},
  {"título": "Too old to rock' in roll", "tocou": 32}
]

max = 0
min = 9999

for musica in musicas:
  if musica["tocou"] > max:
    max = musica["tocou"]

for musica in musicas:
  if musica["tocou"] == max:
    print(musica["título"])

for musica in musicas:
  if musica["tocou"] < min:
    min = musica["tocou"]

for musica in musicas:
  if musica["tocou"] == min:
    print(musica["título"])
```

```
Too old to rock' in roll
Dead Skin Mask
```
"""