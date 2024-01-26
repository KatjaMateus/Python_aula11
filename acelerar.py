class Carro:
    def __init__(self, marca, modelo, velocidade):
        self.marca = marca
        self.modelo = modelo
        self.velocidade = velocidade
    
    def acelerar(self):
        self.velocidade += 10
        print(f"{self.marca} {self.modelo} acelerando. Velocidade atual {self.velocidade} km/h.")


carro1=Carro(marca="Fiat", modelo="Uno", velocidade=0)

print(carro1.acelerar())
