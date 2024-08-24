"""
Pacotes

Módulo→ É apenas um arquivo Python que pode ter diversas funções para utilizarmos;

Pacote → É um diretório contendo uma coleção de módulos;

Obs: Nas versões 2.x do Python, um pacote Python deveria conter dentro dele um arquivo chamado ‘__init__.py’

Nas versões do Python 3.x, não é mais obrigatório a utilização deste arquivo, mas normalmente ainda é utilizado para manter compatibilidade.

Exemplo:

- geek1

```python
pi = 3.1456

def funcao1(a, b):
    return a + b
```

- geek2

```python
curso = 'Programação em Python: Essencial'

def funcao2():
    return curso
```

- geek3

```python
def funcao3():
    return 'Geek'
```

- geek4

```python
def funcao4():
    return 'University'
```

Usando os pacotes:

```python
from geek import geek1, geek2

from geek.university import geek3, geek4

print(geek1.pi)

print(geek1.funcao1(4, 6))

print(geek2.curso)

print(geek2.funcao2())

print(geek3.funcao3())

print(geek4.funcao4())
```

```
3.1456
10
Programação em Python: Essencial
Programação em Python: Essencial
Geek
University
```

---

```python
from geek.geek1 import funcao1
from geek.university.geek4 import funcao4

print(funcao1(6, 9))

print(funcao4())
```

```
15
University
```
"""