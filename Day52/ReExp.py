

import re

pattern = r"\d*"
str ="My 456 name 1333444 is 123 1   2 3 "

result = re.findall(pattern,str)


pattern2 = r"\S+"
str2 = "All my      chilhood is very better \n and also it is very good fro health"
result2 = re.findall(pattern2,str2)
print(result2)



