#default constructor

class info:
    def __init__(self):
        self.name = "Prajval"
        self.age = 21
        self.branch = "CSE"
        self.division = "TY A"

    def display(self):
        print("Name is :",self.name)
        print("Age is :",self.age)
        print("Branch is :",self.branch)
        print("Division is :",self.division)

o = info()

o.display()