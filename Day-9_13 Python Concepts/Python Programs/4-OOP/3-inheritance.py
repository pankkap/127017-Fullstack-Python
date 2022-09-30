# # parent class
# class A:
#     def __init__(self):
#         self.x = 100
#         self.y = 200

# # subclass | child class
# class B(A):
#     def __init__(self, z):
#         super().__init__()
#         self.z = z

        
# obj = B(300)
# print(obj.x)


from tokenize import Single


class Person:
    def __init__(self, fname, lname):
        self.firstName = fname
        self.lastName = lname
    def printname(self):    
        print(self.firstName, self.lastName)

class Student(Person):
    def __init__(self, fname, lname, dob):
        # Person.__init__(self, fname, lname)
        super().__init__(fname, lname)
        self.year = dob

    def printname(self): 
        # super().printname() will call the Parent Method
        super().printname();   
        print(self.year)

s1 = Student("Jonathan", "Luhunga", 1992)
s1.printname()


# 1. Single Inheritance
# 2. Multiple Inheritance
# 3. Multi-level Inheritance
# 4. Hierarchical Inhertance
# 5. Hybrid Inheritance
