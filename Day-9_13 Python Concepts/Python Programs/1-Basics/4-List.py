
list1 = [1,2,3,4,5]                         # integer List
list2 = ["apple", "banana", "cherry"]       # string List
list3 = ["abc", 1, 2, 3, True, "male"]      # mixed List

print(list1)
print(list2)
print(list3)
print(type(list3))                          #<class 'list'>

# List constructor
list4 = list((1, "one", True, "jonathan", "Pankaj", 347387 ))
           #   0    1     2      3           4        5
           #  -6   -5    -4     -3          -2       -1
print(list4)

# Access the List
print(list4[1])
print(list4[-3])

# Access Full List
for i in list4:
    print(i)

# Access all using while
i=0
while(i<len(list3)):
    print(list3[i])
    i = i + 1

#access Selected elements with index
print(list4[2:5])

#access Selected elements using -ve index
print(list4[-4:-1])

# List can be changeale
list5 = [1,2,3, 'a','xyz']
list5[2] = 33
print(list5)
list5.append(11)
list5.insert(1,"pqr")
list5.extend(list1)
print(list5)


# Split the list using LOGIC, no direct method available
newList = [11,18,19,21]
length = len(newList)
middle = length //2
print(middle)

first_half = newList[:middle]
second_half = newList[middle:]

print(first_half)
print(second_half)


# Remove of Elements
list6 = ["abc", True, 1, 55, 11, "xyz"]
# remove last element
list6.pop()

# remove element by index value
del list6[1]

# remove element by value
list6.remove('abc')

# Empty the list
list6.clear()

# Delete the list 
del list6
# print(list6)


list11 = list1 + list2 
# list11.append(list3)   put entire list as Elements
list11.extend(list3)
print(list11)