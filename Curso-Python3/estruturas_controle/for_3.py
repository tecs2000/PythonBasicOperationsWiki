produto = {'nome': 'Caneta Chic', 'preco': 14.99,
           'importada': True, 'estoque': 793}

for chave in produto:  # produto.keys()
    print(chave)

for valor in produto.values():
    print(valor)

for chave, valor in produto.items():
    print(chave, '=', valor)

# As variaveis criadas no laco permanecem apos o seu fim, ou seja, n sao locais
# print(chave, valor)
