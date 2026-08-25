# for loop use chjeyakunda driect ga sigle line lo list create

squars = [x**2 for x in range(11)] #0,1,2,3,4,5,6,7,8,9,10
print(squars)


evens = [ "even" if x%2==0 else "odd" for x in range(11) ]
print(evens)

for x in range(0,11):
    if x%2==0:
        print("even")
    else:
        print("odd")


divisibleBy5 = [ "divisble by 5"  if x%5==0 else "" for x in range(0,11)]
print(divisibleBy5)

