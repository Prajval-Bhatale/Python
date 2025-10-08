# Destructor

class boy:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print(f"Boy {self.name} is created.")
        print("Age is created :",self.age)
 
    def __del__(self):
        print("Name is distroy")

s1 = boy("Prajval",21)



    
