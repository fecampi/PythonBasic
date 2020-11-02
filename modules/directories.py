# -*- coding: utf-8 -*-
import os.path
import sys


#caminho Absoluto
caminho1 = os.path.abspath("i/j/k/texto.txt")

#ultima parte do caminho
caminho2 = os.path.basename("i/j/k/texto.txt")

#caminho a esquerda da ultima barra
caminho3 = os.path.dirname("i/j/k/texto.txt")

#split com basename e dirname separados
caminho4 = os.path.split("i/j/k/texto.txt")

#separa caminho da expensão
caminho5 = os.path.splitext("i/j/k/texto.txt")

#separa a letra do caminho
caminho6 = os.path.splitdrive("i/j/k/texto.txt")

#caminho desde a raiz
caminho7 = os.path.abspath("i/j/k/texto.txt")

#Junta os componentes do caminho
caminho8 = os.path.join("c:","dados","texto.tx")

#--caminho--

print(caminho5)