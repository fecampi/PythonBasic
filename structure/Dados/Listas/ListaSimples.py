#Propriedades:Ordenado,iterável,mutável e plural.


#criar lista vazia
L = []
L = list()

#criar lista com elementos
L = [ 15, 8, 9,19,20,80,32 ]

#acesso 
L[0]

#modificando
L[0] = 7


#copia
V = L[:]
V = list(L)

#fatiamento
L[0:5]
L[:5]
L[:-1]
L[1:3]
L[3:]
L[:3]
L[-1]

#invertendo
L[::-1]
list(reversed(L))

#tamanho
len(L)

# Ordem crescente
sorted(L)

# Ordenando decrescente
sorted(L,reverse = True)

#adição elemento
L.append("a")

#adição de listas
L.extend(["b","c"])

# inserir no indice
L.insert(0,"novo")

# Remoção elemento com indice
del L[1]

# Remoção do elemento
L.remove("novo")

# Remove o elemento retornando
L.pop(0)

# Quantas vezes o elemento aparece
L.count("c")

#Obter o indice
L.index("b")

# Ordenando
L.sort()

# Ordenando reverse
L.sort(reverse = True)

#remoção de fatia
L = list(range(101))
del L[1:99]

#listas com string
S = ["maçãs", "peras", "kiwis"]

#listas elementos tipos diferentes
produto1 = [ "maçã", 10, 0.30]

#listas dentro de listas
produto1 = [ "maçã", 10, 0.30]
produto2 = [ "pêra",   5, 0.75]
produto3 = [ "kiwi",   4, 0.98]
compras = [ produto1, produto2, produto3]


#Pesquisa em uma lista
def pesquise(lista, valor):
     for x,e in enumerate(lista):
         if e == valor:
               return x
     return None

# verifica se é o mesmo objeto
L is V


# Verifica se tem o mesmo elemento
V == L

