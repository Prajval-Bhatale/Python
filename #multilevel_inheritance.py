#multilevel inheritance

class Animal:
    def speak(self):
        print("Animal can make sounds.")

class Dog(Animal):
    def bark(self):
        print("Dog is barking like woof! Woof!!")

class Puppy(Dog):
    def play(self):
        print("Puppy Loves to play.")

puppy = Puppy()

puppy.speak()
puppy.bark()
puppy.play()