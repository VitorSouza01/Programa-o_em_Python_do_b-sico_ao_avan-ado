"""
Lendo arquivos CSV

CSV - Comma Separeted Values - Valores Separados por Vírgula

Separador por vírgula:

1, 2, 3, 4, 5, 6

“gekk”, “unversity”, “python”, “ciencia”, “dados”

---

Separador por ponto e vírgula:

1; 2; 3, 4; 5; 6

“gekk”; “unversity”; “python”; “ciencia”; “dados”

---

Site para testar dados:

https://dados.gov.br/dateset

---

Possível de se trabalhar, mas não é o ideal (trabalhoso):

```python
with open("lutadores.csv") as arquivo:
  dados = arquivo.read()
  #print(type(dados))
  dados = dados.split(","[2:])
  print(dados)
```

---

A linguagem Python possui duas formas diferentes para ler dados em arquivos CSV;

- reader → Permite que iteremos sobre as linhas do arquivo CSV como listas.
- DictReader → Permite que iteremos sobre as linhas do arquivo CSV como listas.

Obs: Os códigos usando a biblioteca csv atualmente não está funcionando!

```python
from csv import reader

with open("lutadores.csv") as arquivo:
  leitor_csv = reader(arquivo)
  next(leitor_csv)  # Pular o cabeçalho
  for linha in leitor_csv:
    # Cada linha é uma lista
    print(f"{linha[0]} nasceu no(a)(s) {linha[1]} e mede {linha[2]} centimetros")
```

![WhatsApp Image 2023-12-12 at 17.04.12.jpeg](https://prod-files-secure.s3.us-west-2.amazonaws.com/50f6c3e8-cd39-40a2-a8ee-7ed9bb20ee47/acaed14e-1387-435b-97b1-4cb2c96f0f51/WhatsApp_Image_2023-12-12_at_17.04.12.jpeg)
"""