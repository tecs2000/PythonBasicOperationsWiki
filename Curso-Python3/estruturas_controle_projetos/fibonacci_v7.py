def fibonacci(quantidade):
    resultado = [0, 1]

    for i in range(2, quantidade):
        resultado.append(sum(resultado[-2:]))

    return resultado


if __name__ == '__main__':
    # Listas os 20 primeiros numeros da sequencia
    for fib in fibonacci(10):
        print(fib)
