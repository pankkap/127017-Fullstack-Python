# 1. Function Defination:
# What are the Tasks functions Performed

# 2. Function Calling:
# You called the function to Perform some Task

# Two Types of Functions
# 1. System Defined: That is created by Python
# 2. User Defined: That is created by User

# Ver-1: Function not recieveing any data
# and not returning any Data


# Function defination
def myFunction():
    x = 10
    y = 20
    print("This is Function")
    print("Result: ", x + y)


# Function calling
myFunction()

# Ver-2: Function will recieve some data
# and not returning any Data


def myFunction2(x, y):
    print("This is 2nd Variation of Function")
    print("Result: ", x + y)

myFunction2(10, 15)


# Ver-3: Function will recieve  data
# and returning Data
def myFunction3(x, y):
    print("3rd Varient of Function")
    z = x + y
    return z

result = myFunction3(20, 25)
print(result)


# This function will recieve arbitrary Arguments
# *x --> reciveing multiple arguments
# **x--> reciveing multiple dictionary arguments
def function1(**x):
    for i, j in x.items():
        print(i, j)

function1(fname="Pankaj", mname="kumar", lname="kapoor")


# Default Arguments
def function2(x, y=0):
    print(x + y)

function2(10, 5)


def function3():
    pass

function3()

#global vaiable
x = 10


def display():
    #local variable
    global x
    x = 15
    print("Result: ", x)

display()
print(x)

# ----------------------------------------------
# Lamda Function is Anonymous function
# It can take any number of Number of Arguments
# But can have only one Expression
# also known Expression Function
# its a single line function

# Arrow function in JS
# var x = (a) => a*a;

x = lambda a: a * a
print(x(5))

# multiple argument lambda function
y = lambda a, b, c: a + b + c
print(y(5, 10, 15))


def function5(n):
    return lambda a: a * n

myTripler =  function5(3)
myDoubler =  function5(2)
print(myTripler(11))
print(myDoubler(11))