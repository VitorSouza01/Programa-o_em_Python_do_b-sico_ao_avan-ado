"""
Heranças

POO - Herança (Inheritance)

A ideia de herança é a de reaproveitar código. Também extender nossas classes.

Obs: Com a herança, a partir de uma classe existente, nós extedendemos outra classe que passa a herdar atributos e métodos da classe herdada.

Exemplo:

Cliente

-nome;

-sobrenome;

-cpf;

-renda;

Funcionario

-nome

-sobrenome

-cpf

-matricula

```python
class Cliente:

    def __init__(self, nome, sobrenome, cpf, renda):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__renda = renda

    def nome_completo(self):
        return f"{self.__nome} {self.__sobrenome}"

class Funcionario:

    def __init__(self, nome, sobrenome, cpf, matricula):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__matricula = matricula

    def nome_completo(self):
        return f"{self.__nome} {self.__sobrenome}"

cliente1 = Cliente("Angelia", "Jolie", "123.456.789-00", 5000)
funcionario1 = Funcionario("Brad", "Pitt", "987.654.321-01", 1234)

print(cliente1.nome_completo())
print(funcionario1.nome_completo())
```

```python
Angelia Jolie
Brad Pitt
```

Pergunta: Existe alguma entidade genérica o suficiente para encapsular os atributos e métodos comuns a outras entidades?

```python
class Pessoa:

    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f"{self.__nome} {self.__sobrenome}"

class Cliente(Pessoa):
    # Cliente herda de Pessoa

    def __init__(self, nome, sobrenome, cpf, renda):
        Pessoa.__init__(self, nome, sobrenome, cpf) # Forma não comum de acessar dados da super classe
        self.__renda = renda

class Funcionario(Pessoa):
    # Funcionario herda de Pessoa

    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf) # Forma comum de acessar dados da super class
        self.__matricula = matricula

cliente1 = Cliente("Angelia", "Jolie", "123.456.789-00", 5000)
funcionario1 = Funcionario("Brad", "Pitt", "987.654.321-01", 1234)

print(cliente1.nome_completo())
print(funcionario1.nome_completo())
```

```python
Angelia Jolie
Brad Pitt
```

Obs: Quando uma classe herda de outra classe ela herda TODOS os atributos e métodos da classe herdada.

Quando uma classe herda de outra classe, a classe herdada é conhecida por:

[Pessoa]

-Super Classe;

-Classe Mãe;

-Classe Pai;

-Classe Base;

-Classe Genérica;

Quando uma classe herda de outra classe, ela é chamada;

[Cliente, Funcionário]

-Sub Classe;

-Classe Filha;

-Classe Específica;

---

Sobrescrita de Métodos (Overriding)

Sobrescrita de método, ocorre quando reescrevemos/reimplementamos um método presente na super classe em classes filhas

```python
class Pessoa:

    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f"{self.__nome} {self.__sobrenome}"

class Cliente(Pessoa):
    # Cliente herda de Pessoa

    def __init__(self, nome, sobrenome, cpf, renda):
        Pessoa.__init__(self, nome, sobrenome, cpf) # Forma não comum de acessar dados da super classe
        self.__renda = renda

class Funcionario(Pessoa):
    # Funcionario herda de Pessoa

    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf) # Forma comum de acessar dados da super class
        self.__matricula = matricula

    def nome_completo(self):
        print(super().nome_completo())
        print(self._Pessoa__cpf)
        return f"Funcionário: {self.__matricula} Nome: {self._Pessoa__nome}"

cliente1 = Cliente("Angelia", "Jolie", "123.456.789-00", 5000)
funcionario1 = Funcionario("Brad", "Pitt", "987.654.321-01", 1234)

print(cliente1.nome_completo())
print(funcionario1.nome_completo())
```

```python
Angelia Jolie
Brad Pitt
987.654.321-01
Funcionário: 1234 Nome: Brad
```
"""