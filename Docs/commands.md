## twitter.com/rochacbruno
## rochacbruno@gmail.com


>>> import os
>>> os
<module 'os' (frozen)>
>>> help(os)
>>> os.environ
>>> os.getenv
<function getenv at 0x7fdbea995800>
>>> os.getenv('LANG')
'en_US.UTF-8'

>>> lang = 'pt_BR.utf8'
>>> lang
'pt_BR.utf8'
>>> len(lang)
10
>>> lang[:5]
'pt_BR'
>>> lang.split('.')
['pt_BR', 'utf8']
>>> lang.split('.')[0]
'pt_BR'
>>> lang.split('.')[1]
'utf8'
## Para alterar a variavel de ambiente LANG
export LANG=pt_BR.utf8
❯ ./hello.py
Olá, Mundo!

export LANG=it_IT.utf8
❯ ./hello.py            
Ciao, Mondo!

export LANG=us_EN.utf8tenv
❯ ./hello.py            bin()
Hello, World!

---

## Expressão/ Expression
Instrução que espera um valor de retorna
1+1     -> 2
8 > 10  -> False
8 < 10  -> True

## Declaração/ Statement
Istrução que prepara o interpretador para uma determinada tarefa
mas não retorna valor
if, else    def     for     while   pass

## Atribuição / Assignment
Instrução que pega o retorno de uma expressão e processa o seu
valor com intuito de armazenar
soma = 40 + 2 
soma += 3
soma -= 3

---

# Tipos de dados

>>> num = 65
>>> num
65
>>> id(num)
94280152827112
>>> bin(num)
'0b1000001'
>>> type(num)
<class 'int'>

>>> letra = 'A'
>>> letra
'A'
>>> id(letra)
94280152869312
>>> type(letra)
<class 'str'>

>>> dir(int)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_count', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']


>>> num == 65
True
>>> numero == 0
False
>>> num.__eq__(65)
True
>>> num > 100
False
>>> num.__gt__(100)
False

In [6]: nome = 'Jorge'

In [7]: bytes(nome, "utf-8")
Out[7]: b'Jorge'

In [8]: list(bytes(nome, 'utf-8'))
Out[8]: [74, 111, 114, 103, 101]

In [9]: chr(74)
Out[9]: 'J'

In [10]: chr(111)
Out[10]: 'o'

In [11]: chr(114)
Out[11]: 'r'

In [12]: nome.__getitem__(2)
Out[12]: 'r'

In [15]: nome[:3]
Out[15]: 'Jor'

In [17]: nome
Out[17]: 'Jorge'

In [18]: nome.upper()
Out[18]: 'JORGE'

In [19]: nome.lower()
Out[19]: 'jorge'

In [20]: nome.capitalize()
Out[20]: 'Jorge'

In [21]: nome.title()
Out[21]: 'Jorge'

In [22]: nome.split()
Out[22]: ['Jorge']

In [23]: sorted('Jorge')
Out[23]: ['J', 'e', 'g', 'o', 'r']

In [25]: list(reversed('Jorge'))
Out[25]: ['e', 'g', 'r', 'o', 'J']

---

