class Funcionarios:
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

class Empresa:
    def __init__(self):
        self.lista_de_funcionarios = []
    
    def adicionar_funcionario(self):
        nome_funcionario = str(input("Digite o nome do funcionário: "))
        cargo_funcionario = str(input("Digite o cargo do funcionário: "))
        salario_funcionario = float(input("Digite o salário do funcionário: "))

        funcionario = Funcionarios(nome=nome_funcionario, cargo=cargo_funcionario, salario=salario_funcionario)

        self.lista_de_funcionarios.append(funcionario)

    def remover_funcionario(self):
        nome_removido = str(input("Digite o nome do funcionário que você quer deletar: "))
        for funcionario in self.lista_de_funcionarios:
            if funcionario.nome == nome_removido:
                self.lista_de_funcionarios.remove(funcionario)
    
    def listar_funcionarios(self):
        for funcionario in self.lista_de_funcionarios:
            print(f"""
            Nome: {funcionario.nome}
            Cargo: {funcionario.cargo}
            Salário: {funcionario.salario}
""")

empresa1 = Empresa()

while True:
    menu = int(input("""
    Escolha uma opção:
    1 - Adicionar funcionário
    2 - Remover funcionário
    3 - Listar funcionários
    0 - Sair
"""))
    
    if menu == 1:
        empresa1.adicionar_funcionario()
    elif menu == 2:
        empresa1.remover_funcionario()
    elif menu == 3:
        empresa1.listar_funcionarios()
    elif menu == 0:
        print("Fim do programa")
        break
    else:
        print("Opção inválida")
    # match menu:
    #     case 1:
    #         empresa1.adicionar_funcionario()
    #     case 2:
    #         empresa1.remover_funcionario()
    #     case 3:
    #         empresa1.listar_funcionarios()
    #     case 0:
    #         print("Fim do programa")
    #         break
    #     case _:
    #         print("Opção Inválida")
