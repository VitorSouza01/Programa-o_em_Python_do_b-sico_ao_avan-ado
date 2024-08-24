"""
Modos de Arquivos

r → Abre para leitura - padrão

w → Abre para escrita - sobrescreve caso o arquivo já exista

x → Abre para escrita - somente se o arquivo não existir. Caso contrário existir, gera FileExistsError

a → Abre para escrita - adicionando o conteúdo ao final do arquivo

‘+’ → Abre para o modo

Obs: abrindo no modo ‘a’ → append, se o arquivo não existir será criado. Caso exista, o novo conteúdo será adicionado SEMPRE ao final do arquivo. Com o modo ‘a’, não controlamos o cursor.

```python
# Exemplo x
try:
    with open('university.txt', 'x') as arquivo:
        arquivo.write('Teste de conteúdo 2.\n')
except FileExistsError:
    print('Arquivo já existe')
```



---

```python
# Exemplo a
with open('frutas.txt', 'a') as arquivo:
    while True:
        fruta = input('Informe uma fruta ou sair: ')
        if fruta != 'sair':
            arquivo.write(fruta)
            arquivo.write('\n')
        else:
            break
```



---

```python
# Uso do +
with open('outro.txt', 'r+') as arquivo:
    arquivo.write('Adicionada\n')
    arquivo.seek(11)
    arquivo.write('Nova linha.\n')
    arquivo.seek(32)
    arquivo.write('Mais uma linha.\n')
```

"""