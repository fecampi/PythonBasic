# Propriedades: Desordenado, Mutável,Plural,Acessado por chave


# Criando um dicionario vazio
D = {}
D = dict()

# Criando
D = { "Alface": 0.45,
           "Batata": 1.20,
           "Tomate": 2.30,
           "Feijão": 1.50 }

D = dict(Alface = 0.45,
               Batata = 1.20,
               Tomate = 2.30,
               Feijão = 1.50)           

# Tupla em Dicionario 
L = [("Arroz",2.30),("Lasanha",9.00)]
D1 = dict(L)

# Adicionando elemento
D["Cebola"] = 1.20

#Adicionar Lista 
D["Bolo"] = [3.50,8.50]

# Mudando elemento
D["Tomate"] = 2.50


# Verificando se existe
"Manga" in L
"Batata" in L


# Examinando
D["Batata"]
D["Bolo"][0]


# Obter chave e valor
D.keys()
D.values()
D.items()

# Obter tamanho
len(D)

print()

#Excluir valor acessado
del D["Tomate"]

#Substituição de String
print("preço cebola: %(Cebola)s" % D) 

#Dicionario com lista
estoque={ "tomate": [ 1000, 2.30],
          "alface": [   500, 0.45],
          "batata": [ 2001, 1.20],
          "feijão": [   100, 1.50] }

#Exemplo de estoque
estoque={ "tomate": [ 1000, 2.30],
          "alface": [   500, 0.45],
          "batata": [ 2001, 1.20],
          "feijão": [   100, 1.50] }
venda = [ ["tomate", 5], ["batata", 10], ["alface",5]]
total = 0

print("Vendas:\n")

for operação in venda:
     produto, quantidade = operação
     preço = estoque[produto][1]
     custo = preço * quantidade
     print("%12s: %3d x %6.2f = %6.2f" %
         (produto, quantidade,preço,custo))
     estoque[produto][0] -= quantidade
     total += custo
print(" Custo total: %21.2f\n" % total)
print("Estoque:\n")
for chave, dados in estoque.items():
     print("Descrição: ", chave)
     print("Quantidade: ", dados[0])
     print("Preço: %6.2f\n" % dados[1])


# Retornar o valor e remover elemento
D.pop("Batata")

# Adicionar varias entradas
D.update({"Café":4.50,"Morango":2.50})

# Retornar Valor(RECOMENDADO)
D.get("Café")

# Retornar Valor(RECOMENDADO)
D.get("Batata","Não Encontrado")

# Remover elemento 
D["Bolo"].remove(3.50)

