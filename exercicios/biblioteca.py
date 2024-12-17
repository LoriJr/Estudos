#5. Crie um arquivo chamado biblioteca.py e importe a classe Livro neste arquivo.

from aplicacao import Livro

#6. No arquivo biblioteca.py, empreste o livro chamando o método emprestar e imprima se o livro está disponível ou não após o empréstimo.

livro3 = Livro('Jr', 'A vida', 2024)
livro3 = Livro('lo', 'A vida', 2024)
livro3 = Livro('la', 'A vida', 2023)
livro3 = Livro('cla', 'A vida', 2024)
livro3 = Livro('ma', 'A vida', 2024)

print(livro3.emprestar())
print(livro3.emprestar())

#7. No arquivo biblioteca.py, utilize o método estático verificar_disponibilidade para obter a lista de livros disponíveis publicados em um ano específico.

livros_disponiveis = Livro.verificar_disponibilidade(2024)
#print(f"Livros disponíveis de 2024: {[str(livro) for livro in livros_disponiveis]}")

