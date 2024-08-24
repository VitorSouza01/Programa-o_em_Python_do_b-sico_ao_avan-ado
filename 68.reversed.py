"""
Reversed

Obs: Não confunda com a função reverse() que estudamos nas listas.

A função reverse() só funciona em listas.

Já a função reversed() funciona com qualquer iterável.

Sua função é inverter o iterável.

A função reversed() retorna um iterável chamado ‘List Reverse Iterator’

Exemplos;

```python
lista = [1, 2, 3, 4, 5]

res = reversed(lista)

print(res)
print(type(res))
```

```
<list_reverseiterator object at 0x000001FF51C9AB00>
<class 'list_reverseiterator'>
```

Podemos converter o elemento retornando para uma lista, Tupla ou Conjunto

```python
lista = [1, 2, 3, 4, 5]

# Lista
print(list(reversed(lista)))

# Tupla
print(tuple(reversed(lista)))

# Conjunto (Set)
print(set(reversed(lista)))
```

```
[5, 4, 3, 2, 1]
(5, 4, 3, 2, 1)
{1, 2, 3, 4, 5}
```

Obs; Em Conjuntos (Set), não definimos a ordem dos elementos

---




# Podemos iterar sobre reversed
for letra in reversed('Geek University'):
    print(letra, end='')

# Podemos fazer o mesmo sem o uso do for
print(''.join(list(reversed('Geek University'))))

# Já vimos como fazer isso mais fácil com o slice de strings
print('Geek University'[::-1])

# Podemos também utilizar o reversed() para fazer um loop for reverso
for n in reversed(range(0, 10)):
    print(n)
"""

# Apesar que também já vimos como fazer isso utilizando o próprio range()
for n in range(9, -1, -1):
    print(n)




