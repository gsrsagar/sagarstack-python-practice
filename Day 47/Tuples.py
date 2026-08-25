# And Immutable collection of Elements
tuple = (1, 2, 3) #0,1,2
print(tuple)

namesTuple = ("Sagar","Sunny","Sheema","Reena","Supriya",tuple)
print(namesTuple)

#unpacked TUple
unpackedTupe_exp =  1,2,3,4,5,6,7,"Sagar"
print(unpackedTupe_exp)
a,b,c,d,e,f,g,h = unpackedTupe_exp
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)

*var1 , var3 , var2,var4= unpackedTupe_exp
print(var1)
print(var2)
print(var3)
print(var4)

#Methods
print("len is ",len(var1))
print("Max element is :",max(var1))
print("Min element is :",min(var1))
print("Sum of total elements are :",sum(var1))
      #0,1,2
tup2 =(1,2,3,3,4,56,6,7,3,3,3,3,3)
tup3 = (1,2,3)
print(tup2==tup3) #Equality order is important

print(tup2.count(7)) #index= 7
print(tup2.index(3)) #index = 2