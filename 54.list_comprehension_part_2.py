"""

List Comprehension

Nós podemos adicionar estruturas condicionais logicas as nossas List Comprehensio

Exemplos

# 1

numeros = [1, 2, 3, 4, 5, 6]
pares = [numero for numero in numeros if numero % 2 == 0]
impares = [numero for numero in numeros if numero % 2 != 0]
print(pares)
print(impares)

[2, 4, 6]
[1, 3, 5]

# Refatorar

numeros = [1, 2, 3, 4, 5, 6]
# Qualquer número par módulo de 2 é o 0 e 0 em Python é 'False'. not False = True
pares = [numero for numero in numeros if not numero % 2 ]

# Qualquer número ímpar módulo de 2 é 1, e 1 em Python é True
impares = [ numero for numero in numeros if numero % 2 ]

print(pares)
print(impares)
```

```
[2, 4, 6]
[1, 3, 5]
```

---

```python
# 2

numeros = [1, 2, 3, 4, 5, 6]

res = [numero * 2 if numero % 2 == 0 else numero / 2 for numero in numeros]
print(res)
```

```
[0.5, 4, 1.5, 8, 2.5, 12]
```
"""