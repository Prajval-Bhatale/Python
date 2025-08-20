import array as arr

num1 = arr.array("i",[1,2,3,4,5])
#num2 = arr.array("u",["Prajval","Vishal","Prithvi","Suhas"])

num1.append(9)
num1.insert(6,54)
num1.index(4)
num1.pop(3)
num1.remove(5)
num1.count(6)

print(num1.reverse())
print(num1.count(2))
print(num1.index(3))

for j in num1:
    print(j,end=" ")

