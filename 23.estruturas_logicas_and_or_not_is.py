"""
Extruturas Lógicas: And (E), Or (Ou), Not (Não), Is (É)

Operadores unários:
    - not, is

Operadores binários:
    - and, or, is

Regras de funcionamento:

- Para o 'and', ambos os valores precisam ser True.
- Para o 'or', um ou outro valor precisa ser True.
- Para o 'not', o valor do booleano é invertido, ou seja, se for True, vire False, se for False vira True.
- Para o 'is', o valor é comparado com o segundo.
Ela nega o valor.
-
"""
ativo = False
logado = False

if ativo is True:
    print('Você precisa ativar sua conta. Por favor, cheque seu e-mail')
else:
    print('Bem-vindo usuário')

# ativo é falso?
#print(ativo is False)

nome = 'Geek'
nome.isupper()
False




