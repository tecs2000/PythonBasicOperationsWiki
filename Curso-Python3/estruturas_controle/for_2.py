palavra = 'paralelepipedo'

for letra in palavra:
    print(letra, end=' ')
print('Fim')

aprovados = ['Rafaela', 'Pedro', 'Renato', 'Maria']

for nome in aprovados:
    print(nome)

for posicao, nome in enumerate(aprovados):
    print(f'{posicao + 1})', nome)

for letra in set('muito legal'):
    print(letra)
