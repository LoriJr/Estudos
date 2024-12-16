from modelos.avaliacao import Avaliacao

class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        '''
        Método construtor, nele contém os atributos da classe, e também uma lista contendo os mesmos atributos
        '''
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        Restaurante.restaurantes.append(self)
        self._avaliacao = []
        
    # def __str__(self): 
    #     '''
    #     método especial para alterar a forma de impressão dos itens do objeto em String
    #     nesse caso só está como exemplo, pois o método listar_restaurante já está com a formatação do abjeto
    #     '''
    #     return self._nome, self._categoria
    
    @classmethod
    def listar_restaurantes(cls):
        '''
        Este é um método da classe, onde no seu argumento por convenção, coloca-se um cls.
        no for restaurante in cls.restaurantes é onde ele faz a referência para a classe.
        a saída do método são os prints, já formatados.
        '''
        mensagem = (f'{'Nome do Restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | {'Status'}')
        print(mensagem)
        print('-'* len(mensagem))
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo}')
        
    @property
    def ativo(self):
        '''
        Propriedade que altera a impressão do atributo ativo, conforme está no return
        '''
        return '☒' if self._ativo else '☐'
    
    def alternar_estado(self):
        '''
        método que altera o estado do ativo para True, já que o default é false
        '''
        self._ativo = not self._ativo
    
    def receber_avaliacao(self, cliente, nota):
        nota = Avaliacao(cliente, nota)
        self._avaliacao.append(nota)

    @property #o property aqui nos dá a condiçao de ler esses dados
    def media_avaliacoes(self):
        if not self._avaliacao:
            return 0
        else:
            soma_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
            quantidade_notas = len(self._avaliacao)
            media = round(soma_notas / quantidade_notas, 1) #o round aredonta os valores e no final escolhemos quantas cadas depois da vírgula, que no caso é 1
            return media
        





#print(vars(restaurante_praca))

