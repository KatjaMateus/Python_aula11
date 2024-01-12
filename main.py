class Carro:
    def __init__(self, marca, cor, modelo, ano, qtde_portas):
        self.marca = marca
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.qtde_portas = qtde_portas
        
carro1 = Carro(marca="Ford", cor="Preto", modelo="KA", ano=2019, qtde_portas=4)

print(carro1.marca, carro1.modelo, carro1.cor)
