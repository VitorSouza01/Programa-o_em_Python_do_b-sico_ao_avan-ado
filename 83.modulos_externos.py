"""
Instalando e utilizando módulos externos

Módulos Externos

Utilizamos o gerenciamento de pacotes Python chamado Pip - Python Installer Package

Você pode conhecer todos os pacotes externos oficiais em: https://pypi.org/

Exemplo: colorama

(coloroma → É utilizado para permitir impressão de textos coloridos no terminal.)

---

Instalando um módulo:

```python
pip install nome_do_modulo
```

Instalando o pacote colorama:

```python
pip install colorama
```

Utilizando o pacote instalado

```python
from colorama import init, Fore

init()

print(Fore.MAGENTA + 'Geek University')
print(Fore.BLUE + 'Geek University')
```

```
Geek University
Geek University
```

---

Gerando PDF:

```python
import pydf

pdf = pydf.generate_pdf('<h1>Geek University</h1><br>Curso de Python</br>')

with open('test_doc.pdf', 'wb') as f:
    f.write(pdf)
```
"""