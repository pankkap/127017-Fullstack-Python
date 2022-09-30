# Dictionary in Python
# Dictionary is also a Collection

# it stores data in Key:Value pair
# Ordered*
# changeable
# Does'nt allow duplicate data
# dictionary is similart to Objects in JS
# ITEMS => key + value

dict1 = {
    "name": "Jonathan",
    "age": 25,
    "address": "Congo",
    "designation": "Developer"
}

# print(dict1)
# print(type(dict1))
# print(len(dict1))

# # Access Data of Dictionary
# print("My Age is :" + str(dict1["age"]))
# print("My Profession is :" + (dict1.get("designation")))

# # getting list of keys and values
# myKeys = dict1.keys()
# print(myKeys)
# myValues = dict1.values()
# print(myValues)

# # Items retures combinations of Key and Value
# myData = dict1.items()
# print(myData)

# # Update the data of Dictionary
# # As well as update the dictionary itself with new value
# dict1["age"] = 30
# print(dict1)

# dict1.update({"age": 31})
# print(dict1)

# dict1.update({"email": "jonathan@abc.com"})
# print(dict1)

# # Remove data from Dictionary
# dict1.pop("address")
# print(dict1)

# dict1.popitem()
# print(dict1)

# del dict1["name"]
# print(dict1)

# dict1.clear()
# print(dict1)

# del dict1
# print(dict1)

# Loop through Dictionary
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "color": "white",
    "seats": [2, 4, 6]
}

# x is index of car dictionary
for x in car:
    print(x, car[x])

print("\n")

# Print only keys
for i in car.keys():
    print(i)

print("\n")

# Print only values
for i in car.values():
    print(i)

car["seats"].insert(3, 12)
# print(car)
print("\n")

for i, j in car.items():
    print(i, j)

# copy the Dictionary

# newDict = car
# only reference is copied

newDict = car.copy()
newDict1 = dict(car)
print(newDict)

# Merge two Dictionaries
dict1.update(car)
print(dict1)

# Convert the List into Dictionary
list1 = [1, 2, 3, 4, 5]
# dict1 = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Dictionary Comprehensive concept
sq_list = {n:n*n for n in list1}
print(sq_list)