
class Ninja:

    # implment attributes
    def __init__(self, first_name, last_name, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.petfood = pet_food
        self.dapet = Pet()

    # methods
    def walk(self):
        self.dapet.play()
        return self

    def feed(self):
        self.dapet.eat()
        return self

    def __str__(self):
        pass
    

class Pet:
    def __init__(self, name = 'bob', type = 'dog', tricks = 'backflip', health = 100, energy = 70):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy

    def sleep(self, amout):
        self.energy += 25
        return self

    def eat(self):
        self.energy += 5
        self.health += 10

    def play(self):
        self.health += 5

    def showEnergy(self):
        return self.energy

    def showHealth(self):
        return self.health


ninja1 = Ninja('Samir', 'Hossain', 'Bacon', 'Steak')
print(ninja1.dapet.showHealth())
print(ninja1.dapet.showEnergy())
print(ninja1.walk().dapet.showHealth())
print(ninja1.feed().dapet.showHealth())
print(ninja1.dapet.showEnergy())