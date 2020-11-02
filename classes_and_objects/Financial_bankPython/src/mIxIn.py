#mix-ins
#existe para adicionar funcionalidade extra a outra classe através de herança múltipla.
# A ideia é que classes herdem estes mix-ins, essas "misturas de funcionalidades".
# apenas fornecem métodos adicionais mas não inicializam nada.
#Evitar diamante

class AutenticavelMixIn:
    def autentica(self, senha):
        pass
      

class AtendimentoMixIn:
    def cadastra_atendimento(self):
        # faz cadastro atendimento
        pass

    def atende_cliente(self):
        # faz atendimento
        pass

class HoraExtraMixIn:
    def calcula_hora_extra(self, horas):
        # calcula horas extras
        pass