print("----Global Variables used in function-------")

x= "Python is Best!!"
def myFunction():
    print("programming Language"+ x)
    
y="Programming lang"
myFunction()

print(y + x)


def myfunc():
    global x
    x = "fantastic"
    print(x)

myfunc()

print("Python is " + x)
