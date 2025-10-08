#multiple inheritance tyre,wheels,rubber



class Rubber:
    def material(self):
        print("Rubber is used to make tyres.")

class Wheels:
    def rotate(self):
        print("Wheels helps to move Vehicle.")

class Tyre(Rubber,Wheels):
    def __init__(self):
        print("Tyre is created.")

    def shape(self):
        print("Shape is round.")


t = Tyre()

t.shape()
t.material()
t.rotate()
