compras = (
    {'quantidade': 2, 'preco': 10},
    {'quantidade': 3, 'preco': 20},
    {'quantidade': 5, 'preco': 14}
)


def cal_preco_total(compra):
    return compra['quantidade'] * compra['preco']


totais = tuple(map(cal_preco_total, compras))

print('Precos totais:', totais)
print('Totais gerais:', sum(totais))
