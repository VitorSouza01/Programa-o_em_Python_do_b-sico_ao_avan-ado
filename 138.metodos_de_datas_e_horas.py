"""
Métodos de datas e horas

Com now() podemos especificar um timezone (Fuso Horário)

```python
import datetime

agora = datetime.datetime.now()  # now == hoje
print(agora)
print(type(agora))
print(repr(agora))

hoje = datetime.date.today()  # today == hoje
print(hoje)
print(type(hoje))
print(repr(hoje))
```

```
2023-12-18 18:31:42.530774
<class 'datetime.datetime'>
datetime.datetime(2023, 12, 18, 18, 31, 42, 530774)
2023-12-18
<class 'datetime.date'>
datetime.date(2023, 12, 18)
```

---

Mudanças ocorrendo à meia-noite combine()

```python
import datetime

manutencao = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=1)), datetime.time())

print(manutencao)
print(type(manutencao))
print(repr(manutencao))
```

```
2023-12-19 00:00:00
<class 'datetime.datetime'>
datetime.datetime(2023, 12, 19, 0, 0)
```

---

Encontrar o dia da semana. weekday()

Os dias da semana do método weekday() começa em 0, sendo esta a segunda-feira

0 - Segunda-feira (Monday)

1 - Terça-feira (Tuesday)

2 - Quarta-feira (Wednesday)

3 - Quinta-feira (Thursday)

4 - Sexta-feira (Friday)

5 - Sábado (Saturday)

6 - Domingo (Sunday)

```python
import datetime

manutencao = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=1)), datetime.time())

print(manutencao.weekday())
```

```
1
```

```python
import datetime

aniversario = input("Qual sua data de nascimento? (dd/mm/aaaa): ")

aniversario = aniversario.split("/")
aniversario = datetime.datetime(year=int(aniversario[2]), month=int(aniversario[1]), day=int(aniversario[0]))

if aniversario.weekday() == 0:
    print("Você nasceu em uma segunda-feira")
elif aniversario.weekday() == 1:
    print("Você nasceu em uma terça-feira")
elif aniversario.weekday() == 2:
    print("Você nasceu em uma quarta-feira")
elif aniversario.weekday() == 3:
    print("Você nasceu em uma quinta-feira")
elif aniversario.weekday() == 4:
    print("Você nasceu em uma sexta-feira")
elif aniversario.weekday() == 5:
    print("Você nasceu em um sábado")
elif aniversario.weekday() == 6:
    print("Você nasceu em um domingo")
```

```
Qual sua data de nascimento? (dd/mm/aaaa): 04/07/2001
Você nasceu em uma quarta-feira
```

---

Formatando datas/horas com strftime() (String Format Time)

dd/mm/yy hora:minuto

```python
import datetime

hoje = datetime.datetime.today()

print(hoje)

hoje_formatado = hoje.strftime("%d/%m/%Y")

print(hoje_formatado)
```

```
2023-12-18 20:02:54.548595
18/12/2023
```

```python
import datetime

def formata_data(data):
    if data.month == 1:
        return f'{data.day} de Janeiro de {data.year}'
    elif data.month == 2:
        return f'{data.day} de Fevereiro de {data.year}'
    elif data.month == 3:
        return f'{data.day} de Março de {data.year}'
    elif data.month == 4:
        return f'{data.day} de Abril de {data.year}'
    elif data.month == 5:
        return f'{data.day} de Maio de {data.year}'
    elif data.month == 6:
        return f'{data.day} de Junho de {data.year}'
    elif data.month == 7:
        return f'{data.day} de Julho de {data.year}'
    elif data.month == 8:
        return f'{data.day} de Agosto de {data.year}'
    elif data.month == 9:
        return f'{data.day} de Setembro de {data.year}'
    elif data.month == 10:
        return f'{data.day} de Outubro de {data.year}'
    elif data.month == 11:
        return f'{data.day} de Novembro de {data.year}'
    elif data.month == 12:
        return f'{data.day} de Dezembro de {data.year}'

hoje = datetime.datetime.today()

print(formata_data(hoje))
```

```
19 de Dezembro de 2023
```

---

Não consegui executar deu erro:

```python
import datetime
from textblob import TextBlob

def formata_data(data):
    return f"{data.day} de {TextBlob(data.strftime('%B')).translate(to='pt-br')} de {data.year}"

hoje = datetime.date.today()

print(formata_data(hoje))
```

Não consegui executar deu erro:

```python
import datetime

nascimento = datetime.datetime.strptime('10/04/1998', '%d/%m/%y')

print(nascimento)

nascimento = input("Qual sua data de nascimento? (dd/mm/aaaa): ")

nascimento = datetime.datetime.strptime(nascimento, '%d/%m/%y')

print(nascimento)
```

---

Somente a hora

```python
import datetime

almoco = datetime.time(12, 30, 0)

print(almoco)
```

```
12:30:00
```

---

Marcando tempo de execução do nosso código com timeit

```python
import timeit

# Loop for
tempo = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
print(tempo)

# List Comprehension
tempo = timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000)
print(tempo)

# Map
tempo = timeit.timeit('"-".join(map(str, range(100)))', number=10000)
print(tempo)
```

```
0.5833554120035842
0.7950733869947726
0.6700781170075061
```

```python
import timeit, functools

def teste(n):
    soma = 0
    for num in range(n * 200):
        soma = soma + num ** num + 4
    return soma

print(timeit.timeit(functools.partial(teste, 2), number=10000))
```

```
27.397791956012952
```
"""