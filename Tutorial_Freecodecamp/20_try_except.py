# catching error in python

# number = int(input("Enter your number: "))
# print(number) will create error in case user enter alphabet instead of number

try:
    number = int(input("Enter your number: "))
    print(number)
    num = 10 / 0
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Invalid Input")


