class Conta:
    def __init__(self, conta, titular, saldo):
        self.conta = conta
        self.titular = titular
        self.saldo = saldo
    
    def sacar(self, qtd):
        if self.saldo > qtd:
            self.saldo -= qtd
            return qtd
        else:
            return f"Saldo insuficiente para sacar {qtd}"
    
    def depositar(self, qtd):
        self.saldo += qtd
        return f"Saldo adicionado {qtd}. Novo saldo é {self.saldo + qtd}"
    
    def visualizar_saldo(self):
        return self.saldo
    
    def resumo(self):

class Conta_corrente(Conta):
    def __init__(self, conta, titular, saldo, taxa_manutencao, limite):
        super().__init__(conta, titular, saldo)
        self.taxa_manutencao = taxa_manutencao
        self.limite = limite

    def visualizar_saldo(self):
        return super().visualizar_saldo()

class Conta_poupanca(Conta):
    def __init__(self, conta, titular, saldo, taxa_juros):
        super().__init__(conta, titular, saldo)
        self.taxa_juros = taxa_juros
    
    def calcular_juros(self):
        return
    
    

    