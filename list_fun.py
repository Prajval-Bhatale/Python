my_list=[]

n=int(input("Enter how many elements you want in list:"))

for i in range(n):
    elements=int(input(f"Enter Element{i}:"))
    my_list.append(elements)

print("Original list:",my_list)

my_list.append(1111)
print("After append:",my_list)
my_list.insert(1, 50)
print("After insert(1, 50):", my_list)

my_list.sort()
print("After sort:",my_list)

my_list.reverse()
print("After reverse():", my_list)

if 50 in my_list:
    my_list.remove(50)
    print("After remove(50):", my_list)
else:
    print("50 not found to remove")

if len(my_list) > 0:
    popped = my_list.pop()
    print("After pop():", my_list)
    print("Popped element:", popped)

print("Count of 100:", my_list.count(100))

if 100 in my_list:
    print("Index of 100:", my_list.index(100))

# Clear the list
my_list.clear()
print("After clear():", my_list)