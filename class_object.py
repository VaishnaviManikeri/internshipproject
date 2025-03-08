class student:
    def __init__(stud,name,id):#init () is executed automatically when class is created
        stud.name = name
        stud.id = id
  
  #with __str__()
    def __str__(stud):
     return f"{stud.name}\n{stud.id}"
p1 = student("tnvi",14)
print(p1)
#without __str__() we have to use object name .and parameter
s1 = student("vaishu",11)
print(s1.name)
print(s1.id)
#object function
  
