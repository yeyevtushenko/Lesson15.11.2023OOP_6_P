class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def show(self):
        print(f"Name: {self.name}")
        print(f"Species: {self.species}")

    def sound(self):
        pass


class Dog(Pet):
    def sound(self):
        return "Woof! Woof!"


class Cat(Pet):
    def sound(self):
        return "Meow!"


class Parrot(Pet):
    def sound(self):
        return "Squawk! Squawk!"


class Hamster(Pet):
    def sound(self):
        return "Squeak!"


dog = Dog(name="Buddy", species="Dog")
cat = Cat(name="Whiskers", species="Cat")
parrot = Parrot(name="Sunny", species="Parrot")
hamster = Hamster(name="Fluffy", species="Hamster")

pets = [dog, cat, parrot, hamster]

for pet in pets:
    pet.show()
    print(f"Sound: {pet.sound()}\n")
