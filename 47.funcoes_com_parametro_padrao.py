"""
Funções com parâmetro padrão (Default Paramters)

- Funções onde a passagem de parâmetro seja opcional


# Exemplo de função onde a passagem de parâmetro seja opcional
Exemplo Print;

print('Geek University')

print()



# Exemplo de função onde a passagem de parâmetro seja obrigatório

def quadrado(numero):
    return numero ** 2

print(quadrado(3))
print(quadrado())



def exponencial(numero, potencia=2):
    return numero ** potencia

print(exponencial(2, 3))  # 2 * 2 * 2 = 8
print(exponencial(3, 2))  # 3 * 3 = 9

print(exponencial(3))  # Por padrão eleva ao quadrado
print(exponencial(3, 5))  # Eleva á potência informada pelo usuário

# Obs;
# - Se o usuário passar somente 1 argumento, este será atribuído ao parâmetro número,
# e será calculado o quadrado deste número.
# - Se o usuário passar 2 argumentos, o primeiro será atribuído ao parâmetro número e o
# segundo ao parâmetro potencia. Então será calculada esta potência.



# Em função Python, os parâmetros com valores 'default' (padrão) DEVEM sempre estar
# ao final da declaração.

# ERRO!
def teste(num=2, potencia):
    return num ** potencia


print(teste(6))




# Outros exemplos

def soma(num1, num2):
    return num1 + num2


print(soma(4, 3))
print(soma(4))  # TypeError
print(soma())  # TypeError

# Como não foi definido um valor, ambos são obrigatorios





# Exemplo mais complexo

def mostra_informacao(nome='Geek', instrutor=False):
    if nome == 'Geek' and instrutor:
        return 'Bem-vindo instrutor Geek!'
    elif nome == 'Geek':
        return 'Eu pensei que você era o instrutor'
    return f'Olá {nome}'


print(mostra_informacao())
print(mostra_informacao(instrutor=True))
print(mostra_informacao(True))
print(mostra_informacao('Ozzy'))
print(mostra_informacao(nome='Stephany'))




# Por que utilizar parâmetros com valor 'default'?

- Nos permite ser mais flexíveis nas funções.
- Evita erros com parâmetros incorretos.
- Nos permite trabalhar com exemplos mais legíveis de código.




# Quais tipos de dados podemos utilizar como valores 'default' para parâmetros?

- Qualquer tipo de dado:
    - Números, strings, floats, booleanos, listas, tuplas, dicionários, funções e etc...




# Exemplos de funções como parâmetros


def soma(num1, num2):
    return num1 + num2


def mat(num1, num2, fun=soma):
    return fun(num1, num2)


def subtracao(num1, num2):
    return num1 - num2


print(mat(2, 3))
print(mat(2, 2, subtracao))



# Escopo - Evitar problemas e confusões...

# Variáveis globais
# Variáveis locais

instrutor = 'Geek'  # Variável global


def diz_oi():
    instrutor = 'Python'  # Variável local
    return f'Oi {instrutor}'


print(diz_oi())

# Obs: Se tivermos uma variável local com o mesmo nome de uma variável global, a local
# terá preferência.




# Variavel local só existe dentro do bloco que ela está

def diz_oi():
    prof = 'Geek'  # Variável local
    return f'Olá {prof}'


print(diz_oi())

print(prof)  # NameError




# Atenção com variáveis globais (Se puder evitarm evite!)

total = 0

def incrementa():
    total = total + 1  # UnboundLocalError (A variável local está sendo utilizada para
    # processamento sem ter sido inicalizada )
    return total

print(incrementa())



# Solução;

total = 0

def incrementa():
    global total  # Avisando que queremos utilizar a variável global
    total = total + 1
    return total

print(incrementa())
"""

# Podemos ter funções que são declaradas dentro de funções, e também tem uma forma
# especial de escopo de variável.

def fora():
    contador = 0

    def dentro():
        nonlocal contador  # Não é local nem global

        contador = contador + 1
        return contador
    return dentro()


print(fora())
print(fora())
print(fora())

#print(dentro())  # NameError






