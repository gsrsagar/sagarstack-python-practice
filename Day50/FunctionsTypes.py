

class Types:

    course="Dotnet full stack"

    def __init__(self,age,name):  #constructor helps to create object
        self.age = age
        self.name = name

    def displayAge(self): #instance method
        print(self.age)

    @classmethod
    def displayNameClass(cls):
        print(cls.course)

    @staticmethod
    def addition(a,b):
        return a+b



o = Types(25,"Sagar")
o.displayAge()
print(o.name)
print(o.course)

Types.displayNameClass()
print(Types.addition(1,2))