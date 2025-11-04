#User Defined Exception

class InvalidAge(Exception):
    pass

try:
    age=int(input("Enter the Age :"))
    if age < 18:
        raise InvalidAge
    else:
        print("Eligible for Vote.")

except InvalidAge:
    print("Not eligible for vote.")