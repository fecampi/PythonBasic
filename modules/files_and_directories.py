#importação arquivos
import os
import os.path

#importação tempo
import time

#importação detalhes do arquivo
import sys

#criar arquivo
open("antigo.txt","w").close()

#Criar um ok
os.mkdir("a")

#Criar diretorios ---------
os.makedirs("b/c/d")

#Alterar Nome arquivo
os.rename("antigo.txt","novo.txt")

#alterar nome Diretorio
os.rename("a","anovo")

#Renomer Diretorios
os.renames("b/c/d","bn/cn/dn")

#Obter caminho
print(os.getcwd())

#mudar o diretório
#ir para frente(filho)
os.chdir("anovo")
print(os.getcwd())

#Ir para trás(pai)
os.chdir("..")
print(os.getcwd())

#Ir para trás(voltando ainda mais)
os.chdir("../../..")
print(os.getcwd())

#Indo para o diretório
os.chdir("fecam/Dropbox/Python")
print(os.getcwd())

#verificar se existe
tela = os.path.exists("novo.txt")
tela = os.path.exists("anovo")
tela = os.path.exists("bn/cn/dn")

#verifica se é arquivo
tela = os.path.isfile("novo.txt")

#verifica se é diretório
tela = os.path.isdir("bn/cn/dn")

#Informações do arquivo
#tamanho
tela = os.path.getsize("novo.txt")

#criação em segundos
tela = os.path.getctime("novo.txt")

#modificação em segundos
tela = os.path.getmtime("novo.txt")

#Acessado em segundos
tela = os.path.getatime("novo.txt")

#Excluir arquivo
os.remove("novo.txt")

#Excluir diretorio
os.removedirs("anovo")

#Excluir diretorios
os.removedirs("bn/cn/dn")


print(tela)
