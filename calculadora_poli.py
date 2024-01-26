class Calculadora:
    def __init__(self, n1: int, n2: int):
        self.n1 = n1
        self.n2 = n2
    
    def somar(self):
        return(f"O resultado é {self.n1 + self.n2}.")