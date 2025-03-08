class branch:
    def __init__(field,name):
        field.name1 = name
    def printname(field):
        print(field.name1)

b1 = branch("ai and ds")
b1.printname()
class student(branch): #chiled classes inherits the properties of parent class
    def __init__(field, name,year):
        super().__init__(name)
        field.gyear = year

    def stud(field):
        print("welcome to the branch:" ,field.name1,"student name is:",field.gyear)
    
b2 = student("electronics",22)
b2.stud()
