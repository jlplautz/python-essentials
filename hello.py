#!/usr/bin/env python3

"""Hello World Multi-Language
Depend on the linguage configured into the environment the program is going to
replay with the language
You can see by the follow command:
    ❯ env | grep LANG
    LANG=en_US.UTF-8
    LANGUAGE=en_US:en
    GDM_LANG=en_US

How to use:
    Keep LANG variable properly configured.py
    Ex: export LANG=pt_BT or en_US

How to execute:

    python3 hello.py or 
    ./hello.py or
    LANG=it_IT python hello.py -> to specify the current language

"""

# metadados especiais para o python
__version__ = '0.0.1'
__author__ = 'Jorge Plautz'
__license__ = 'Unlicense'

# to import lib os to modify the environment
import os

# function (os.getenv_ verify the content of environment varible 
# the first five caracteres show 'LANG'
current_language = os.getenv('LANG', 'en_US')[:5]

# variable current_language is writing using format -> snake case
# variable Currentlanguage is writing using format -> Pascal Case


msg = "Hello, World!"

if current_language == "pt_BR":
    msg = "Olá, Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"
elif current_language == "es_SP":
    msg = "Hola, Mundo!"
elif current_language == "fr_FR":
    msg = "Bonjour, Monde!"

print(msg)
