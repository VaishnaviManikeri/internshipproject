b = "hi everyone"
print(b[1:7]) #this is called string slicing and do not print the last no it will print the number before it it like here the second  no is 7 so it will print the character upto 6 form 1 to 6
c = "hello guyse"
print(c[:5])
print(c[1:])
print(c[-5:-2]) #it will print 1st character upto  limit and 2nd before limit
#modify the string
a = "    hello ,world"
print(a.upper())
print(a.lower())
print(a.strip()) #removes white space in the variable containing string
print(a.replace("h","j"))
print(a.split(",")) #splites the string into substring in list format 
#concation of the string
x = "hi"
y = "by"
z = x + y
print(z)
w = x + " " + y
print(w)

d = 11
e = 5
f = d + e
print(f)

age = 26
c = f"my age is {age}" #to concate txt and integer
print(c)
