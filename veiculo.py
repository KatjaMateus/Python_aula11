class Veiculo:
    def __init__(self, marca: str, modelo: str, ano: int, cor: str):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor

    def ligar(self):
        return f"O veículo {self.modelo} ligou."
    
class Carro(Veiculo):
    def __init__(self, marca: str, modelo: str, ano: int, cor: str, qtde_portas: int):
        super().__init__(marca, modelo, ano, cor)
        self.qtd_portas = qtde_portas
    
    def cavalo_de_pau(self):
        return f"O carro {self.modelo} que tem {self.qtd_portas} de portas fez um cavalo de pau."

class Moto(Veiculo):
    def __init__(self, marca: str, modelo: str, ano: int, cor: str, cilindradas: int):
        super().__init__(marca, modelo, ano, cor)
        self.cilindradas = cilindradas
    
    def empinar(self):
        return f"A moto {self.modelo} de {self.cilindradas} cilindradas está empinando."

carro1 = Carro(marca="Fiat", modelo="Uno", ano=2011, cor="Cinza", qtde_portas=4)
moto1 = Moto(marca="Honda", modelo="XRE", ano=2020, cor="Vermelho", cilindradas=300)

print(carro1.qtd_portas)
print(moto1.cilindradas)

print(carro1.ligar())
print(carro1.cavalo_de_pau())
print(moto1.ligar(), moto1.empinar())

    