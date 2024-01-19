# CRIE UMA CLASSE PAI CHAMADA funcionario QUE TEM OS ATRIBUTOS:
# nome (str), cpf (str), idade (int)
# E OS MÉTODOS:
# bater_ponto() QUE RETORNA A HORA QUE O FUNCIONÁRIO BATEU O PONTO
# CRIE UMA CLASSE FILHA CHAMADA gerente QUE TEM OS MÉTODOS A MAIS:
# demitir() QUE RETORNA "O gerente demitiu alguem"
# contratar() QUE RETORNA "O gerente contratou alguem"
# CRIE UMA CLASSE FILHA CHAMADA caixa QUE TEM COMO ATRIBUDO A MAIS:
# num_do_caixa (int)
# E O MÉTODO NOVO CHAMADO:
# fechar_o_caixa() QUE RETORNA "O caixa {nome_do_caixa} fechou o caixa {num_do_caixa}

from datetime import datetime

class Funcionario:
    def __init__(self, nome: str, cpf: str, idade: int):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
    
    def bater_ponto(self):
        horario = datetime.now()
        horario_formatado = horario.strftime("%H:%M") #formata horario para somente horas e minutos
        return f"O funcionário {self.nome} bateu o ponto às {horario_formatado} horas."
    
class Gerente(Funcionario):
    def __init__(self, nome: str, cpf: str, idade: int):
        super().__init__(nome, cpf, idade)
    
    def demitir(self):
        return f"O gerente {self.nome} demitiu alguem"
    
    def contratar(self):
        return f"O gerente {self.nome} contratou alguem"

class Caixa(Funcionario):
    def __init__(self, nome: str, cpf: str, idade: int, num_caixa: int):
        super().__init__(nome, cpf, idade)
        self.num_caixa = num_caixa
    
    def fechar_o_caixa(self):
        return f"O {self.nome} fechou o caixa {self.num_caixa}."

gerente = Gerente(nome= "João", cpf="48585", idade=24)
caixa = Caixa(nome= "Maria", cpf="574023", idade=33, num_caixa=9)

# print(gerente.bater_ponto(17:02))
print(gerente.bater_ponto())
print(gerente.contratar())
print(gerente.demitir())

print(caixa.fechar_o_caixa())
print(caixa.bater_ponto())


