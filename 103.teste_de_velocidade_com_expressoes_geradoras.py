"""
Teste de Velocidade com Expressões Geradoras

```python
# Generators (Geradores)

def nums():
    for num in range(1, 10):
        yield num

ge1 = nums()

print(ge1)  # GEnerator

print(next(ge1))
print(next(ge1))

# Generator Expression

ge2 = (num for num in range(1, 10))

print(ge2)  # Generation Expression

print(next(ge2))
print(next(ge2))
```

```
<generator object nums at 0x7faed1a0f5e0>
1
2
<generator object <genexpr> at 0x7faed1aeb440>
1
2
```

Realizando o teste de velocidade

```python
import time

# Generator Expression

gen_inicio = time.time()
print(sum(num for num in range(100000000)))
gen_tempo = time.time() - gen_inicio

# List Comprehension

list_inicio = time.time()
print(sum([num for num in range(100000000)]))
list_tempo = time.time() - list_inicio

print(f"Generator Expression levou {gen_inicio}")
print(f"List Comprehension levou {list_inicio}")
```

```
4999999950000000
4999999950000000
Generator Expression levou 1697746526.397315
List Comprehension levou 1697746531.5155137
```
"""