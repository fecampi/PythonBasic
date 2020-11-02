from mIxIn import AutenticavelMixIn,AtendimentoMixIn,HoraExtraMixIn
#Herança:
# Um jeito de relacionarmos uma classe de tal maneira que uma delas herda tudo que o outra tem. 
#uma relação entre classe 'mãe' e classe 'filha'.
# aumenta o acoplamento entre as classes.

#Classe Abstrata
#Uma classe abstrata não pode ser instanciada e deve conter pelo menos um método abstrato.


class Funcionario:
    def __init__(self, nome, cpf, salario):
        self._nome = nome
        self._cpf = cpf
        self._salario = salario

    def get_bonificacao(self):
        return self._salario * 0.10

    # Apresentar mensagens para os usuários finais    
    def __str__(self): 
        return "Nome: "+ self._nome + ", CPF: " + self._cpf
    
    # Apresentar mensagens para os desenvolvedores
    def __repr__(self):
        return "{0[0]}#{0[1]}#{0[2]}".format([self._nome, self._cpf, self._salario])
     

 

class Gerente(Funcionario,HoraExtraMixIn):
    def __init__(self, nome, cpf, salario, senha, qtd_gerenciaveis):
        super().__init__(nome, cpf, salario)
        self._senha = senha
        self._qtd_gerenciaveis = qtd_gerenciaveis

    # Especialização.
    def get_bonificacao(self):
        return self._salario * 0.15

    # Regra da superclasse,adicionando 1000.0 reais.
    def get_bonificacaoEspecial(self):
        return super().get_bonificacao() + 1000 
