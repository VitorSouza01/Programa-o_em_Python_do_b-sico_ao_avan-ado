"""
Try, Except, Else e Finally

Try / Except / Else / Finally

Dica de quando e onde tratar o código:

TODA ENTRADA DEVE SER TRATADA!

Obs; A função de usuário é DESTRUIR seu sistema!

Else → É executado somente se não ocorrer o erro.

```python
try:
    num = int(input("Informe um número: "))
except ValueError:
    print("Valor incorreto")
else:
    print(f"Você digitou {num}")
```

```
Informe um número: 45
Você digitou 45
```

---

Finally

```python
try:
    num = int(input("Informe um número: "))
except ValueError:
    print("Valor não digitou um valor válido.")
else:
    print(f"Você digitou o número {num}")
finally:
    print("Executando o finally")
```

```
Informe um número: 92
Você digitou o número 92
Executando o finally
```

Obs; O bloco finally é SEMPRE executado. Independente se houve execução ou não.

O finally, geralmente, é utilizado para fechar os deslocar recursos.

---

Exemplo complexo ERRADO;

```python
def dividir(a, b):
    return a / b

num1 = int(input("Informe o primeiro número: "))

try:
    num2 = int(input("Informe o segundo número: "))
except ValueError:
    print("O valor precisa ser numérico")
try:
    print(dividir(num1,num2))
except NameError:
    print("Valor incorreto")
```

```
Informe o primeiro número: 3
Informe o segundo número: c
O valor precisa ser numérico
Valor incorreto
```



Exemplo mais complexo CORRETO;

Obs: Você é responsável pelas entradas das suas funções. Então, trate-as!

def dividir(a, b):
    try:
        return int(a) / int(b)
    except ValueError:
        return "Valor Incorreto"
    except ZeroDivisionError:
        return "Não é possível realizar uma divisão por zero"


num1 = input("Informe o primeiro número: ")
num2 = input("Informe o segundo número: ")

print(dividir(num1, num2))
"""

# Exemplo mais complexo Genérico;

def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f"Ocorreu um problema: {err}"


num1 = input("Informe o primeiro número: ")
num2 = input("Informe o segundo número: ")

print(dividir(num1, num2))