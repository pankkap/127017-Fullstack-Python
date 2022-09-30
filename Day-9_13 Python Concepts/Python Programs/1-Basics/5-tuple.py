tup1 = ("apple", "banana", 1,2,3, True)

# Important: Tuple can not update, add, and remove the  data

# We can update, add and remove tuble's data indirectly

temp = list(tup1)
# print(type(temp))

temp[0]  = "kiwi"
temp.append("jonathan")
# print(temp)

tup1 = tuple( temp)
print(tup1)