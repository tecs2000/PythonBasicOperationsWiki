def mapear(funcao, lista):
    for elemento in lista:
        yield funcao(elemento)

    # new_list = []
    # for elemento in lista:
    #     new_list.append(funcao(elemento))
    # return new_list


if __name__ == '__main__':
    print(list(mapear(lambda x: x**2, [2, 3, 4])))
