"""

Criando sua própria versão de loop

Loop Normal

```python
for num in [1, 2, 3, 4, 5]:
    print(num)

for letra in "Geek University":
    print(letra)

iter([1, 2, 3, 4, 5])

iter("Geek University")
```

```
1
2
3
4
5
G
e
e
k

U
n
i
v
e
r
s
i
t
y
```

Loop Próprio

```python
def meu_for(interavel):
    it = iter(interavel)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break

meu_for("Geek University")
numeros = [1, 2, 3, 4, 5]
meu_for(numeros)
```

```
G
e
e
k

U
n
i
v
e
r
s
i
t
y
1
2
3
4
5
```
"""