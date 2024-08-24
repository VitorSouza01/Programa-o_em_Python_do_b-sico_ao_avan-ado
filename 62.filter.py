"""
Filter

filter() → Serve para filtrar dados de uma determinada coleção.

```python
# Biblioteca para trabalhar com dados estatísticos
import statistics

# Dados coletados de algum sensor
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# Calculando a média dos dados utilizando a função mean()
media = statistics.mean(dados)

print(f"Média: {media}")

# Obs: Assim como a função map(), o filter() recebe dois parâmetros, sendo uma função e um iterável.

# Valor maior da média
res = filter(lambda valor: valor > media, dados)
print(list(res))
print(list(res))
```

```
Média: 2.183333333333333
[2.7, 4.1, 4.3]
[]
```

Obs: Assim como na função map(), após serem utilizados os dados de filter() eles são excluídos da memória.

---

Outro exemplo, removendo itens vazios;

```python
paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colombia', '', 'Equador', '', '', 'Venezuela']

print(paises)

res = filter(None, paises)

print(list(res))
```

```
['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colombia', '', 'Equador', '', '', 'Venezuela']
['Argentina', 'Brasil', 'Chile', 'Colombia', 'Equador', 'Venezuela']
```

---

A diferença entre map() e filter() é:

map() → Recebe dois parâmetros, uma função e um iterável e retorna um objeto mapeando a função para cada elemento do iterável.

filter() → Recebe dois parâmetros, uma função e um iterável e retorna um objeto filtrando apenas os elementos de com a filter.

---

Exemplo mais complexo:

Filtrar os usuários que estão inativos no Twitter

```python
# Forma 1

suarios = [
  {"username": "Samuel", "tweets": ["Eu adoro bolo", "Eu adoro Pizza"]},
  {"username": "Carla", "tweets": ["Eu amo meu gato"]},
  {"username": "Jeef", "tweets": []},
  {"username": "Bob123", "tweets": []},
  {"username": "Doggo", "tweets": ["Eu gosto de cachorros", "Vou sair hoje"]},
  {"username": "Gal", "tweets": []},
]

print(usuarios)

inativos = list(filter(lambda usuario: len(usuario['tweets']) == 0, usuarios))

print(f"\n{inativos}")
```

```
[{'username': 'Samuel', 'tweets': ['Eu adoro bolo', 'Eu adoro Pizza']}, {'username': 'Carla', 'tweets': ['Eu amo meu gato']}, {'username': 'Jeef', 'tweets': []}, {'username': 'Bob123', 'tweets': []}, {'username': 'Doggo', 'tweets': ['Eu gosto de cachorros', 'Vou sair hoje']}, {'username': 'Gal', 'tweets': []}]

[{'username': 'Jeef', 'tweets': []}, {'username': 'Bob123', 'tweets': []}, {'username': 'Gal', 'tweets': []}]
```

```python
# Forma 2

usuarios = [
  {"username": "Samuel", "tweets": ["Eu adoro bolo", "Eu adoro Pizza"]},
  {"username": "Carla", "tweets": ["Eu amo meu gato"]},
  {"username": "Jeef", "tweets": []},
  {"username": "Bob123", "tweets": []},
  {"username": "Doggo", "tweets": ["Eu gosto de cachorros", "Vou sair hoje"]},
  {"username": "Gal", "tweets": []},
]

print(usuarios)

inativos = list(filter(lambda usuario: not usuario['tweets'], usuarios))

print(f"\n{inativos}")
```

```
[{'username': 'Samuel', 'tweets': ['Eu adoro bolo', 'Eu adoro Pizza']}, {'username': 'Carla', 'tweets': ['Eu amo meu gato']}, {'username': 'Jeef', 'tweets': []}, {'username': 'Bob123', 'tweets': []}, {'username': 'Doggo', 'tweets': ['Eu gosto de cachorros', 'Vou sair hoje']}, {'username': 'Gal', 'tweets': []}]

[{'username': 'Jeef', 'tweets': []}, {'username': 'Bob123', 'tweets': []}, {'username': 'Gal', 'tweets': []}]
```

---

Exemplo combinando filter() com map()

```python
# Devemos criar uma lista contendo 'Sua instrutora é' + nome, desde que cada nome tenha menos de 5 caracteres

nomes = ["Vanessa", "Ana", "Maria"]

lista = list(map(lambda nome: f"Sua instrutora é {nome}", filter(lambda nome: len(nome) < 5, nomes)))

print(lista)
```

```
['Sua instrutora é Ana']
```
"""