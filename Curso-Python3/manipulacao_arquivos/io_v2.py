# Lendo arquivo por streaming

arquivo = open('pessoas.csv')
for registro in arquivo:  # Le linha por linha c o arquivo aberto
    print('Nome: {}, Idade: {}'.format(*registro.split(',')), end='')
arquivo.close()
