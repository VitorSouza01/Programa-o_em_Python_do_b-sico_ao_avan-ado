"""
Assertions (afirmações)

Checagens/Questionamentos

Em Python utilizamos a palavra reservada ‘assert’ para realizar simples afirmações utilizadas nos testes.

Utilizamos o ‘assert’ em uma expressão que queremos checar se é válida ou não.

Se a expressão for verdadeira, retorne None e caso seja falsa levanta um erro do tipo AssertionError.

Obs: Nós podemos especificar, opcionalmente, um segundo argumento ou mesmo uma mensagem de erro personalizada.

Obs: A palavra ‘assert’ pode ser utilizada em qualquer função ou código nosso… precisa ser exclusivamente nos teste.

ALERTA: Cuidado ao utilizar ‘assert’

Se um programa Python for executado com o parâmetro -O, nenhum assertion será validado. Ou seja, todas as suas validações já eram.

```python
def soma_numeros_positivos(a, b):
    assert a > 0 and b > 0, "Os números precisam ser positivos."
    return a + b

ret = soma_numeros_positivos(2, 4)  # 6
ret = soma_numeros_positivos(-2, 4)  # AssertionError: Os números precisam ser positivos.
print(ret)
```

```python
def comer_fast_food(comida):
    assert comida in [
        'pizza',
        'hamburguer',
        'hot dog'
        'batata frita'
    ], "Comida precisa ser fast food"
    return f"Eu estou comendo {comida}"

comida = input("Digite uma comida: ")
print(comer_fast_food(comida))

# ALERTA: Cuidado ao utilizar 'assert'

def faca_algo_ruim(usuario):
    assert usuario.eh_admin, "Somente administradores podem fazer isso"
    destroi_todo_o_sistema()
    return 'Adeus'
```

```
Digite uma comida: bolo
Traceback (most recent call last):
  File "C:\Users\vmendes\Documents\Python\teste.py", line 13, in <module>
    print(comer_fast_food(comida))
          ^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\vmendes\Documents\Python\teste.py", line 4, in comer_fast_food
    assert comida in [
           ^^^^^^^^^^^
AssertionError: Comida precisa ser fast food
```
"""