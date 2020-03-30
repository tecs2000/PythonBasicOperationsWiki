from functools import reduce

pessoas = [
    {'nome': 'Pedro', 'idade': 11},
    {'nome': 'Mariana', 'idade': 18},
    {'nome': 'Arthur', 'idade': 26},
    {'nome': 'Rebeca', 'idade': 6},
    {'nome': 'Tiago', 'idade': 19},
    {'nome': 'Gabriela', 'idade': 17}
]

so_idades = map(lambda p: p['idade'], pessoas)
# print(list(so_idades))

menores = filter(lambda idade: idade < 18, so_idades)
# print(list(menores))

# No reduce, o terceiro parametro indica o valor
# inicial do acumulador que vai percorrer a lista
soma_idades = reduce(lambda somador, idade: somador + idade, menores, 0)
print(soma_idades)
