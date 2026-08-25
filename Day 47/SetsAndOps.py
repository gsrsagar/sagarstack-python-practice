ls = [1,2,2,2,2,3,3,4,4,5,6,7]
#Converting list to set
setExp = set(ls)
print(setExp) #{ ..values}

#Declaring sirect set
setDirect = {1,2,34,45,56}
setDirect.add(100)
print(setDirect)
setDirect.discard(100) # discard , remove
print(setDirect)
setDirect.pop()
setDirect.clear()
print(setDirect)