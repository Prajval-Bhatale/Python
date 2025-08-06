n = int(input("Enter how many numbers you want to compare: "))

count = 1
smallest = None

while count <= n:
    num = float(input(f"Enter number {count}: "))
    
    if smallest is None or num < smallest:
        smallest = num

    count += 1

print("The smallest number is:", smallest)
