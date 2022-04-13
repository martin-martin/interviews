import re
from datetime import datetime

with open("devicelog.log", "r") as logfile:
    logs = logfile.readlines()
    relevant_lines = [line for line in logs if re.match(r"ON|OFF|ERR", line)]
    for line in logs:
        print(re.match(r"(ON)|(OFF)|(ERR)", line))




print(logs)
print(relevant_lines)

