
import re
# date is 2707-2026
pattern =r"\b\d{2}-\d{2}-\d{4}\b"
dateToday = "Spo 28-09-2026 todays date is 27-07-2026 and all is happening rain today"
result = re.findall(pattern,dateToday)
print(result)