"""
**Kwargs

Poderíamos chamar este parâmetro de **xis, mas por convenção chamamos de **kwargs

Este é só mais um parâmetro, mas diferente do *args que coloca os valores extras em uma tupla,
o **kwargs exige que utilizemos parâmetros nomeados, e transforma esses parâmetros extras em um
dicionário.




# Exemplo


def cores_favoritas(**kwargs):
    print(kwargs)


cores_favoritas(marcos='verde', julia='amarelo', fernanda='azul', vanessa='branco')



# Exemplo


def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa} é {cor}.')


cores_favoritas(marcos='verde', julia='amarelo', fernanda='azul', vanessa='branco')

# Obs: Os parâmetros *args e **kwargs não obrigatórios.

cores_favoritas()

cores_favoritas(geek='navy')




# Exemplo mais complexo


def comprimento_especial(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'Python':
        return 'Você recebeu um comprimento Pythônico Geek!'
    elif 'geek' in kwargs:
        return f"{kwargs['geek']} Geek!"
    return 'Não tenho certeza quem você é...'


print(comprimento_especial())
print(comprimento_especial(geek='Python'))
print(comprimento_especial(geek='Oi '))
print(comprimento_especial(geek='especial'))




# Nas nossas funções, podemos ter (nesta ordem):

- Parâmetros obrigatórios
- *args
- Parâmetros 'default' (não obrigatórios)
- **kwargs

# Exemplo;


def minha_funcao(idade, nome, *args, solteiro=False, **kwargs):
    print(f'{nome} tem {idade} anos.')
    print(args)
    if solteiro:
        print('Solteiro!')
    else:
        print('Casado!')
    print(kwargs)


minha_funcao(8, 'Julia')
minha_funcao(18, 'Felicity', 4, 5, 3, solteiro=True)
minha_funcao(34, 'Felipe', eu='Não', voce='Vai')
minha_funcao(19, 'Carla', 9, 4, 3, java=False, python=True)




# Entenda por que é importante manter a ordem dos parâmetros na declaração

# Função com a ordem correta de parâmetros;
#def mostra_info(a, b, *args, instrutor='Geek', **kwargs):
#    return [a, b, args, instrutor, kwargs]

# Função com a ordem incorreta de parâmetros


def mostra_info(a, b, instrutor='Geek', *args, **kwargs):
    return [a, b, args, instrutor, kwargs]


a = 1
b = 2
args = (3,)
instrutor = 'Geek'
kwargs = {'sobrenome': 'University', 'cargo': 'Instrutor'}


print(mostra_info(1, 2, 3, sobrenome='University', cargo='Instrutor'))




# Desempacotar com **kwargs

def mostra_nomes(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"

nomes = {'nome': 'Felicity', 'sobrenome': 'Jones'}

print(mostra_nomes(**nomes))
"""


def soma_multiplos_numeros(a, b, c):
    print(a + b +c)


lista = [1, 2, 3]
tupla = (1, 2, 3)
conjunto = {1, 2, 3}
dicionario = dict(a=1, b=2, c=3)

soma_multiplos_numeros(*lista)
soma_multiplos_numeros(*tupla)
soma_multiplos_numeros(*conjunto)
soma_multiplos_numeros(**dicionario)

# Obs: Os nomes da chave em um dicionário devem ser os mesmos dos parâmetros da função

# dicionario = dict(d=1, e=2, f=3)  # TypeError
# soma_multiplos_numeros(**dicionario)
