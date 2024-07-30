import re

def is_valid_phone_number(phone_number):
 pattern = re.compile("^[0-9]{3}-[0-9]{3}-[0-9]{4}$")
 match = pattern.match(phone_number)
 return bool(match)

print(is_valid_phone_number("123-456-7890"))
