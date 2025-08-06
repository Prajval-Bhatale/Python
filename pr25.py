n = int(input("Enter how many numbers you want to compare: "))

count = 1
largest = None

while count <= n:
    num = float(input(f"Enter number {count}: "))
    
    if largest is None or num > largest:
        largest = num

    count += 1

print("The largest number is:", largest)
