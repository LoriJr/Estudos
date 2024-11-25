class ContaCorrente:

    def __init__(self, nome, cpf, agencia, numero_conta):
        self.nome = nome
        self.cpf = cpf
        self.saldo = 0
        self.agencia = agencia
        self.numero_conta = numero_conta

    def sacar(self, valor_saque):
        self.saldo -= valor_saque
        print(f"Saque realizado, saldo: {self.consultar_saldo()}")

    def depositar(self, valor_deposito):
        self.saldo += valor_deposito 
        print(f"Depósito realizado, saldo: {self.consultar_saldo()}")

    def consultar_saldo(self):
        print(f'Seu saldo é de R$ {self.saldo}')
        

conta_lou = ContaCorrente("Lourival", "123.456.789-10", 1234, 3046)

conta_lou.depositar(200)
conta_lou.consultar_saldo()


