# Method Overriding

class Calculator:
    def add(self, a, b):
        sum = a+b
        print(f"Addition of two numbers is = {sum}")

class NewCalculator(Calculator):
    def add(self, a, b, c):
        sum = a+b+c
        print(f"Addition of three numbers is = {sum}")

c1 = Calculator()
c1.add(10, 45)      

c2 = NewCalculator()
c2.add(20, 50, 10)  

