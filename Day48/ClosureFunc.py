




def CreateObj(name,age):
    def innerFUnc():
        print(f"Hi my name is {name} and age is {age}")

    return innerFUnc

#Nested Function

func = CreateObj("Sagar",26)
func()