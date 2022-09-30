# class is a Template
class MyClass:
    # properties | data Members | attribues
    x = 100
    name = "OOPS"
    
    # functions | member functions | methods
    def displayDetails(classFunction):
        print("This is a Member Function")

    def __str__(self):
        return 'String Represntation of Object with data '+ str(self.x) + ' and ' + str(self.name)

# Creating Objects
obj1 = MyClass()
print(obj1)

# print(obj1.x)
# print(obj1.name)
# obj1.displayDetails()

obj2 = MyClass()

# Update data for Object-2
# obj2.x = 200
# obj2.name = "Python"
# print(obj2.x)
# print(obj2.name)
# obj2.displayDetails()





















