from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_pizza = Restaurante('pizza express', 'Italiana')
restaurante_mexicano = Restaurante('Mexican Food', 'Mexicana')

restaurante_mexicano.alternar_estado()

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()