#Parameterized Constructor

class student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display(self):
        print("Name is :",self.name)
        print("Age is :",self.age)

a = input("Enter name: ")
b = int(input("Enter age :"))

s1 = student(a,b)

s1.display()
        