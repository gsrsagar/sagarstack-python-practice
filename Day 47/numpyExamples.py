import numpy as np
import array

arr = np.array(["Sagar","Sunny","Sumps","Sameer"], dtype=str)
print(arr[0][0:4])
# [ 'S',"a","g","a","r"
#   "s,"u","n","n","y
#   "S","u","m","p","s"
#   "S","a","m","e" "e" "r"
#]

arr = np.delete(arr,2) # reassign changes
print(arr)

arr = array.array("I",[12,456,6,7,7])
del arr[0];
print(arr)

#insert at last
arr.append(34) # single value insertion
arr.extend([2,45,778,44,55,3434]) # multi value of array insertion
print(arr)

#insert
arr.insert(5,455555)
print(arr)

#remove
arr.remove(2);
print(arr)

#pop
arr.pop()
print(arr)

#remove element at index
arr.pop(4)
print(arr)

arr.reverse()
print(arr)