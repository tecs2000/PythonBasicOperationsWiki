from functools import reduce
from operator import add

valores = [30, 10, 25, 70, 100, 94]

# Nao modifica a lista:
print(sorted(valores))
print(min(valores))
print(max(valores))
print(sum(valores))
print(reduce(add, valores))
print(list(reversed(valores)))

print(valores)

# Modifica a lista:
# valores.sort()
# valores.reverse()

# print(valores)
