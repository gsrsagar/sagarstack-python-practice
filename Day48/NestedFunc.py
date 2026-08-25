


def CreateObj():
    def innerFUnc(name,age):
        print(f"Hi my name is {name} and age is {age}")

    return innerFUnc

#Nested Function

func = CreateObj()
func("Sagar",29)