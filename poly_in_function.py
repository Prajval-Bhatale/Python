#Polymorphism in function

def add(a, b, c=0):
    return a + b + c

result1 = add(10, 20)
print(f"Addition of 2 numbers: {result1}")

result2 = add(10, 20, 30)
print(f"Addition of 3 numbers: {result2}")
