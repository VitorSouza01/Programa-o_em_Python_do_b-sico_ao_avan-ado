"""
Classes

POO - Classes

Em POO, Classes nada mais são do que modelos dos objetos do mundo real sendo representados computacionalmente.

Imagine que você queira fazer um sistema para automatizar o controle das lâmpadas da sua casa.

Classes podem conter:

- Atributos → Representam as características do objeto, ou seja, pelos atributos conseguimos representar
computacionalmente estados de um objeto. No caso da lâmpada, possivelmente iríamos querer saber se a lâmpada é 110 ou
220 volts, se ela é branca, amarela, vermelha ou outra cor, qual é a luminosidade dela etc.
- Métodos (funções) → Representam os comportamentos do objeto, ou seja, as ações que este objeto pode realizar no seu
sistema. No caso da lâmpada, por exemplo, um comportamento comum que muito provavelmente iriamos querer representar no
nosso sistema é o de ligar e desligar a mesa.

```python
class Lampada:
    pass

lamp = Lampada()
print(type(lamp))
```

```
<class '__main__.Lampada'>
```

Em Python, para definir uma classe utilizamos a palavra reservada class.

Obs: Utilizamos a palavra “pass” em Python quando temos um bloco de código que ainda não está implementado.

Obs: Quando nomeamos nossas classes em Python utilizamos por convenção o nome com inicial em maiusculo. Se o nome for
composto, utiliza-se as iniciais de ambas as palavras em maiúsculo, todas juntas.

```python
class ContaCorrente:
    pass

class Produto:
    pass

class Usuario:
    pass
```

Dica Geek: Em computação não utilizamos; acentuação, caracteres especiais, espaços ou similares para nomes de classes,
atributos, métodos, arquivos, diretórios e etc.

Obs: Quando estamos planejando um software e definimos quais classes teremos que ter no sistema, chamamos estes objetos
que serão mapeados para classes de entidade.
"""