![PYFORMAT] (https://pyformat.info/mat.info/)

python or ipython -> help('FROMATTING')

## Concatenação %S
-> usar com logging (devido ser uma lib antiga

## str.format {}
-> usar com mensagens longas, e-,mail

## f-strings
-> usar com o restante, msg, print, error

## UTF-8

---

# Estrutura composta de dados -> Tupla

In [3]: 'Plautz', 1, True, None , 4,8
Out[3]: ('Plautz', 1, True, None, 4, 8)

In [4]: dados = 'Plautz', 1, True, None , 4,8

In [5]: type(dados)
Out[5]: tuple

In [6]: dir(tuple)
Out[6]: 
['__add__',
 '__class__',
 '__class_getitem__',
 '__contains__',
 '__delattr__',
 '__dir__',
 '__doc__',
 '__eq__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__getitem__',
 '__getnewargs__',
 '__getstate__',
 '__gt__',
 '__hash__',
 '__init__',
 '__init_subclass__',
 '__iter__',
 '__le__',
 '__len__',
 '__lt__',
 '__mul__',
 '__ne__',
 '__new__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__rmul__',
 '__setattr__',
 '__sizeof__',
 '__str__',
 '__subclasshook__',
 'count',
 'index']

 In [11]: dados.count('Plautz')
Out[11]: 1

In [12]: dados.count(False)
Out[12]: 0

In [13]: dados[-1] -> com  indice negativa os elementos são verificados 
Out[13]: 8

In [14]: dados
Out[14]: ('Plautz', 1, True, None, 4, 8)

In [15]: 'en_US.utf8'[:5]  -> slicing
Out[15]: 'en_US'

In [18]: for info in dados:
    ...:     print('-->', info)
    ...: 
--> Plautz
--> 1
--> True
--> None
--> 4
--> 8

## tuplas são imutável

## desempacotar uma tupla -> unpacking
In [19]: pontos = 1,2,15

In [20]: x, y, z = pontos

In [21]: x
Out[21]: 1

In [22]: y
Out[22]: 2

In [23]: z
Out[23]: 15


In [24]: x, *_ = pontos

In [25]: x
Out[25]: 1

In [26]: _   -> _ significa que os demais dados serão descartados
Out[26]: [2, 15]


In [27]: head, *body, tail = pontos

In [28]: head
Out[28]: 1

In [29]: tail
Out[29]: 15

In [30]: body
Out[30]: [2]

---

# LISTA -> os elementos são mutaveis

## o comando pop remove o utima elemento da lista
In [2]: res=[]
In [3]: for num in range(1,9):
   ...:     res.append(num * 4)
   ...: 
In [4]: res
Out[4]: [4, 8, 12, 16, 20, 24, 28, 32]

In [5]: res.__contains__
Out[5]: <method-wrapper '__contains__' of list object at 0x7fa15b52af80>

In [6]: 15 in res
Out[6]: False

---
# SET para criar um conjunto usar a sintase abaixo
In [9]: c1 = set()

In [10]: type(c1)
Out[10]: set

## União entre dois conjuntos
In [18]: conj_a = [1,2,3,4,5]

In [19]: conj_b = [4,5,6,7,8]

In [20]: set(conj_a) | set(conj_b)
Out[20]: {1, 2, 3, 4, 5, 6, 7, 8}

In [21]: set(conj_a).union(set(conj_b))
Out[21]: {1, 2, 3, 4, 5, 6, 7, 8}


In [22]: conj_a = set([1,2,3,4,5])
In [23]: conj_b = set([4,5,6,7,8])

In [24]: conj_a | conj_b
Out[24]: {1, 2, 3, 4, 5, 6, 7, 8}

## Intercessão entre dois conjuntos
In [25]: conj_a & conj_b
Out[25]: {4, 5}
In [26]: conj_a.intersection(conj_b)
Out[26]: {4, 5}

## Diferença entre dois conjuntos
In [27]: conj_a - conj_b
Out[27]: {1, 2, 3}

In [28]: conj_a.difference(conj_b)
Out[28]: {1, 2, 3}

## Diferença simetrica entre dois conjuntos
In [30]: conj_a.symmetric_difference(conj_b)
Out[30]: {1, 2, 3, 6, 7, 8}

In [31]: conj_a ^ conj_b
Out[31]: {1, 2, 3, 6, 7, 8}

## Set implementa um hash table
-> em listas a busca é O(n) , pois tem que passar em cada elemento
-> em set a busca é O(1) -> constante pois o set tem o hash table

---

# Dicionário

-> a busca em um dicionario é O(1) -> constante
-> quando a busca é na chave é rapido.
-> mas quando a busca é no valor a busca não é rapida.
-> precisa usar um arvore invertida para buscar o valor

In [34]: cliente = {'nome': 'Jorge', 'idade': 64}

In [35]: cliente
Out[35]: {'nome': 'Jorge', 'idade': 64}

In [36]: len(cliente)
Out[36]: 2

In [37]: cliente.keys()
Out[37]: dict_keys(['nome', 'idade'])

In [38]: cliente.values()
Out[38]: dict_values(['Jorge', 64])

In [39]: cliente.items()
Out[39]: dict_items([('nome', 'Jorge'), ('idade', 64)])

In [41]: extra_info = {'cidade': 'Curitiba'}

In [42]: cliente.update(extra_info)

In [43]: cliente
Out[43]: {'nome': 'Jorge', 'idade': 64, 'cidade': 'Curitiba'}

In [45]: extra_info
Out[45]: {'cidade': 'Curitiba'}

In [46]: {**extra_info, **cliente}
Out[46]: {'cidade': 'Curitiba', 'nome': 'Jorge', 'idade': 64}

In [47]: final = {**cliente, **extra_info}
In [48]: final
Out[48]: {'nome': 'Jorge', 'idade': 64, 'cidade': 'Curitiba'}

In [49]: for chave in cliente:
    ...:     print(chave, '->', cliente[chave])
    ...: 
nome -> Jorge
idade -> 64
cidade -> Curitiba


In [50]: for chave, valor  in cliente.items():
    ...:     print(chave, '->', cliente[chave])
    ...: 
nome -> Jorge
idade -> 64
cidade -> Curitiba
