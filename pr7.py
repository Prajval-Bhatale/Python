a=int(input("Enter the 1st number:"))
b=int(input("Enter the 2nd number:"))
c=int(input("Enter the 3rd number:"))


if a<b and a<c:
    print(f"1st number which is {a} is smallest number")

elif b<a and b<c:
    print(f"2nd number {b} is smallest number")

else:
    print(f"3rd number which is {c} is smallest number")
