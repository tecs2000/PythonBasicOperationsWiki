def cores_arco_iris():
    # Quando uma funcao que esta executando encontra o yield,
    # ela suspende a execucao naquele ponto, salva seu contexto
    # e retorna para o chamador, juntamente c qualquer valor na list_expressao;
    # quando o chamador invoca o metodo next() no objeto,
    # a execucao da funcao continua ate outro yield ou return ser encontrado,
    # ou quando o fim da funcao e atingido.

    yield 'vermelho'
    yield 'laranja'
    yield 'amarelo'
    yield 'verde'
    yield 'azul'
    yield 'indigo'
    yield 'violeta'


if __name__ == '__main__':
    generator = cores_arco_iris()
    print(type(generator))

    while True:
        print(next(generator))
