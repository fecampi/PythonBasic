class Banco:
     #construtor
     def __init__(self, nome):
         self.nome = nome
         self.clientes = []
         self.contas = []
         
     #metodos personalizados    
     def abre_conta(self, conta):
         self.contas.append(conta)
     def lista_contas(self):
         print("BAnco%s" % (self.nome))
         for c in self.contas:
               c.resumo()


               