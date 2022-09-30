#scenario-1
x = -1
# try:
#     if x < 0:
#         raise Exception("Sorry, number below Zero")
# except Exception as ex:
#     print(ex)

#scenario-2

# a =int (input("Enter First Number"))
# b =int (input("Enter Second Number"))

# try:
#     if( b==0):
#         raise ZeroDivisionError("Can't divide any Number by 0")        
# except ZeroDivisionError as ex:
#     print("There is an Exception: ", ex)
# else:
#     print("Result: ",a/b)    
# finally:
#     print("There is an Exception Handling deployed")




try:
  f = open("3-Modules\demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")






