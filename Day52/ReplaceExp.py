import re

pattern = r"\d+"
str =" My name is 123 and my roll no is 123 and my sister no is also 123"
result = re.sub(pattern, "#",str)
print(result)