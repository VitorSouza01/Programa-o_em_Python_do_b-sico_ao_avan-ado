"""
JSON e Pickle

JSON → JavaScript Object Notation

API → São meios de comunicação entre os serviços oferecidos por empresas (Twitter, Facebook, Youtube…) e terceiros (nós desenvolvedores).

```python
import json

ret = json.dumps(['produto', {'PlayStation 4': ('2TB', 'Novo', '220V', 2340)}])

print(type(ret))
print(ret)
```

```
<class 'str'>
["produto", {"PlayStation 4": ["2TB", "Novo", "220V", 2340]}]
```

```python
import json

class Gato:
    def __init__(self, nome, raca):
      self.__nome = nome
      self.__raca = raca

    @property
    def nome(self):
      return self.__nome

    @property
    def raca(self):
      return self.__raca

felix = Gato('Felix', 'Persa')

print(felix.__dict__)

ret = json.dumps(felix.__dict__)

print(ret)
```

```
{'_Gato__nome': 'Felix', '_Gato__raca': 'Persa'}
{"_Gato__nome": "Felix", "_Gato__raca": "Persa"}
```

---

Integrando o JSON com o Pickle

pip install jsonpickle

```python
import jsonpickle

class Gato:
  def __init__(self, nome, raca):
    self.__nome = nome
    self.__raca = raca

  @property
  def nome(self):
    return self.__nome

  @property
  def raca(self):
    return self.__raca

felix = Gato("Felix", "Persa")

ret = jsonpickle.encode(felix)

print(ret)
```

```
{"py/object": "__main__.Gato", "_Gato__nome": "Felix", "_Gato__raca": "Persa"}
```

---

Escrevendo o arquivo json/pickle:

```python
import jsonpickle

class Gato:
  def __init__(self, nome, raca):
    self.__nome = nome
    self.__raca = raca

  @property
  def nome(self):
    return self.__nome

  @property
  def raca(self):
    return self.__raca

felix = Gato("Felix", "Persa")

with open("felix.json", "w") as arquivo:
    ret = jsonpickle.encode(felix)
    arquivo.write(ret)
```

Arquivo json:

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/50f6c3e8-cd39-40a2-a8ee-7ed9bb20ee47/a09dcdad-5aaf-4b3e-8c0c-b61cd6865681/Untitled.png)

```python
import jsonpickle

class Gato:
  def __init__(self, nome, raca):
    self.__nome = nome
    self.__raca = raca

  @property
  def nome(self):
    return self.__nome

  @property
  def raca(self):
    return self.__raca

with open("felix.json", "r") as arquivo:
    conteudo = arquivo.read()
    ret = jsonpickle.decode(conteudo)
    print(ret)
    print(type(ret))
    print(ret.nome)
    print(ret.raca)
```

```
<__main__.Gato object at 0x000001EC052B8FD0>
<class '__main__.Gato'>
Felix
Persa
```
"""