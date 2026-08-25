
#variable length arguments
def add(*args):
    sum=0;
    for arg in args:
        sum+=arg
    return sum


print(add(1,2))
print(add(1,2,3,45,56,7,8,9,9,0))