"""
Seek e Cursors

seek () → É utilizada para movimentar o cursor pelo arquivo.

```python
arquivo = open("texto.txt")

print(arquivo.read)
print(arquivo.read)
```

A leitura do arquivo é feito do inicio ao fim. Depois de ler pela primeira vez o curso fica parado depois do último texto, por isso quando é executado pela segunda vez ele não lê (não tem mais nada escrito na sequencia).

Seek () → Procurar

seek () → A função seek() é utilizada para movimentação do cursor pelo arquivo. Ela recebe um parâmetro que indica onde queremos colocar o cursor.

Movimentando o cursor pelo arquivo com a função seek () até a posição zero.

```python
arquivo.seek(0)
print(arquivo.read)
```

```python
#Lendo a partir da posição 22 do texto
arquivo.seek(22)
print(arquivo.read)
```

---

readline() → Função que lê o arquivo linha a linha (readline → lê linha)

```python
ret = arquivo.readline()
print(ret)
```

readlines() → Lê as linhas (no plural) com conteudo.

Cada linha será um item da lista.

```python
print(arquivos.readlines())
```

É usado também para saber a quantidade de linhas num arquivo:

```python
linhas = arquivo.readlines()
print(len(readlines))
```

---

Obs: Quando abrimos um arquivo com a função open() é criada uma conexão entre o arquivo no disco do computador e o nosso programa. Essa conexão é chamada de streaming. Ao finalizar os trabalhos com o arquivo devemos fechar essa conexão. Para isso utilizamos a função close().

Passos para se trabalhar com um arquivo:

1 - Abrir o arquivo;

2 - Trabalhar o arquivo;

3 - Fechar o arquivo;

```python
# 1 - Abrir o arquivo;
arquivo = open('texto.txt')

# 2 - Trabalhar o arquivo;
print(arquivo.read())
print(arquivo.closed)  # Verifica se o arquivo está aberto ou fechado - False

# 3 - Fechar o arquivo;
arquivo.close()
print(arquivo.closed) # Verifica se o arquivo está aberto ou fechado - True

# Obs: Se tentarmos manipular o arquivo após seu fechamento, teremos um ValueError
print(arquivo.read())

```

---

Com a função read() podemos limitar a quantidade de caracteres a serem lidos no arquivo.

```python
print(arquivo.read(50))
```
"""