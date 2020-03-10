#!/usr/lib/python3.6
from math import pi
import sys


def circulo(raio):
    return pi * float(raio)**2


if __name__ == '__main__':
    raio = sys.argv[1]  # permite pegar argumento do console
    area = circulo(raio)
    print('Area do circulo:', area)
    print(sys.path)
