
#Creating Variables 
x=10        # x is of type int
print (x)


y="Python Str"        # y is type of string 
x="Python Str"      # x is type of string 


print(y)
print (x)

# used in Casting 
a= str(5)
b= int (5)
c= float(5)

print(a)
print(b)
print(c)

# Get the Type of dataType used in type() function
print(type(a))
print(type(b))
print(type(c))

"""
Variable Names
A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
"""

#Many Values to Multiple Variables
print("----------Many Values to Multiple Variables--------")


Free, manty_to, Multi = "many values ", "To", "Multiple"

print(Free)
print(manty_to)
print(Multi)

print("-------One Value to Multiple Variables-------")

x=y=z ="one to multi variables"

print(x)
print(y)
print(z)



print("-------Unpack a Collection-------")
foysal_khai = ["Apple","Banana", "cherry","vat"]

x,y,z,a= foysal_khai

print(x)
print(y)
print(z)
print(a)
 
print ("--Output Variables---")

python= "Best!"
print("Python is "+python)



