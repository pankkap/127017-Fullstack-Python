# 1. Absctract class is used for providing the Template
# 2. Abstract class can instantiate (we can't create Objects)
# 3. Abstract class may contain abstract Methods
# 4. The class inherting the Abstract class, responsible for provideing the implementation Abstarct methods,
# otherwise it will also trated as Abstarct Class



from abc import ABC, abstractmethod

class X(ABC):
    @abstractmethod
    def m1(self):
        pass

    @abstractmethod    
    def m2(self):
        None

class Y(X):
    def m1(self):
        print("This is an Abstarct Method")

# Y become an Abstarct class, because it was not providing the Implementation of Abstract methods        

class Z(Y):    
    def m2(self):
        print("Class Z is providing the implementation of Abstact Method")
        
# obj = Y()         can't create an object of an Abstract class
obj = Z()

obj.m1()
obj.m2()

# obj1 = X()          can't create an object of an Abstract class

