#Abstract class method

from abc import ABC, abstractmethod

class Animal(ABC):
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Dog Barks")

class Cat(Animal):
    def sound(self):
        print("Cat meow")

d=Dog()
d.sound()

c=Cat()
c.sound()