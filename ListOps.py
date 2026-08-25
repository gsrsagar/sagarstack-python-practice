
courses = ["MERN","HEAN","MEVN","AENN","ZOTNET","JAVA","PYTHON"]
#print(courses)
courses.sort()
courses.reverse()

# list indexes means  courses[0], course[1].... course[n-1]
# index starts from 0 to length-1 courses[0] to courses[6]
for course in courses:
    print(course)


#0
#1
#last value remove
courses.pop()
courses.pop(len(courses)-2);

courses.append("JAVA")

courses.insert(1,"AI DS")
#courses.clear()
#(courses)

#insertion

#sorting