#multiple inheritance

class Animal:
    def eat(self):
        print("Animal is eating.")

class Breed:
    def Breed(self):
        print("Breed is normal.")

class Dog(Animal,Breed):
    def bark(self):
        print("Dog is Barking.")

my_dog = Dog()

my_dog.eat()
my_dog.Breed()
my_dog.bark()
    