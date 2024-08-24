"""
Trabalhando com deltas de data e hora

data_inicial = dd/mm/yyyy 12:55:34.99939329

data_final = dd/mm/yyyy 13:54:23.0948484

delta = data_final - data_inicial

```python
import datetime

# Temos a data de hoje
data_hoje = datetime.datetime.now()

# Data para ocorrer um determinado evento futuro
aniversario = datetime.datetime(2025, 3, 3, 0)

# Calculando o delta
tempo_para_evento = aniversario - data_hoje

print(type(tempo_para_evento))

print(repr(tempo_para_evento))

print(tempo_para_evento)

print(f"Faltam {tempo_para_evento.days} dias, {tempo_para_evento.seconds // 60 // 60} horas...")
```

```
<class 'datetime.timedelta'>
datetime.timedelta(days=443, seconds=16397, microseconds=986967)
443 days, 4:33:17.986967
Faltam 443 dias, 4 horas...
```

```python
import datetime

data_da_compra = datetime.datetime.now()

print(data_da_compra)

regra_boleto = datetime.timedelta(days=3)

print(regra_boleto)

vencimento_boleto = data_da_compra + regra_boleto

print(vencimento_boleto)
```

```
2023-12-15 19:32:44.316943
3 days, 0:00:00
2023-12-18 19:32:44.316943
```
"""