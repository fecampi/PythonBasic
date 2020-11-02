#Propriedades:Desordenado, Iterável, mutável, plural e elementos repetidos.


# Criando um conjunto vazio
animais = set()

# Criando
animais = {"cobra","cachorro","gato"}
animaisDomesticos = set(["cachorro","gato"])

# Examinando
tela = "cobra" in animais

# Tamanho
tela = len(animais)

# Ordenando
sorted(set(animais))

#Operações relacionais
# Igual
tela = {1,2,3}=={1,2,3}
# Diferente
tela = {1,2,6}!={1,2,3}
# Contem
tela = {1,2,3}>={1}
# Está Contido
tela = {3}<={1,2,3}

#Metodos

# Operações para conjunto
# União
tela = animais.union(animaisDomesticos)
# Interseção
tela = animais.intersection(animaisDomesticos)
# Diferença
tela = animais.difference(animaisDomesticos)

# Adicionar um novo elemento
animais.add("cavalo")
# Remover elemento, erro se não encontrado(Não usar)
animais.remove("cobra")
# Remover sem erro caso não encontrado
animais.discard("rato")
# retorna e remove o ultimo elemento
tela = animais.pop()
# Remover todos os elementos
animais.clear()
# Adiciona vários elementos
animais.update({"rato"},{"tigre"})
animais.update(animaisDomesticos)








print(animais)