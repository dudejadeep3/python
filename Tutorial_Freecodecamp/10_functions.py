# functions are block of code which are groupped together
# allow us to break up the code reusable chunks
# functions are started with def keyword and all code inside
# the functions are indented
# to call the function <function-name>()


def say_hi():
    print("Hello User")


print("Top")
say_hi()
print("Bottom")


# passing parameters to the functions
def say_hi(name):
    print("Hello "+name)


say_hi("Mike")


def say_hi(name,age):
    print("Hello "+name + ". You are " + str(age))


say_hi("Deep", 27)


# using return statements
# returns value to the calling function
def cube(num):
    return num*num*num
    print("here")  # never getting printed


print(cube(3))  # if nothing was returned from the function, it will print NONE

result = cube(4)
print(result)







