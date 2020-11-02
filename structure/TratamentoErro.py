###### Principais Erros ######
# Erros podem ocorrer,investigando e "contornando"

# SintaxError
    #   SyntaxError: EOL while scanning string literal 
        #    Erro de sintaxe quando o interpretador não consegue ler o que foi escrito.
    #   SyntaxError: invalid syntax
        #   Aspas sem completar.
        #   While,for,if e else sem :
        #   Letras maisculas e minusculas trocadas.
        #   Nomes incorretos


# IndentationError
    #   IndentationError: unindent does not match any outer indentation level.
        #   Indentação(recuo de um texto).
        #   espaço no lugar de TAB

# KeyError
    #   KeyError: "NomeDaChave"  
        #   Tentar acessar chave que não exite.  

# NameError
    #   NameError: name "x" is not defined
        #   Variavel sem ser inicializada.
        #   variavel com nome trocado "x" invés de "X"   

# ValueError
    #   ValueError: could not convert string to float:maria
        #   float("maria")
    #   ValueError: substring not found
        #   String que não existe
    #   ValueError: invalid literal for int() with base 10:"abc"
        #   int("abc") 

#   TypeError
    #   TypeError: float() takes at most 1 argument (2 given)
        #   usar virgula no lugar de ponto
    #   TypeError: string indices must be integers
        #   lista indexada por letras   

#   IndexError
    #   IndexError: string index out of range
        #   valor errado do indice (acessar S[10] de s="abc")     


try:
    arq = open('data/filmes.txt', 'r')
except FileNotFoundError:
    print("Erro: arquivo não encontrado")
except ZeroDivisionError:
    input("Digite outro numero")
else:
    filmes = arq.readlines()
    print("se não tiver erro,faz!")

finally:
    print("sempre executado")


