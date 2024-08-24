"""
Antes e após hooks

hooks - são os testes em si, ou seja, a execução dos testes.

setup() → é  executado antes de cada método de teste. E útil para criarmos instâncias de objetos e outros dados.

tearDown → é executado ao final de cada método de teste, é útil para excluir dados ou fechar conexões com bancos de dados.

```python
import unittest

class ModuloTest(unittest.TestCase):

    def setUp(self):
        # Configurações do setUp()
        pass

    def test_primeiro(self):
        # setUp vai rodar antes do teste
        # tearDown() vai rodar após o teste
        pass

    def test_segundo(self):
        # setUp vai rodar antes do teste
        # tearDown() vai rodar após o teste
        pass

    def tearDown(self):
        # Configurações do tearDown()
        pass
```

Robô:

```python
class Robo:

    def __init__(self, nome, bateria=100, habilidades=[]):
        self.__nome = nome
        self.__bateria = bateria
        self.__habilidades = habilidades

    @property
    def nome(self):
        return self.__nome

    @property
    def bateria(self):
        return self.__bateria

    @property
    def habilidades(self):
        return self.__habilidades

    def carregar(self):
        self.__bateria = 100

    def dizer_nome(self):
        if self.__bateria > 0:
            self.__bateria -= 1
            return f"BEEP BOOP BEEP BOOP. EU SOU {self.__nome.upper}"
        return "Bateria fraca. Por favor, recarregue e tente novamente."

    def aprender_habilidade(self, nova_habilidade, custo):
        if self.__bateria >= custo:
            self.__bateria -= custo
            self.__habilidades.append(nova_habilidade)
            return f"Uau! EU APRENDI {nova_habilidade.upper()}."
        return "Bateria insuficiente. Por favor, recarregue e tente novamente."
```

Robô Teste:

```python
import unittest

from robo import Robo

class RoboTestes(unittest.TestCase):

    def test_carregar(self):
        megaman = Robo('Mega Man', bateria=50)
        megaman.carregar()
        self.assertEqual(megaman.bateria, 100)

if __name__ == '__main__':
    unittest.main()
```

Executando:

```python
import unittest

from robo import Robo

class RoboTestes(unittest.TestCase):

    def setUp(self):
        self.megaman = Robo(nome="Mega man", bateria=50)
        print("setUp() sendo executado...")

    def test_carregar(self):
        self.megaman.carregar()
        self.assertEqual(self.megaman.bateria, 100)

    def test_dizer_nome(self):
        self.assertEqual(self.megaman.dizer_nome(), "BEEP BOOP BEEP BOOP. EU SOU MEGA MAN")
        self.assertEqual(self.megaman.bateria, 49, "A bateria deveria estar em 49")

    def tearDown(self):
        print("tearDown() sendo executado...")

if __name__ == '__main__':
    unittest.main()
```

Terminal:
"""