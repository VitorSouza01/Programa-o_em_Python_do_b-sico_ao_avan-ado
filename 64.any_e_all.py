"""
Any e All

all() → Retorna True se todos os elementos do iterável são verdadeiros ou ainda se o iterável está vazio.

Exemplo All()

```python
print(all([0, 1, 2, 3, 4]))  # Todos os números são verdadeiro? False

print(all([1, 2, 3, 4]))  # Todos os números são verdadeiro? True

print(all([]))  # Todos os números são verdadeiro? True

print(all((0, 1, 2, 3, 4)))  # Todos os números são verdadeiro? True

print(all({0, 1, 2, 3, 4}))  # Todos os números são verdadeiro? True

print(all("Geek"))  # Todos os números são verdadeiro? True
```

```python
nomes = ['Carlos', 'Camila', 'Carla', 'Cassiane', 'Cristina']

print(all([nome[0] == 'C' for nome in nomes]))
```

```
True
```

Obs: Um iterável vazio convertido em boolean é False, mas o all() entende como True

```python

# O resultado da lista ficara vazio
print(all([num for num in [4, 2, 10, 6, 8] if num % 2 == 1]))
```

```
True
```

---

Any() → Retorna True se qualquer elemento do interável for verdadeiro. Se o iterável estiver vazio, retorna False

```python
print(any([0, 1, 2, 3, 4]))  # True
print(any([0, False, {}, (), []]))  # False

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiane', 'Cristina', 'Vanessa']
print(any([nome[0] == 'C' for nome in nomes]))

print(any([num for num in [4, 2, 10, 6, 8, 9] if num % 2 == 0]))
```

```
True
False
True
True
```
"""