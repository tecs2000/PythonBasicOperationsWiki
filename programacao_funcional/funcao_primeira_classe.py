def dobro(x):
    return x*2


def quadrado(x):
    return x**2


if __name__ == '__main__':
    d = dobro
    print(d(5))

    q = quadrado
    print(q(5))
    print()

    # Retorna alternadamente o dobro ou o quadrado nos numeros de 1 a 10
    funcs = [dobro, quadrado] * 5
    for func, numero in zip(funcs, range(1, 11)):
        # Resultado do zip: (dobro, 1), (quadrado, 2), (dobro, 3),
        # (quadrado, 4), (dobro, 5), (quadrado, 6), (dobro, 7),
        # (quadrado, 8), (dobro, 9), (quadrado, 10)
        print(f'O {func.__name__} de {numero} eh {func(numero)}')
