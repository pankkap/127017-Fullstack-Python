# Python Array: is a collection of similar Data types

import array as arr
from unicodedata import decimal

numbersArray = arr.array('i', [1,2,3,4,5,-10])
decimalArray = arr.array('f', [1.2, 3.14, -2.6546])

print(numbersArray)
print(decimalArray)

print(numbersArray[0])
print(decimalArray[1])

# Iterating over the loop
for i in numbersArray:
    print(i)

# updating array value
numbersArray[0] = 101
print(numbersArray)   

#length of the Array
print(len(numbersArray))
print(len(decimalArray))

# insert for insert at a perticular index
# append to insert data at the end
numbersArray.insert(1, 102)
decimalArray.append(-20)
print(numbersArray)
print(decimalArray)

# remove function to remove data by value
# pop method to remove data in the last
decimalArray.remove(-20.0)
del numbersArray[-1]
decimalArray.pop()

print(numbersArray)
print(decimalArray)


# concatenation 
a=arr.array('d',[1.1 , 2.1 ,3.1,2.6,7.8])  
b=arr.array('d',[3.7,8.6])  

c = arr.array('d')

c = a + b
print(c)
