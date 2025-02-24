class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self, food):
        print(f"{self.name} is eating {food}.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

    def speak(self):
        
        print(f"{self.name} makes a generic animal sound.")

class Cow(Animal):
    def __init__(self, name, age, milk_production):
        super().__init__(name, age)
        self.milk_production = milk_production  

    def speak(self):
        print(f"{self.name} says Moo!")

    def give_milk(self):
        print(f"{self.name} gives {self.milk_production} liters of milk today.")


class Pig(Animal):
    def speak(self):
        print(f"{self.name} says Oink!")

    def roll_in_mud(self):
        print(f"{self.name} is rolling in the mud to cool off.")


class Chicken(Animal):
    def speak(self):
        print(f"{self.name} says Cluck!")

    def lay_egg(self):
        print(f"{self.name} has laid an egg!")


class Farm:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"Added {animal.name} to the farm.")

    def show_all_animals(self):
        print("\nAnimals on the farm:")
        for animal in self.animals:
            print(f"- {animal.name}, Age: {animal.age}", end=", ")
            animal.speak()

    def feed_animals(self, food):
        print("\nFeeding all animals with", food)
        for animal in self.animals:
            animal.eat(food)

