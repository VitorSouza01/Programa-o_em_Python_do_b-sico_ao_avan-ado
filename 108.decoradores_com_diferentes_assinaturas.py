"""
Decoradores com diferentes assinaturas

```python
# Relembrando

def gritar(funcao):
    def aumentar(nome):
        return funcao(nome).upper()
    return aumentar

@gritar
def saudacao(nome):
    return f"Olá, eu sou o/a {nome}"

@gritar
def ordernar(principal, acompanhamento):
    return f"Olá, eu gostaria de {principal}, acompanhado de {acompanhamento}, por favor"

# Testando

print(saudacao("Angelina"))

print(ordernar("Picanha", "Batata Frita"))
```

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f6246be9-a051-4551-9083-ac2c2300eddd/69865010-1246-4864-bea9-f1b64db09f24/Untitled.png)

Para resolver, utilizaremos um padrão de projeto chamado Decorator Pattern.

A assinatura de uma função é representada pelo seu retorno, nome e parâmetro de entrada.

```python
# Refatorando com a Decorator Pattern

def gritar(funcao):
    def aumentar(*args, **kwargs):
        return funcao(*args, **kwargs).upper()
    return aumentar

@gritar
def saudacao(nome):
    return f"Olá, eu sou o/a {nome}"

@gritar
def ordenar(principal, acompanhamento):
    return f"Olá, eu gostaria de {principal} acompanhada de {acompanhamento}, por favor."

print(saudacao("Felicity"))

print(ordenar("Picanha", "Batata Frita"))

@gritar
def lol():
    return "lol"

print(lol())

# Obs: Vale lembrar que podemos utilizar parâmetros nomeados

print(ordenar(acompanhamento="Batata Frita", principal="Picanha"))
```

```
OLÁ, EU SOU O/A FELICITY
OLÁ, EU GOSTARIA DE PICANHA ACOMPANHADA DE BATATA FRITA, POR FAVOR.
LOL
OLÁ, EU GOSTARIA DE PICANHA ACOMPANHADA DE BATATA FRITA, POR FAVOR.
```

Decorator com Argumentos

```python
def verificar_primeiro_argumento(valor):
    def interna(funcao):
        def outra(*args, **kwargs):
            if args and args[0] != valor:
                return f"Valor incorretor! Primeiro argumento precisa ser {valor}"
            return funcao(*args, **kwargs)
        return outra
    return interna

@verificar_primeiro_argumento("Pizza")
def comida_favorita(*args):
    print(args)

@verificar_primeiro_argumento(10)
def soma_dez(num1, num2):
    return num1 + num2

# Testando

print(soma_dez(10, 12))  # 22

print(soma_dez(1, 21))  # 22

print(comida_favorita("Pizza", "Churrasco"))

print(comida_favorita("Sanduiche", "Pizza"))
```

```
22
Valor incorretor! Primeiro argumento precisa ser 10
('Pizza', 'Churrasco')
None
Valor incorretor! Primeiro argumento precisa ser Pizza
```
"""