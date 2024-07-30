import re

string = "ABCDDEFG"
pattern = "AB*EFG"
match = re.search(pattern, string)
 
if match:
    print("Pattern found!")
else:
    print("Pattern not found!")
