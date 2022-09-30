# Level-1
class GrandFather:
    def __init__(self, grandFathername):
        self.grandFathername = grandFathername

# Level-2 
class Father(GrandFather):
    def __init__(self, fathername, grandFathername):
        self.fathername = fathername
        # invoking the constructor of GrandFather
        GrandFather.__init__(self, grandFathername)

# Level-3
class Son(Father):
    def __init__(self, grandFathername, fathername, sonname):
        self.sonname = sonname
        # invoking the constructor of Father
        Father.__init__(self, fathername, grandFathername)

    def print_name(self):
        print("Grandfather Name: ", self.grandFathername)    
        print("Father Name: ", self.fathername)    
        print("Son Name: ", self.sonname)    

s1 = Son("Jack", "Danial", "Mike")
s1.print_name()