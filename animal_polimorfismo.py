class Animal:
    def __init__(self) -> None:
        pass
         
    def emitir_som(self):
        pass

class Cachorro(Animal):
    def emitir_som(self):
        return "Woof!"

class Gato(Animal):
    def emitir_som(self):
        return "Meow!"

class Pato(Animal):
    def emitir_som(self):
        return "Quack!"

def fazerAnimalFalar(animal):
    return animal.emitir_som()

cachorro=Cachorro()
gato=Gato()
pato=Pato()

animais=[cachorro,gato,pato]

for animal in animais:
    print(animal.__class__.__name__, "faz", fazerAnimalFalar(animal))
