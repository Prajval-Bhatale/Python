n = int(input("Enter the number: "))

i = 1
sum_odd = 0

while i <= n:
    sum_odd += i
    i += 2  

print("Sum of odd numbers up to", n, "is:", sum_odd)
