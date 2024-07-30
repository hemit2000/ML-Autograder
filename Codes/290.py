def move_num(test_str):
    res = ''
    dig = ''
    for ele in test_str:
        if ele.isdigit():
            dig += ele
        else:
            res += ele
    res += dig
    return res

print(move_num('geeks4geeks'))