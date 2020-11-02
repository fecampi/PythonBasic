#Importando Type
import types

#Retornando o tipo
a=5
print(type(a))


#Retornando o tipo usando uma função
def diz_o_tipo(a):
    tipo = type(a)
    if tipo == str:
        return("String")
    elif tipo == list:
        return("Lista")
    elif tipo == dict:
        return("Dicionário")
    elif tipo == int:
        return("Número inteiro")
    elif tipo == float:
        return("Número decimal")
    elif tipo == types.FunctionType:
        return("Função")
    elif tipo == types.BuiltinFunctionType:
        return("Função interna")
    else:
        return(str(tipo))
print(diz_o_tipo(10))

#tipo do elemento de uma lista
L=[ 2, "Alô", ["!"], { "a":1, "b":2}]
for e in L:
    print(type(e))

#Navegar lista por seus elementos
L=["a", ["b","c","d"], "e"]
for x in L:
    if type(x)==str:
        print(x)
    else:
        print("Lista:")
        for z in x:
            print(z)


