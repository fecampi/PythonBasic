###### Seleção ######
x,y,z=2,2,2

if x > 0:
    print('positivo')
elif x == 0:
    print('zero')
else:
    print('negativo')

# Declaração em linha
if y > 0: print('positive')

# Conhecido como um 'operador ternário'
'Positivo' if z > 0 else 'zero ou negativo'

###### Repetição indefinida ###### 

#Contadores
inicio = 1
fim = 2
while inicio <= fim:
     print(x)
     inicio = inicio + 1

#Acumuladores
inicio = 1
soma = 0
while inicio <= 10:
     x = 2
     soma = soma + x
     inicio = inicio + 1
print("Soma: %d"%soma)

#Interrompendo
s = 0
while True:
     v = int(input("Digite um número a somar ou 0 para sair:"))
     if v == 0:
         break
     s = s + v
print(s)

#Break&Continue
i = 0
while(i<10):
    i += 1
    if(i%2==0):
        continue
        #interrompe só e somente só, o ciclo que estava, ou seja, somente um ciclo é executado.
    if(i>5):
        break
        #interrompe toda a execução da estrutura de repetição
    print(i)
else:
    print("else")
print("fim")
print()




######Repetição definida ######
#por elemento elemento ######
L = [8,9,15]
for e in L:
    print(e)

# por indice e elemento
L = [5,9,13]
for x, e in enumerate(L):
     print("[%d] %d" % (x,e))    


