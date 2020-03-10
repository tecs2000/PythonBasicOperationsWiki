PALAVRAS_PROIBIDAS = {'futebol', 'religiao', 'politica'}
textos = [
    'Joao gosta de futebol e politica',
    'A partida foi divertida'
]

for frase in textos:
    intersecao = PALAVRAS_PROIBIDAS.intersection(set(frase.lower().split()))

    if intersecao:  # conjunto vazio == false
        print('Texto possui palavras proibidas:', intersecao)

    else:
        print('Texto autorizado:', frase)
