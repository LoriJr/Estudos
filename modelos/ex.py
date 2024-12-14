'''
Agora é sua vez! Crie uma nova classe chamada Pessoa com atributos como nome, idade e profissão. Adicione um método especial __str__ para imprimir uma representação em string da pessoa. Implemente também um método de instância chamado aniversario que aumenta a idade da pessoa em um ano. Por fim, adicione uma propriedade chamada saudacao que retorna uma mensagem de saudação personalizada com base na profissão da pessoa.
'''
class Pessoa:
    def __init__(self, nome, idade, profissao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao
    
    def __str__(self):
        return f'{self.nome} {self.idade} {self.profissao}'
    
    def aniversario(self):
        self.idade += 1

    def imprime_resultado(self):
        print(f'{self.nome} {self.idade} {self.saudacao}')

    @property
    def saudacao(self):
        if self.profissao:
            return f'Olá, sou {self.nome}! Trabalho como {self.profissao}.'
        else:
            return f'Olá, sou {self.nome}!'

junior = Pessoa('Junior', 39, 'Analista de Sistemas Jr')

junior.aniversario()

junior.imprime_resultado()

