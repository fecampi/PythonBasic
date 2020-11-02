#Propriedade: Ordenado,Iterável,Imutável e Plural.


#Criando
tupla = ("a","b","v")
tupla = 100,200,300
tupla = "a","b","c"
tupla = tuple(["a","b","v"]) 

#Criando uma tupla com um elemento(Necessário a virgula)
a = (1,)
a = "a",

#Criando uma tupla vazia
tupla = ()

#Criando uma tupla de listas
L = [1,2,3]
tupla = tuple(L)

#tamanho
tela = len(tupla)

#Acessando
tela1 = tupla[0]

# Desepacotando
a,b,c = L

#Persistencia de valor
print(1 in L)
print(1 not in L)

#Fatiamento
L[0:-2]

#Retorna a primeira instancia
L.index(1)

#Quantas vezes o elemento aparece
L.count(2)

#Acessando com for
for elemento in tupla:
    print(elemento)

#concatenando
tupla1 = (1,2,3)
tupla2 = (4,5,6)
tupla = tupla1+tupla2

