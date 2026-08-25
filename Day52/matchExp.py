
import re
pattern = r"dear$"
str="Hello world my dear"
result = re.findall(pattern,str)
if result:
    print(result)