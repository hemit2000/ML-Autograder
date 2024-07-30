def reverse_string(str):
    str_rev = ''
    i = len(str) - 1

    while i >= 0:
        str_rev += str[i]
        i -= 1

    return str_rev

print(reverse_string('Hemit'))