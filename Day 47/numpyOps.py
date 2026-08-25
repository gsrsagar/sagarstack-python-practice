
import numpy as np
arr=  np.array([1,3,4,5,6,8,89,90,0,0,6,4,4,1,2])
arrReshaped = np.reshape(arr,(3,5))
#[
#  1,3,4
#  5,6,8
#  89,90,0
#  0,6,4
# ]
print(arrReshaped)
# dimensions
arrFlatten = arrReshaped.flatten()
print(arrFlatten)


#Concatenation
arrStudents =["sagar","Sheema","Supripa","Reena",]
arrMarks = [104,101,105,103]
arrMerged = np.array(arrStudents+arrMarks)
print(arrMerged)

arrMarks.sort()
print(arrMarks)