
################# DAY 3 ####################

pattern = r"mul\(\d+,\d+\)|do\(\)|don\'t\(\)"
content = ""
with open('input day 3.txt', 'r') as file:
    content = file.read()
import re
matches = re.findall(pattern, content)
total = 0
enabled = True
for match in matches:
    if match == "do()":
        enabled = True
    elif match == "don't()":
        enabled = False
    else:
        total += int(match.split(",")[0][4:]) * int(match.split(",")[1][:-1]) if enabled else 0
print(total)