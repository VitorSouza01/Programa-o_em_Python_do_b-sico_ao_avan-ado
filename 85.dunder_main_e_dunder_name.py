"""
Dunder Main e Dunder Name

Dunder → Doble Under (Dobro Underline)

Dunder Name → __name__

Dunder Main → __main__

Em Python, são utilizados dunder para criar funções, atributos, propriedades e etc utilizando Double Under para não
gerar conflito com os nomes desses elementos na programação.

Main → Significa principal.

Na linguagem C, temos um programa da seguinte forma:

```c
int main(){
	return 0;
}
```

Na linguagem Java, temos um programa da seguinte forma:

```java
public static void main(String[] args){
}
```

Em Python se executamos um módulo Python diretamente na linha de comando, internamente o Python atribuirá à variavel __name__ o valor __main__ indicando que este módulo é o módulo de execução principal.

```python
from funcoes_com_parametro import soma_impares
print(soma_impares([1, 2, 3, 4, 5, 6]))
```

```python
9
```
"""

import primeiro
import segundo