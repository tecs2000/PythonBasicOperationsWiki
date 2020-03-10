def tipo_dia(dia):
    dias = {
        1: 'Fim da semana',
        2: 'Dia da semana',
        3: 'Dia da semana',
        4: 'Dia da semana',
        5: 'Dia da semana',
        6: 'Dia da semana',
        7: 'Fim da semana',
    }
    return dias.get(dia, "** invalido **")


if __name__ == '__main__':
    for dia in range(9):
        print(f'{dia} : {tipo_dia(dia)}')
