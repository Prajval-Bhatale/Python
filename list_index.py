my_list=[]

n=int(input("Enter the no.of elements:"))

for i in range(n):
    elements=input(f"Enter the element no.{i}:")
    my_list.append(elements)

print("Final list is:",my_list)

print(my_list[1:])
print(my_list[-3])
print(my_list[1])
print(my_list[4:])
print(my_list[:-2])

