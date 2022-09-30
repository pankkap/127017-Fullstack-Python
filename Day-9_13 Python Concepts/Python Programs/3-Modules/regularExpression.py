import re
txt = "The rain in spain"

# below one Search Pattern | Regular Expression | Regx
x = re.search("^The.*spain$", txt)

# I am interested to search a pattern which means there The word in the starting, after The there can some character and at the end of string, i am looking for the word Spain.
if x:
    print("YES! we have a match")
else:
    print("No Match")    

x = re.findall('in', txt)
# show the list of matched patterens


x = re.search("\s", txt)
print("The First White space character located at: ", x.start())


x = re.split("\s", txt)


x = re.sub("in", "_", txt, 2)
print(x)


