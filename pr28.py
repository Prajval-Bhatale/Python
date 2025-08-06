n = int(input("Enter the number up to which you want to print even numbers: "))

print("Even numbers up to", n, "are:")
for i in range(2, n + 1, 2):
    print(i, end=" ")
