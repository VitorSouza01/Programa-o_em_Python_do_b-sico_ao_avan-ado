"""
Sistema de Arquivos - Manipulação

Descobrindo se um arquivo ou diretório existe

```python
import os

# Arquivo
print(os.path.exists('arquivo.txt'))  # False
print(os.path.exists('frutas.txt'))  # True

# Diretório
# Path relativos
print(os.path.exists('geek'))  # True
print(os.path.exists('geek/university'))  # True
print(os.path.exists('geek/university/../geek3.py'))  # False
print(os.path.exists('outro'))  # False

# Paths absolutos
print(os.path.exists('/home/geek/university'))  # False
print(os.path.exists('/home/geek/Imagens'))  # True
```

---

Criando arquivos

Forma 1:

```python
open('arquivo-teste.txt', 'w').close()
```

Forma 2:

```python
open('arquivo-teste2.txt', 'a').close()
```

Forma 3:

```python
with open('arquivo.teste3.txt', 'w') as arquivos:
    pass
```

---

Criando arquivos

```python
import os
os.mknod('arquivo-teste4.txt')
os.mknod('/home/geek/university.txt')
```

Obs: Se você estiver utilizando no Mac OS, pode haver um erro de PermissionError
Obs: Criando um arquivo via mknod() se o arquivo já existir teremos o erro FileExistsError

---

Criando diretórios

```python
import os

# Path Relativo
os.mkdir('templates')

# Path Absoluto
os.mkdir('/home/geek/templates')
```

Obs: A função mkdir() cria um diretório se esta não existir. Caso exista, teremos FileExistsError

Obs: Se não tivermos permissão para criar o diretório teremos um PermissionError

---

Criando multi-diretórios (árvore de diretórios)

```python
import os
os.makerdirs('template/geek//university/outro')
```

Obs: Se já existir, teremos um FileExistsError

---

Renomear arquivos e diretórios

```python
# Diretórios
os.rename('geeek2/novo2', 'geek2')

# Arquivos
os.rename('geek2/novo2/outro2/teste.txt', 'geek.txt')
```

Obs: Se o diretório não existir teremos um FileNotFoundError

Obs: Se o diretório que queremos renomear não estiver vazio, teremos um OSError

---

Atenção! Tome cuidado com os comandos de deleção. Ao deletaremos um arquivo ou diretório, eles não vão para a lixeira. Eles somem.

```python
import os

# Removendo arquivos
os.remove('geek.txt')
```

Obs: Se você estiver no Windows e o arquivo que você for deletar estiver em uso, você terá um erro.

Obs: Caso o arquivo não exista, teremos o FileNotFoundError

Obs: Se você informar um diretório ao invés de um arquivo, teremos um IsADirectoryError

---

Removendo diretórios vazios

```python
import os
os.rmdir('templates')
```

Obs: Se o diretório tiver qualquer conteúdo teremos um OSError

Obs: Se o diretório não existir teremos um FileNotFondError

Removendo uma árvore de diretórios

```python
import os
for arquivo in os.scandir('geek2'):
    if arquivo.is_file():
        os.remove(arquivo.path)
```

Podemos remover uma árvore de diretórios vazios

```python
import os
os.removedirs('geek/mais')
```

Se algum dos diretórios contiver arquivos ou outros diretórios, o processo para.

---

Atenção! Ao remover arquivos e diretórios com Python eles não vão para a Lixeira. Eles vão embora!

```python
import os

# Importando a biblioteca send2trash (Envia arquivos e diretórios para a lixeira. Eles vão embora!)
from send2trash import send2trash

os.remove('cesta1.txt')  # Não vai para a lixeira. É deletado imediatamente
send2trash('cesta2.txt')  # Vai para a lixeira. Pode ser restaurado
```

Obs: Se o arquivo não existir, teremos OSError

---

Trabalhando com arquivos e diretórios temporários

```python
import os
import tempfile

# Criando um diretório temporário
with tempfile.TemporaryDirectory() as tmp:
    print(f'Criei o diretório temporário em {tmp}')
    with open(os.path.join(tmp, 'arquivo_temporario.txt'), 'w') as arquivo:
        arquivo.write('Geek University\n')
    input()
```

Estamos criando um diretório temporário, abrindo o mesmo e dentro dele criando um arquivo para escrevermos um texto. No final, usamos o input() só para mantermos os arquivos temporários ‘vivos’ dentro dos blocos with.

Obs: Possivelmente, o código acima não irá funcionar se você estiver utilizando o Windows. Por conta desse sistema trabalhar de forma diferente com arquivos temporários.

```python
import os
import tempfile

# Criando um arquivo temporário
with temfile.TemporaryFile() as tmp:
    tmp.write(b'Geek University\n')
    tmp.seek(0)
    print(tmp.read())
```

Obs: Em arquivos temporários só conseguimos escrever bits. Por isso, utilizamos ‘b’.
"""