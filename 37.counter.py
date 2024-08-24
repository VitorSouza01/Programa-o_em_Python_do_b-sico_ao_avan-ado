"""
Módulo Collections - Counter (Contador)

Collection -> High-perfomance Container Datetypes. (Tipos de dados de contêiner de alta performance)

Container - A partir de um tipo de dado, pode adicionar vários elementos dentro dele.

'Um container tem como objetivo principal a separação de processos ou partes de uma aplicação
de seu sistema operacional.'


Counter -> Recebe um interável como parâmetro e cria um objeto do tipo Collections Counter que é parecido
com um dicionário, contendo como chave o elemento da lista passada como parâmetro e como valor a quantidade
de ocorrências desse elemento.



# Realizando o import

from collections import Counter

# Exemplo 1

# Podemos utilizar qualquer iterável, aqui usamos uma lista.
lista = [1, 1, 1, 2, 2, 3, 3, 3, 3, 1, 1, 2, 2, 4, 4, 4, 5, 5, 5, 5, 3, 45, 45, 66, 66, 43, 34]

# Utilizando o Counter
res = Counter(lista)

print(type(res))
print(res)

# Veja que, para cada elemento da lista, o Counter criou uma chave e colocou como valor a quantidade de
# ocorrênciais.



# Exemplo 2

from collections import Counter


print(Counter('Geek University'))



# Exemplo 3

from collections import Counter


texto = ""Como faz show de cabeça quente, cê me pede fendi, em casa me ofende, sua mãe me defende, mexeu com a minha
mente, eu fiquei carente, foi me abandonar""

palavras = texto.split()

# print(palavras)

res = Counter(palavras)

print(res)




# Encontrando as 5 palavras com mais ocorrências no texto

from collections import Counter


texto = ""Todos os editores da Wikipédia são voluntários e integram uma comunidade colaborativa, sem um líder, onde
coordenam esforços em projetos temáticos e espaços de discussão. Dentre as várias páginas de ajuda à disposição, estão
as que explicam como criar um artigo ou editar um artigo. Em caso de dúvidas, não hesite em perguntar. Debates e
comentários sobre os artigos são bem-vindos. As páginas de discussão servem para centralizar reflexões e avaliações
sobre como melhorar o conteúdo da Wikipédia.""

palavras = texto.split()
res = Counter(palavras)
print(res)

print(res.most_common(5))
"""







