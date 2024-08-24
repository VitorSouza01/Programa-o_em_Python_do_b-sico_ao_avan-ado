"""
O método super()

POO - O método super()

O método super() se refere á super classe.

```python
class Animal:

    def __init__(self, nome, especie):
        self.__nome = nome
        self.__especie = especie

    def faz_som(self, som):
        print(f"O {self.__nome} fala {som}")

class Gato(Animal):

    def __init__(self, nome, especie, raca):
        super().__init__(nome, especie)
        self.__raca = raca

felix = Gato("Felix", "Felino", "Angorá")
felix.faz_som("Miau")
```

```python
O Felix fala Miau
```
"""