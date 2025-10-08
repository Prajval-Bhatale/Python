# Single Inheritance Example with getName()

class Animal:
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name   

    def speak(self):
        print(f"{self.name} makes a sound.")


class Dog(Animal):   
    def speak(self):
        print(f"{self.getName()} barks.")


my_dog = Dog("Puppy")
my_dog.speak()
