class Organism:
    alive = True

class Animal(Organism):
    def eat(self):
        print("This animal is eating")

class Orca(Animal):
    def swim(self):
        print("This Orca is swiming")

orca = Orca()
print(orca.alive)
orca.swim()
orca.eat()
