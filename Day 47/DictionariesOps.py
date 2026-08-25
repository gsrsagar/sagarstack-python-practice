import copy

course = {
    "courseName": "90 Days Plan, Dot Net Full Stack Development",
    "courseDescription":"This is the Dotnet Full Stack Development for 90 Days Plan",
     "totalSubjects":21,
     "resources":1,
     "tag":"Telugu Tech"
}


course1 = copy.deepcopy(course)
print(course)
course["courseName"] ="90 Days plan -SAGAR STACK Dotnet Full Stack"
del course["resources"]
print(course)
course.pop("tag")
print(course)
course.popitem()
print(course)
print("Course1",course1)
for key in course:
    print( key,":"+ course[key] )


for value in course.values():
    print( "Values :",value)

for key, value in course.items():
    print( "In Items",key,":"+value)

