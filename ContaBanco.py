class ContaCorrente:

    def __init__(self, nome, cpf, agencia, numero_conta):
        self.nome = nome
        self.cpf = cpf
        self.saldo = 0
        self.agencia = agencia
        self.numero_conta = numero_conta

    def _limite_conta(self): #métodos com o _ no início significam que são métodos privados por convenção
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
        #print(f"Depósito realizado, saldo: {self.consultar_saldo()}")   

    def consultar_saldo(self):
        print(f'Seu saldo é de R$ {self.saldo}')

    def consultar_limite_cheque_especial(self):
        print("Seu limite de cheque especial é de {:,.2f}".format(self._limite_conta()))
        

conta_lou = ContaCorrente("Lourival", "123.456.789-10", 1234, 3046)

conta_lou.depositar(200)
conta_lou.consultar_saldo()


