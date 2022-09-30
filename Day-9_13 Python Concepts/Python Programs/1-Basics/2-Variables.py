# Casting: conversion from one into another
a = 10
print(type(a))

# Casting 

a = str(a)
print(type(a))

a = float(a)
print(type(a))

a = int(a)
print(type(a))


# Rules for creating variables
# A variable name must start with a letter or the underscore character
# A variable name cannot start with a number
# A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# Variable names are case-sensitive (age, Age and AGE are three different variables)

# Types of variable declaration
# Camel Case
myVariableName = "John"

# Passcal Case
MyVariableName = "John"

# Snake Case
my_variable_name = "John"


# Multiple variable declaration
a,b,c = 10,15,20
print(a)        #10
print(b)        #15
print(c)        #20

# Multiple variable with One Value
a = b = c = 15
print(a)        #15
print(b)        #15
print(c)        #15

# UnPacking the List: value stored in separate variable 
data = ["Jonathan", "Yannick", "Antoine"]
dev1, dev2, dev3 = data 

print(dev1)
print(dev2)
print(dev3)

fname = "Koenig"
lname = "Solutions"
print(fname+lname)      #KoenigSolutions
# + is used concatenation Operator
print(fname,lname)      #Koenig Soltion
print(fname)
print(lname)