#Modos de abertura
#r  leitura
#w  escrita rescrevendo
#a  escrita adicionando
#b  modo binario
#+  atualizando(leitura e escrita)

#Criando e escrevendo 
arquivo = open("números.txt","w")
for linha in range(1,101):
         arquivo.write("%d\n" % linha)
arquivo.close()

#criando e escrevendo em dois arquivos
ímpares = open("ímpares.txt","w")
pares = open("pares.txt","w")
for n in range(0,1000):
     if n % 2 == 0:
         pares.write("%d\n" % n)
     else:
         ímpares.write("%d\n" % n)
ímpares.close()
pares.close()

#Lendo
arquivo = open("números.txt","r")
for linha in arquivo.readlines():
     print(linha)
arquivo.close()

#Lendo, processando, criando novo
novo = open("múltiplos de 4.txt","w")
velho = open("números.txt")
for l in velho.readlines():
     if int(l) % 4 == 0:
         novo.write(l)
velho.close()
novo.close()

