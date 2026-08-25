
    # r - readmode
    # w- writemode
    # a- append mode -> extra adding content
    # b- binary mode


with open("sample.txt","r") as  f:
    #content = f.readlines() #array of lines
    context2 = f.read()
    #print(content)
    print(context2)