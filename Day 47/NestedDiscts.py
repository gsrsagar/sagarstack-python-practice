


my_courses = {
    "course": { "courseName":"Dotnet", "totalStudents":30},
    "modules" :{ "totalModules":16,"compltedModules":4,
                 "modulesList":
                     [
                         { "moduleName":"Java Core Part 1", "isCompleted":True},
                         {"moduleName":"Sata types in java", "isCompleted":False},

                      ]
                 },
    "students": { }
}
print(my_courses)



day_1_part_1 = {
    "day": 1,
    "part": 1,
    "title": "About the Course Plan and Internet World",
    "status": "Done",

    "description": (
        "Learn about the course plan, software development, "
        "software technologies, and awareness of how the Internet works."
    ),

    "topics": [
        "About Software Development",
         "Technologies",
         "How Internet Works",
         "Software Technologies",
         "How Real-Time Applications Work"
    ]
}

day_1_part_1.update( {"modules" :{ "totalModules":16,"compltedModules":4,
                 "modulesList":
                     [
                         { "moduleName":"Java Core Part 1", "isCompleted":True},
                         {"moduleName":"Sata types in java", "isCompleted":False},

                      ]
                 }})
for key in day_1_part_1.keys():
    print("keys ", key,":",day_1_part_1[key])

for value in day_1_part_1.values():
    print("values ", value)

for key, value in day_1_part_1.items():
    print("entries ", key,":",value)