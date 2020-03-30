# from generators_v1 import cores_arco_iris


def sequence():
    num = 0
    while True:
        num += 1
        yield num


if __name__ == '__main__':
    # for cor in cores_arco_iris():
    #     print(cor)

    # print('Fim')

    seq = sequence()
    print(next(seq))
    print(next(seq))
    print(next(seq))
    print(next(seq))
    print(next(seq))
    print(next(seq))
    print(next(seq))
    print(next(seq))
