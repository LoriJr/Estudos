
#1. Crie uma classe chamada Livro com um construtor que aceita os parâmetros titulo, autor e ano_publicacao. Inicie um atributo chamado disponivel como True por padrão.
class Livro:
    livros = []
    def __init__(self, autor, titulo, ano_publicacao):
        self.autor = autor
        self.titulo = titulo
        self.ano_publicacao = ano_publicacao
        self._disponivel = True
        Livro.livros.append(self)
        
#2 . Na classe Livro, adicione um método especial str que retorna uma mensagem formatada com o título, autor e ano de publicação do livro. Crie duas instâncias da classe Livro e imprima essas instâncias.    

    def __str__(self):
        return f'{self.titulo} | {self.autor} | {str(self.ano_publicacao)}'

#3. Adicione um método de instância chamado emprestar à classe Livro que define o atributo disponivel como False. Crie uma instância da classe, chame o método emprestar e imprima se o livro está disponível ou não.
    
    def emprestar(self):
        if self._disponivel:
            self._disponivel = False
            return 'Livro emprestado com sucesso'
        else:
            return 'Livro indisponível para empréstimo'
    
#4. Adicione um método estático chamado verificar_disponibilidade à classe Livro que recebe um ano como parâmetro e retorna uma lista dos livros disponíveis publicados nesse ano.
    @staticmethod
    def verificar_disponibilidade(ano):
        livros_disponiveis = [livro for livro in Livro.livros if livro.ano_publicacao == ano and livro._disponivel] 
        return livros_disponiveis


livro1 = Livro('Paulo Coelho', 'Minha vida', 1990)
livro2 = Livro('Monteiro Lobato', 'Alto da Compadecida', 1995)


ano = 1995
livrosss = Livro.verificar_disponibilidade(ano)

#print(f"Livros disponíveis de {ano}: {[str(livro) for livro in livrosss]}")


    