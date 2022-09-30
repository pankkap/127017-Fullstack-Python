from copyreg import constructor


# constructor is a special function 
# that is used to initialize the data members of the class
# constructor function is auto called once the object has been created
class MyClass:
     
    x = 100
    name = "OOPS"
    def __init__(self, datavalue, nameValue):
        print("This is a constructor")
        self.x = datavalue
        self.name = nameValue
     
    def displayDetails(self):
        print("This is a Member Function")
        print("Value of x: ", self.x)
        print("Value of name: ", self.name)


obj1 = MyClass(101, "new name")
# print(obj1.x)
# print(obj1.name)
obj1.displayDetails()


# Assignment 
# Create an Employee class
# properties: name, age, email
# constructor to initialize the data
# function: display Employee Details
# create two Object of Employee class
