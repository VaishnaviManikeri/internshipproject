#E-commerce product stock checker project
x = int(input("enter the product unit available:"))
if x >= 5:
    print("available")
elif x > 0 and x < 5:
    print("some are here")
elif x == 0:
    print("out of stock")


