n = int(input("Enter the number up to which you want to print natural numbers: "))

print("Natural numbers up to", n, "are:")
for i in range(1, n + 1):
    print(i, end=" ")
