"""
O comando With

O bloco with

Passo para se trabalhar com arquivos:

1 - Abrimos o arquivo

2 - Manipulamos o arquivo

3 - Fechamos o arquivo

O block with é utilizado para criar um contexto de trabalho onde os recursos utilizados são fechados após o block with

```python
# O block with - Forma Pythônica de manipular arquivos

with open('texto.txt') as arquivos:
    print(arquivos.realines())

# O arquivo é fechado quando saí do with
```
"""