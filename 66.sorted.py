"""
Sorted

Obs: Não Confunda, apesar do nome, com a função sort() que já estudamos em Listas. O sort() só funciona em listas.

Podemos utilizar o sorted() com qualquer iterável.

Como o próprio nome diz, sorted() serve para ordenar.

Obs: O sorted(), SEMPRE retorna uma lista com os elementos do iterável ordenados.

Exemplo:

```python
numeros = (6, 1, 8, 2)
print(numeros)

print(sorted(numeros))  # Ordenar de menor para o maior
print(numeros)
```

```
(6, 1, 8, 2)
[1, 2, 6, 8]
(6, 1, 8, 2)
```

---

Outro exemplo;

```python
numeros = (6, 1, 8, 2)
print(numeros)

print(sorted(numeros))

# Adicionando parâmetros ao sorted()
print(sorted(numeros, reverse=True))  # Ordena do maior para o menor
```

```
(6, 1, 8, 2)
[1, 2, 6, 8]
[8, 6, 2, 1]
```

Podemos utilizar o sorted() para coisas mais complexas;

```python
usuarios = [
  {"username": "Samuel", "tweets": ["Eu adoro bolo", "Eu adoro Pizza"]},
  {"username": "Carla", "tweets": ["Eu amo meu gato"]},
  {"username": "Jeef", "tweets": [], "cor": "amarelo"},
  {"username": "Bob123", "tweets": []},
  {"username": "Doggo", "tweets": ["Eu gosto de cachorros", "Vou sair hoje"]},
  {"username": "Gal", "tweets": [], "cor": "preto", "musica": "rock"},
]

print(usuarios)

# Ordenando por username - Ordem Alfabética
print(f"\n{sorted(usuarios, key=lambda usuario: usuario['username'])}")

# Ordenando pelo número de tweets
print(f"\n{sorted(usuarios, key=lambda usuario: len(usuario['tweets']))}")
```

```
[{'username': 'Samuel', 'tweets': ['Eu adoro bolo', 'Eu adoro Pizza']}, {'username': 'Carla', 'tweets': ['Eu amo meu gato']}, {'username': 'Jeef', 'tweets': [], 'cor': 'amarelo'}, {'username': 'Bob123', 'tweets': []}, {'username': 'Doggo', 'tweets': ['Eu gosto de cachorros', 'Vou sair hoje']}, {'username': 'Gal', 'tweets': [], 'cor': 'preto', 'musica': 'rock'}]

[{'username': 'Bob123', 'tweets': []}, {'username': 'Carla', 'tweets': ['Eu amo meu gato']}, {'username': 'Doggo', 'tweets': ['Eu gosto de cachorros', 'Vou sair hoje']}, {'username': 'Gal', 'tweets': [], 'cor': 'preto', 'musica': 'rock'}, {'username': 'Jeef', 'tweets': [], 'cor': 'amarelo'}, {'username': 'Samuel', 'tweets': ['Eu adoro bolo', 'Eu adoro Pizza']}]

[{'username': 'Jeef', 'tweets': [], 'cor': 'amarelo'}, {'username': 'Bob123', 'tweets': []}, {'username': 'Gal', 'tweets': [], 'cor': 'preto', 'musica': 'rock'}, {'username': 'Carla', 'tweets': ['Eu amo meu gato']}, {'username': 'Samuel', 'tweets': ['Eu adoro bolo', 'Eu adoro Pizza']}, {'username': 'Doggo', 'tweets': ['Eu gosto de cachorros', 'Vou sair hoje']}]
```

---

Último exemplo
"""