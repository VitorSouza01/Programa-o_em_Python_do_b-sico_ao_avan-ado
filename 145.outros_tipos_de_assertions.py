"""
Outros tipos de assertions

Unittest - Outros tipos de assertions

asserEqual(a, b)

assertTrue(x)

assertFalse(x)

Código 1:

```python
def eh_engracado(pessoa):
    comediantes = ['Jim Carrey', 'Bozo']
    if pessoa in comediantes:
        return True
    return False
```

Código 2:

```python
import unittest

from teste import eh_engracado

class AtividadesTestes(unittest.TestCase):

    def test_eh_engracado(self):
        # self.assertEqual(eh_engracado('Sérgio Malandro'), False)
        self.assertFalse(eh_engracado('Sérgio Malandro'))
        self.assertTrue(eh_engracado('Jim Carrey'), 'Jim Carrey deveria ser engraçado')

    if __name__ == '__main__':
        unittest.main()
```

Resultado terminal:

```
----------------------------------------------------------------------
Ran 0 tests in 0.000s

OK
```
"""