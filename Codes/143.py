def max_ones(num):
    count = 0 
    result = 0
    for i in range(len(num)):
        if num[i] == '1':
            count += 1 
            result = max(result, count)
        else:
            count = 0 
    return result

num = '10101010001'
print(max_ones(num))
