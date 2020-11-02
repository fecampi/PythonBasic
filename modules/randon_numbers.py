#Importação Aleatórios
import random

#####Geração######

#Números Inteiros
for x in range(10):
     print(random.randint(1,100))

#Números entre 0 e 1
for x in range(10):
     print(random.random())

#Números de ponto flutuante
for x in range(10):
     print(random.uniform(15,25))

#Usando uma lista para escolher n números
print(random.sample(range(1,101), 6))

######Emabralhar######
a = list(range(1,11))
random.shuffle(a)