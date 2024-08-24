"""
Calculadora de conversão de temperatura
celsius, kelvin e fahrenheit
"""

print("\n *** CALCULADORA DE CONVERSÃO DE TEMPERATURA ***\n")
celsius=input("- Digite a temperatura com base em graus Celsius(ºC):")

kelvin = float(celsius)+273.15
fahrenheit = float(celsius)*1.8+32

print("\n[]Conversão de Valores Celsius em Valores Kelvin e Fahrenheit:\n")

print('Valor em Celsius [ ', celsius, ' ] ºC')
print('Valor convertido para Kelvin é [ ', kelvin, ' ] ºK')
print('Valor convertido para Fahrenheit é [ ', fahrenheit, ' ] ºF')
