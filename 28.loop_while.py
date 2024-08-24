"""
Loop While

While; O comando de repetição while permite repetir instruções enquanto uma condição for verdadeira,
quando o resultado dessa condição passa a ser falso, a execução do loop é interrompida.

Forma geral

while expressão_booleana:
    //execução do loop

O bloco do while será repetido enquanto a expressão booleana for verdadeira.

Expressão Booleana é toda expressão onde o resultado é verdadeiro ou falso.

Exemplo;

#>>> num = 5
#>>> num > 6
False

# Exemplo 1
numero = 1
while numero < 10:
    print(numero)
    numero = numero + 1

# Exemplo 2
resposta = ''
while resposta != 'sim':
    resposta = input('Já acabou Jéssica? ')

#Obs; Em um loop while, é importante que cuidemos do critério de parada para não causar um loop infinito.

#C ou Java
While(expressão){
    //execução
}

#Do While (Tem em C e Java, não tem em Python)
do {
    //execução
}while(expressão);

"""
