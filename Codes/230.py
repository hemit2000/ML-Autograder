def check_monthnum_number(monthnum1):
    if monthnum1 == 2:
        return True
    elif monthnum1 >= 1 and monthnum1 <= 12:
        return False
    else:
        return None

print(check_monthnum_number(13))