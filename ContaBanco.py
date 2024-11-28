from datetime import datetime #importa biblioteca de data e hora
import pytz #importa biblioteca para fuso horário

class ContaCorrente:

    @staticmethod #método estático
    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/east')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR.strftime('%d/%m/%Y %H:%M:%S')

    def __init__(self, nome, cpf, agencia, numero_conta):
        self.nome = nome
        self.cpf = cpf
        self.saldo = 0
        self.limite = None
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.transacoes = []

    def _limite_conta(self): #métodos com o _ no início significam que são métodos privados por convenção, e deve ser usado somente dentro da classe 
        self.limite = -1000
        return self.limite

    def sacar(self, valor_saque):
        if self.saldo - valor_saque < self._limite_conta():#aqui está fazendo referência ao método privado _limite_conta
            print("você não tem saldo suficiente para sacar esse valor")
        else:
            self.saldo -= valor_saque
            print(f"Saque realizado, saldo: {self.consultar_saldo()}")

    def depositar(self, valor_deposito):
        self.saldo += valor_deposito 
        self.transacoes.append((valor_deposito, self.saldo, ContaCorrente._data_hora()))
        
    def consultar_saldo(self):
        print(f'Seu saldo é de R$ {self.saldo}')

    def consultar_limite_cheque_especial(self):
        print("Seu limite de cheque especial é de {:,.2f}".format(self._limite_conta()))

    def consultar_historico_transacoes(self):
        print("Histórico de Transações")
        print("Valor, Saldo, Data e Hora")
        for transacao in self.transacoes:
            print(transacao)

    def transferir(self, valor, conta_destino):
        self.saldo -= valor
        self.transacoes.append((valor, self.saldo, ContaCorrente._data_hora()))
        conta_destino.saldo += valor
        conta_destino.transacoes.append((valor, conta_destino.saldo, ContaCorrente._data_hora()))

        

conta_lou = ContaCorrente("Lourival", "123.456.789-10", 1234, 304678)
conta_lais = ContaCorrente('Lais', '121.950.656-10', 222, 123456)

conta_lou.depositar(1500)
#print('-' * 20)

conta_lou.transferir(500, conta_lais)
conta_lou.consultar_saldo()
conta_lais.consultar_saldo()

print('-' * 20)
conta_lou.consultar_historico_transacoes()
conta_lais.consultar_historico_transacoes()


