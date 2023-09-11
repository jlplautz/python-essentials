email_tmpl = """Ola, %(nome)s

Tem interesse em comprar %(produto)s?

Este produto é ótimo para resolver %(texto)s

Clique agora em %(link)s

Apena %(quantidade)d disponives!

Preço promocional %(preco).2f
"""

clientes = ['Maria', 'Joao', 'Jorge']

for cliente in clientes:
    print(
        email_tmpl
        % {
            'nome': cliente,
            'produto': 'caneta',
            'texto': 'Execelente e elegante escrita',
            'link': 'https://canetaslegais.com',
            'quantidade': 1,
            'preco': 50.5,
        }
    )
