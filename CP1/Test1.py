a=20 #global variable
def variable():
    b=30
    c=a+b
    return c
print(a) #can be accessed because a is an global variable
print(variable())
#print(b) #can not be accessed because b is a local variable
