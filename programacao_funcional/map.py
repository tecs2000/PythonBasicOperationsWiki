lista_1 = [1, 2, 3]
dobro = list(map(lambda x: x*2, lista_1))
print(dobro)

lista_2 = [
    {'nome': 'Joao', 'idade': 31},
    {'nome': 'Maria', 'idade': 37},
    {'nome': 'Jose', 'idade': 26}
]
so_nomes = map(lambda p: p['nome'], lista_2)
print(list(so_nomes))

so_idades = map(lambda p: p['idade'], lista_2)
print(sum(so_idades))

frases = map(lambda x: f'{x["nome"]} tem {x["idade"]} anos.', lista_2)
print(list(frases))
