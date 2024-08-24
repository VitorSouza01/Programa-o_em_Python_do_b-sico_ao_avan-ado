"""
Oque é Orientação a objetos?

-Programação orientada a objetos é um paradigma de programação baseado no conceito de "objetos", que podem conter dados
na forma de campos, também conhecidos como atributos, e códigos, na forma de procedimentos, também conhecidos como
métodos.

A orientação a objetos tem como objetivo utilizar esse paradigma de mapear objetos do mundo real para modelos
computacionais.

**Classe** = Modelo do objeto no mundo real sendo representado computacionalmente.

**Atributos** = Características do Objeto.

(Uma classe pode ter nenhum ou vários atributos)

**Métodos** = Comportamento do Objeto, quais ações que ele executa.

Método é parecido com uma Função, a diferença é que o método está dentro de uma classe.

**Construtor** = É um método especial, é utilizado para criar objetos a partir da classe.

**Objeto** = Elemento criado baseado na classe.

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/50f6c3e8-cd39-40a2-a8ee-7ed9bb20ee47/063b54db-a184-4a9c-aef2-68cebc48e95f/Untitled.png)

---

Programação Orientada a Objetos - POO

- POO é um paradigma de programação que utiliza que mapeamento de objetos do mundo real para modelos computacionais.
- Paradigma de programação é a forma/metodologia utilizada para pensar/desenvolver sistemas.

Principais elementos de Orientação a Objetos:

- Classe → Modelo do objeto do mundo real sendo representado computacionalmente.
- Atributo → Características do Objeto.
- Método → Comportamento do Objeto (Função)
- Construtor → Método especial utilizado para criar os objetos
- Objeto → Instância da classe

```python
numero = 10
print(numero)
print(type(numero))

nome = "Geek"
print(nome)
print(type(nome))

class Produto:
    pass

ps4 = Produto()
print(ps4)
print(type(ps4))
```

```
10
<class 'int'>
Geek
<class 'str'>
<__main__.Produto object at 0x7fe412ba6550>
<class '__main__.Produto'>
>
```

Poda-se criar a própria classe e modelar o tipo de software.
"""