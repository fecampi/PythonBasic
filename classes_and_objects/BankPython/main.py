#importações
from clientes import Cliente
from contas import Conta, ContaEspecial
from bancos import Banco


#criar banco
tatu = Banco("Tatú")

#criar clientes
cliente1= Cliente("João da Silva", "777-1234")
cliente2 = Cliente("Maria da Silva", "555-4321")

#criar contas
conta1 = Conta(cliente1, 1, 1000)
conta2 = ContaEspecial([cliente1, cliente2], 2, 500, 1000)


#abrir contas

tatu.abre_conta(conta1)
tatu.abre_conta(conta2)

#operações
conta1.saque(50)
conta2.deposito(300)
conta1.saque(190)
conta2.deposito(95.15)
conta2.saque(1500)
conta1.extrato()
conta2.extrato()


#listar contas

tatu.lista_contas()
