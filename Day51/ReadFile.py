
with open("Sagar.text","r") as ReadFile:
    context = ReadFile.read()
    print(context)


    for line in ReadFile:
        print(line)