
import re
pattern = r"\d+"
str ="My name is 53334 and also roll no is 524"
result = re.search(pattern,str)

print(result.span())
print(result.string)
print(result.group())