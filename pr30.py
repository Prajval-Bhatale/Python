n = int(input("Enter a number: "))
limit = n ** 2

print("Series: ")
value = 1
for i in range(limit):  
    if value > limit:
        break
    print(value, end=" ")
    value *= 2
