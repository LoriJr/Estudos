class Restaurante:
    nome = ''
    categoria = ''
    ativo = False

restaurante_praca = Restaurante()
restaurante_praca.nome = 'Italiana'

print(f'o restaurante {restaurante_praca.nome} está ativo' if restaurante_praca.ativo==True else f'o restaurante {restaurante_praca.nome} está inativo')

restaurante_praca.categoria = 'Bistrô'
categoria = restaurante_praca.categoria

restaurante_pizza = Restaurante()
restaurante_pizza.nome = 'Pizza Place'
restaurante_pizza.categoria = 'Fast Food'
restaurante_pizza.ativo = True

print(vars(restaurante_pizza))