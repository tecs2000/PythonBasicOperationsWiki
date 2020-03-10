def fibonacci(limite):
    penultimo = 1
    ultimo = 0
    print(f'{ultimo},{penultimo}', end=',')

    while ultimo < limite:
        proximo = penultimo + ultimo
        print(proximo, end=',')
        ultimo = penultimo
        penultimo = proximo


if __name__ == '__main__':
    fibonacci(1000)
