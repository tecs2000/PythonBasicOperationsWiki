def fibonacci():
    penultimo = 1
    ultimo = 0
    print(f'{ultimo},{penultimo}', end=',')

    while True:
        proximo = penultimo + ultimo
        print(proximo, end=',')
        ultimo = penultimo
        penultimo = proximo


if __name__ == '__main__':
    fibonacci()
