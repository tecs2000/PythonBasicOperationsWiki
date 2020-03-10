try:
    arquivo = open('pessoas.csv')

    for registro in arquivo:  # Le linha por linha c o arquivo aberto
        print('Nome: {}, Idade: {}'.format(*registro.strip().split(',')))

finally:
    print('finally!')
    arquivo.close()

if arquivo.closed:
    print('Arquivo ja foi fechado!')
