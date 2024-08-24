"""
O que são decoradores?

Decoradores (Decorators)

O que são decorators?

- Decorators são funções;
- Decorators envolvem outras funções e aprimoram seus comportamento;
- Decorators também são exemplos de Higher Order Functions
- Decoratos tem uma sintaxe própria, usando “@” (Syntact Sugar / Açúcar Sintático)

Decorators como funções (Sintaxe não recomendada / Sem Açúcar Sintático)

```python
def seja_educado(funcao):
    def sendo():
        print("Foi um prazer conhecer você!")
        funcao()
        print("Tenha um ótimo dia!")
    return sendo

def saudacao():
    print("Seja bem-vindo(a) à Geek University")

# Testando 1

# saudacao()  # Seja bem-vindo(a) à Geek University

teste = seja_educado(saudacao)

teste()
```

```
Foi um prazer conhecer você!
Seja bem-vindo(a) à Geek University
Tenha um ótimo dia!
```

```python
def seja_educado(funcao):
    def sendo():
        print("Foi um prazer conhecer você!")
        funcao()
        print("Tenha um ótimo dia!")
    return sendo

def saudacao():
    print("Seja bem-vindo(a) à Geek University")

# Testando 2

def raiva():
    print("EU TE ODEIO!")

raiva_educada = seja_educado(raiva)

raiva_educada()v
```

```
Foi um prazer conhecer você!
EU TE ODEIO!
Tenha um ótimo dia!
```

---

Decorators com Syntax Sugar (Açúcar Sintático)

```python
def seja_educado_mesmo(funcao):
    def sendo_mesmo():
        print("Foi um prazer em conhecer você!")
        funcao()
        print("Tenha um excelente dia!")
    return sendo_mesmo

@seja_educado_mesmo
def apresentando():
    print("Meu nome é Pedro")

# Testando

apresentando()

@seja_educado_mesmo
def dormir():
    print("Quero dormir...")

dormir()
```

```
Foi um prazer em conhecer você!
Meu nome é Pedro
Tenha um excelente dia!
Foi um prazer em conhecer você!
Quero dormir...
Tenha um excelente dia!
```

---

Um exemplo não funcional de um site web com Decorators.

No site Web possui os seguintes menus: Home, Serviços, Produtos e Administrativo.

```
www.exemplo.com.br/home
www.exemplo.com.br/servicos
www.exemplo.com.br/produtos
www.exemplo.com.br/admin
```

Obs: Não é um código funcional (Que funcione) é apenas um exemplo

```python
def checa_login():
    if not request.usuario:
        credits("www.exemplo.com.br")

def home(request):
    return "Pode acessar home"

def servicos(request):
    return "Pode acessar servicos"

def produtos(request):
    return "Pode acessar produtos"

@checa_login
def admin(request):
    return "pode acessar admin"
```
"""