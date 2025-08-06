num = int(input("Enter a number to check if it's a palindrome: "))

original_num = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

if original_num == reverse:
    print(original_num, "is a palindrome number")
else:
    print(original_num, "is not a palindrome number")
