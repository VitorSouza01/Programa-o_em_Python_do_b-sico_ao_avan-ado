"""
Saindo de loops com break

Em Python, a instrução break oferece a possibilidade de sair de um loop quando uma condição externa é acionada.
A instrução break será colocada dentro do bloco de código abaixo da sua instrução de loop, geralmente após uma
instrução condicional if .

Break funciona da mesma forma que nas linguagens C ou Java.

Utilizamos o break para sair de loops de maneira projetada.



"""
# Exemplo 1
for numero in range(1, 11):
    if numero == 6:
        break
    else:
        print(numero)
print('Sai do loop')

# Exemplo 2
while True:
    comando = input("Digite 'sair' para sair: ")
    if comando == 'sair':
        break
