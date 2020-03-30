pessoas = [
    {'nome': 'Pedro', 'idade': 11},
    {'nome': 'Mariana', 'idade': 18},
    {'nome': 'Arthur', 'idade': 26},
    {'nome': 'Rebeca', 'idade': 6},
    {'nome': 'Tiago', 'idade': 19},
    {'nome': 'Gabriela', 'idade': 17}
]

# No caso do filter, a funcao lambda sempre vai retornar True or False

menores = filter(lambda p: p['idade'] < 18, pessoas)
print(list(menores))

nomes_grandes = list(filter(lambda p: len(p['nome']) > 6, pessoas))
print(nomes_grandes)
