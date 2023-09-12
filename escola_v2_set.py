#!/usr/bim/env python3

''' Exibe relatório de criancas por atividade

Imprimir a lista de crianças agrupadas por sala que
frequentas cada uma das atividades.
'''
__version__ = '0.1.1'

# dados
sala1 = ['Erik', 'Maia', 'Gustavo', 'Manuel', 'Sofia', 'Joana']
sala2 = ['Joao', 'Antonio', 'Carlos', 'Maria', 'Sofia', 'Isolda']

aula_ingles = ['Erik', 'Maia', 'Joana', 'Carlos', 'Antonio']
aula_musica = ['Erik', 'Carlos', 'Maria']
aula_danca = ['Gustavo', 'Sofia', 'Joana', 'Antonio']

atividades = [
    ('Ingles', aula_ingles),
    ('Musica', aula_musica),
    ('Dança', aula_danca),
]

# Listar alunos em cada atividade por sala

for nome_atividade, atividade in atividades:

    print(f'Alunos da atividade {nome_atividade}\n')
    print('-' * 43)

    atividade_sala1 = []
    atividade_sala2 = []

    # sala1 que tem interseção com atividade
    atividade_sala1 = set(sala1) & set(atividade)
    atividade_sala2 = set(sala2) & set(atividade)

    print(f' {nome_atividade} sala1 ', atividade_sala1)
    print(f' {nome_atividade} sala2 ', atividade_sala2)
    print('#' * 43)
