#Propriedades:Iterável,Imutável e simples


#Criando
a = str("Maria Amélia Souza")
b = str(42)
c = "João"

#manipulando
tela = a[0] 

#concatenando
tela = "-"*3 + a + " e Silva" + "-"*3

#Pular Linha
print("Primeira linha \nSegunda linha")


######Marcadores Inteiros#####
idade = 22

#inteiro
tela = "[%d]" % idade

#Ocupando 5 posições alinhado a direita
tela = "[%5d]" % idade

#Ocupando 5 posições preenchendo com 0 antes
tela = "[%05d]" % idade

#Ocupando 5 posições alinhado a esquerda
tela = "[%-5d]" % idade

#####Marcadores Decimais#####
#Caracteres a reservar
tela = "%10f" % 5

#Caracteres a reservar e casas decimais
tela = "%5.2f" % 5

######Fatiamento######
s="ABCDEFGHI"
tela = s[0:2]
tela = s[1:8]
tela = s[:2]
tela1 = s[-1:]
tela = s[1:]
tela = s[0:-2]




######Conversão######

#Minusculas
tela = a.lower()

#Maisculas
tela = a.upper()

#Em lista
tela = list(a)

#Lista para String usando delimitador neste caso o ("")
tela = " ".join(a)

#combinando lower/upper com in/not in
tela = "joão" in a.lower()
"joão" in a.lower()

######contagem de letras e palavras######

######Pesquisa######

#Quantas vezes o elemento aparece
tela = a.count(a)

#tamanho
tela = len(a)


#Verifica se possui no inicio a string
tela = a.startswith("Maria")

#Verifica se possui no fim a string
tela = a.endswith("Souza")

#Pesquisa usando in
tela = "Maria" in a

#Pesquisa usando not in
tela = "Fernanda" not in a 

#Com find(retorna a posição da primeira ocorrência a esquerda)
tela = a.find("A")

#Com rfind(retorna a posição da primeira ocorrência a direita)
tela = a.rfind("uza")

#Delimitando inicio e/ou fim
tela = a.find("A",0,-1)

#Todas as ocorrências
s = "um tigre, dois tigres, três tigres"
p = 0
while(p>-1):
     p = s.find("tigre", p)
     if p >= 0:
         tela = ("Posição: %d" % p)
         p += 1

######Formatação######
#Centro
tela = "X"+b.center(10)+"X"

#Centro com caracteres 
tela = "X"+b.center(10,".")+"X"

#Esquerda
tela = "X"+b.ljust(10)+"X"

#Esquerda com caracteres
tela = "X"+b.ljust(10,".")+"X"

#Direita
tela = "X"+b.rjust(10)+"X"

#Direita com caracteres
tela = "X"+b.rjust(10,".")+"X"


#####Separação###### 

#Linhas em strings
tela = (a.split())
tela = a.split(" ")

#Varias linhas em String Separadas
texto = "PrimeiraLinha\nSeguntaUltima"
tela = texto.splitlines()

#substituição de string
tela = a.replace("a","@")

#Remoção de espaço em brancos

#Remover todos
texto = "   -   Olá   -   "
tela = (texto)
tela = texto.strip()

#Remover a esquerda
tela = texto.lstrip()

#Remover a direita
tela = texto.rstrip()

#Remoção de caracteres.
#Remover todos
texto = "  +  -Olá-  +  "
tela = texto.strip("-")

#Remover a esquerda
tela = texto.lstrip("-")

#Remover a direita
tela = texto.rstrip("-")


######Verificações######

#Letra ou número
tela = "12B".isalnum()

#Letra
tela = "AB".isalnum()

#número
tela = "23".isdigit()

#representação númerica
tela = "\u2153".isnumeric()

#Maiscula
tela = a.isupper()

#Minuscula
tela = a.islower()

#Possui caracteres de espaçamento
tela = "\t\n\r".isspace()

#Pode ser impressa
tela = "OI".isprintable()


######Formatações######

#Format
tela = "{0} x {1} R${2}".format(5,"maçã", "1.20")

#Mesmo parametro mais de uma vez
tela = "{0} {1} {0}".format("-","x")

#Alteração de ordem
tela = "{1} {0}".format("primeiro", "segundo")

#limitar tamanho para imprimir
tela = "X{0:10}X".format("123456789012345")

#espaços a esquerda
tela = "X{0:<10}X".format("123")

#espaços a direita
tela = "X{0:>10}X".format("123")

#espaços e centralizar
tela = "X{0:^10}X".format("123")

#Mascara com lista
tela = "{0[0]} {0[1]}".format(["123", "456"])

#Mascara com dicionario 
tela = "{0[nome]} {0[telefone]}".format({ "telefone": 572, "nome":"Maria"})

#zero a esquerda 00002
tela = "{0:05}".format(99)

#Preenchimento com caracteres
tela= "{0:*=7}".format(32)

#Preenchimento com caracteres centralizando
tela = "{0:*^10}".format(123)

#Preenchimento com caracteres alinhando a esquerda
tela = "{0:*<10}".format(123)

#Preenchimento com caracteres alinhando a direita
tela = "{0:*>10}".format(123)

#Milhares
tela = "{0:10,}".format(7532)
tela = "{0:10.5f}".format(1500.31)

#Positivo e Negativo
tela = "{0:+10} {1:-10}".format(5,-6)
tela = "{0:-10} {1: 10}".format(5,-6)
tela = "{0: 10} {1:+10}".format(5,-6)

#Formatos de Números inteiros
tela = "{:b}".format(5678)  #Binário
tela = "{:c}".format(65)    #Caractere
tela = "{:o}".format(5678)  #Octal
tela = "{:x}".format(5678)  #Hexadecimal minusculo
tela = "{:X}".format(5678)  #Hexadecinal maiusculo
tela = "{:d}".format(5678)  #Base 10
tela = "{:n}".format(5678)  #Base 10 Local


#Decimais
tela = "{:f}".format(1579.543)  #Decimal
tela = "{:n}".format(1579.543)  #Local
tela = "{:8e}".format(3.141592653589793)    #Notação cientifica com minusculo
tela = "{:8E}".format(3.141592653589793)    #Notação cientifica com maiúsculo
tela = "{:8g}".format(3.141592653589793)    #Generico
tela = "{:5.2%}".format(0.05)   #Percentual

