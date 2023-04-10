# classe
class Dog:
    def __init__(self, namePassed, agePassed):
        # cria um atributo name da classe Dog
        self.name = namePassed
        self.age = agePassed

    # método: função de uma classe
    def bark(self):
        print("barking")
    
    def getHumanAge(self):
        return self.age*7

    def setOwner(self, ownerPassed):
        self.owner = ownerPassed
    
    def getOwner(self):
        return(self.owner)

# criando uma nova instância da classe Dog() 
d = Dog("Finn", 4)
d2 = Dog("Banzai", 4)
d3 = Dog("Blu", 2)

d.setOwner("Chico")
d3.setOwner("Ge")

print(d3.owner)
