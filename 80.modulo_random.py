"""
O módulo random

Módulos são uteis para deixar o programa mais simples, reutilizando o código.

Módulo Random e o que são módulos?

- Em Python, módulos nada mais são do que outros arquivos Python.

Módulo Random → Possui várias funções para geração de números pseudo-aleatório.

Obs: Existem duas formas de se utilizar um módulo ou função deste.

Forma 1 - Importando todo o módulo (Não recomendado).

```python
import random

# random() -> Gera um número pseudo-aleatório entre 0 e 1.
```

Obs: Ao realizar o import de todo módulo, todas as funções, atributos, classes e propriedades que estiverem dentro do módulo ficarão disponíveis (Ficarão em Memória). Caso você saiba quais funções você precisar utilizar deste módulo, então esta não seria a forma ideal de utilização. Nós veremos uma forma melhor na Forma 2.

```python
print(random.random())
```

Veja que para utilizar a função random() do pacote random, nós colocamos o nome do pacote e o nome da função, separado por ponto.

Obs: Não confunda a função random() com o pacote random. Pode parecer confuso, mas a função random() é apenas uma função dentro do módulo random.

---

Forma 2 - Importando uma função específica do módulo (forma recomendada)

from random import random

# No import acima, estamos falando: Do módulo random, importe a função random

for i in range(10):
    print(random())




uniform() → Gerar um número real pseudo-aleatório entre os valores estabelicidos.

from random import uniform

for i in range(10):
    print(uniform(5, 10))  # 10 não é incluido.




randint() → Gera valores inteiros pseudo-aleatórios entre os valores estabelecidos.
# Gerador de apostas para a mega-sena
from random import randint

for i in range(6):
    print(randint(1, 61), end=', ')  # Começa em 1 e vai até 60



choice() → Mostra um valor aleatório entre um iterável.

from random import choice

jogadas = ['pedra', 'papel', 'tesoura']

print(choice(jogadas))



shuffle() → Tem a função de embaralhar dados
"""
from random import shuffle
cartas = ['K', 'Q', 'J', 'A', '2', '3', '4', '5', '6', '7']

print(cartas)
shuffle(cartas)
print(cartas)
print(cartas.pop())







