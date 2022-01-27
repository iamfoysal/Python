print("------Python Data Type-------")
x =str("Hello python")
print(x)
print(type(x))

print("int type")
y = int(20)
#display y:
print(y)
#display the data type of y:
print(type(y)) 

print("Float type")
y = float(20.34)

print(y)
print(type(y))

print("complex type")
y = complex(665j)

print(y)
print(type(y))


print("-----------list--------------")
x = list(("apple", "banana", "cherry"))
print(x)
print (type(x))

print("-----------=tuple=--------------")
x = tuple(("apple", "banana", "cherry"))
print(x)
print (type(x))

print("----------range--------------")
x = range(6)
print(x)
print(type(x))

print("----------bytes--------------")
x = bytes(5)
print(x)
print(type(x))

print("----------bytearry--------------")
x = bytearray(10)
print(x)
print(type(x))


print("----------memoryview-------------")
x = memoryview(bytes(2))
print(x)
print(type(x))

print("=====Random Number=======")




#Import the random module, and display a random number between 1 and 19

import random

print(random.randrange(1,20))