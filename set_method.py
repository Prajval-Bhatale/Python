set1 = set()
set2 = set()

n1 = int(input("Enter number of elements for set1: "))
for i in range(n1):
    element = input(f"Enter element {i+1} for set1: ")
    set1.add(element)

n2 = int(input("\nEnter number of elements for set2: "))
for i in range(n2):
    element = input(f"Enter element {i+1} for set2: ")
    set2.add(element)

print("\nSet 1:", set1)
print("Set 2:", set2)

union_set = set1.union(set2)
print("\nUnion of Set 1 and Set 2:", union_set)

intersection_set = set1.intersection(set2)
print("Intersection of Set 1 and Set 2:", intersection_set)

