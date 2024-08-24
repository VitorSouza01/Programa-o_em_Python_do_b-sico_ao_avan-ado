"""
Erros mais comuns em Python

ATENÇÃO: É importante prestar atenção e aprender a ler as saídas de erros gerados pela execução de um código.

NameError;

```
>>> printf('Geek University')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'printf' is not defined. Did you mean: 'print'?
>>>
```

Os erros mais comuns:

1 - SyntexError → Ocorre quando o Python encontra um erro de sintaxe, ou seja, você escreveu algo que o Python não reconhece como parte da linguagem;

```python
#Exemplos SyntaxError

#a)
def funcao:
	print('Geek University')

#b)
def = 1

#c)
return
```

```
File "C:\Users\vmendes\Documents\Python\Ler_txt\ler_txt.py", line 1
    def funcao:
              ^
SyntaxError: expected '('

Process finished with exit code 1
```

```
File "C:\Users\vmendes\Documents\Python\Ler_txt\ler_txt.py", line 1
    def = 1
        ^
SyntaxError: invalid syntax

Process finished with exit code 1
```

```
File "C:\Users\vmendes\Documents\Python\Ler_txt\ler_txt.py", line 1
    return
    ^^^^^^
SyntaxError: 'return' outside function

Process finished with exit code 1
```

---

2 - NameError → Ocorre quando uma variável ou função não foi definida;

```python
# Exemplos NameError
#a)
print(geek)

#b)
geek()

#c)
a = 18
if a < 10:
	msg = "É maior que 10"
print(msg)
```

```
Traceback (most recent call last):
  File "C:\Users\vmendes\Documents\Python\Ler_txt\ler_txt.py", line 1, in <module>
    print(geek)
          ^^^^
NameError: name 'geek' is not defined

Process finished with exit code 1
```

```
Traceback (most recent call last):
  File "C:\Users\vmendes\Documents\Python\Ler_txt\ler_txt.py", line 1, in <module>
    geek()
    ^^^^
NameError: name 'geek' is not defined

Process finished with exit code 1
```

```
Traceback (most recent call last):
  File "C:\Users\vmendes\Documents\Python\Ler_txt\ler_txt.py", line 4, in <module>
    print(msg)
          ^^^
NameError: name 'msg' is not defined

Process finished with exit code 1
```

---

3 - TypeError → Ocorre quando uma função/operação/ação é aplicada a um tipo errado;

```python
# Exemplos TypeError
#a)
print(len(5)

#b)
print('Geek' + [])

#c)
print('Geek' + 4)
```

```
File "C:\Users\vmendes\Documents\Python\Ler_txt\ler_txt.py", line 1
    print(len(5)
         ^
SyntaxError: '(' was never closed
```

```
Traceback (most recent call last):
  File "C:\Users\vmendes\Documents\Python\Ler_txt\ler_txt.py", line 1, in <module>
    print('Geek' + [])
          ~~~~~~~^~~~
TypeError: can only concatenate str (not "list") to str

Process finished with exit code 1
```

```
Traceback (most recent call last):
  File "C:\Users\vmendes\Documents\Python\Ler_txt\ler_txt.py", line 1, in <module>
    print('Geek' + 4)
          ~~~~~~~^~~
TypeError: can only concatenate str (not "int") to str

Process finished with exit code 1
```

---

4 - IndexError → Ocorre quando tentamos acessar um elemento de uma lista ou outro tipo de dado indexado utilizando um índice invalido;

```python
# Exemplos IndexError
#a)
lista = ['Geek']
print(lista[2])

#b)
lista = ['Geek']
print(lista[0][10])

#c)
tupla = ('Geek',)
print(tupla[0][10])

```

```
Traceback (most recent call last):
  File "C:\Users\vmendes\Documents\Python\Ler_txt\ler_txt.py", line 2, in <module>
    print(lista[2])
          ~~~~~^^^
IndexError: list index out of range

Process finished with exit code 1
```

```
Traceback (most recent call last):
  File "C:\Users\vmendes\Documents\Python\Ler_txt\ler_txt.py", line 2, in <module>
    print(lista[0][10])
          ~~~~~~~~^^^^
IndexError: string index out of range

Process finished with exit code 1
```

```
Traceback (most recent call last):
  File "C:\Users\vmendes\Documents\Python\Ler_txt\ler_txt.py", line 2, in <module>
    print(tupla[0][10])
          ~~~~~~~~^^^^
IndexError: string index out of range

Process finished with exit code 1
```

---

5 - ValueError → Ocorre quando uma função/operação built-in (integrada) recebe um argumento com tipo correto mas o valor inapropriado;

```python
# Exemplos ValueError
#a)
print(int('Geek'))

#b)
print(float('Geek'))

```

```
Traceback (most recent call last):
  File "C:\Users\vmendes\Documents\Python\Ler_txt\ler_txt.py", line 1, in <module>
    print(int('Geek'))
          ^^^^^^^^^^^
ValueError: invalid literal for int() with base 10: 'Geek'

Process finished with exit code 1
```

```
Traceback (most recent call last):
  File "C:\Users\vmendes\Documents\Python\Ler_txt\ler_txt.py", line 1, in <module>
    print(float('Geek'))
          ^^^^^^^^^^^^^
ValueError: could not convert string to float: 'Geek'

Process finished with exit code 1
```

---

6 - KeyError → Ocorre quando tentamos acessar um dicionário com uma chave que não existe;

```python
# Exemplos KeyError
#a)
dic = {'python': 'university'}
print(dic['geek'])
```

```
Traceback (most recent call last):
  File "C:\Users\vmendes\Documents\Python\Ler_txt\ler_txt.py", line 2, in <module>
    print(dic['geek'])
          ~~~^^^^^^^^
KeyError: 'geek'

Process finished with exit code 1
```

---

7 - AttributeError → Ocorre quando uma variável não tem um atributo/função;

```python
# AttributeError
#a)
tupla = (11, 2, 31, 4)
print(tupla.sort())
```

```
Traceback (most recent call last):
  File "C:\Users\vmendes\Documents\Python\Ler_txt\ler_txt.py", line 2, in <module>
    print(tupla.sort())
          ^^^^^^^^^^
AttributeError: 'tuple' object has no attribute 'sort'

Process finished with exit code 1
```

---

8 - IndentationError → Ocorre quando não respeitamos a endentação do Python (4 espaços)

```python
# AttributeError
#a)
for i in range(10):
   print(i)
    i += 1
```

```
File "C:\Users\vmendes\Documents\Python\Ler_txt\ler_txt.py", line 3
    i += 1
IndentationError: unexpected indent

Process finished with exit code 1
```

---

Obs: Exceptions e Erros são sinônimos na programação.

Obs: Importante ler e prestar atenção a saída de erro.
"""