def check_rotation(str1, str2):
    if len(str1) != len(str2):
        return False
    
    temp = str1 + str1
    return str2 in temp

s1 = "Hello World"
s2 = "World Hello"
if check_rotation(s1, s2):
    print('These strings are rotations of each other')
else:
    print('These strings are not rotations of each other')
