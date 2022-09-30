# Class -1
class Father:
    def __init__(self, fname):
        self.fathername = fname

# Class -2
class Mother:
    def __init__(self, mname):
        self.mothername = mname

# Multiple Inheritance
class Son(Father, Mother):
    def __init__(self, fname, mname):
        Father.__init__(self, fname)
        Mother.__init__(self, mname)
    def parentsName(self):
        print("Father Name: ", self.fathername)    
        print("Mother Name: ", self.mothername)    

# Driver's code
s1 = Son("John", "Monika")
# s1.fathername = "Jack"
# s1.mothername = "Dani"
s1.parentsName()