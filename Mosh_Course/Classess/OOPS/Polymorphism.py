# Method overriding

class Animal:

    def __init__(self):
        print("Animal constructor")
        self.age = 1


    def eat(self):
        print("eat")


class Mammal(Animal):

    def __init__(self):
        print("Mammal constructor")
        self.weight = 3
        super().__init__()


    def walk(self):
        print("walk")


class Fish(Animal):

    def swim(self):
        print("swim")


m = Mammal()
m.eat()
print(m.age)
print(m.weight)