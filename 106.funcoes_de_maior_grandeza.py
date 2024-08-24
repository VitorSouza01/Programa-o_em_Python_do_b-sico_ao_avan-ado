"""
Funções de maior Grandeza

Funções de Maior Grandeza - Higher Order Functions - HOF

Oque isso significa?

- Quando uma linguagem de programação suporta HOF, indica que podemos ter funções que retornam outras funções como resultado ou mesmo que podemos passar funções como argumentos para outras funções, e até mesmo criar variáveis do tipo de funções nos nossos programas.

Obs: Na seção de funções, nós utilizamos isso.

Em Python, as funções são Cidadãos de Primeira Classe, First Class Citizen

```python
# Exemplo - Definindo as funções

def somar(a, b):
    return a + b

def diminuir(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

def calcular(num1, num2, funcao):
    return funcao(num1, num2)

# Testando as funções

print(calcular(4, 3, somar))

print(calcular(4, 3, diminuir))

print(calcular(4, 3, multiplicar))

print(calcular(4, 3, dividir))
```

```
7
1
12
1.3333333333333333
```

---

Nested Functions - Funções Aninhadas

Em Python podemos também ter funções dentro de funções, que são conhecidas por Nested Functions  ou também Inner Functions (Funções Internas).

```python
# Exemplo

from random import choice

def cumprimento(pessoa):
    def humor():
        return choice(("E ai ", "Suma daqui ", "Gosto muito de você "))
    return humor() + pessoa

# Testando

print(cumprimento("Angelina"))

print(cumprimento("Felicity"))
```

```
Gosto muito de você Angelina
Suma daqui Felicity
```

```python
# Retornando funções de outras funções

from random import choice

def faz_me_rir():
    def rir():
        return choice(("hahahaha", "kkkkkkkkk", "ksksksksk", "rsrsrsrs"))
    return rir

# Testando

rindo = faz_me_rir()
print(rindo())
print(rindo())
print(rindo())
```

```
rsrsrsrs
kkkkkkkkk
hahahaha
```

---

Inner Functions (Funções Internas / Nested Functions) podem acessar o escopo de funções mais externas.

```python
from random import choice

def faz_me_rir_novamente(pessoa):
    def dando_risada():
        risada = choice(("hahahaha", "lollollollol", "asdkalsfjlkfsd"))
        return f"{risada} {pessoa}"
    return dando_risada

# Testando

rindo = faz_me_rir_novamente("Fernanda")

print(rindo())
print(rindo())
print(rindo())
```

```python
hahahaha Fernanda
asdkalsfjlkfsd Fernanda
hahahaha Fernanda
```
"""