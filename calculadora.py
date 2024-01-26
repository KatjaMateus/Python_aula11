class Calculadora:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
    
    def somar(self):
        print(f"O resultado é {self.n1 + self.n2}.")
    
    def subtrair(self):
        print(f"O resultado é {self.n1 - self.n2}.")
    
    def multiplicar(self):
        print(f"O resultado é {self.n1 * self.n2}.")
    
    def dividir(self):
        print(f"O resultado é {self.n1 / self.n2}.")


while True:
    menu = int(input("""Escolhe uma opção:
                     1 - somar
                     2 - subtrair
                     3 - multiplicar
                     4 - dividir
                     0 - sair
                     """))
    

    if menu == 1:
        numbers=Calculadora(n1=int(input("Digite o primeiro número: ")),n2=int(input("Digite o segundo número: ")))
        print(numbers.somar())
    elif menu == 2:
        numbers=Calculadora(n1=int(input("Digite o primeiro número: ")),n2=int(input("Digite o segundo número: ")))
        print(numbers.subtrair())
    elif menu == 3:
        numbers=Calculadora(n1=int(input("Digite o primeiro número: ")),n2=int(input("Digite o segundo número: ")))
        print(numbers.multiplicar())
    elif menu == 4:
        numbers=Calculadora(n1=int(input("Digite o primeiro número: ")),n2=int(input("Digite o segundo número: ")))
        print(numbers.dividir())
    elif menu == 0:
        print("Programa encerrado")
        break
    else:
        print("opção inválida")

