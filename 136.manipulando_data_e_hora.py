"""
Manipulando data e hora

Python tem um módulo built-in (integrado) para se trabalhar com data e hora chamado datetime.

```python
import datetime

print(dir(datetime))
```

```
['MAXYEAR', 'MINYEAR', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'date', 'datetime', 'datetime_CAPI', 'sys', 'time', 'timedelta', 'timezone', 'tzinfo']
```

```python
import datetime

print(datetime.MAXYEAR)

print(datetime.MINYEAR)

# Retorna a data e hora atual
print(datetime.datetime.now())

print(repr(datetime.datetime.now()))
```

```
9999
1
2023-12-15 18:15:10.190278
datetime.datetime(2023, 12, 15, 18, 15, 10, 190364)
```

replace() → ajusta a data e hora

```python
import datetime

inicio = datetime.datetime.now()

print(inicio)

# Alterar o horario para 16 horas, 0 minutos, 0 segundos e 0 microsegundos.
inicio = inicio.replace(hour=16, minute=0, second=0, microsecond=0)

print(inicio)
```

```
2023-12-15 18:17:55.603940
2023-12-15 16:00:00
```

---

Recebendo dados do usuário e convertendo para data:

```python
import datetime

evento = datetime.datetime(2019, 1, 1, 0)

print(type(evento))

print(type("31/12/2018"))

print(evento)

nascimento = input("Informa sua data de nascimento (dd/mm/yyyy): ")

nascimento = nascimento.split("/")

nascimento = datetime.datetime(int(nascimento[2]), int(nascimento[1]), int(nascimento[0]))

print(nascimento)

print(type(nascimento))
```

```
<class 'datetime.datetime'>
<class 'str'>
2019-01-01 00:00:00
Informa sua data de nascimento (dd/mm/yyyy): 04/07/2001
2001-07-04 00:00:00
<class 'datetime.datetime'>
```

---

Acessa individual dos elementos de data e hora

```python
import datetime

evento = datetime.datetime.now()
print(evento)

print(evento.year)  # Ano
print(evento.month) # Mês
print(evento.day) # Dia
print(evento.hour) # Hora
print(evento.minute) # Minuto
print(evento.second) # Segundo
print(evento.microsecond) # Microsegundo

print(dir(evento))
```

```
2023-12-15 19:00:46.839055
2023
12
15
19
0
46
839055
['__add__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__radd__', '__reduce__', '__reduce_ex__', '__repr__', '__rsub__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', 'astimezone', 'combine', 'ctime', 'date', 'day', 'dst', 'fold', 'fromisocalendar', 'fromisoformat', 'fromordinal', 'fromtimestamp', 'hour', 'isocalendar', 'isoformat', 'isoweekday', 'max', 'microsecond', 'min', 'minute', 'month', 'now', 'replace', 'resolution', 'second', 'strftime', 'strptime', 'time', 'timestamp', 'timetuple', 'timetz', 'today', 'toordinal', 'tzinfo', 'tzname', 'utcfromtimestamp', 'utcnow', 'utcoffset', 'utctimetuple', 'weekday', 'year']
```
"""