"""
Estrutura condicionais
if (Se), else (Se não), elif (else if)

 *Estruturas condicionais,pode dar caminhos diferentes para resolver problemas.

'Uma estrutura condicional é aquela que faz uma verificação em uma determinada expressão para identificar se ela
atende à condição especificada. A partir do resultado, uma ou mais instruções são executadas'


----Estrutura condicional if, else em C
if(idade < 18){
    printf("Menor de idade");
}else if(idade == 18){
    printf("Tem 18 anos");
}else{
    printf("É menor de idade")
}


----Estrutura condicional if, else em Java
if(idade < 18){
    System.out.println("Menor de idade");
}else if(idade == 18){
    System.out.println("Tem 18 anos");
}else{
    System.out.println("É menor de idade");
}

"""

idade = 25

if idade < 18:
    print('Menor de idade')
elif idade == 18:
    print('Tem 18 anos')
elif idade == 26:
    print('Tem 26 anos')
else:
    print('Maior de idade')
# É bom utilizar somente o If uma vez, o Else uma vez enquanto o Elif voce pode usar varias vezes