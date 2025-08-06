num = int(input("Enter a number to check if it's prime: "))

if num < 2:
    print(num, "is not a prime number")
else:
    i = 2
    is_prime = True

    while i <= num // 2:
        if num % i == 0:
            is_prime = False
            break
        i += 1

    if is_prime:
        print(num, "is a prime number")
    else:
        print(num, "is not a prime number")