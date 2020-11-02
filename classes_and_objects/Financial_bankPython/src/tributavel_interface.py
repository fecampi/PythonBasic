import abc
#Protocolos são interfaces e são definidos apenas por documentação 
#a boa prática é documentar esta classe garantindo o contrato semântico:


class Tributavel(abc.ABC):
    """ Classe que contém operações de um objeto autenticável
    As subclasses concretas devem sobrescrever o método get_valor_imposto.
    """
    @abc.abstractmethod
    def get_valor_imposto(self):
        """ aplica taxa de imposto sobre um determinado valor do objeto """
        pass