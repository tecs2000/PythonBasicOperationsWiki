# Lendo arquivo por streaming

arquivo = open('pessoas.csv')
for registro in arquivo:  # Le linha por linha c o arquivo aberto
    print('Nome: {}, Idade: {}'.format(*registro.strip().split(',')))
arquivo.close()

# .strip() retira elementos repetidos nas laterais
# por default, tira espacos em branco
