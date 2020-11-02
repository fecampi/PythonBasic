######Criar Variavel######
inteiro = 2      
pontoFlutuante = 2.0     
string = 'two'   
booleano = True    
vazio = None      

######Dizer o tipo#####
tela = (type(inteiro))
tela = (type(pontoFlutuante))
tela = (type(string))
tela = (type(booleano))
tela = (type(vazio))

#######Verificar o tipo#####
tela = isinstance(string, int)           
tela = isinstance(2.0, (int, float)) 

# Converter um objeto para um determinado tipo
float(2)
int(2.9)
str(2.9)

print(tela)