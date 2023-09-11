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