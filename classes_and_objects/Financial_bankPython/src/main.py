#importações
from cliente_agregacao import Cliente
from conta_classe import ContaInvestimento,ContaCorrente,SeguroDeVida
from historico_composicao import Historico
from funcionario_heranca import Gerente,Funcionario
from controleDeBonificacoes_polimorfismo import ControleDeBonificacoes
from manipulador_tributaveis import ManipuladorDeTributaveis
from tributavel_interface import Tributavel


cliente1 = Cliente('João', 'Oliveira', '11111111111-11')
cliente2 = Cliente('José', 'Azevedo', '222222222-22')



conta1 = ContaInvestimento('123-6', 'Maria', 1000)
conta2 = ContaInvestimento('999-9', 'João', 0)

conta1.deposita(1000.0)
conta1.atualiza(0.01)
print(conta1.saldo)

conta1.deposita(100.0)
conta1.saca(50.0)
conta1.transfere_para(conta2, 200.0)
conta1.historico.imprime()

print("- total de contas:", ContaInvestimento.total_contas)#Chama método de classe, opera na classe
print(ContaInvestimento.assinatura())#Chama método estatico,sem relação ao objeto


funcionario = Funcionario('João', '111111111-11', 2000.0)
gerente = Gerente("Fabi","222222222-22",5000.0,2,0)
print(vars(funcionario))
print(vars(gerente))

#Bonificações
print("Bonificações")
controle = ControleDeBonificacoes()
controle.registra(funcionario)
controle.registra(gerente)
print("bonificacao funcionario: {}".format(funcionario.get_bonificacao()))
print("bonificacao gerente: {}".format(gerente.get_bonificacao()))
print("total: {}".format(controle.total_bonificacoes))



#Apresentar mensagens
print("Apresentar mensagens")
print(funcionario) #printa __str_
print(repr(funcionario))   #printa __repr__


if __name__ == '__main__':
    cc = ContaCorrente('João', '123-4')
    cc.deposita(1000.0)
    seguro = SeguroDeVida(100.0, 'José', '345-77')
    Tributavel.register(ContaCorrente)
    Tributavel.register(SeguroDeVida)
    lista_tributaveis = []
    lista_tributaveis.append(cc)
    lista_tributaveis.append(seguro)
    mt = ManipuladorDeTributaveis()
    total = mt.calcula_impostos(lista_tributaveis)
    print(total)

    