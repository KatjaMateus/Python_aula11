class Funcionarios:
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

class Empresa:
    def __init__(self):
        self.lista_funcionarios = []   #empresa começa com a lista de funcionarios vazia

    def adicionar_funcionario(self):
        nome = str(input("Digite o nome do funcionário: "))
        cargo = str(input("Digite o cargo do funcionário: "))
        salario = float(input("Digite o salário do funcionário: "))

        funcionario = Funcionarios(nome=nome, cargo=cargo, salario=salario)
        self.lista_funcionarios.append(funcionario)
    
    def remover_funcionario(self):
        nome_removido = str(input("Digite o nome do funcionario a deletar> "))
        for funcionario in self.lista_funcionarios:
            if funcionario.nome == nome_removido:    #procura nome tal de variavel funcionario
                self.lista_funcionarios.remove(nome_removido)
    
    def lista_funcionarios(self):
        for funcionario in self.lista_funcionarios:
            print(f"""
            Nome: {nome}
            Cargo: {cargo}
            Salário: {salario}
            """)

empresa1 = Empresa()

