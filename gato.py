#CRIE UMA CLASSE CHAMADA gato QUE TEM OS ATRIBUTOS:
# nome (str), raça (str), peso (float), idade (int), castrado (bool)
# TENHA O MÉTODO:
# miar() QUE RETORNA UMA MENSAGEM DIZENDO:
# "O {nome do gatim} está miando, dê atenção pra ele"
# INSTACIE 2 GATOS E USE O MÉTODO PARA AMBOS.


class Gato:
    def __init__(self, name: str, breed: str, weight: float, age: int, neutered: bool):
        self.nome = name
        self.raca = breed
        self.peso = weight
        self.idade = age
        self.castrado = neutered

    def miar(self):
        return f"O {self.nome} está miando, dê atenção para ele."
    
gato1 = Gato(name="Zico", breed= "siamese", weight = 6.2, age= 4, neutered = True)
gato2 = Gato(name="Chalita", breed= "tigre", weight = 2.6, age= 1, neutered = False)

print(gato1.miar())
print(gato2.miar())