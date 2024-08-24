"""
Doctests

Doctests são testes que colocamos na docstring das funções/métodos Python.

Para rodar um test do doctest no terminal:

```python
python -m doctest -v nome_do_modulo.py
```

```python
def soma(a, b):
    """"""#soma os números a e b

    #3
    """"""
    return a + b

print(soma(3, 4))  # 7
```
Executando normalmente:

```
7
```

No terminal:

```
7
Trying:
    soma(1, 2)
Expecting:
    3
ok
1 items had no tests:
    teste
1 items passed all tests:
   1 tests in teste.soma
1 tests in 2 items.
1 passed and 0 failed.
Test passed.
```

Falhando no teste
```python
def soma(a, b):
    """"""soma os números a e b

    #>>> soma(5, 2)
    3
    """"""""
    return a + b
```
```
Trying:
    soma(5, 2)
Expecting:
    3
**********************************************************************
File "G:\Meu Drive\Documentos\CURSO PYTHON\guppe\teste.py", line 4, in teste.soma
Failed example:
    soma(5, 2)
Expected:
    3
Got:
    7
1 items had no tests:
    teste
**********************************************************************
1 items had failures:
   1 of   1 in teste.soma
1 tests in 2 items.
0 passed and 1 failed.
***Test Failed*** 1 failures.
```

---

Outro Exemplo, Aplicando o TDD

```python
def duplicar(valores):
    """"""#duplica os valores em uma lista

   # >>> duplicar([1, 2, 3, 4])
   # [2, 4, 6, 8]

    #>>> duplicar([])
   # []

    #>>> duplicar(['a', 'b', 'c'])
    #['aa', 'bb', 'cc']

    #>>> duplicar([True, None])
    #Traceback (most recent call last):
        #...
   #TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
    """"""
    pass
```

```
Trying:
    duplicar([1, 2, 3, 4])
Expecting:
    [2, 4, 6, 8]
**********************************************************************
File "G:\Meu Drive\Documentos\CURSO PYTHON\guppe\teste.py", line 4, in teste.duplicar
Failed example:
    duplicar([1, 2, 3, 4])
Expected:
    [2, 4, 6, 8]
Got nothing
Trying:
    duplicar([])
Expecting:
    []
**********************************************************************
File "G:\Meu Drive\Documentos\CURSO PYTHON\guppe\teste.py", line 7, in teste.duplicar
Failed example:
    duplicar([])
Expected:
    []
Got nothing
Trying:
    duplicar(['a', 'b', 'c'])
Expecting:
    ['aa', 'bb', 'cc']
**********************************************************************
File "G:\Meu Drive\Documentos\CURSO PYTHON\guppe\teste.py", line 10, in teste.duplicar
Failed example:
    duplicar(['a', 'b', 'c'])
Expected:
    ['aa', 'bb', 'cc']
Got nothing
Trying:
    duplicar([True, None])
Expecting:
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
**********************************************************************
File "G:\Meu Drive\Documentos\CURSO PYTHON\guppe\teste.py", line 13, in teste.duplicar
Failed example:
    duplicar([True, None])
Expected:
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
Got nothing
1 items had no tests:
    teste
**********************************************************************
1 items had failures:
   4 of   4 in teste.duplicar
4 tests in 2 items.
0 passed and 4 failed.
***Test Failed*** 4 failures.
```

Arrumando:

```python
def duplicar(valores):
    """"""#duplica os valores em uma lista

    #>>> duplicar([1, 2, 3, 4])
   # [2, 4, 6, 8]

    #>>> duplicar([])
    #[]

    #>>> duplicar(['a', 'b', 'c'])
    #['aa', 'bb', 'cc']

    #>>> duplicar([True, None])
    #Traceback (most recent call last):
    #TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
    """"""
    return [2 * elemento for elemento in valores]
```

```
Trying:
    duplicar([1, 2, 3, 4])
Expecting:
    [2, 4, 6, 8]
ok
Trying:
    duplicar([])
Expecting:
    []
ok
Trying:
    duplicar(['a', 'b', 'c'])
Expecting:
    ['aa', 'bb', 'cc']
ok
Trying:
    duplicar([True, None])
Expecting:
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
ok
1 items had no tests:
    teste
1 items passed all tests:
   4 tests in teste.duplicar
4 tests in 2 items.
4 passed and 0 failed.
Test passed.
```

---

Erro Inesperado

```python
def fala_oi():
    """"""#Fala oi

    #>>> fala_oi()
    "oi"
    """"""
    return "oi"
```

```
Trying:
    fala_oi()
Expecting:
    "oi"
**********************************************************************
File "G:\Meu Drive\Documentos\CURSO PYTHON\guppe\teste.py", line 4, in teste.fala_oi
Failed example:
    fala_oi()
Expected:
    "oi"
Got:
    'oi'
1 items had no tests:
    teste
**********************************************************************
1 items had failures:
   1 of   1 in teste.fala_oi
1 tests in 2 items.
0 passed and 1 failed.
***Test Failed*** 1 failures.
```

Resolvendo (aspas):

```python
def fala_oi():
    """"""#Fala oi

    #>>> fala_oi()
    'oi'
    """"""
    return "oi"
```

```
Trying:
    fala_oi()
Expecting:
    'oi'
ok
1 items had no tests:
    teste
1 items passed all tests:
   1 tests in teste.fala_oi
1 tests in 2 items.
1 passed and 0 failed.
Test passed.
```

Obs: Dentro do docteste, o Python não reconhece string com aspas duplas. Precisa ser aspas simples.

---

Um último caso estranho…

Se tiver um espaço depois do true o código vai dar errado mais o Pycharm ajuda removendo eles

```python
def verdade():
    """"""#Retorna verdade

   # >>> verdade()
    #True
    """"""
    return True
```

```
Trying:
    verdade()
Expecting:
    True
ok
1 items had no tests:
    teste
1 items passed all tests:
   1 tests in teste.verdade
1 tests in 2 items.
1 passed and 0 failed.
Test passed.
```
"""