"""
Métodos Mágicos

POO - Métodos Mágicos

Métodos Mágicos, são todos os métodos que utilizam dunder.

dunder init → __init__()

```python
 def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
```

Dunder → Double Underscore

```python
    def __repr__(self):
        return f"{self.titulo} escrito por {self.autor}"
```



```python
class Livro:
  def __init__(self, titulo, autor, paginas):
    self.titulo = titulo
    self.autor = autor
    self.paginas = paginas

  def __str__(self):
    return self.titulo

  def __repr__(self):
    return f"{self.titulo} escrito por {self.autor}"

  def __len__(self):
    return self.paginas

  def __del__(self):
    print("Um objeto do tipo Livro foi deletado da memória")

  def __add__(self, outro):
    return f"{self} - {outro}"

  def __mul__(self, outro):
    if isinstance(outro, int):
      msg = " "
      for i in range(outro):
        msg += " " + str(self)
      return msg
    return "Não posso multiplicar"

livro1 = Livro("O Senhor dos Anéis", "J.R.R. Tolki", 500)
livro2 = Livro("O Hobbit", "J.R.R. Tolki", 380)

print(livro1)
print(livro2)

print(len(livro1))
print(len(livro2))

print(livro1 + livro2)
print(livro1 * 5)
```

```
O Senhor dos Anéis
O Hobbit
500
380
O Senhor dos Anéis - O Hobbit
  O Senhor dos Anéis O Senhor dos Anéis O Senhor dos Anéis O Senhor dos Anéis O Senhor dos Anéis
Um objeto do tipo Livro foi deletado da memória
Um objeto do tipo Livro foi deletado da memória
```
"""