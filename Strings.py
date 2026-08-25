

name ="Sagar Reddy"
name2 = 'sagar'
name3 = '''Sagar 
        Reddy
'''
name4 = """Sagar 
            Reddy
"""

# print(name)
# print(name2)
# print(name3)
# print(name4)


firstName ='     Sagar    '
lastName="reddy.com"
fullName = firstName+ " "+ lastName #string concatenation
#Sagar reddy
names ="Sagar\nSumanth\nSumi\nSUps"
words = names.splitlines()
print(words)

name="Sagar"
age =20

print(f"{name} is {age} years old")
print(f"Hello is {name} and age is {age}".format(name,age))
print("Hello is {} and age is {}".format(age,name))