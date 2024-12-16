'''
Rfatore a classe ContaBancaria para utilizar a abordagem "pythonica" na criação de atributos. Utilize propriedades, se necessário.


Crie um método de classe para a conta ClienteBanco.
'''
#Crie uma classe chamada ContaBancaria com um construtor que aceita os parâmetros titular e saldo. Inicie o atributo ativo como False por padrão.
class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        self._ativo = False
#Na classe ContaBancaria, adicione um método especial __str__ que retorna uma mensagem formatada com o titular e o saldo da conta. Crie duas instâncias da classe e imprima essas instâncias.
    def __str__(self):
        return f'{self.titular} | {self.saldo}'
    
    @property
    def print_estado(self):
        return 'Ativada' if self._ativo else 'Desativada'    
#Adicione um método de classe chamado ativar_conta à classe ContaBancaria que define o atributo ativo como True. Crie uma instância da classe, chame o método de classe e imprima o valor de ativo.   
    def ativar_conta(self):
        self._ativo = True
    

    
conta_junior = ContaBancaria('Lourival Junior', 200)
conta_lais = ContaBancaria('Laís Macedo', 500)

#Crie uma instância da classe e imprima o valor da propriedade titular.
##########print(conta_junior.titular)


#Crie uma classe chamada ClienteBanco com um construtor que aceita 5 atributos. Instancie 3 objetos desta classe e atribua valores aos seus atributos através do método construtor.

class ClienteBanco:
    def __init__(self, nome, idade, cpf, endereco, estado_civil):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.endereco = endereco
        self.estado_civil = estado_civil

    def __str__(self):
        return f'{self.nome}, {str(self.idade)}, {str(self.cpf)}'

op1 = ClienteBanco('Marcos', 30, 12345678910, 'Rua Itacava', 'Solteiro')
# op2 = ClienteBanco()
# op3 = ClienteBanco()

print(op1)