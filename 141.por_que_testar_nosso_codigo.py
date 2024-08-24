"""
Por que testar nosso código?

Testes Automatizados!

Por que testar nosso código?

- Reduzir bugs (problemas) no código existe;
- Testes garantem que novos recursos de suas aplicação não quebrem (alterem) recurso antigo;
- Testes garantem que bugs (problemas) que forem corrigidos anteriormente continuem corrigidos;
- Testes garantem que a refatoração que costumamos a fazer não tragam novos bugs (problemas);

TDD - Test Driven Development (Desenvolvimento Guiado por Testes)

Com TDD é utilizado estágios de desenvolvimento;

- Você escreve seu teste primeiro;
- Então você escreve o código mínimo suficiente para fazer o teste passar (ou seja, executar com sucesso);
- Então refatora o código para realizar a funcionalidade e teste novamente;
- Uma vez que o teste passe, o recurso é considerado completo;

Estes estágios de desenvolvimento do TDD são quase como um mantra que os desenvolvedores seguem, conhecidos como;

- Red;
- Green;
- Refactor;

```python
class Gato:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def miar(self):
        print(f'{self.__nome} está miando...')

felix = Gato('Felix')

felix.miar()

print(felix.nome)
```

```
Felix está miando...
Felix
```
"""