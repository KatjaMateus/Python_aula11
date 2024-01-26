class Conta:
    def __init__(self, tipo,conta, titular, saldo):
        self.tipo = tipo
        self.conta = conta
        self.titular = titular
        self.saldo = saldo
    
    def sacar(self, qtd):
        if self.saldo > qtd:
            self.saldo -= qtd
            return self.saldo
        else:
            return f"Saldo insuficiente para sacar {qtd}"
    
    def depositar(self, qtd):
        self.saldo += qtd
        return f"Depósito de {qtd} adicionado com sucesso. Novo saldo é {self.saldo}"
    
    def visualizar_saldo(self):
        return self.saldo
    
    def resumo(self):
        return f"""
        Tipo de conta: {self.tipo}
        Número de conta: {self.conta}
        Títular da conta: {self.titular}
        Saldo da conta: {self.saldo}
        """    
    
class Conta_corrente(Conta):
    def __init__(self, conta, titular, saldo, taxa_manutencao, limite):
        super().__init__(conta, titular, saldo)
        self.taxa_manutencao = taxa_manutencao
        self.limite = limite
    
    def conta_corrente_sacar(self, qtd):
        if self.limite > qtd:
            self.limite -= qtd
            return f"Saque de {qtd} realizado com sucesso. O novo saldo é {self.limite}"
        else:
            print(f"O limite de cheque especial insuficiente para o saque de {qtd}")
    

class Conta_poupanca(Conta):
    def __init__(self, conta, titular, saldo, taxa_juros):
        super().__init__(conta, titular, saldo)
        self.taxa_juros = taxa_juros
    
    def calcular_juros(self):
        juros = (self.taxa_juros * self.saldo) / 100
        return f"O novo saldo é {juros + self.saldo}"

def resumo(conta):
    return conta.resumo()

conta1=Conta_corrente(tipo="Conta Corrente",conta="8766-9876",titular="João Lima", saldo=8765.50, taxa_manutencao=34.45, limite=15000)
conta2=Conta_poupanca(tipo="Conta Poupança",conta="8766-9888",titular="João Lima", saldo=18765.35, taxa_juros=3)

print(conta2.calcular_juros())
    
    

    
