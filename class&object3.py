#object parametere
class people:
    def __init__(self,name,age):
        self.name1=name
        self.age2 = age
    def new(self):
        print("my name is:" + self.name1 ,self.age2)
         
p = people("vaishu",22)
p.age=20
p.new()
class student(people): #child class1
    def __init__(self, name, age):
       super().__init__(name, age)
      
       pass #use keyword pass to add the use the properties of parent class
s = student("jonhy",22)
s.new()
class stud(people): #chiled class 2
    def __init__(self,name,age,year):
         super().__init__(name,age)
         self.gyear = year
    def method(self):
        print("welcom",self.name1,self.age2,self.gyear)
s1 = stud("tnu",22,2024)
s1.method()
           
