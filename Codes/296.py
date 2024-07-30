def sortList(myList):
    myList.sort(key=lambda x: x[1])

    print("The sorted list in ascending order is:")
    for i in range(len(myList)):
        print(myList[i])

myList = [('Tom', 7), ('Harry', 5), ('Bob', 8)]
sortList(myList)
