"""
O bloco Try/Except

Utilizamos o bloco try/excpet para tratar erros que podem ocorrer no nosso código. Prevenindo assim que o programa para
 de funcionar e o usuário recebe mensagens de erro inesperado.

A forma geral mais simples é:

try:

//execução problemática

excpet:

//o que deve ser feito em caso de problema

Exemplo 1 - Tratando um erro genérico

```python
try:
    geek()
except:
    print('Deu algum problema')
```

```
Deu algum problema
```

Exemplo 2 - Tratando um erro genérico

```python
try:
    len(5)
except:
    print('Deu algum problema')
```

```
Deu algum problema
```

Tenta executa a função geek(), caso encontra erro, imprima a mensagem de erro.

Obs: Tratar erro de forma genérica não é a melhor forma de tratamento de erro. O ideal é SEMPRE tratar de
forma especifica.


# Exemplo 3 - Tratando um erro específico
try:
    geek()
except NameError:
    print('Você está utilizando uma função inexistente')



# Exemplo 4 - Tratando um erro específico
try:
    len(5)
except TypeError:
    print('Você está utilizando uma função inexistente')



# Exemplo 5 - Tratando um erro específico com detalhes do erro
try:
    len(5)
except TypeError as err:
    print(f'A aplicação gerou o seguinte erro: {err}')



# Podemos efetuar diversos tratamentos de erros de uma vez;

try:
    geek()
except NameError as erra:
    print(f'Deu NomeError: {erra}')
except TypeError as errb:
    print(f'Deu TypeError: {errb}')
except:
    print('Deu um erro diferente')
"""

def paga_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:
        return None
    except TypeError:
        return None

dic = {"nome": "Geek"}

print(paga_valor(dic, 8))




