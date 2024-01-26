class Fatura:
    def __init__(self, nome, preço, quantidade):
        self.nome = nome
        self.preço = preço
        self.quantidade = quantidade
        
        
    
    def gerar_fatura(self):
        return f"O valor total da fatura é R${self.preço * self.quantidade}"
        

item1=Fatura(nome="mesa",preço=456,quantidade=2)
item2=Fatura(nome="cama",preço=2780,quantidade=3)

print(item1.gerar_fatura())
print(item2.gerar_fatura())
