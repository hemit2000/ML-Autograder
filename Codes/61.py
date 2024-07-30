def count_frequency(l):
    frequencies = {}
    for i in l:
        if i in frequencies:
            frequencies[i] += 1
        else:
            frequencies[i] = 1
    return frequencies

l = [1,4,1,4,4,4,9,7]
print(count_frequency(l))
