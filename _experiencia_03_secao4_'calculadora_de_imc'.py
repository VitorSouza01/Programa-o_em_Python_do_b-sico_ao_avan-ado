""""
Calculadora de IMC
"""
print('[ Calculadora de IMC ]\n')

peso=input('Informe o seu peso (Kg):')
altura=input('Informe a sua altura (Metro):')

imc=str(float(peso)/(float(altura)*float(altura)))

print('\n- O seu IMC é:',imc[0:4])


if float(imc) <= 18.5:
    print('* Você está em estado de Magreza!')
elif float(imc) <= 24.9:
    print('* Você está em estado Normal!')
elif float(imc) <=29.9:
    print('* Você está em estado de Sobrepeso!')
elif float(imc) <=39.9:
    print('* Você está em estado de Obesidade!')
elif float(imc) >=40.0:
    print('* Você está em estado de Obesidade Grave!')
