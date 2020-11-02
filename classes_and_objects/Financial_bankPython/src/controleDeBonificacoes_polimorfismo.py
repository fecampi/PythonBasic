from funcionario_heranca import Funcionario
# Polimorfismo
# capacidade de um objeto poder ser referenciado de várias formas
# diminui o acoplamento entre as classes, para evitar que novos códigos resultem em modificações.

class ControleDeBonificacoes:

    def __init__(self, total_bonificacoes=0):
        self._total_bonificacoes = total_bonificacoes


    #Limita a classe funcionario o registro de bonificação
    def registra(self, obj): 
        if(isinstance(obj, Funcionario)):
            self._total_bonificacoes += obj.get_bonificacao()
        else:
            print('instância de {} não implementa o método get_bonificacao()'.format(self.__class__.__name__))
    
    @property
    def total_bonificacoes(self):
        return self._total_bonificacoes