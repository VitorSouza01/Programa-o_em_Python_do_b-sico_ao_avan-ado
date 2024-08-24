"""
Polimorfismo

Poli  → Muitas

Morfis → Formas

Quando a gente reimplementa um método presente na classe pai em classes filhas estamos realizando uma sobrescrita de método (Overriding).

O everriding é a melhor representação do polimorfismo.

```python
class Animal(object):

    def __init__(self, nome):
        self.__nome = nome

    def falar(self):
        raise NotImplementedError('A classe filha precisa implementar este método')

    def comer(self):
        print(f"{self.__nome} está comendo...")

class Cachorro(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f"{self._Animal__nome} fala wau wau")

class Gato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f"{self._Animal__nome} fala miau miau")

class Rato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f"{self._Animal__nome} fala algo...")

# Testes

felix = Gato("Feliz")
felix.comer()
felix.falar()

pluto = Cachorro("Pluto")
pluto.comer()
pluto.falar()

mickey = Rato("Mickey")
mickey.comer()
mickey.falar()
```

```
Feliz está comendo...
Feliz fala miau miau
Pluto está comendo...
Pluto fala wau wau
Mickey está comendo...
Mickey fala algo...
```
"""