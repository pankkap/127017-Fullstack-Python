# I want to perfor sum of two number
# a = 10
# b = 20
# These are static value
# I need dynamic values enter by user

name = input("Hey! Enter Your Name")
print(name)

print("Enter a Number")
a = int(input())
print("Enter a another Number")
b = int(input())
s = a + b

if (s == 0):
    print("Sum of numbers is Zero")
elif (s % 2 == 0):
    print("Sum of numbers is Even")
else:
    print("Sum of numbers is Odd")


