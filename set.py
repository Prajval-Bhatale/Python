my_set = set()

n = int(input("Enter how many elements you want to add in the set: "))

for i in range(n):
    element = input(f"Enter element {i+1}: ")
    my_set.add(element)  

print("\nYour set is:", my_set)

print("Length of set:", len(my_set))

new_element = input("Enter a new element to add: ")
my_set.add(new_element)
print("Set after adding new element:", my_set)

# Convert set to list
my_list = list(my_set)
print("Converted to list:", my_list)

