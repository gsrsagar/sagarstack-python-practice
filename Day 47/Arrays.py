import array
import numpy as np

arr = array.array("i",[1,2,3,5])
print(arr)
print(arr[0])
print(arr[-1])
print(arr[-2])
print(arr[-2:])
print(arr[:-1])

arr1 = array.array("I",[1,2,3,4])
print(arr[0])
arr2 = array.array("f",[1.44,2.455,3.32,4.2])
print(arr2[0])

arr3 = array.array("d",[1.3444,67.45,7.45,9,5])
print(arr3[0])

arr4 = array.array("u","Sagar")
print(arr4[0])



