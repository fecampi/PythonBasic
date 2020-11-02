
#Agregação:Cliente existe independente da classe Conta

class Cliente:
    #####Construtor#####
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome 
        self._sobrenome = sobrenome #Protegido
        self.__cpf = cpf #Privado





