with open('pessoas.csv') as arquivo:  # usa o recurso e fecha automaticamente!
    for registro in arquivo:  # Le linha por linha c o arquivo aberto
        print('Nome: {}, Idade: {}'.format(*registro.strip().split(',')))

if arquivo.closed:
    print('Arquivo ja foi fechado!')
