import os

arquivo = open('atributos.txt')
print('Modo do arquivo: ', arquivo.mode)
print('O arquivo está fechado? ', arquivo.closed)
#arquivo.close()

# Verifica se o arquivo está fechado após o fechamento
print('O arquivo está fechado? ', arquivo.closed)  

# Verifica se o arquivo foi fechado corretamente
if arquivo.closed:
    print("O arquivo foi fechado corretamente.")
else:
    print("O arquivo ainda está aberto.")

#ABAIXO COMENTEI UM BLOCO DE CÓDIGO PARA EXECUTAR APENAS AS FUNÇÕES READLINE E READLINES
"""
# Adiciona conteúdo ao arquivo em modo append ('a')
open('atributos.txt', 'a').write('Aula de C++\n') 
for linha in arquivo:
    # Imprime cada linha do arquivo
    print(repr(linha)) 

# O bloco with garante que o arquivo seja fechado automaticamente após o término do bloco
# Verifica se o arquivo foi fechado corretamente
with open('atributos.txt', 'r') as arquivo_leitura:
    for linha in arquivo_leitura:
        print(repr(linha))

if arquivo_leitura.closed:
    print("O arquivo foi fechado corretamente dentro do bloco with.")
else:
    print("O arquivo ainda está aberto dentro do bloco with.")
# Imprime o conteúdo do arquivo usando a função with
# Isso é útil para garantir que o arquivo seja fechado automaticamente

"""
#UTILIZANDO READLINE E READLINES
with open('atributos.txt', 'r') as file:
     content = file.readline() # Lê apenas a primeira linha do arquivo e armazena na variável content
     print('Utilizando readLine esta função lê apenas a primeira linha do arquivo: =>', content) # Imprime o conteúdo lido
     
     # Imprime cada linha restante do arquivo
     content_readlines = file.readlines() # Lê todas as linhas restantes do arquivo e armazena em uma lista
     print('Utilizando readLines serão lidas todas as demais linhas, armazenadas em uma lista, e impressas na tela:\n', content_readlines) # Imprime a lista de linhas lidas
