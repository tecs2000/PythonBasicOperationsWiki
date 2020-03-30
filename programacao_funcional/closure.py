def multiplicar(x):
    def calcular(y):
        return x*y
    return calcular


if __name__ == '__main__':
    dobro = multiplicar(2)  # parametro mais externo - x
    triplo = multiplicar(3)
    print(dobro)
    print(triplo)
    print(f'O triplo de 3 e {triplo(3)}')
    print(f'O dobro de 7 e {dobro(7)}')
