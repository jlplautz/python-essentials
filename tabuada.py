#!/usr/bin/env python
"""
Imprime a tbuada do 1 ao 10.

---Tabuada do 1---
    1 x 1 = 1
    2 x 1 = 2
    3 x 1 = 3
...
##################
---Tabuada do 2---
    1 x 2 = 3
    2 x 2 = 4
    3 x 2 = 6
...
##################
"""
__version__ = "0.1.1"
__authon__ = 'Plautz'


# base = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Iterable (percorriveis)
numeros = list(range(1, 11))

for n1 in numeros:
    bloco = ''
    for n2 in numeros:
        resultado = n1 * n2
        bloco = f'{n1} x {n2} = {resultado}\n'

        print(template.format(bloco=bloco))
