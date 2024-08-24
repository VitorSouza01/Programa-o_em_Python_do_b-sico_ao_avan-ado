"""
Quantidade Vogais
"""

nome=input('\nQual é o seu nome completo?')
print('\n- Seu nome é', nome)

print(nome.split()[0],'seu nome completo possui no total',(nome.count("a")+nome.count("e")+nome.count("i")+nome.count("o")+nome.count("u")),'Vogais;')

print(nome.count("a"), 'Vogal da letra A')
print(nome.count("e"), 'Vogal da letra E')
print(nome.count("i"), 'Vogal da letra I')
print(nome.count("o"), 'Vogal da letra O')
print(nome.count("u"), 'Vogal da letra U\n')

print('Seu nome ao contrário é:',nome.split()[0][::-1])


