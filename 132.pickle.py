"""
Conhecendo o Pickle

A função Pickle é realizar o seguinte processo:

Objetos Python → Binarização

Binarização → Objetos Python

Este processo é chamado de serialização/deserialização

Obs: O módulo Pickle não é seguro contra dados maliciosos e desta forma não é recomendado trabalhar com arquivos pickle vindos de outras pessoas que você não conheça ou de fontes desconhecidas.

 Fazendo a escrita em arquivos pickle:

```python
import pickle

class Animal:

    def __init__(self, nome):
        self.__nome = nome

    def comer(self):
        print(f"{self.__nome} está comendo...")

class Gato(Animal):

    def __init__(self, nome):
      super().__init__(nome)

    def mia(self):
        print(f"{self.nome} está miando...")

class Cachorro(Animal):

    def __init__(self, nome):
      super().__init__(nome)

    def late(self):
        print(f"{self.nome} está latindo...")

# Fazendo a escrita em arquivos pickle

felix = Gato("Felix")
pluto = Cachorro("Pluto")

with open("animais.pickle", "wb") as arquivo:
    pickle.dump((felix, pluto), arquivo)
```

Arquivo pickle:

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/50f6c3e8-cd39-40a2-a8ee-7ed9bb20ee47/29904ad3-99f7-4fab-9bbe-4d3c00b358ad/Untitled.png)

Fazendo a leitura de dados em arquivos pickle

```python
import pickle

class Animal:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def comer(self):
        print(f"{self.__nome} está comendo...")

class Gato(Animal):

    def __init__(self, nome):
      super().__init__(nome)

    def mia(self):
        print(f"{self.nome} está miando...")

class Cachorro(Animal):

    def __init__(self, nome):
      super().__init__(nome)

    def late(self):
        print(f"{self.nome} está latindo...")

# Fazendo a leitura de dados em arquivos pickle

with open("animais.pickle", "rb") as arquivo:
    gato, cachorro = pickle.load(arquivo)
    print(f"O gato chama-se {gato.nome}")
    gato.mia()
    print(f"O tipodo gato é {type(gato)}")

    print(f"O cachorro chama-se {cachorro.nome}")
    cachorro.late()
    print(f"O tipo do cachorro é {type(cachorro)}")
```

```
O gato chama-se Felix
Felix está miando...
O tipodo gato é <class '__main__.Gato'>
O cachorro chama-se Pluto
Pluto está latindo...
O tipo do cachorro é <class '__main__.Cachorro'>
```
"""