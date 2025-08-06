n = int(input("Enter the number up to which you want to print odd numbers: "))

print("Odd numbers up to", n, "are:")
for i in range(1, n + 1, 2):
    print(i, end=" ")
