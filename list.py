user_input = "yes,i ,am ,in ,love"
seperate = user_input.split(',')
print(seperate)

x = input("enter your favourite song with seperate commas")
y = x.split("-")  #split method divides the string into list
print(y)     #split() seperate the string wherever the comma appears

x=[1,2,3,4,5,6,7,8,9]
x.append("d")
print(x)
y=30
a=10
c=y+a
print(c)

#all operations in python list
#1st is append
my_list = [1,2,3]
my_list.append(4) #by using append method we can add one item at the end of list
print(my_list)
my_list.insert(3,"g") #by using this method we can add item in list at specific index which you want
print(my_list)

my_list.extend([22,3,4,5])   #add multiple items  in list by using extend method
print(my_list)
#remove item from list
w = [1,1,2,3,45,6]
print(w.pop(1)) #removes the item at specific position
print(w.remove(2)) #rmoves the item with specified value
print(w.clear())
print(w.add(44))
