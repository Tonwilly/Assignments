class Birds:
    wings = 2
    legs = 2

    def move(self):
        return "Move by flying"
    
    def feeding(self):
        return "Birds feed differently"

    def __init__(self,beak,classification, feet):
        self.beak = beak
        self.classification = classification
        self.feet = feet

bird1 = Birds("Hooked","Flesh eater","Clawed")
bird2 = Birds("Straight","Filter feeder","Webbed")

print("Birds that have " + bird1.beak + " beak feed on prey.")
print(bird1.feet + " feet birds " + str(bird1.move()))
print("Birds that have " + bird2.feet + " feet can swim.")

# for testing purposes before initializing the constructor
# print("Birds have " + str(bird1.wings) + " wings")
# print("Birds have " + str(bird1.legs) + " legs of different sizes and shapes respective to the species")
# bird1.move()

# polmorphism

class Parrot(Birds):
    def feeding(self):
        return "Parrots feed on fruits and seeds by cracking them"

class Duck(Birds):
    def feeding(self):
        return "Duck feed by filtering feed fom water pools"

class HummingBird(Birds):
    def feeding(self):
        return "Humming bird feed on nectar with its long thin beek"

class Eagles(Birds):
    def feeding(self):
        return "Eagles feed by tearing flesh with their hooked beaks from their prey"

goldenheadeagle = Eagles()
print(goldenheadeagle.feeding)

redparrot = Parrot()
print(redparrot.feeding)