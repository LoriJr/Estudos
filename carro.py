## criar uma classe carro com atributos e métodos 

class Carro:

    def __init__(self):
        self.cor = "Preto"
        self.modelo = "Astra"
        self.marcha = 0
        self.velocidade_minima = 0
        self.velocidade_maxima = 120
    
    def trocar_marcha(self, nova_marcha):
        self.marcha = nova_marcha
        

    def pintura(self, nova_cor):
        self.cor = nova_cor

velocidade = 0
unidade = "km/h"

velocidade_carro = Carro()

altera_marcha = 1

for velocidade in range(velocidade_carro.velocidade_minima, velocidade_carro.velocidade_maxima, 2 ):
    velocidade_carro.trocar_marcha(altera_marcha)
    
    if velocidade == 10:
        altera_marcha +=1
        velocidade_carro.trocar_marcha(altera_marcha)
    elif velocidade == 20:
        altera_marcha +=1
        velocidade_carro.trocar_marcha(altera_marcha)
    elif velocidade == 30:
        altera_marcha +=1
        velocidade_carro.trocar_marcha(altera_marcha)
    elif velocidade == 80:
        altera_marcha +=1
        velocidade_carro.trocar_marcha(altera_marcha)
    print(f"{velocidade} km/h", f"Marcha {velocidade_carro.marcha}")


    



