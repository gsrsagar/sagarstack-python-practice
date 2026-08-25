

def printOBjs(**kwargs):
    #It is in the form of dict
    #Key word arguments { "key": "value", "key2": "value2"}
    for key,value in kwargs.items():
        print(f"{key}: {value}")


printOBjs(name ="Dotnet Full stack",age =26)



