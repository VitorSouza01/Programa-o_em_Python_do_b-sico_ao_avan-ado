"""
Escopo de variáveis

/                       / -> Escopo com espaço dentro

Em Ciência da Computação escopo é um contexto delimitante aos quais valores e expressões
estão associados. Linguagens de programação têm diversos tipos de escopos. O tipo de escopo vai
determinar quais tipos de entidades este pode conter e como estas são afetadas, em outras palavras, a sua semântica.


Dois casos de escopo:

1 - Variáveis globais;
    - Variáveis globais são reconhecidas, ou seja, seu escopo compreende, todo o programa.

2 - Variáveis locais;
    - Variáveis locais são reconhecidos apenas no bloco onde foram declaradas, ou seja, seu escopo
    está limitado ao bloco onde foi declarada.


Para declarar variáveis em Python fazemos:
nome_da_variavel = valor_da_variavel

Python é uma linguagem dde tipagem dinâmica. Isso significa que ao declarar
uma variável, nós não colocamos o tipo de dado dela.
Esse tipo é inferido ao atribuímos o valor à mesma.

--Em outras linguagens de proframação ao declarar uma variável
Exemplo em C:
    int numero = 42

Exempplo em Java:
    int numero = 42

Exemplo em Python = 42
    numero = 42


-- Reatribuição, em Python possivel ja nas linguagens Java e C não


numero = 42         -> *Exemplo de variável global
print(numero)
print(type(numero))

numero = 'Geek'
print(numero)
print(type(numero))

"""

numero = 42
# novo = 0      -> A variavel 'novo' está declarada localmente dentro do bloco do if. Portanto, é local.
if numero > 10:
    novo = numero + 10
    print(novo)
