import os

#caminho relativo
arquivo1 = open('aulas.txt', 'w')  # Abre o arquivo em modo escrita ('w') e se o aruivo não existir, ele será criado     
arquivo1.write('Aula de Python\n') # Escreve no arquivo
arquivo1.close() # Fecha o arquivo
open('aulas.txt', 'a').write('Aula de Java\n') # Abre o arquivo em modo append ('a') e adiciona conteúdo
arquivo1.close() # Fecha o arquivo
open('aulas.txt', 'a').write('Aula de C++\n') # Abre o arquivo em modo append ('a') e adiciona conteúdo
arquivo1.close() # Fecha o arquivo
open('aulas.txt', 'a').write('Aula de C#\n') # Abre o arquivo em modo append ('a') e adiciona conteúdo
arquivo1.close() # Fecha o arquivo
#caminho absoluto
caminho_absoluto = os.path.abspath('aulas.txt') # Pega o caminho absoluto do arquivo
arquivo2 = open(caminho_absoluto, 'r') # Abre o arquivo em modo leitura ('r')
conteudo = arquivo2.read() # Lê o conteúdo do arquivo
arquivo2.close() # Fecha o arquivo
print(conteudo) # Imprime o conteúdo do arquivo na tela
# Imprime o caminho absoluto do arquivo
print(f'Caminho absoluto do arquivo: {caminho_absoluto}')
# Imprime o diretório do arquivo
diretorio = os.path.dirname(caminho_absoluto) # Pega o diretório do arquivo
print(f'Diretório do arquivo: {diretorio}') # Imprime o diretório do arquivo na tela
# Imprime o nome do arquivo
nome_arquivo = os.path.basename(caminho_absoluto) # Pega o nome do arquivo
print(f'Nome do arquivo: {nome_arquivo}') # Imprime o nome do arquivo na tela
# Imprime a extensão do arquivo 