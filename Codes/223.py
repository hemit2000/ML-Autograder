def countOccurrences(list, element):
    count = 0
    for i in range(len(list)):
        if list[i] == element:
            count += 1
    return count

if __name__ == '__main__':
    list = [1, 2, 5, 4, 1, 5]
    element = 5
    print(countOccurrences(list, element))
