"""
Escrevendo em arquivos

Obs: Ao abrir um arquivo para leitura, não podemos realizar a escrita nele, apenas ler. Da mesma forma, se abrirmos um arquivo para escrita, não podemos lê-lo, somente escrever nele.

Obs: Ao abrir um arquivo para escrita, o arquivo é criado no sistema operacional.

Para escrevermos dados em um arquivo, após abrir o arquivo utilizaremos a função write(). Essa função recebe uma string como parâmetro, caso contrario teremos um TypeError.

```python
# Exemplo de escrita - modo 'w' - write (escrita)

with open('novo.txt', 'w') as arquivo:
    arquivo.write('Escrever dados em arquivos é muito fácil.\n')
    arquivo.write('Podemos colocar quantas linhas quisermos.\n')
    arquivo.write('Está é a última linha.')
```


Abrindo um arquivo para escrita com o modo ‘w’, se o arquivo não existir será criado. Caso ele já exista, o anterior será apagado e um novo será criado. Dessa forma, todo o conteúdo no arquivo anterior é perdido.

```python
# Forma Pythônica

with open('novo.txt', 'w') as arquivo:
    arquivo.write('Novos dados.\n')
    arquivo.write('Podemos colocar quantas linhas quisermos.\n')
    arquivo.write('Está é a última linha.')
```


---

```python
# Forma tradicional de escrita em um arquivo (Não Pythônica)
arquivo = open('mais.txt', 'w')

arquivo.write('Um texto qualquer.\n')
arquivo.write('Mais um texto')

arquivo.close()
```

---

```python
with open('geek.txt', 'w') as arquivo:
    arquivo.write('Geek ' * 1000)
```


---

```python
with open('frutas.txt', 'w') as arquivo:
    while True:
        fruta = input("Informe uma fruta ou digite sair: ")
        if fruta != 'sair':
            arquivo.write(fruta)
            arquivo.write('\n')
        else:
            break
```


"""