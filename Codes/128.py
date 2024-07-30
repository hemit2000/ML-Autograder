def find_common_elements(list1, list2):
    common_elements = []

    for e1 in list1:
        for e2 in list2:
            if e1 == e2:
               common_elements.append(e1)

    return common_elements

list1 = [1, 2, 3, 4, 5]
list2 = [2, 4, 6, 8]

print(find_common_elements(list1, list2))
