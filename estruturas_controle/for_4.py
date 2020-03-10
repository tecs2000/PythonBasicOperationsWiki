# for i in range(1, 11):
#     print(i)
# else:
#     print('fim!')

# Desafio: Funcao sortear_dado 6 numeros entre 1 e 6
# For com range 1 a 6
# Se for impar, continue
# Se o numero for par e for igual ao valor sorteado
# pela funcao dado, imprimir 'ACERTOU' e depois chamar o break;
# Se nao acertar, chama o else... print('Nao acertou o numero!')

from random import randint


def sortear_dado():
    return randint(1, 6)


if __name__ == '__main__':

    number = sortear_dado()

    for i in range(1, 7):
        if i % 2 == 1:
            continue
        elif i == number:
            print('Acertou!', i)
            break
    else:
        print("Nao acertou o numero!")
