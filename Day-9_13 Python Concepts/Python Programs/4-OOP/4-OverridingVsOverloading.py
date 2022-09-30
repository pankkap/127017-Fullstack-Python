# # Method Overriding
# class Parent:
#     def welocme(self):
#         print("This is Welcome in Parent")


# class Child(Parent):
#     # method is overrided by Child Class
#     def welocme(self):
#         print("This is Welcome in Child")

# obj = Child()    
# obj.welocme()   # call child function
# obj = Parent()   
# obj.welocme()   # call parent function


# --------------------------- Method Overloading------------------------

# Method Overloading works with One Class 

class ABC:
    def Hello(self, fname=None, lname=None):
        if fname is None and lname is None:
            print("Hello")
        elif lname is None:
            print("Hello "+fname)
        else:
            print("Hello "+fname + " " + lname)        
    
obj = ABC()
obj.Hello()
obj.Hello("Pankaj")
obj.Hello("Pankaj", "kapoor")