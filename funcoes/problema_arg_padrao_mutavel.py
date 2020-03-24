def fibonacci(sequencia=[0, 1]):
    # Uso de mutaveis com valor default (armadilha)
    sequencia.append(sequencia[-1]+sequencia[-2])
    return sequencia


if __name__ == '__main__':
    # Mexer no param. default mutavel, altera diretamente seu valor
    # na memoria, ou seja seq = [0,1] apenas na 1a chamada

    inicio = fibonacci()
    print(inicio, id(inicio))

    print(fibonacci())

    restart = fibonacci()
    print(restart, id(restart))
    assert restart == [0, 1, 1]
