"""
POO - Herança Múltipla

Herança Múltipla nada mais é do que a possibilidade de uma classe herdar de múltiplas classes, fazendo com que a classe filha herde todos os atributos e métodos de todas as classes herdadas.

Obs: A herança múltipla pode ser feita de duas maneiras;

Por Multiderivação Direta;

Por Multiderivação Indireta;

Exemplo 1 - Multiderivação Direta

```python
class Base1:
    pass

class Base2:
    pass

class Base3:
    pass

class MultiDerivada(Base1, Base2, Base3):
    pass
```

Exemplo 2 - Multiderivação Indireta

```python
class Base1:
    pass

class Base2(Base1):
    pass

class Base3(Base2):
    pass

class MultiDerivada(Base3):
    pass
```

Obs: Não importa se a derivação é direta ou indireta. A classe que realizar a herança herdará todos os atributos e métodos das super classes.

Method Resolution Order - MRO;

```python
class Animal:

    def __init__(self, nome):
        self.__nome = nome

    def cumprimentar(self):
        return f"Eu sou {self.__nome}"

class Aquatico(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def nadar(self):
        return f"{self._Animal__nome} está nadando"

    def cumprimentar(self):
        return f"Eu sou {self._Animal__nome} do mar!"

class Terrestre(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def andar(self):
        return f"{self._Animal__nome} está andando."

    def cumprimentar(self):
        return f"Eu sou {self._Animal__nome} da terra!"

class Pinguim(Terrestre, Aquatico):

    def __init__(self, nome):
        super().__init__(nome)

# Testando

baleia = Aquatico("Wally")
print(baleia.nadar())
print(baleia.cumprimentar())

tatu = Terrestre("Xim")
print(tatu.andar())
print(tatu.cumprimentar())

tux = Pinguim("Tux")
print(tux.andar())
print(tux.nadar())

# Method Resolution Order - MRO
print(tux.cumprimentar())  # Eu sou Tux da terra!
```

```python
Wally está nadando
Eu sou Wally do mar!
Xim está andando.
Eu sou Xim da terra!
Tux está andando.
Tux está nadando
Eu sou Tux da terra!
```

```python
class Animal:

    def __init__(self, nome):
        self.__nome = nome

    def cumprimentar(self):
        return f"Eu sou {self.__nome}"

class Aquatico(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def nadar(self):
        return f"{self._Animal__nome} está nadando"

    def cumprimentar(self):
        return f"Eu sou {self._Animal__nome} do mar!"

class Terrestre(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def andar(self):
        return f"{self._Animal__nome} está andando."

    def cumprimentar(self):
        return f"Eu sou {self._Animal__nome} da terra!"

class Pinguim(Aquatico, Terrestre):

    def __init__(self, nome):
        super().__init__(nome)

# Testando

baleia = Aquatico("Wally")
print(baleia.nadar())
print(baleia.cumprimentar())

tatu = Terrestre("Xim")
print(tatu.andar())
print(tatu.cumprimentar())

tux = Pinguim("Tux")
print(tux.andar())
print(tux.nadar())

# Method Resolution Order - MRO
print(tux.cumprimentar())  # Eu sou Tux do mar!
```

```python
Wally está nadando
Eu sou Wally do mar!
Xim está andando.
Eu sou Xim da terra!
Tux está andando.
Tux está nadando
Eu sou Tux do mar!
```

Objeto é instancia de…

```python
print(f"Tux é instância de Pinguim? {isinstance(tux, Pinguim)}")
print(f"Tux é instância de Aquatico? {isinstance(tux, Aquatico)}")
print(f"Tux é instância de Terrestre? {isinstance(tux, Terrestre)}")
print(f"Tux é instância de Animal? {isinstance(tux, Animal)}")
print(f"Tux é instância de Object? {isinstance(tux, object)}")
```

```python
Tux é instância de Pinguim? True
Tux é instância de Aquatico? True
Tux é instância de Terrestre? True
Tux é instância de Animal? True
Tux é instância de Object? True
```
"""