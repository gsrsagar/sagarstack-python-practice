
#A function calling it self


def FuncTIon(n):
    if n<=1:
        return 1;
    else:
        return n*FuncTIon(n-1)


print(FuncTIon(5))

#Factorial 5*(4)*(3)*(2)*(1)
# n =5
# n*(n-1)*(n-1-1)*(n-1-1-1)*((n-(n-1))
# n*(n-1)*(n-2)....(n-(n-1))
#5....1