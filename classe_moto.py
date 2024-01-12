class Moto:
    def __init__(self, brand, model, cylinders, colour):
        self.marca = brand
        self.modelo = model
        self.cilindradas = cylinders
        self.cor = colour

    def ligar(self):
        return f"A moto {self.modelo} ligou."
    
    def ver_informacoes(self):
        return f"""
        Marca: {self.marca}
        Modelo: {self.modelo}
        Cilindradas: {self.cilindradas}
        Cor: {self.cor}
    """
    
moto1 = Moto(brand="Yamaha", model="NMax", cylinders=160, colour="Vermelho")
moto2 = Moto(brand="Honda", model="TXis", cylinders=250, colour="Prata")
moto3 = Moto(brand="Harley Davidson", model="ZTurbo", cylinders=300, colour="Preto")
moto4 = Moto("Honda", "bros", 160, "branco")

# print(moto1.marca)
# print(moto2.cilindradas, moto2.cor)
# print(moto3.marca, moto3.modelo, moto3.cilindradas, moto3.cor)

# print(moto1.ligar())
# print(moto2.ligar())
# print(moto3.ligar())

print(moto1.ver_informacoes())
print(moto2.ver_informacoes())