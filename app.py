from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'Gourmet')
# restaurante_pizza = Restaurante('pizza express', 'Italiana')
# restaurante_mexicano = Restaurante('Mexican Food', 'Mexicana')

restaurante_praca.receber_avaliacao('Jr', 10)
restaurante_praca.receber_avaliacao('Joca', 2)
restaurante_praca.receber_avaliacao('Lili', 5)

restaurante_praca.alternar_estado()

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()