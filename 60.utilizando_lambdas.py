"""
Utilizando Lambdas

Conhecidas  por Expressões Lambdas, ou simplesmente Lambdas, são funções sem nome, ou seja, funções anônimas.

# Função em Python
def funcao(x):
  return 3 * x + 1

print(funcao(4))




# Expressão Lambda e como utilizar a expressão Lambda
calc = lambda x: 3 * x + 1
print(calc(4))



Podemos ter expressões lambdas com múltiplas entradas.
nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()

print(nome_completo(' angelina', 'JOLIE'))




Em funções Python podemos ter nenhuma ou várias entradas. Em Lambdas também
amar = lambda: 'Como não amar Python?'
uma = lambda x: 3 * x + 1
duas = lambda x, y: (x * y) ** 0.5
tres = lambda x, y, z: 3 / (1 / x + 1 / y + 1 / z)

print(amar())
print(uma(6))
print(duas(5, 7))
print(tres(3, 6, 9))

Obs: Se passarmos mais argumentos do que parâmetros esperados teremos TypeError



Outro exemplo:
autores = ['Machado de Assis', 'Clarice Lispector', 'Cecília Meireles', 'Mário de Andrade', 'H. P. Lovecraft', 'J. R. R. Tolkien', 'J. K. Rowling']

print(autores)

autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())

print(f'\n{autores}')



Função Quadrática.

f(x) = a * x ** 2 + b * x + c

Definindo a função;
def geradora_funcao_quadratica(a, b, c):
# Retorna a função f(x) = a * x ** 2 + b * x + c
	return lambda x: a * x ** 2 + b * x + c

print(geradora_funcao_quadratica(3, 0, 1)(2))  # 2 representa o x
"""
