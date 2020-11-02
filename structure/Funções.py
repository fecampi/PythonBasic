#Definindo a função
def soma(a,b):
     print(a+b)

#Retornando um valor
def soma(a,b):
     return(a+b)

#Reutilização de função
def épar(x):
     return(x % 2 == 0)
def par_ou_ímpar(x):
     if épar(x):
         return "par"
     else:
         return "ímpar"

#Soma e Media
def média(L):
     total = 0
     for e in L:
         total += e
     return total / len(L)

#Fatorial
def fatorial1(n):
     fat = 1
     while n > 1:
         fat *= n
         n -= 1
     return fat

def fatorial2(n):
     fat = 1
     x = 1
     while x <= n:
         fat *= x
         x += 1
     return fat

#Variavel Global
a = 5
def MudarVariavel():
    global a 
    a = 0

#Função recursiva fatorial
def fatorial(n):
     if n == 0 or n == 1:
         return 1
     else:
         return n * fatorial(n-1)

#Função recursiva Fibonacci
def fibonacci(n):
     if n <= 1:
         return n
     else:
         return fibonacci(n-1) + fibonacci(n-2)

#Parâmetros opcionais(opcionais tem que ser os últimos)
def soma(a, b, imprime = False):
     s = a + b
     if imprime:
         print(s)
     return s

#Função com funções
def soma(a,b):
     return a+b
def subtração(a,b):
     return a-b
def imprime(a,b, operação):
     print(operação(a,b))

#Função com empacotamento(pega os valores de L[0] e L[1])
def soma(a,b):
     print(a+b)
L = [2,3]
soma(*L)

#Função com desempacotamento(pega os valores de uma lista na função)
def soma(*args):
     s = 0
     for x in args:
         s += x
     return s
soma(1,2)
soma(5,6,7,8)

#Função Lambda(crie funções simples)
multiplica = lambda a,b: (a*b)

#Módulos
import Fila









