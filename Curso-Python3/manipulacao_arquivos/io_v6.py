with open('pessoas.csv') as arquivo:  # usa o recurso e fecha automaticamente!
    with open('pessoas.txt', 'w') as saida:
        for registro in arquivo:  # Le linha por linha c o arquivo aberto
            pessoa = registro.strip().split(',')
            print('Nome: {}, Idade: {}'.format(*pessoa), file=saida)

if arquivo.closed:
    print('Arquivo ja foi fechado!')

if saida.closed:
    print('Arquivo de saida ja foi fechado!')
