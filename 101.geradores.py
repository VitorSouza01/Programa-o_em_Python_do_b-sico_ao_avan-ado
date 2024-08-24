"""
Geradores (Generators) são Iterators (Iteradores):

Obs: O contrário não é verdadeiro. Ou seja, nem todo iterator é um generator.

Outras informações:

- Generators podem ser criados com funções geradoras;
- Funções geradoras utilizam a palavra reservada yield;
- Generators podem ser criados com Expressões Geradoras;

Diferenças entre Funções e Generaor Functions (Funções Geradoras)

FUNÇÕES:

- Utilizam return
- Retorna uma vez
- Quando executado, retorna um valor

GENERATOR FUNCTIONS:

- Utilizam yield
- Podem utilizar yield múltiplas vezes
- Quanto executada, retorna um generator

---

Exemplo Função Geradora (Generator Funcrion)

```python
def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador = contador + def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador = contador + 1

gen = conta_ate(5)
# print(type(gen))  # <class 'generator'>

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
```

```
1
2
3
4
5
```

Obs: Um Generator Function não é um Generator. Ele gera um generator, ok?

```python
def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador = contador + 1

gen = conta_ate(10)
# print(type(gen))  # <class 'generator'>

for num in gen:
    print(num)
```

```
1
2
3
4
5
6
7
8
9
10
```

```python
def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador = contador + 1

gen = conta_ate(10)
print(next(gen))  # 1

print("Geek")

for num in gen:
    print(num)
```

```
1
Geek
2
3
4
5
6
7
8
9
10
```

```python
def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador = contador + 1

gen = list(conta_ate(10))
print(gen)
```

```
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

Obs: yield fica aguardando o próximo next!
"""