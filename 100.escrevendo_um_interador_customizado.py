"""
Escrevendo um Interador Customizado

```python
class Contador:

    # Método Construtor
    def __init__(self, menor, maior):
        self.menor = menor
        self.maior = maior

    # Declaração do iter
    def __iter__(self):
        return self

    # Declaração do next
    def __next__(self):
        if self.menor < self.maior:
            numero = self.menor
            self.menor = self.menor + 1
        raise StopIteration

for n in Contador(1, 61):
    print(n)

# Replicação do range
print("\n")
for n in range(1, 61):
    print(n)
```

```
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
```
"""