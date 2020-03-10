def fibonacci(limite):
    penultimo = 1
    ultimo = 0
    print(f'{ultimo},{penultimo}', end=',')

    while penultimo < limite:
        ultimo, penultimo = penultimo, penultimo + ultimo
        print(penultimo, end=',')


if __name__ == '__main__':
    fibonacci(1000)
