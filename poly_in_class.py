# Polymorphism in class

class Vehicle:
    def start_engine(self):
        print("Starting vehicle engine....")

class Car(Vehicle):
    def start_engine(self):
        print("Car engine started.")

class Bike(Vehicle):
    def start_engine(self):
        print("Bike engine strated.")

class Truck(Vehicle):
    def start_engine(self):
        print("Truck Engine Started.")

v=Vehicle()
v.start_engine()

c=Car()
b=Bike()
t=Truck()

c.start_engine()
b.start_engine()
t.start_engine()