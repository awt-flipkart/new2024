import re
text = "hope rcb will win ipl 2024"

pattern = r" "
match = re.match(pattern,text)
if match :
    print(" match found", match.group())
else:
    print(" not found")