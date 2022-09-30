list1 = ["apple", "apple", 123, "xyz", 123]
print(list1)
set1 = {"apple", "banana", "cherry", "apple"}
set2 = set(list1)
set2.add("kiwi")
# remove will throw an error if element is not available in the set
set1.remove("banana")

# discard will not throw an error if element is not available in the set
set2.discard("banana")
set2.clear()
del set2
# print(set2)

A = { 0, 2, 4, 6, 8}
B = {1, 3, 5, 7, 9, 0, 2}

print("Union : " , A|B)
print("Intersection : " , A&B)