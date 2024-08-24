"""
Atributos

POO - Atributos

Atributos → Representam as características do objeto, ou seja, pelos atributos nós conseguimos representar
computacionalmente os estados de um objeto.

Em Python, dividimos os atributos em 3 grupos:

- Atributos de Instancia
- Atributos de Classe
- Atributos Dinâmicos

Atributos de instancia: São atributos declarados dentro do método construtor.

Obs: Método construtor: É um método especial utilizado para a construção do objeto.

Classe lâmpada, incluindo seus atributos ficaria mais ou menos assim:

Classes com Atributos de Instancia Publico

```python

class Lampada:

    def __init__(self, voltagem, cor):
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False

class ContaCorrente:

    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo

class Produto:

    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor

class Usuario:

    def __init__(self, nome, email, senha):
        self.mome = nome
        self.email = email
        self.senha = senha
```

O método é uma função dentro de uma classe!

O self sempre vem antes do atributo.

---

Em Python, por convenção, ficou estabelecido que, todo atributo de uma classe é público. Ou seja, pode ser acessada em
todo o projeto.

Caso queiramos demostrar que determinado atributo deve ser tratado como privado, ou seja, que deve ser
acessado/utilizando somente dentro da própria classe onde está declarado, utilizando-se __ duplo underscore no inicio
de seu nome.

Isso é conhecido também como Name Mangling.

__ significa que o atributo é privado!

Atributos Públicos e Atributos Privados

```python
class Acesso:

    def __init__(self, email, senha):
        self.email = email
        self.__senha = senha

    def mostra_senha(self):
        print(self.__senha)

    def mostra_email(self):
        print(self.email)

# Exemplo

user = Acesso("user@gmail.com", "123456")

print(user.email)

# print(user.__senha)  # AttributeError

print(user._Acesso__senha)  # Temos acesso. Mas não deveriamos fazer este acesso. (Name Mangling)

user.mostra_senha()
user.mostra_email()
```

```
user@gmail.com
123456
123456
user@gmail.com
```

Obs: Lembre-se que isso é apenas uma convenção, ou seja, a linguagem Python não vai impedir que façemos acesso aos
atributos sinalizados como privados fora da classe.

---

**Atributo de Instancia**

O que significa atributos de instancia?

Significa, que ao criarmos instancias/objetos de uma classe, todas as instancias terão estes atributos

```python
class Acesso:

    def __init__(self, email, senha):
        self.email = email
        self.__senha = senha

    def mostra_senha(self):
        print(self.__senha)

    def mostra_email(self):
        print(self.email)

user1 = Acesso("user1@gmail.com", "123456")
user2 = Acesso("user2@gmail.com", "789000")

user1.mostra_email()
user2.mostra_email()
```

```
user1@gmail.com
user2@gmail.com
```

---

**Atributos de Classe**

```python
p1 = Produto("PlayStation 4", "Video Game", 2300)
p2 = Produto("Xbox S", "Video Game", 4500)
```

Atributos de classe, são atributos, claro, que são declarados diretamente na classe, ou seja, fora do construtor.
Geralmente já inicializamos um valor, e este valor é compartilhado entre todas as instancias da classe, ou seja, ao
invés de cada instância da classe ter seus próprios valores como é o caso dos atributos de instancia, com os atributos
de classe todas as instancias terão o mesmo valor para este atributo

Refatorar a classe Produto

```python
class Produto:

    # Atributo de classe
    imposto = 1.05  # 0.05% de imposto
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)
        Produto.contador = self.id

p1 = Produto("PlayStation 4", "Video Game", 2300)
p2 = Produto("Xbox S", "Video Game", 4500)

print(p1.valor)  # Acesso possível, mas incorreto de um atributo de classe.
print(p2.valor)  # Acesso possível, mas incorreto de um atributo de classe.

print(Produto.imposto)  # Acesso correto de um atributo de classe

print(p1.id)
print(p2.id)

```

```
2415.0
4725.0
1.05
1
2
```

Obs: Não precisamos criar uma instância de uma classe para fazer acesso a um atributo de classe

Obs: Em linguagens como o Java, os atributos conhecidos como atributos de classe aqui em Python são chamados de
atributos estáticos

---

**Atributos Dinâmicos**

Atributos dinâmicos, um atributos de instancia que pode ser criado em tempo de execução.

Obs: O atributo dinâmico  será exclusivo da instancia que o criou.

```python
class Produto:

    # Atributo de classe
    imposto = 1.05  # 0.05% de imposto
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)
        Produto.contador = self.id

p1 = Produto("PlayStation 4", "Video Game", 2300)
p2 = Produto("Arroz", "Mercearia", 5.99)

# Criando um atributo dinamico em tempo de execução

p2.peso = "5kg"  # Note que na classe Produto não existe o atributo peso

print(f"Produto: {p2.nome}, Descrição: {p2.descricao}, Valor: {p2.valor}, Peso: {p2.peso}")
# print(f"Produto: {p1.nome}, Descrição: {p1.descricao}, Valor: {p1.valor}, Peso: {p1.peso}")

# Deletando atributos

print(p1.__dict__)
print(p2.__dict__)

# print(Produto.__dict__)

del p2.peso
del p2.valor
del p2.descricao

print(p1.__dict__)
print(p2.__dict__)
```

```
Produto: Arroz, Descrição: Mercearia, Valor: 6.2895, Peso: 5kg
{'id': 1, 'nome': 'PlayStation 4', 'descricao': 'Video Game', 'valor': 2415.0}
{'id': 2, 'nome': 'Arroz', 'descricao': 'Mercearia', 'valor': 6.2895, 'peso': '5kg'}
{'id': 1, 'nome': 'PlayStation 4', 'descricao': 'Video Game', 'valor': 2415.0}
{'id': 2, 'nome': 'Arroz'}
```
"""