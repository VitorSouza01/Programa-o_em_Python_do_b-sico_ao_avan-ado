"""
Introdução ao módulo Unittest

Unittest → Testes Unitários

O que são testes unitários?

Teste é a forma de se testar unidades individuais de código fonte.

Unidades individuais podem ser: funções, métodos, classes, módulos etc.

Obs: Teste unitário não é específico da Linguagem Python.

Para criar nossos testes, criamos classes que herdam de unitttest, TestCase e a partir de então ganhamos todos os ‘assertions’ presentes no módulo.

Para rodar os testes, utilizamos unittest.main()

---

TestCase → Casos de teste para sua unidade

Conhecendo as assertions

| Método | Avalia se |
| --- | --- |
| https://docs.python.org/pt-br/3/library/unittest.html#unittest.TestCase.assertEqual | a == b |
| https://docs.python.org/pt-br/3/library/unittest.html#unittest.TestCase.assertNotEqual | a != b |
| https://docs.python.org/pt-br/3/library/unittest.html#unittest.TestCase.assertTrue | bool(x) is True |
| https://docs.python.org/pt-br/3/library/unittest.html#unittest.TestCase.assertFalse | bool(x) is False |
| https://docs.python.org/pt-br/3/library/unittest.html#unittest.TestCase.assertIs | a is b |
| https://docs.python.org/pt-br/3/library/unittest.html#unittest.TestCase.assertIsNot | a is not b |
| https://docs.python.org/pt-br/3/library/unittest.html#unittest.TestCase.assertIsNone | x is None |
| https://docs.python.org/pt-br/3/library/unittest.html#unittest.TestCase.assertIsNotNone | x is not None |
| https://docs.python.org/pt-br/3/library/unittest.html#unittest.TestCase.assertIn | a in b |
| https://docs.python.org/pt-br/3/library/unittest.html#unittest.TestCase.assertNotIn | a not in b |
| https://docs.python.org/pt-br/3/library/unittest.html#unittest.TestCase.assertIsInstance | isinstance(a, b) |
| https://docs.python.org/pt-br/3/library/unittest.html#unittest.TestCase.assertNotIsInstance | not isinstance(a, b) |

Por convenção, todos os testes em um test case, devem ter seu nome iniciado com ‘test_’

---

Para executar os testes com unittest:

‘python nome_do_modulo.py’

Para executar os testes com unittest no modo verbose:

‘python nome_do_modulo.py  -v’

Docstrings nos testes

Podemos acrescentar e é recomendado docstrings nos nossos testes

---

Prática - Utilizando a abordagem TDD

Código 1:

```python
def comer(comida, eh_saudavel):
    pass

def dormir(num_horas):
    pass
```

Código 2:

```python
import unittest

from teste import comer, dormir

class AtividadesTestes(unittest.TestCase):

    def test_comer_saudavel(self):
        self.assertEqual(
            comer('quiabo', True),
            'Estou comendo quiabo porque quero manter a forma'
        )

    def test_comer_nao_saudavel(self):
        self.assertEqual(
            comer(comida='pizza', eh_saudavel=False),
            'Estou comendo pizza porque não quero manter a forma'
        )

    def test_dormir_pouco(self):
        self.assertEqual(
            dormir(4),
            'Estou cansado após dormir 4 horas'
        )

    def test_dormir_muito(self):
        self.assertEqual(
            dormir(8),
            'Dormi muito, esto atrasado após dormir 8 horas'
        )

if __name__ == '__main__':
    unittest.main()
```

Resultado terminal:

```
FFFF
======================================================================
FAIL: test_comer_nao_saudavel (__main__.AtividadesTestes.test_comer_nao_saudavel)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\vmendes\Documents\Python\teste1.py", line 15, in test_comer_nao_saudavel
    self.assertEqual(
AssertionError: None != 'Estou comendo pizza porque não quero manter a forma'

======================================================================
FAIL: test_comer_saudavel (__main__.AtividadesTestes.test_comer_saudavel)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\vmendes\Documents\Python\teste1.py", line 9, in test_comer_saudavel
    self.assertEqual(
AssertionError: None != 'Estou comendo quiabo porque quero manter a forma'

======================================================================
FAIL: test_dormir_muito (__main__.AtividadesTestes.test_dormir_muito)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\vmendes\Documents\Python\teste1.py", line 27, in test_dormir_muito
    self.assertEqual(
AssertionError: None != 'Dormi muito, esto atrasado após dormir 8 horas'

======================================================================
FAIL: test_dormir_pouco (__main__.AtividadesTestes.test_dormir_pouco)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\vmendes\Documents\Python\teste1.py", line 21, in test_dormir_pouco
    self.assertEqual(
AssertionError: None != 'Estou cansado após dormir 4 horas'

----------------------------------------------------------------------
Ran 4 tests in 0.003s

FAILED (failures=4)
```

Arrumando os Testes;

Código 1:

```python
def comer(comida, eh_saudavel):
    if eh_saudavel:
        final = "quero manter a forma"
    else:
        final = "não quero manter a forma"
    return f"Estou comendo {comida} porque {final}"

def dormir(num_horas):
    if num_horas > 8:
        return f"Dormi muito, esto atrasado após dormir {num_horas} horas"
    else:
        return f"Estou cansado após dormir {num_horas} horas"
```

Código 2:

```python
import unittest

from teste import comer, dormir

class AtividadesTestes(unittest.TestCase):

    def test_comer_saudavel(self):
        ""Testando o retorno com comida saudável""
        self.assertEqual(
            comer('quiabo', True),
            'Estou comendo quiabo porque quero manter a forma'
        )

    def test_comer_nao_saudavel(self):
        ""Testando o retorno com comida não saudável""
        self.assertEqual(
            comer(comida='pizza', eh_saudavel=False),
            'Estou comendo pizza porque não quero manter a forma'
        )

    def test_dormir_pouco(self):
        ""Testando o retorno com dormir pouco""
        self.assertEqual(
            dormir(4),
            'Estou cansado após dormir 4 horas'
        )

    def test_dormir_muito(self):
        ""Testando o retorno com dormir muito""
        self.assertEqual(
            dormir(10),
            'Dormi muito, esto atrasado após dormir 10 horas'
        )

if __name__ == '__main__':
    unittest.main()
```

Resultado terminal:

```
..F.
PS C:\Users\vmendes\Documents\Python> python .\teste1.py -v
test_comer_nao_saudavel (__main__.AtividadesTestes.test_comer_nao_saudavel)
Testando o retorno com comida não saudável ... ok
test_comer_saudavel (__main__.AtividadesTestes.test_comer_saudavel)
Testando o retorno com comida saudável ... ok
test_dormir_muito (__main__.AtividadesTestes.test_dormir_muito)
Testando o retorno com dormir muito ... ok
test_dormir_pouco (__main__.AtividadesTestes.test_dormir_pouco)
Testando o retorno com dormir pouco ... ok

----------------------------------------------------------------------
Ran 4 tests in 0.002s

OK
```
"""