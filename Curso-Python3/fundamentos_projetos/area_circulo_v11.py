#!/usr/lib/python3.6
from math import pi
import sys    # permite pegar argumento do console
import errno  # permite colocar excessoes


def circulo(raio):
    return pi * float(raio)**2


def help():
    return (f"""\
Eh necessario informar o raio do circulo.
Sintaxe: {sys.argv[0]} <raio>""")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(help())
        sys.exit(errno.EPERM)   # breaka a execucao

    if not sys.argv[1].isnumeric():
        print(help())
        print('O raio deve ser um valor numerico')
        sys.exit(errno.EINVAL)  # arg invalido

    raio = sys.argv[1]
    area = circulo(raio)
    print('Area do circulo:', area)
