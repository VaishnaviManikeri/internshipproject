x = 100 #global variable
def fun1():
    x = 300 #local variable
    print(x)
    global y
    y = 400
    print(y)
fun1()
print(x)