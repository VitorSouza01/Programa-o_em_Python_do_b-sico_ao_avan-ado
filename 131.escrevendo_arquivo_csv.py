"""
Escrevendo em arquivos CSV

reader() (leitor), writer() (escrever)

writerow() → Escreva uma linha

writer() → Gera um objeto para que possamos escrever em um arquivo csv. Utilizamos o método writerow() para escrever cada linha. Este método recebe uma lista.

```python
from csv import writer

with open('filmes.csv', 'w') as arquivo:
    escritor_csv = writer(arquivo)
    filme = None
    escritor_csv.writerow(['Título', 'Gênero', 'Duração'])
    while filme != "sair":
        filme = input("Digite o nome do filme: ")
        if filme == "sair":
            genero = input("Digite o gênero do filme: ")
            duracao = input("Digite a duração do filme: ")
            escritor_csv.writerow([filme, genero, duracao])
```

```
Digite o nome do filme: Maze Runner: Correr ou Morrer
Digite o gênero do filme: Ficção científica
Digite a duração do filme: 1h 53m
Digite o nome do filme: Maze Runner: Prova de Fogo
Digite o gênero do filme: Ficção científica
Digite a duração do filme: 2h 13m
Digite o nome do filme: Maze Runner: A Cura Mortal
Digite o gênero do filme: Ação
Digite a duração do filme: 2h 22m
Digite o nome do filme: sair
```

Arquivo csv:

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/50f6c3e8-cd39-40a2-a8ee-7ed9bb20ee47/d677730e-0869-4797-b4fb-605ab7bd2afe/Untitled.png)

---

DicrWriter

Obs: As chaves do dicionário devem ser as mesmas utilizadas como cabeçalho.

```python
from csv import DictWriter

with open('filmes2.csv', 'w') as arquivo:
    cabecalho = ["Titulo", "Gênero", "Duração"]
    escritor_csv = DictWriter(arquivo, fieldnames=cabecalho)
    escritor_csv.writeheader()
    filme = None
    while filme != "sair":
        filme = input("Digite o nome do filme: ")
        if filme != "sair":
            genero = input("Digite o gênero do filme: ")
            duracao = input("Digite a duração do filme: ")
            escritor_csv.writerow({"Titulo": filme, "Gênero": genero, "Duração": duracao})
```

```
Digite o nome do filme: Divergente
Digite o gênero do filme: Ação
Digite a duração do filme: 2h 19m
Digite o nome do filme: Insurgente
Digite o gênero do filme: Ação
Digite a duração do filme: 1h 59m
Digite o nome do filme: Convergente
Digite o gênero do filme: Ação
Digite a duração do filme: 2h
Digite o nome do filme: sair
```

Arquivo CSV:

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/50f6c3e8-cd39-40a2-a8ee-7ed9bb20ee47/08637fd5-e8b4-40e2-b1bd-6aba92cbda9e/Untitled.png)
"""