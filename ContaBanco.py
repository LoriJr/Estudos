from datetime import datetime #importa biblioteca de data e hora
import pytz #importa biblioteca para fuso horário

class ContaCorrente:

    @staticmethod #método estático
    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/east')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR.strftime('%d/%m/%Y %H:%M:%S')

    def __init__(self, nome, cpf, agencia, numero_conta):
        self._nome = nome
        self._cpf = cpf
        self._saldo = 0
        self._limite = None
        self._agencia = agencia
        self._numero_conta = numero_conta
        self._transacoes = []
        self.cartoes = []

    def _limite_conta(self): #métodos com o _ no início significam que são métodos privados por convenção, e deve ser usado somente dentro da classe 
        self._limite = -1000
        return self._limite

    def sacar(self, valor_saque):
        if self._saldo - valor_saque < self._limite_conta():#aqui está fazendo referência ao método privado _limite_conta
            print("você não tem saldo suficiente para sacar esse valor")
        else:
            self._saldo -= valor_saque
            print(f"Saque realizado, saldo: {self.consultar_saldo()}")

    def depositar(self, valor_deposito):
        self._saldo += valor_deposito 
        self._transacoes.append((valor_deposito, self._saldo, ContaCorrente._data_hora()))
        
    def consultar_saldo(self):
        print(f'Seu saldo é de R$ {self._saldo}')

    def consultar_limite_cheque_especial(self):
        print("Seu limite de cheque especial é de {:,.2f}".format(self._limite_conta()))

    def consultar_historico_transacoes(self):
        print("Histórico de Transações")
        print("Valor, Saldo, Data e Hora")
        for transacao in self._transacoes:
            print(transacao)

    def transferir(self, valor, conta_destino):
        self._saldo -= valor
        self._transacoes.append((valor, self._saldo, ContaCorrente._data_hora()))
        conta_destino.saldo += valor
        conta_destino.transacoes.append((valor, conta_destino.saldo, ContaCorrente._data_hora()))

    def CartaoCredito():

        def __init__(self, titular, conta_corrente):
            self.numero= None
            self.titular = titular
            self.validade  = None 
            self.cod_seguranca = None
            self.limite = None
            self.conta-corrente = conta_corrente 

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


