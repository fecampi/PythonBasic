from historico_composicao import Historico
from tributavel_interface import Tributavel
import abc

class Conta(abc.ABC):

    #ATRIBUTO DE CLASSE
    total_contas = 0 

    #####Construtor#####  
    __slots__ = ["numero", "_titular", "_saldo", "limite","historico"]  #Boa pratica para reservar espaço.

    def __init__(self, numero, titular, saldo=0, limite=1000.0):
        self.numero = numero
        self._titular = titular
        self._saldo = saldo
        self.limite = limite
        self.historico = Historico()    #cria o historico
        Conta.total_contas +=1

# Quando a existência de uma classe depende de outra classe, 
# como é a relação da classe Histórico com a classe Conta, 
# dizemos que a classe Historico compõe a classe Conta . 
# Esta associação chamamos Composição.

####Métodos Especiais




    @staticmethod   #Método Estatico(funciona como uma função comum, sem relação ao objeto)
    def assinatura():
        return "Obrigado,volte sempre ao Banco Tatu"

    @classmethod    #Método de classe(Servem para definir um método que opera na classe)
    def get_total_contas(cls):
        return cls._total_contas

   
    @property #DECORATOR(Comportamento de Get)
    def saldo(self):
        return self._saldo
        
    @saldo.setter #Set
    def saldo(self, saldo):
        if(self._saldo < 0):
            print("saldo não pode ser negativo")
        else:
            self._saldo = saldo



#####Métodos Personalizados#####
    def deposita(self, valor):
        self._saldo += valor
        self.historico.transacoes.append("depósito de {}".format(valor))

    def saca(self, valor):
        if (self._saldo < valor):
            return False
        else:
            self.saldo -= valor
            self.historico.transacoes.append("saque de {}".format(valor))

    def extrato(self):
        print("numero: {} \nsaldo: {}".format(self.numero, self.saldo))
        self.historico.transacoes.append("tirou extrato - saldo de {}".format(self.saldo))

    def transfere_para(self,destino,valor):
        retirou = self.saca(valor)  
        if (retirou == False):
            return False
        else:
            destino.deposita(valor)
            self.historico.transacoes.append("transferencia de {} para conta {}".format(valor, destino.numero))
            return True
    
    #Uma classe abstrata não pode ser instanciada e deve conter pelo menos um método abstrato.
    @abc.abstractmethod
    def atualiza():
        pass

class ContaInvestimento(Conta):
    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 5


class ContaCorrente(Conta):

    def get_valor_imposto(self):
        return self._saldo * 0.01

    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 5
    
    
        
class SeguroDeVida:
    def __init__(self, valor, titular, numero_apolice):
        self._valor = valor
        self._titular = titular
        self._numero_apolice = numero_apolice

    def get_valor_imposto(self):
        return 50 + self._valor * 0.05