import os

#caminho relativo
arquivo1 = open('aulas.txt', 'w')  # Abre o arquivo em modo escrita ('w') e se o aruivo não existir, ele será criado     
arquivo1.write('Aula de Python\n') # Escreve no arquivo
arquivo1.close() # Fecha o arquivo