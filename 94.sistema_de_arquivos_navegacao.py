"""
Sistema de Arquivos - Navegação

Para fazer uso de manipulação de arquivos do sistema operacional, precisa importar e fazer uso do modulo os.

*A principal diferença é que os caminhos absolutos são independentes do diretório atual, enquanto os caminhos relativos dependem do diretório atual. Os caminhos relativos são frequentemente usados quando você está trabalhando em um contexto específico e deseja fazer referência a arquivos ou diretórios dentro desse contexto. Por outro lado, os caminhos absolutos são usados quando você deseja especificar a localização precisa de um arquivo ou diretório em todo o sistema de arquivos.*

os → Operating System - Sistema operacional

```python
# Fazer o import
import os

# getcwd() -> pega o current work directory - diretório de trabalho corrente
# Retorna o path (caminho) absoluto
print(os.getcwd())  # C:\Users\vmendes\Documents\Python

# Para mudar o diretório, podemos utilizar o chdir()

os.chdir('..')

print(os.getcwd())  # C:\Users\vmendes\Documents

os.chdir('..')

print(os.getcwd())  # C:\Users\vmendes
```

Podemos checar se um diretório é absoluto (vindo da raiz) ou relativo

```python
import os

# Linux
print(os.path.isabs('/home/vitor/'))  # True
```

Obs: Para usuários Windows, se você, infelizmente, estiver utilizando um computador com Windows, terá que ter cuidado ao verificar diretórios.

```python
import os

# Windows
print(os.path.isabs('C:\\Users\\vmendes'))  # True
```

Podemos identificar o sistema operacional com o module os

```python
import os

print(os.name)  # nt (Windows), posix (Linux e Mac)
```

Podemos ter mais detalhes no sistema operacional

```python
import os

print(os.uname())
```

```python
# Fazer o import
import sys

print(sys.platform)  # win32
```

---

```python
import os

print(os.getcwd())

res = os.path.join(os.getcwd(), 'geek', 'university')

os.chdir(res)

print(os.getcwd())
```


Veja que o os.path.join() recebe dois parâmetros, sendo o primeiro o diretório atual e o segundo o diretório que será juntando ao atual.

---

Podemos listar os arquivos e diretórios com o listdir()

```python
import os

print(os.listdir())
```


---

```python
import os

# Podemos listar os arquivos e diretórios com mais detalhes com scandir()

scanner = os.scandir()

arquivos = list(scanner)

# print(arquivos)
# print(dir(arquivos[0]))

print(arquivos[0].inode())  # ??
print(arquivos[0].is_dir())  # É um diretório? False
print(arquivos[0].is_file())  # É um arquivo? True
print(arquivos[0].is_symlink())  # É um link simbólico? False
print(arquivos[0].name)  # Nome do arquivo
print(arquivos[0].path)  # Caminho até o arquivo
print(arquivos[0].stat())  # Estatísticas...

# Obs: Quando utilizamos a função scandir() nós precisamos fechá-la, assim quando abrimos um arquivo.

scanner.close()
```

"""