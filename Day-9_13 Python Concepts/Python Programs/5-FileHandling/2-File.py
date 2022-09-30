# copy file from one location to another loaction

# # Standard Utility Module
# import shutil

# #source Path
# source = 'C:/Users/pankk/Desktop/Python Programs/5-FileHandling/documents/sample1.txt'

# #destination Path 
# destination = "C:/Users/pankk/Desktop/Python Programs/5-FileHandling/documents/sample1.txt"

# try:
#     shutil.copy(source, destination)
# except shutil.SameFileError:
#     print("Source and Destination represent the same file")    
# except PermissionError:
#     print("Permission Error")
# except:
#     print("Error occurred while copying file")        



# --------Rename a FIle ----------------------

# import os
# old_name = "C:/Users/pankk/Desktop/Python Programs/5-FileHandling/documents/sample.txt"
# new_name = "C:/Users/pankk/Desktop/Python Programs/5-FileHandling/documents/newName.txt"

# os.rename(old_name, new_name)
# print("Renaming Done")


# --------Deleting a FIle ----------------------


import os
file_name = "C:/Users/pankk/Desktop/Python Programs/5-FileHandling/documents/newName.txt"
os.remove(file_name)
print("Deletion Done")