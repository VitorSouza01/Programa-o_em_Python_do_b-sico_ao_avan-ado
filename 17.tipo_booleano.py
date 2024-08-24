"""
Tipo Booleano

O tipo Booleando, vem da Algebra Booleana, criada por George Boole.

Onde existe 2 constantes, verdadeiro ou falso.

True -> Verdadeiro
False -> Falso

Obs: Sempre com a inicial maiúscula

Errado:
true, false.

Certo:
True, False.
"""

#Saber se o úsuario está ativo no sistema
ativo = True
print(ativo)

"""
Operações básicas:
"""

# Negação (not):
"""
Fazendo a negação, se o valor booleano for verdadeiro o resultado será falso,
se for falso o resultado será verdadeiro. Ou seja, sempre ao contrário.
"""
print(not ativo)

logado = True

# Ou (or):
"""
É uma operação binária, ou seja, depende de dois valores. Ou um ou outro deve ser verdadeiro.

True or True -> True
True or False -> True
False or True -> True
False or False -> False
"""
print(ativo or logado)

# E (and):
"""
Também é uma operação binária, ou seja, depende de dois valores.
Ambos os valores devem ser verdadeiro.

True and True -> True
True and False -> False
False and True -> False
False and False -> False
"""

"""
Outros exemplos de operação boolenar;

>>> 5 > 6
False

>>> 5 < 6
True

>>> 6 == 6
True

>>> num1 = 7
>>> num2 = 8

>>> num1 >= num2
False

>>> num1 ==num2
False

>>> num1 < num2 or num1 > 3
True

>>> num1 < num2 and num1 >3
True

>>> type(True)
<class 'bool'>

>>> type(False)
<class 'bool'>

>>> ativo = True

>>> type(ativo)
<class 'bool'>
"""
