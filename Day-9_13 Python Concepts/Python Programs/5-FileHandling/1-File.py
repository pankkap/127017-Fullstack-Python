# There are two types of File
# 1. Text File: stores character Data. Eg: test.txt
# 2. Binary File: stores data in binary Format. Eg: images, video files, audio etc. 

# File Path: A file path that defines the location of a File or Folder.
# We have two types of Path.

# 1. Absolute Path: Full address of Location with Root Folder
# C:\Users\pankk\Desktop\Python Programs\1-Basics\1-Basics.py

# 2. Relative Path: Path related to your current working Directory of your Project
# 1-Basics\1-Basics.py

# # Read a File
# fp = open('C:/Users/pankk/Desktop/File Handling/sample.txt', 'r')
# print(fp.read())
# # fp.close()

# # Write into a File
# # Note: If the destination file is not available, it will create one
# text = "Jonathan"
# fp= 0

# fp = open("sample1.txt", 'w+')
# fp.seek(5)
# # w mode will overrite the previous data
# # fp = open("sample1.txt", 'a')
# fp.write(text)
# print("Writing Done!")
# fp.close()


# # ------------Binary Data---------------

# some_bytes = b'\x21'
# fp = open("myfile.txt", 'wb')
# fp.write(some_bytes)
# print("Writing Done!")
# fp.close()



# -------------------Byte Araay ----------------------

arr = [65,66,67,68]
arr_bytes = bytearray(arr)
print(arr_bytes)

bytes_data = bytes(arr_bytes)

# fp = open("myfile.txt", 'wb')

with open("myfile.txt", "wb") as fp:
    fp.write(bytes_data)

print("Writing Done")
fp.close()