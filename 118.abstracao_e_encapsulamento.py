"""
# Aula 118. Abstração e Encapsulamento

---

Abstração e Encapsulamento

POO - Abstração e Encapsulamento

O grande objetivo da POO é encapsular nosso código dentro de um grupo lógico e hierárquico utilizando classes.

Encapsular → cápsula

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/50f6c3e8-cd39-40a2-a8ee-7ed9bb20ee47/1da6b572-9aee-4667-bb10-bd4d7b5fa1d8/Untitled.png)

---

Relembrando Atributos/Métodos privados em Python

Imagine que temos um classe chamada Pessoa, contendo um atributo privado chamado __nome e um método privado chamado
__falar()

Esses elementos privados só devem/deveriam ser acessados dentro da classe. Mas Python não bloqueia este acesso fora da
classe. Com Python acontece um fenômeno chamado “Name Mangling”, que faz uma alteração na forma de se acessar os
lementos privados conforme:

*Classe*_elemento

Exemplo - Acessando elementos privados fora da classe:

instancia._Pessoa__nome

instancia._Pessoa__falar()

Abstração, em POO, é o ato de expor apenas dados relevantes de uma classe, escondendo atributos e métodos privados de
usuário.



O Underline __ deixa o atributo privado!

```python
# Sem Underline
class Conta:

    contador = 400

    def __init__(self, titular, saldo, limite):
        self.numero = Conta.contador
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        Conta.contador += 1

    def extrato(self):
        print(f"Saldo de {self.saldo} do titular {self.titular} com limite de {self.limite}")

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        self.saldo -= valor

# Testando

conta1 = Conta("Geek", 150.00, 1500)

print(conta1.numero)
print(conta1.titular)
print(conta1.saldo)
print(conta1.limite)

conta1.numero = 42
conta1.titular = "Xuxa"
conta1.saldo = 999999999
conta1.limite = 999999999999999999999

print(conta1.__init__)
conta1.extrato()
```

```
400
Geek
150.0
1500
<bound method Conta.__init__ of <__main__.Conta object at 0x000002CA4D807400>>
Saldo de 999999999 do titular Xuxa com limite de 999999999999999999999
```

```python
# Com Underline
class Conta:

    contador = 400

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        print(f"Saldo de {self.__saldo} do titular {self.__titular} com limite de {self.__limite}")

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

# Testando

conta1 = Conta("Geek", 150.00, 1500)

print(conta1.numero)
print(conta1.titular)
print(conta1.saldo)
print(conta1.limite)

conta1.numero = 42
conta1.titular = "Xuxa"
conta1.saldo = 999999999
conta1.limite = 999999999999999999999

print(conta1.__init__)
conta1.extrato()
```

```
AttributeError: 'Conta' object has no attribute 'numero'
```

```python
# Com Underline
class Conta:

    contador = 400

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        print(f"Saldo de {self.__saldo} do titular {self.__titular} com limite de {self.__limite}")

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

# Testando

conta1 = Conta("Geek", 150.00, 1500)

print(conta1.__init__)
conta1.extrato()
```

```
<bound method Conta.__init__ of <__main__.Conta object at 0x000001E248657400>>
Saldo de 150.0 do titular Geek com limite de 1500
```

```python
class Conta:

    contador = 400

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        print(f"Saldo de {self.__saldo} do titular {self.__titular} com limite de {self.__limite}")

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print("O valor precisa ser positivo")

    def sacar(self, valor):
        if valor >0:
            if self.__saldo >= valor:
                self.__saldo -= valor
            else:
                print("Saldo insuficiente")
        else:
            print("O valor deve ser positivo")

# Testando

conta1 = Conta("Geek", 150.00, 1500)

print(conta1.__dict__)

conta1.depositar(150)

print(conta1.__dict__)

conta1.sacar(200)

print(conta1.__dict__)
```

```
{'_Conta__numero': 400, '_Conta__titular': 'Geek', '_Conta__saldo': 150.0, '_Conta__limite': 1500}
{'_Conta__numero': 400, '_Conta__titular': 'Geek', '_Conta__saldo': 300.0, '_Conta__limite': 1500}
{'_Conta__numero': 400, '_Conta__titular': 'Geek', '_Conta__saldo': 100.0, '_Conta__limite': 1500}
```

---
"""