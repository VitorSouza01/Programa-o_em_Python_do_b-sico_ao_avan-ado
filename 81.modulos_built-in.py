"""
Trabalhando com módulos Built-In

Trabalhando com Módulls Builtin (módulos integrados, que já vem instalados no Python).

|Python | Módulos builtin|

Utilizando alias (apelidos) para módulos/funções

```python
import random as rdm
print(rdm.random())
```

```
0.6113982941455559
```

---

Podemos importar todas as funções de um módulo utilizando o *

```python
from random import *
print(random())
```

```
0.8212742899720294
```

Importando todo o módulo

```python
import random
print(random.random())
```

```
0.6379577789613265
```

---

Utilizando alias (apelidos) para módulos/funções

```python
from random import randint as rdi, random as rdm
print(rdi(5, 89))
print(rdm())
```

```
35
0.26026449441557153
```

---

Costumamos a utilizar tuple () para colocar múltiplos imports de um mesmo módulo.

```python
from random import(
  random,
  randint,
  shuffle,
  choice
)

print(random())

print(randint(3, 7))

lista = ['Geek', 'University', 'Python']
shuffle(lista)
print(lista)

print(choice('University'))
```

```
0.5251421877265616
7
['Python', 'University', 'Geek']
i
```
"""