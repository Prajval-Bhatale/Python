#Predefined Exception

try:
    num1=int(input("Enter the Numerator:"))
    num2=int(input("Enter the Denominator:"))
    result=num1/num2
    print("Result :",result)

except ZeroDivisionError:
    print("Error : Division by zero is not allowed.")

except ValueError:
    print("Error : Enter the valid Integers.")

print("Programe Contionue....")