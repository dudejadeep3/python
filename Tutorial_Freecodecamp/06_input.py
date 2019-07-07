# Getting the input from the users
name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello " + name + "! You are "+age)

# Building a basic calculator
num1 = input("Enter a number:")
num2 = input("Enter another number:")

result = float(num1) + float(num2);  # we could use int() but it will remove decimal points
print(result);

# if we int() and pass number with decimal then we will get
# an error and program will stop.

# result = int(5.5)