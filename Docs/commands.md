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
❯ ./hello.py            
Hello, World!

