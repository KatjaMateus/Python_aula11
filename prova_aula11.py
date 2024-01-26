class Elevador:
    def __init__(self, totalCapacidade, atualCapacidade, totalAndar, atualAndar):
        self.totalCapacidade = totalCapacidade
        self.atualCapacidade = atualCapacidade
        self.totalAndar = totalAndar
        self.atualAndar = atualAndar
    
    def subir(self):
        if self.atualAndar < self.totalAndar:
            self.atualAndar += 1
            print(f"Subindo. O andar atual é {self.atualAndar}.")
        else:
            print("VOCÊ ESTÁ NO ANDAR MAIS ALTO")
    
    def descer(self):
        if self.atualAndar > 0:
            self.atualAndar -= 1
            print(f"Descendo. O andara atual é {self.atualAndar}.")
        else:
            print("VOCÊ JÁ ESTÁ NO TÉRREO")
    
    def entrar(self):
        if self.atualCapacidade < self.totalCapacidade:
            self.atualCapacidade += 1
            print(f"Entrando uma pessoa. Há {self.atualCapacidade} pessoas no elevador.")
        else:
            print("O ELEVADOR ESTÁ CHEIO")
    
    def sair(self):
        if self.atualCapacidade > 0:
            self.atualCapacidade -= 1
            print(f"Saindo uma pessoa. Ficam {self.atualCapacidade} pessoas no elevador.")
        else:
            print("NÃO TEM NINGUÉM")

elevador1 = Elevador(atualCapacidade=0,totalCapacidade=5,atualAndar=0,totalAndar=5)

while True:
    escolha = int(input("""Escolha uma opção:
                        1 - subir
                        2 - descer
                        3 - entrar
                        4 - sair
                        0 - encerrar
                        """))
    
    if escolha == 1:
        elevador1.subir()
    elif escolha == 2:
        elevador1.descer()
    elif escolha == 3:
        elevador1.entrar()
    elif escolha == 4:
        elevador1.sair()
    elif escolha == 0:
        print("Programa encerrado")
        break
    else:
        print("Opção inválida")


