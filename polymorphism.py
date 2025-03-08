#polymorphism : means multiple classes with same method here we used 3 classes and one common method which is new()
class car:
    def __init__(self,name):
        self.name = name

    def new(self):
        print("drive !")

class boat:
    def __init__(self,name):
        self.name = name

    def new(self):
        print("move !")

class plane:
    def __init__(self,name):
        self.name = name
     
    def new(self):
        print("fly !")

c = car("ford")
p = plane("india")

b = boat("slane")
for i in (c,p,b):
    print(i.name)
    i.new()


