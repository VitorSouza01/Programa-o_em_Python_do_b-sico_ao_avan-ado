"""
Len, Abs, Sum, Round

len() -> Retorna o tamanho (ou seja, o número de itens) de um iterável.

Só pra revisar

```python
print(len('Geek University'))

print(len([1, 2, 3, 4, 5]))

print(len((1, 2, 3, 4, 5)))

print(len({1, 2, 3, 4, 5}))

print(len({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}))

print(len(range(0, 10)))
```

```
15
5
5
5
5
10
```

Por debaixo dos panos, quando utilizamos a função len() O Python faz o seguinte:

- Dunder len

```python
print('Geek University'.__len__())
```

```
15
```

---

Abs

abs () -> Retorna o valor absoluto de um número inteiro ou real. De forma, básica, seria o seu valor real sem o sinal.

Exemplos Abs;

```python
print(abs(-5))
print(abs(-5))
print(abs(3.14))
print(abs(-3.14))
```

```
5
5
3.14
3.14
```

---

Sum

sum() → Recebe como parâmetro um iterável, podendo receber um valor inicial, e retorna a soma total dos elementos, incluindo o valor inicial.

Obs: O valor inicial default = 0

```python
print(sum([1, 2, 3, 4, 5]))

print(sum([1, 2, 3, 4, 5], 5))

print(sum([3.145, 5.678]))
print(sum((1, 2, 3, 4, 5)))
print(sum({1, 2, 3, 4, 5}))
print(sum({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}.values()))
```

```
15
20
8.823
15
15
15
```

---

Round

round() → Retorna um número arredondado para ‘n’ dígito de precisão após a casa decimal. Se a precisão não for informada retorna o inteiro mais próximo da entrada.

Exemplo Round

```python
print(round(10.2))

print(round(10.5))

print(round(10.6))

print(round(1.212121212121, 2))

print(round(1.21999999999, 2))
```

```
10
10
11
1.21
1.22
```
"""