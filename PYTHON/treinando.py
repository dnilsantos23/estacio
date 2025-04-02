import os
#criando um arquivo de texto em python
arquivo1 = open('atributos.txt', 'r+')
arquivo1.write('Escrevendo em arquivos de texto com python!\n')
arquivo1.write('testando a escrita em arquivos de texto com python!\n')

if arquivo1.closed: # Verifica se o arquivo está fechado
    print("O arquivo está fechado.")
else:
    print("O arquivo está aberto.")
    arquivo1.close() # Fecha o arquivo se estiver aberto

with open('atributos.txt', 'r+') as arquivo1:
    # Lê o conteúdo do arquivo e substitui 'testando' por 'testando a leitura'
    print(arquivo1.read().replace('testando a escrita', 'testando a leitura e a escrita')) 
print(arquivo1.name, type(arquivo1.name)) # Imprime o nome do arquivo e seu tipo
print(arquivo1.mode) # Imprime o modo de abertura do arquivo
print(arquivo1.closed) # Verifica se o arquivo está fechado

arquivo2 = open('treinando-em-arquivos-com-python.txt')